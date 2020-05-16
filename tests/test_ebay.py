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
    my_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={}&_sacat=0".format(product)
    response = requests.get(my_url)
    assert response.status_code == 200


def test_response(input_value):
    product = urllib.parse.quote_plus(input_value, safe="", encoding=None, errors=None)
    my_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={}&_sacat=0".format(product)
    response = requests.get(my_url)

    html = response.content.decode()
    page = bs4.BeautifulSoup(html, "html.parser")
    all_products = page.find_all("div", {"class": "s-item__wrapper clearfix"})
    assert len(all_products) > 0 