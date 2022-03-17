import random

# import logging
# logging.basicConfig(level="DEBUG")
# logging.getLogger('oda_api.api').setLevel('DEBUG')

import astroquery.heasarc
from astropy.coordinates import SkyCoord
from astropy import units as u
from astroquery.simbad import Simbad

from odaexperiments.run import test_func

# these kind of calls should be traced and noted in the KG
platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="6b36d8f")(cdciplatform=x)

import logging

logging.basicConfig(level="DEBUG")

logging.getLogger("oda_api").setLevel("DEBUG")
    

def get_named_source_coord(name):
    r = Simbad.query_object(name) # and also IREFCAT name?
    print("found this", r)

    cat = Simbad.query_catalog("INTREF")

    print("cat", cat)
    

    return SkyCoord(r[0]['RA'], r[0]['DEC'], unit=("hourangle", "deg"))
    
Heasarc = astroquery.heasarc.Heasarc()

def get_scw_list(ra_obj, dec_obj,radius,start_date,end_date ):
    R = Heasarc.query_region(
            position = SkyCoord(ra_obj, dec_obj, unit='deg'), 
            radius = f"{radius} deg",
            mission = 'intscw',                 
            time = start_date + " .. " + end_date,
            good_isgri = ">1000",
        )  

    R.sort('SCW_ID')
            
    return [ f"{s}.{v}".strip() for s, v in zip(R['SCW_ID'], R['SCW_VER']) ]



def custom_progress_formatter(L):
    nscw = len(set([l['scwid'] for l in L]))
    return "in %d SCW so far"

def test_oneimage(cdciplatform, *a, **aa):
    print("running test one image at ",cdciplatform)

    from oda_api.api import DispatcherAPI
    from oda_api.plot_tools import OdaImage,OdaLightCurve
    from oda_api.data_products import BinaryData

    import os
    from astropy.io import fits
    import numpy as np
    from numpy import sqrt


    endpoint = platform_endpoint(cdciplatform)
        
    disp=DispatcherAPI(host=endpoint)

    print(disp)

    onescw = aa.get("scw", "186500220010.001")

    disp.set_custom_progress_formatter(custom_progress_formatter)

    data=disp.get_product(instrument='isgri',
                          product='isgri_image',
                          scw_list=[onescw],
                          E1_keV=25,
                          E2_keV=80,
                          osa_version='OSA11.0',
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')

    print(data)



def test_n_recentscw(cdciplatform, timestamp=None, osaversion="osa10.2", n_scw=2, e_offset=0, source=None, *a, **aa):
    import requests
    import time


    logging.getLogger('oda_api').setLevel(logging.DEBUG)
    logging.getLogger('oda_api').addHandler(logging.StreamHandler())

    from logging_tree import printout
    printout()


    if timestamp is None:
        timestamp=time.time()
    else:
        timestamp=float(time.time())

    if source is None:
        ra = 0
        dec = 0
        radius = 180
        t1 = timestamp - 24*3600*580
        t2 = timestamp - 24*3600*530
    elif source == "Crab":
        ra = 83
        dec = 22
        radius = 5
        t1 = timestamp - 24*3600*980
        t2 = timestamp - 24*3600*530
    elif source in ["Sco X-1", "Cyg X-1"]:
        c = get_named_source_coord(source)
        ra = c.ra.deg
        dec = c.dec.deg
        print(c)
        radius = 5
        t1 = timestamp - 24*3600*365*15
        t2 = timestamp - 24*3600*365*1.5
    else:
        raise NotImplementedError

    r = get_scw_list(
            ra_obj=ra, 
            dec_obj=dec,
            radius=radius,
            start_date=time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t1)),
            end_date=time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t2))
        )

    random.seed(0)

    scwpick = random.sample(r, n_scw)

    print("picked:", scwpick)

    assert len(scwpick) > 0

    print("running test image at ",cdciplatform)

    from oda_api.api import DispatcherAPI
    from oda_api.plot_tools import OdaImage,OdaLightCurve
    from oda_api.data_products import BinaryData

    import os
    from astropy.io import fits
    import numpy as np
    from numpy import sqrt

    endpoint = platform_endpoint(cdciplatform)

        
    disp=DispatcherAPI(host=endpoint)
    disp.set_custom_progress_formatter(custom_progress_formatter)

    print(disp)

    if '10.2' in osaversion:
        osa_version='OSA10.2'
    elif '11.0' in osaversion:
        osa_version='OSA11.0'
    else:
        osa_version='OSA10.2' # default

    data=disp.get_product(instrument='isgri',
                          product='isgri_image',
                          scw_list=[str(s) for s in scwpick],
                          E1_keV=25 + e_offset,
                          E2_keV=80 + e_offset,
                          osa_version=osa_version,
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')
    
    printout()

    print(data)
    print(dir(data))

    catalog_table = data.dispatcher_catalog_1.table
    m = catalog_table['significance'] >= 0.0

    print(catalog_table[m])

    if source is not None:
        print(f"\033[31m source check requested for {source}\033[0m")
        print(f"found sources:", catalog_table['src_names'])

        t = catalog_table[ catalog_table['src_names'] == source ]
        print(t)

        assert len(t) == 1

