import logging
from odaexperiments.run import test_func

logging.basicConfig(level="INFO")
logging.getLogger("oda_api").setLevel("INFO")
    

platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="66bbd60")(cdciplatform=x)

def test_ls_im(cdciplatform, *args, **kwargs):
    endpoint = platform_endpoint(cdciplatform) + "/dispatch-data"
    print('Dispatcher at:', endpoint)
    
    from oda_api.api import DispatcherAPI
    
    disp = DispatcherAPI(url=endpoint)
    
    par_dict={
        "DEC": -0.013294166666667,
        "RA": 40.66962125,
        "T1": "2017-03-06T13:26:48.000",
        "T2": "2017-03-06T15:32:27.000",
        "T_format": "isot",
        "data_release": 9,
        "image_band": "g",
        "image_size": 3.0,
        "instrument": "legacysurvey",
        "pixel_size": 1.0,
        "product": "legacy_survey_image",
        "product_type": "Real",
        "src_name": "ngc1068"
    }

    data_collection = disp.get_product(**par_dict)
    
    data_collection.show()


def test_ls_ph(cdciplatform, *args, **kwargs):
    endpoint = platform_endpoint(cdciplatform) + "/dispatch-data"
    
    print('Dispatcher at:', endpoint)
    
    from oda_api.api import DispatcherAPI
    
    disp = DispatcherAPI(url=endpoint)
    
    par_dict={
        "DEC": -0.013294166666667,
        "RA": 40.66962125,
        "T1": "2017-03-06T13:26:48.000",
        "T2": "2017-03-06T15:32:27.000",
        "T_format": "isot",
        "data_release": 9,
        "instrument": "legacysurvey",
        "product": "legacy_survey_photometry",
        "product_type": "Real",
        "radius_photometry": 1.0,
        "src_name": "ngc1068"
    }

    data_collection = disp.get_product(**par_dict)
    
    data_collection.show()
