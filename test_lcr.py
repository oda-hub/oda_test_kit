from odaexperiments.run import test_func

# these kind of calls should be traced and noted in the KG
platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="6b36d8f")(cdciplatform=x)


def test_one(cdciplatform, *a, **aa):
    print("running test one lc at ",cdciplatform)

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


    data=disp.get_product(instrument='isgri',
                          product='isgri_lc',
                          scw_list=["066500220010.001"],
                          E1_keV=20,
                          E2_keV=80,
                          osa_version='OSA10.2',
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')

    print(data)

    print(data.show())

    print(data._p_list)

    print(data.isgri_lc_0_Crab)

    print(data.isgri_lc_0_Crab.data_unit[1].data)

    #assert 'XAX_E' in data.isgri_lc_0_Crab.data_unit[1].data

    return data


def test_n_recentscw(cdciplatform, timestamp=None, n_scw=3, *a, **aa):
    import requests
    import time

    if timestamp is None:
        timestamp=time.time()
    else:
        timestamp=float(time.time())

    t1 = timestamp - 24*3600*590
    t2 = timestamp - 24*3600*550
    s ="https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/scwlist/cons/{}/{}?&ra=83&dec=22&radius=200.0&min_good_isgri=1000".format(
            time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t1)),
            time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t2)),
        )
    print(s)

    r = requests.get(s)

    print(r.json())

    scwpick = r.json()[:n_scw]

    print("picked")

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

    print(disp)


    data=disp.get_product(instrument='isgri',
                          product='isgri_lc',
                          scw_list=[str(s)+".001" for s in scwpick],
                          E1_keV=20,
                          E2_keV=80,
                          osa_version='OSA10.2',
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')

    print(data)
