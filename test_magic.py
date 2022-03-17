import json
import requests

from odaexperiments.run import test_func

# these kind of calls should be traced and noted in the KG
platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="6b36d8f")(cdciplatform=x)


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

    print("got this", r)

    assert r['query_status'] == "done"
    assert r['exit_status']['status'] == 0

    print("this is done and status zero; good!")

def test_urlrequest_realsource(cdciplatform, *a, **aa):
    print("running test direct url at ",cdciplatform)

    r = requests.get("http://in.internal.odahub.io/staging-1-3/dispatcher/run_analysis?src_name=HESSJ1841-055&RA=280.22916667&DEC=-5.55&instrument=magic&query_type=Real&radius=20&product_type=magic_spectrum&query_status=new&session_id=TEST").json()

    print("got this", r)

    assert r['query_status'] == "done"
    assert r['exit_status']['status'] == 0
    assert 'Bokeh' in r['products']['image'][0]['image']['script']

    print("this is done and status zero; good!")
