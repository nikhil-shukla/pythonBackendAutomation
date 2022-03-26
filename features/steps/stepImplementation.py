import requests
from behave import *

from utilities.configurations import getConfig, getAccessToken
from utilities.payloads import buildPayloadFromDB, addBookpayload
from utilities.resources import ApiResources


@given('the book details which needed to be added to library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookpayload('masfnfdhdf', '433')


@when('we execute the AddBook API method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers)


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response = context.response.json()
    context.bookId = response['ID']
    print(context.bookId)
    assert response['Msg'] == "successfully added"


@given('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = addBookpayload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.headers = getAccessToken()
    context.url = 'https://api.github.com/user'
    context.url2 = 'https://api.github.com/user/repos'


@when('I hit gitRepo API of github')
def step_impl(context):
    response = requests.get(context.url, headers=getAccessToken())
    print(response.status_code)
    context.response = context.se.get(context.url2)
    # print(context.response.json())


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
