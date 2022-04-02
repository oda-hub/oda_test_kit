import logging
from odaexperiments.run import test_func

logging.basicConfig(level="DEBUG")

logging.getLogger("oda_api").setLevel("DEBUG")
    

platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="6b36d8f")(cdciplatform=x)

def test_grb(cdciplatform, *a, **aa):
    print("running test one image at ", cdciplatform)

    endpoint = platform_endpoint(cdciplatform)

    print('endpoint', endpoint)

