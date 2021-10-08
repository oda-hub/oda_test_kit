import json

from odaexperiments.run import test_func

# these kind of calls should be traced and noted in the KG
platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="a86f682292e6233247bb299e5b4b5155faeaf214")(cdciplatform=x)


def disp_for_platform(cdciplatform):
    from oda_api.api import DispatcherAPI
    from oda_api.plot_tools import OdaImage,OdaLightCurve
    from oda_api.data_products import BinaryData

    import os
    from astropy.io import fits
    import numpy as np
    from numpy import sqrt

    endpoint = platform_endpoint(cdciplatform)

        
    return DispatcherAPI(host=endpoint)

def test_one(cdciplatform, *a, **aa):
    print("running test one spectrum at ",cdciplatform)

    disp = disp_for_platform(cdciplatform)
    print(disp)


    data=disp.get_product(instrument='isgri',
                          product='isgri_spectrum',
                          scw_list=["066500220010.001"],
                          E1_keV=20,
                          E2_keV=80,
                          osa_version='OSA10.2',
                          RA=0,
                          DEC=0,                          
                          product_type='Real')

    print(data)



def test_n_recentscw(cdciplatform, timestamp=None, n_scw=2, *a, **aa):
    import requests
    import time

    if timestamp is None:
        timestamp=time.time()
    else:
        timestamp=float(time.time())

    catalog = aa.get('catalog', None)

    t1 = timestamp - 24*3600*680
    t2 = timestamp - 24*3600*570
    s ="https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/scwlist/cons/{}/{}?&ra=83&dec=22&radius=200.0&min_good_isgri=1000".format(
            time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t1)),
            time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t2)),
        )

    r = requests.get(s)


    scwpick = r.json()[:n_scw]

    print("picked", scwpick)

    assert len(scwpick) > 0

    print("running test image at ",cdciplatform)
    disp = disp_for_platform(cdciplatform)

    print(disp)

    data=disp.get_product(instrument='isgri',
                          product='isgri_spectrum',
                          scw_list=[str(s)+".001" for s in scwpick],
                          E1_keV=20,
                          E2_keV=80,
                          osa_version='OSA10.2',
                          RA=0,
                          DEC=0,
                          product_type='Real',
                          selected_catalog=catalog,
                          )

    print(data)
    
    for k,v in data.__dict__.items():
        print(k, v)

def test_shortcat_n_recentscw(cdciplatform, timestamp=None, n_scw=2, *a, **aa):
    disp = disp_for_platform(cdciplatform)

    data=disp.get_product(instrument='isgri',
                          product='isgri_image',
                          scw_list=["066500220010.001"],
                          E1_keV=25,
                          E2_keV=80,
                          osa_version='OSA10.2',
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')


    api_cat = data.dispatcher_catalog_1.get_api_dictionary()
    print("api_cat:", api_cat)

    test_n_recentscw(cdciplatform, 
                     timestamp, 
                     n_scw, 
                     catalog=[
                             #{'NAME': 'Crab', 'RA':83, 'DEC':22},
                         ])

def test_verylongcat_n_recentscw(cdciplatform, timestamp=None, n_scw=2, *a, **aa):
    disp = disp_for_platform(cdciplatform)

    data=disp.get_product(instrument='isgri',
                          product='isgri_image',
                          scw_list=["066500220010.001"],
                          E1_keV=25,
                          E2_keV=80,
                          osa_version='OSA10.2',
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')


    # would be good to have a more clear function to construct from arrays
    api_cat = json.loads(data.dispatcher_catalog_1.get_api_dictionary())
    print("api_cat:", api_cat) 

    api_cat['cat_column_list'][1][0] = "slighly-longer-source-name"
    api_cat['cat_column_list'] = [ c*100 for c in api_cat['cat_column_list'] ]

    test_n_recentscw(cdciplatform, 
                     timestamp, 
                     n_scw, 
                     catalog=json.dumps(api_cat)
                     )
