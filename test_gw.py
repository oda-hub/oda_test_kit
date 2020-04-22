def test_timesystem_ct(*a, **aa):
    import requests
    r = requests.get("https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/converttime/REVNUM/2000/IJD")
    print(r.text)

def test_scsystem(*a, **aa):
    import requests
    r = requests.get("https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/scsystem/api/v1.0/sc/3000/0/0")
    print(r.text)


def test_scwlist(*a, **aa):
    import requests
    import time
    t1 = time.time() - 24*3600*21
    t2 = time.time() - 24*3600*19
    s ="https://www.astro.unige.ch/cdci/astrooda/dispatch-data/gw/timesystem/api/v1.0/scwlist/cons/{}/{}?&ra=83&dec=22&radius=200.0&min_good_isgri=1000".format(
            time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t1)),
            time.strftime("%Y-%m-%dT%H:00:00", time.gmtime(t2)),
        )
    print(s)

    r = requests.get(s)

    print(r.json())

    assert len(r.json()) > 0
