import random

import click
import logging

logging.basicConfig(level="INFO", format='%(message)s')
logging.getLogger().handlers[0].setFormatter(
            logging.Formatter('%(message)s'))

logger = logging.getLogger("oda_api")
logger.setLevel("DEBUG")

from odaexperiments.run import test_func

# these kind of calls should be traced and noted in the KG
platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="a86f682292e6233247bb299e5b4b5155faeaf214")(cdciplatform=x)


def custom_progress_formatter(L):
    nscw = len(set([l['scwid'] for l in L]))
    return "in %d SCW so far"

def test_instruments(cdciplatform, *a, **aa):
    print("running test ",cdciplatform)

    from oda_api.api import DispatcherAPI
    from oda_api.plot_tools import OdaImage,OdaLightCurve
    from oda_api.data_products import BinaryData

    import os
    from astropy.io import fits
    import numpy as np
    from numpy import sqrt
    import json


    endpoint = platform_endpoint(cdciplatform)
        
    disp=DispatcherAPI(host=endpoint)

    print(disp)

    r = disp.get_instrument_description('isgri')

    print("\033[34m",json.dumps(r, indent=4, sort_keys=True), "\033[0m")
    
