def platform_endpoint(cdciplatform):  
    urls = {
        "production1.2":  'https://www.astro.unige.ch/cdci/astrooda/dispatch-data',
        "staging1.2": 'http://cdcihn.isdc.unige.ch/staging-1.2/frontend/dispatch-data',
        "staging": 'http://in.internal.odahub.io/staging-1-3/dispatcher'
    }

    matching = { u:v for u,v in urls.items() if u.endswith(cdciplatform) }

    if len(matching) == 0:
        raise Exception("unknown platform")
    elif len(matching) > 1:
        raise Exception(f"multiple matching platforms: {dict(matching}")
    else:
        return list(matching.values())[0]
