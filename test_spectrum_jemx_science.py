import json

import logging
logging.basicConfig(level=logging.DEBUG)

logging.getLogger('matplotlib').setLevel(logging.WARNING)

def platform_endpoint(cdciplatform):
    if cdciplatform.endswith("production"):
        endpoint = "www.astro.unige.ch/mmoda/dispatch-data"
    elif cdciplatform.endswith("production1.2"):
        endpoint = "www.astro.unige.ch/cdci/astrooda/dispatch-data"
    elif cdciplatform.endswith("staging1.2"):
        endpoint = "http://cdcihn.isdc.unige.ch/staging-1.2/frontend/dispatch-data"
    elif cdciplatform.endswith("staging1.3"):
        endpoint = "http://in.internal.odahub.io/staging-1-3/dispatcher"
    elif cdciplatform.endswith("oda-staging"):
        endpoint = "http://in.internal.odahub.io/oda/staging/dispatcher"
    else:
        raise Exception("unknown platform")

    return endpoint


def disp_for_platform(cdciplatform):
    from oda_api.api import DispatcherAPI
    from oda_api.plot_tools import OdaImage, OdaLightCurve
    from oda_api.data_products import BinaryData

    import os
    from astropy.io import fits
    import numpy as np
    from numpy import sqrt

    endpoint = platform_endpoint(cdciplatform)

    return DispatcherAPI(host=endpoint)


def test_source(cdciplatform, *a, **aa):
    import oda_api.token

    print("running test spectrum at ", cdciplatform)

    disp = disp_for_platform(cdciplatform)
    print(disp)


    pars = {

    "DEC": -29.74516667,
    "E1_keV": 3.0,
    "E2_keV": 20.0,
    "RA": 265.97845833,
    "T1": "2017-03-06T13:26:48.000",
    "T2": "2017-03-06T15:32:27.000",
    "api": "True",
    "instrument": "jemx",
    "integral_data_rights": "public",
    "jemx_num": "1",
    "max_pointings": 50,
    "oda_api_version": "1.1.22",
    "off_line": "False",
    "osa_version": "OSA11.2",
    "product": "jemx_spectrum",
    "query_status": "new",
    "query_type": "Real",
    "radius": 4.0,
    "scw_list": [
        "037700020010.001",
        "037700070010.001",
        "037700080010.001",
        "037700090010.001",
        "037700100010.001",
        "037700110010.001",
        "037700120010.001",
        "037700170010.001",
        "037700180010.001",
        "037700190010.001",
        "037700200010.001",
        "037700210010.001",
        "037700220010.001",
        "037700230010.001",
        "037700270010.001",
        "037700280010.001",
        "037700290010.001",
        "037700300010.001",
        "037700310010.001",
        "037700320010.001",
        "037700380010.001",
        "037700390010.001",
        "037700400010.001",
        "037700410010.001",
        "037700420010.001",
        "037700470010.001",
        "037700480010.001",
        "037700490010.001",
        "037700500010.001",
        "037700510010.001",
        "037700520010.001",
        #"037700580010.001",
#        "037700590010.001"
    ],
    "selected_catalog": "{\"cat_frame\": \"fk5\", \"cat_coord_units\": \"deg\", \"cat_column_list\": [[3, 36, 45, 0], [\"1E 1740.7-2942\", \"GRO J1719-24\", \"GX 1+4\", \"Vela X-1\"], [11.70508861541748, 97.77959442138672, 35.312076568603516, 0.0], [265.9955139160156, 259.907958984375, 263.01336669921875, 135.5285875], [-29.773239135742188, -25.0194091796875, -24.745410919189453, -40.55469333333333], [-32768, -32768, -32768, 0], [2, 2, 2, 1], [0, 0, 0, 1], [2.9999999242136255e-05, 0.00014000000373926014, 0.0002800000074785203, 0.0]], \"cat_column_names\": [\"meta_ID\", \"src_names\", \"significance\", \"ra\", \"dec\", \"NEW_SOURCE\", \"ISGRI_FLAG\", \"FLAG\", \"ERR_RAD\"], \"cat_column_descr\": [[\"meta_ID\", \"<i8\"], [\"src_names\", \"<U14\"], [\"significance\", \"<f8\"], [\"ra\", \"<f8\"], [\"dec\", \"<f8\"], [\"NEW_SOURCE\", \"<i8\"], [\"ISGRI_FLAG\", \"<i8\"], [\"FLAG\", \"<i8\"], [\"ERR_RAD\", \"<f8\"]], \"cat_lat_name\": \"dec\", \"cat_lon_name\": \"ra\"}",
    "session_id": "MSLLXFZX1X5D3W5D",
    "src_name": "1E 1740.7-2942",
    "token": oda_api.token.discover_token(),

    }

    datas = {}

    for integral_data_rights in ["public", "all-private"]:
        datas[integral_data_rights] = disp.get_product(        
            **{**pars, "integral_data_rights": integral_data_rights}
        )

    print(datas)

    return datas

