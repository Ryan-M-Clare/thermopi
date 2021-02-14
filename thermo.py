import time
import RPi.GPIO     as GPIO
import Adafruit_DHT as ad
import thermo_query as tq
import write_log    as wl
import email_notify as en
from tools import *

# Set up GPIO board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Set up relay signal
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)

# Empty list for averaging temperatures
temps = [0] * 4

# Write header to log
wl.write_log(" T(F) | H(%) | Time")

try:
    while True:
    
        # Retrieve humidity, temperature, and local time
        hum, temp = ad.read_retry(ad.DHT22, 4)
        temp = C_to_F( temp )
        lt = time.localtime()
        
        # if toggle == True:  ## for toggle switch/button addition
        
        # Discard data with unreasonably high humidity (indicator of bad data)
        if hum <= 104.:
            # Ensure perturbation magnitude is reasonable (don't react to bad data)
            if pert( temp, temps ) < 1.5:
                stat = tq.query( lt[3], lt[4], temp, 
                                 GPIO.input(18) )
                
                try:
                    GPIO.output(18, stat)
                    ## Should probably turn this log entry into its own column (T/F)
                    wl.write_log("Output changed to %s" % stat)
                except:
                    pass
            
            # Write state and times to log
            wl.write_log(" %0.1f | %02d   | %02d:%02d:%02d" \
                        % ( temp, hum, lt[3], lt[4], lt[5] ))
        
            # Add new temp, delete oldest, wait 10 seconds
            temps = update( temp, temps )
            
        # else:                            ## for toggle switch/button addition
            # record state to log anyway   ## may add toggle boolean to log
            
        time.sleep(10)
        
finally:
    wl.write_log("thermopi terminated")
    try:
        en.sendmail( time.asctime() )
    except:
        raise RuntimeWarning("Unable to send email.")
    GPIO.output(18, False)
    GPIO.cleanup()