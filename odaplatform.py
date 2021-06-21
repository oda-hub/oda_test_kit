class URL(str):
    pass

class cdciplatform(str):
    pass

def platform_endpoint(cdciplatform: cdciplatform) -> URL:  
    urls = {
        "production1.2":  'https://www.astro.unige.ch/cdci/astrooda/dispatch-data',
        "staging1.2": 'http://cdcihn.isdc.unige.ch/staging-1.2/frontend/dispatch-data',
        "staging": 'http://dispatcher.staging.internal.odahub.io/'
    }

    matching = { p:u for p,u in urls.items() if cdciplatform.endswith(p) }

    if len(matching) == 0:
        raise Exception(f"unknown platform, known: {list(urls.keys())}")
    elif len(matching) > 1:
        raise Exception(f"multiple matching platforms: {dict(matching)}")
    else:
        return list(matching.values())[0]
