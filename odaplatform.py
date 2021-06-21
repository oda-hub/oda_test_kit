class URL(str):
    pass

class cdciplatform(str):
    pass

def platform_endpoint(cdciplatform: cdciplatform) -> URL:  
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

