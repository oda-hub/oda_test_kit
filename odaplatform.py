class URL(str):
    pass

class cdciplatform(str):
    pass

def platform_endpoint(cdciplatform: cdciplatform) -> URL:  
    urls = {
        "staging": 'http://dispatcher.staging.internal.odahub.io/',
        "production": 'https://dispatcher-staging.obsuks1.unige.ch/'
    }

    matching = { p:u for p,u in urls.items() if cdciplatform.endswith(p) }

    if len(matching) == 0:
        raise Exception(f"unknown platform, known: {list(urls.keys())}")
    elif len(matching) > 1:
        raise Exception(f"multiple matching platforms: {dict(matching)}")
    else:
        return list(matching.values())[0]
