import json
import requests

def platform_endpoint(cdciplatform):  
    if cdciplatform.endswith("staging1.3"):
        endpoint = 'http://in.internal.odahub.io/staging-1-3/dispatcher'
    else:
        raise Exception("unknown platform")

    return endpoint

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

def test_urlrequest(cdciplatform, *a, **aa):
    print("running test direct url at ",cdciplatform)

    r = requests.get("http://in.internal.odahub.io/staging-1-3/dispatcher/run_analysis?instrument=magic&query_status=new&query_type=image&product_type=magic_image").json()
    assert r['query_status'] == "done"
    assert r['exit_status']['status'] == 0


