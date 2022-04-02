import logging
import requests
from odaexperiments.run import test_func

logging.basicConfig(level="DEBUG")

logging.getLogger("oda_api").setLevel("DEBUG")
    

platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="66bbd60")(cdciplatform=x)

def test_crab(cdciplatform, *a, **aa):
    print("running test one image at ", cdciplatform)

    endpoint = platform_endpoint(cdciplatform)

    print('endpoint', endpoint)

    R = requests.get(endpoint + "/resolver/api/v1.1/byname/Crab").json()
    print(R)
