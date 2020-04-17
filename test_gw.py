def test_timesystem_ct(*a, **aa):
    import requests
    r = requests.get("https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/converttime/REVNUM/2000/IJD")
    print(r.text)

def test_scsystem(*a, **aa):
    import requests
    r = requests.get("https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/scsystem/api/v1.0/sc/3000/0/0")
    print(r.text)
