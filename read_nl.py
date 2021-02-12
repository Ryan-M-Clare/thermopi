def read_nl( ):

    nml_opts = {}

    with open("namelist.txt", "r") as f:
        lines = f.readlines()
        
    for line in lines:
        
        # Must add new elif for each new nl variable
        if "#" in line:
            pass
        elif "np_begin" in line:
            exec( "global np_begin; " + line )
            nml_opts["np_begin"] = int(np_begin)
        elif "np_end" in line:
            exec( "global np_end; " + line )
            nml_opts["np_end"] = int(np_end)
        elif "np_temp" in line:
            exec( "global np_temp; " + line )
            nml_opts["np_temp"] = float(np_temp)
        elif "dp_temp" in line:
            exec( "global dp_temp; " + line )
            nml_opts["dp_temp"] = float(dp_temp)
        elif "up_tol" in line:
            exec( "global up_tol; " + line )
            nml_opts["up_tol"] = float(up_tol)
        elif "dn_tol" in line:
            exec( "global dn_tol; " + line )
            nml_opts["dn_tol"] = float(dn_tol)
            
    return nml_opts

## Maybe add a function to reset nl to default values