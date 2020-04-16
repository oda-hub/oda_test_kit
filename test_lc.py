def test_lcpick_largebins(cdciplatform, *a, **aa):
    print("running test test_lcpick_largebins at ",cdciplatform)

def test_timesystem_ct(*a, **aa):
    import requests
    r = requests.get("https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/converttime/REVNUM/2000/IJD")
    print(r.text)

def test_scsystem_ephs(*a, **aa):
    import requests
    r = requests.get("https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/scsystem/api/v1.0/ephs/UTC/2002-01-01T00:00:00/IJD")
    print(r.text)

def test_fail(*a, **aa):
    raise Exception("example fail")
