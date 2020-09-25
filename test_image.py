import random

def platform_endpoint(cdciplatform):  
    if cdciplatform.endswith("production1.2"):
        endpoint = 'www.astro.unige.ch/cdci/astrooda/dispatch-data'
    elif cdciplatform.endswith("staging1.2"):
        endpoint = 'http://cdcihn/staging-1.2/frontend/dispatch-data'
    elif cdciplatform.endswith("staging1.3"):
        endpoint = 'http://in.internal.odahub.io/staging-1-3/dispatcher'
    else:
        raise Exception("unknown platform")

    return endpoint


def test_oneimage(cdciplatform, osaversion, *a, **aa):
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

    onescw = aa.get("scw", "066500220010.001")

    data=disp.get_product(instrument='isgri',
                          product='isgri_image',
                          scw_list=[onescw],
                          E1_keV=25,
                          E2_keV=80,
                          osa_version='OSA10.2',
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')

    print(data)



def test_n_recentscw(cdciplatform, timestamp=None, osaversion="osa10.2", n_scw=2, *a, **aa):
    import requests
    import time

    if timestamp is None:
        timestamp=time.time()
    else:
        timestamp=float(time.time())

    t1 = timestamp - 24*3600*580
    t2 = timestamp - 24*3600*570
    s ="https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/scwlist/cons/{}/{}?&ra=83&dec=22&radius=200.0&min_good_isgri=1000".format(
            time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t1)),
            time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t2)),
        )
    print(s)

    r = requests.get(s)

    print(r.json())

    random.seed(0)

    scwpick = random.sample(r.json(), n_scw)

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

    if '10.2' in osaversion:
        osa_version='OSA10.2'
    elif '11.0' in osaversion:
        osa_version='OSA11.0'
    else:
        osa_version='OSA10.2' # default

    data=disp.get_product(instrument='isgri',
                          product='isgri_image',
                          scw_list=[str(s)+".001" for s in scwpick],
                          E1_keV=25,
                          E2_keV=80,
                          osa_version=osa_version,
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')

    print(data)
