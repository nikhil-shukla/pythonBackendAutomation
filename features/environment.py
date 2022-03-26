import requests
from behave import *
from utilities.configurations import getConfig
from utilities.resources import ApiResources


def after_scenario(context, scenario):

    if "library" in scenario.tags:
        url = getConfig()['API']['endpoint'] + ApiResources.delBook
        del_resp = requests.post(url, json={"ID": context.bookId}, headers=context.headers)
        assert del_resp.status_code == 200
        print(del_resp.json())
        print(del_resp.json()['msg'])
        assert 'deleted' in del_resp.json()['msg']

    else:
        pass
