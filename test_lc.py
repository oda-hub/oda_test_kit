def test_lcpick_largebins(cdciplatform, *a, **aa):
    print("running test test_lcpick_largebins at ",cdciplatform)


def test_jemx_lc(dispatcher_long_living_fixture, dispatcher_local_mail_server):
    from oda_api.api import DispatcherAPI
    disp = DispatcherAPI(url=dispatcher_long_living_fixture)
    exp_time = int(time.time()) + 5000
    secret_key = 'secretkey_test'
    # let's generate a valid token
    token_payload = {
        "sub": "mtm@mtmco.net",
        "name": "mmeharga",
        "exp": exp_time,
        "tem": 0,
        "mstout": "True",
        "mssub": "True",
        "roles": ["general", "integral-private-qla"]
    }
    encoded_token = jwt.encode(token_payload, secret_key, algorithm='HS256')
    par_dict = {
        "src_name": "4U 1700-377",
        "RA": "270.80",
        "DEC": "-29.80",
        "T1": "2021-05-01",
        "T2": "2021-05-05",
        "T_format": "isot",
        "instrument": "jemx",
        "osa_version": "OSA11.0",
        "radius": "4",
        "max_pointings": "50",
        "integral_data_rights": "all-private",
        "jemx_num": "1",
        "E1_keV": "3",
        "E2_keV": "20",
        "product_type": "Real",
        "detection_threshold": "5",
        "product": "jemx_lc",
        "time_bin": "4",
        "time_bin_format": "sec",
        "catalog_selected_objects": "1,2,3",
        "selected_catalog": '{"cat_frame": "fk5", "cat_coord_units": "deg", "cat_column_list": [[0, 1, 2], ["GX 5-1", "MAXI SRC", "H 1820-303"], [96.1907958984375, 74.80066680908203, 66.31670379638672], [270.2771301269531, 270.7560729980469, 275.914794921875], [-25.088342666625977, -29.84027099609375, -30.366628646850586], [0, 1, 0], [0.05000000074505806, 0.05000000074505806, 0.05000000074505806]], "cat_column_names": ["meta_ID", "src_names", "significance", "ra", "dec", "FLAG", "ERR_RAD"], "cat_column_descr": [["meta_ID", "<i8"], ["src_names", "<U10"], ["significance", "<f8"], ["ra", "<f8"], ["dec", "<f8"], ["FLAG", "<i8"], ["ERR_RAD", "<f8"]], "cat_lat_name": "dec", "cat_lon_name": "ra"}',
        "token": encoded_token
    }

    data_collection_lc = disp.get_product(**par_dict)

    data_collection_lc.show()

    l_output = data_collection_lc.as_list()
    print('l_output: \n', l_output)
    assert len(l_output) == 2
    assert l_output[0]['prod_name'] == 'jemx_lc_0_H1820m303'
    assert l_output[0]['meta_data:']['src_name'] == 'H 1820-303'
    assert l_output[1]['prod_name'] == 'jemx_lc_1_MAXISRC'
    assert l_output[1]['meta_data:']['src_name'] == 'MAXI SRC'
