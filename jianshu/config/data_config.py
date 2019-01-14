
class Globals(object):
    # cas_id
    Id = 0
    name = 1
    url = 2
    run = 3
    request_methods = 4
    headers = 5
    precondition = 6
    depend_id = 7
    depend_data = 8
    depend_field = 9
    data = 10
    expect = 11
    result = 12


def get_Case_Id():
    return Globals().Id


def get_Case_name():
    return Globals().name


def get_Case_url():
    return Globals().url


def get_is_run():
    return Globals().run


def get_request_methods():
    return Globals().request_methods


def get_Case_headers():
    return Globals().headers


def get_Case_precondition():
    return Globals().precondition


def get_depend_id():
    return Globals().depend_id


def get_depend_data():
    return Globals().depend_data


def get_depend_field():
    return Globals().depend_field

def get_Case_data():
    return Globals().data

def get_expect():
    return Globals().expect

def get_result():
    return Globals().result


def get_headers_value():
    return {
    "cookie":'sss'
    }
