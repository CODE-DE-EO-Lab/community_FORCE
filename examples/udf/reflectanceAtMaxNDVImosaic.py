import numpy as np
import datetime

"""
>>> Copyright (C) 2021 Franz Schug, based on work from Andreas Rabe and David Frantz
"""

def forcepy_init(dates, sensors, bandnames):
    """
    dates:     numpy.ndarray[nDates](int) days since epoch (1970-01-01)
    sensors:   numpy.ndarray[nDates](str)
    bandnames: numpy.ndarray[nBands](str)
    """

    #return bandnames
    y = str(serial_date_to_string(int(dates[0])))
    return [y + '0101_BGRNS1S2', y + '0201_BGRNS1S2', y + '0301_BGRNS1S2', y + '0401_BGRNS1S2', y + '0501_BGRNS1S2', y + '0601_BGRNS1S2']

def serial_date_to_string(srl_no):
    new_date = datetime.datetime(1970,1,1,0,0) + datetime.timedelta(srl_no)
    return new_date.strftime("%Y")
    
def forcepy_pixel(inarray, outarray, dates, sensors, bandnames, nodata, nproc):
    """
    inarray:   numpy.ndarray[nDates, nBands, nrows, ncols](Int16), nrows & ncols always 1
    outarray:  numpy.ndarray[nOutBands](Int16) initialized with no data values
    dates:     numpy.ndarray[nDates](int) days since epoch (1970-01-01)
    sensors:   numpy.ndarray[nDates](str)
    bandnames: numpy.ndarray[nBands](str)
    nodata:    int
    nproc:     number of allowed processes/threads (always 1)
    Write results into outarray.
    """
    
    inarray = inarray[:, :, 0, 0]
    valid = np.where(inarray[:, 0] != nodata)[0]  # skip no data; just check first band

    if len(valid) == 0:
        return
        
    inds = []

    for z in inarray[valid]:
        if((z[3]+z[2]) == 0): ### avoid that denominator is zero
            continue
        if((z[0] < 300) * (z[3] < 500) * (z[4] < 400)): ### blue, nir, swir1 reflectance filter
            continue
        if((z[0] < 100)): ### blue reflectance filter
            continue

        inds.append(int( ((z[3]-z[2]) / (z[3]+z[2])) *10000))

    
    if(len(inds) == 0):
        return
    
    argMax = valid[np.argmax(inds)]
    
    outarray[:] = inarray[argMax,:]
