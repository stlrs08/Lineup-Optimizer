from requests import get
from requests.exceptions import RequestException
from contextlib import closing

def simple_get(url):
    """
    Makes HTML get request on url and returns response if it is HTML/XML.
    If not, returns None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """ Returns True if resp is HTML, False otherwise """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and
            content_type is not None and
            content_type.find('html') > -1)

def log_error(e):
    """ Prints errors to terminal """
    print("----------")
    print(e)
    print("----------")