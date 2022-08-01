import requests
def api_request(response , url):

    """
    Call the api, converts the results section into a json and return the data, the html status code and the url of the next page
    This function could be unpacked into two functions
    :param response the results liks that the data is appended to:
    :param url the url of the next page of results:
    :return next_url, extracted value of the next page of results:
    :return status, the html status code, primarily for testing as many operations will fail without this:
    """
    call = requests.get(url)
    status = call.status_code
    next_url = call.json()["next"]
    response.append(call.json()["results"])

    return response, next_url, status

def api_call():
    """
    Creates a emtpy parameter called response that has the imported requests appended as pages
    To add all the data to one "page" would require the document to be unpacked and repacked which would
    add time so it was decided to loop through the pages instead
    :return: response, all the pages of starship data extracted from the api call
    """
    response = []
    response, next_url, status = api_request(response, "https://swapi.dev/api/starships")

    while next_url is not None:
        place_holder1, next_url, status = api_request(response , next_url)
    return response

