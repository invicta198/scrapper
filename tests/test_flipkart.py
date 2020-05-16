import urllib
import bs4
import pytest
import requests


@pytest.fixture
def input_value():
    n = "earphone"
    return n


def test_response_code(input_value):
    product = urllib.parse.quote_plus(input_value, safe="", encoding=None, errors=None)
    my_url = "https://www.flipkart.com/search?q={}".format(product)
    response = requests.get(my_url)
    assert response.status_code == 200


def test_response(input_value):
    product = urllib.parse.quote_plus(input_value, safe="", encoding=None, errors=None)
    my_url = "https://www.flipkart.com/search?q={}".format(product)
    response = requests.get(my_url)

    html = response.content.decode()
    page = bs4.BeautifulSoup(html, "html.parser")
    details_1 = page.find_all("div", {"class": "_1-2Iqu row"})
    details_2 = page.find_all("div", {"class": "_3O0U0u"})
    total = len(details_1) + len(details_2)
    assert total > 0