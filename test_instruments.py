import random

import click
import logging

logging.basicConfig(level="INFO", format='%(message)s')
logging.getLogger().handlers[0].setFormatter(
            logging.Formatter('%(message)s'))

logger = logging.getLogger("oda_api")
logger.setLevel("DEBUG")

try:
    import logging_tree
    logging_tree.printout()
except:
    pass

def platform_endpoint(cdciplatform):  
    if cdciplatform.endswith("production1.2"):
        endpoint = 'www.astro.unige.ch/cdci/astrooda/dispatch-data'
    elif cdciplatform.endswith("staging1.2"):
        endpoint = 'http://cdcihn.isdc.unige.ch/staging-1.2/frontend/dispatch-data'
    elif cdciplatform.endswith("staging1.3"):
        endpoint = 'http://in.internal.odahub.io/staging-1-3/dispatcher'
    elif cdciplatform.endswith("staging"):
        endpoint = 'http://dispatcher.staging.internal.odahub.io'
    else:
        raise Exception("unknown platform")

    return endpoint

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
    

@click.command()
@click.argument("test_name")
@click.option('--argument', '-a', multiple=True)
def cli(test_name, argument):
    globals()[test_name](*argument)

if __name__ == "__main__":
    cli()
    
