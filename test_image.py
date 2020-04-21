def test_oneimage(cdciplatform, *a, **aa):
    print("running test one image at ",cdciplatform)

    from oda_api.api import DispatcherAPI
    from oda_api.plot_tools import OdaImage,OdaLightCurve
    from oda_api.data_products import BinaryData

    import os
    from astropy.io import fits
    import numpy as np
    from numpy import sqrt

    if cdciplatform.endswith("production-1.2"):
        endpoint = 'www.astro.unige.ch/cdci/astrooda/dispatch-data'
    else:
        endpoint = 'http://cdcihn/{}/dispatch-data'.format(cdciplatform.split("#")[1].replace("cdcip-"))

        
    disp=DispatcherAPI(host=endpoint)

    print(disp)


    data=disp.get_product(instrument='isgri',
                          product='isgri_image',
                          scw_list=["066500220010.001"],
                          E1_keV=20,
                          E2_keV=80,
                          osa_version='OSA10.2',
                          RA=0,
                          DEC=0,
                          detection_threshold=15,
                          product_type='Real')

    print(data)



