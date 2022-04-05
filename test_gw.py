import logging
from odaexperiments.run import test_func

logging.basicConfig(level="INFO")
logging.getLogger("oda_api").setLevel("INFO")
    

platform_endpoint = lambda x:test_func(
    "odaplatform", 
    "platform_endpoint", 
    ref="66bbd60")(cdciplatform=x)


def test_gw_im(cdciplatform, *args, **kwargs):
    endpoint = platform_endpoint(cdciplatform) + "/dispatch-data"
    
    print('Dispatcher at:', endpoint)
    
    from oda_api.api import DispatcherAPI
    
    disp = DispatcherAPI(url=endpoint)
    
    par_dict={
        "DEC": -44.95,
        "RA": 47.75,
        "T1": "2017-08-14T10:30:38.500",
        "T2": "2017-08-14T10:30:53.500",
        "T_format": "isot",
        "contour_levels": "50,90",
        "detector": "H1",
        "do_cone_search": "false",
        "instrument": "gw",
        "level_threshold": 10,
        "product": "gw_skymap_image",
        "product_type": "Real",
        "radius": 0.0,
        "src_name": "gw170814"
    }

    data_collection = disp.get_product(**par_dict)
    
    data_collection.show()
    
def test_gw_strain(cdciplatform, *args, **kwargs):
    endpoint = platform_endpoint(cdciplatform) + "/dispatch-data"
    
    print('Dispatcher at:', endpoint)
    
    from oda_api.api import DispatcherAPI
    
    disp = DispatcherAPI(url=endpoint)
    
    par_dict={
        "DEC": -44.95,
        "RA": 47.75,
        "T1": "2017-08-14T10:30:38.500",
        "T2": "2017-08-14T10:30:53.500",
        "T_format": "isot",
        "detector": "H1",
        "fmax": 400,
        "fmin": 30,
        "instrument": "gw",
        "product": "gw_strain",
        "product_type": "Real",
        "src_name": "gw170814",
        "whiten": "true"
    }
    
    data_collection = disp.get_product(**par_dict)
    
    data_collection.show()
    
def test_gw_sgram(cdciplatform, *args, **kwargs):
    endpoint = platform_endpoint(cdciplatform) + "/dispatch-data"
    
    print('Dispatcher at:', endpoint)
    
    from oda_api.api import DispatcherAPI
    
    disp = DispatcherAPI(url=endpoint)
    
    par_dict={
        "DEC": -44.95,
        "RA": 47.75,
        "T1": "2017-08-14T10:30:38.500",
        "T2": "2017-08-14T10:30:53.500",
        "T_format": "isot",
        "detector": "H1",
        "instrument": "gw",
        "product": "gw_spectrogram",
        "qmax": 64,
        "qmin": 4,
        "product_type": "Real",
        "src_name": "gw170814",
        "whiten": "true"
    }
    
    data_collection = disp.get_product(**par_dict)
    
    data_collection.show()
