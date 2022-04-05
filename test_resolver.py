import logging
import requests
import pprint
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
    pprint.pprint(R)

    assert abs(R['ra'] - 83.63) < 0.1
    assert abs(R['dec'] - 22.01) < 0.1


def test_gw(cdciplatform, *a, **aa):
    print("running test one image at ", cdciplatform)

    endpoint = platform_endpoint(cdciplatform)

    print('endpoint', endpoint)

    R = requests.get(endpoint + "/resolver/api/v1.1/byname/GW170814").json()
    pprint.pprint(R)

    assert R['utc'] == "2017-08-14T10:30:43.500"

    R = requests.get(endpoint + "/resolver/api/v1.1/byname/GW190425").json()
    pprint.pprint(R)

    assert R['utc'] == "2019-04-25T08:18:05.000"
    assert R['duration'] == 5


def test_grb(cdciplatform, *a, **aa):
    print("running test one image at ", cdciplatform)

    endpoint = platform_endpoint(cdciplatform)

    print('endpoint', endpoint)

    R = requests.get(endpoint + "/resolver/api/v1.1/byname/GRB170105A").json()
    pprint.pprint(R)

    assert R['utc'] == "2017-01-05T06:14:07.00"
    assert R['duration'] == 2

