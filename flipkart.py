import bs4
from bs4 import BeautifulSoup
import requests
import urllib


def first_method(product_details):
    for product_detail in product_details:
        data = product_detail.findAll("div", {"class": "col col-7-12"})
        for datum in data:

            name = datum.div
            print("Product : {}".format(name.text))  # PRINTING NAME OF EACH PRODUCT FOUND

            try:
                rating = datum.find("div", {"class": "hGSR34"})
                print("Rating : {}".format(rating.text))  # PRINTING RATING OF EACH PRODUCT FOUND
            except Exception as e:
                print("")
                # print("Error Occurred {}".format(e))

            detail = datum.findAll("li", {"class": "tVe95H"})
            for k in detail:
                print("Details : {}".format(k.text))  # PRINTING DETAILS OF EACH PRODUCT FOUND

            print("********************")


def second_method(content):
    product_line = content.findAll("div", {"class": "_3O0U0u"})
    print("Total Products : {}".format(len(product_line)))
    for i in product_line:
        for j in i:

            product_name = j.div.find("a", {"class": "_2cLu-l"})['title']
            print("Product : {}".format(product_name))  # PRINTING NAME OF EACH PRODUCT FOUND

            try:
                rating = j.div.find("div", {"class": "niH0FQ _36Fcw_"}).text
                print("Rating(Number) : {}".format(rating))  # PRINTING RATING OF EACH PRODUCT FOUND

                details = j.div.find("a", {"class": "_1Vfi6u"}).text
                print("Details : {}".format(details))  # PRINTING DETAILS OF EACH PRODUCT FOUND

            except Exception as e:
                print("")
                # print("Error Occurred {}".format(e))

            print("********************")


def start_task():
    product = input("ENTER PRODUCT : ").strip()
    product = urllib.parse.quote_plus(product, safe="", encoding=None, errors=None)
    my_url = "https://www.flipkart.com/search?q={}".format(product)
    # click.echo(my_url)
    # print (my_url)
    html = None

    # Use exception handling to handle any runtime exception
    try:
        # It's a pythonic way to use context statement `with` whenever opening or closing a resource.
        response = requests.get(my_url)

        if response.status_code == 200:
            html = response.content.decode()

        page = bs4.BeautifulSoup(html, "html.parser")

        details = page.find_all("div", {"class": "_1-2Iqu row"})

        if len(details) != 0:
            first_method(details)
        else:
            second_method(page)

        print(my_url)
    except Exception as e:
        print("Error Occurred {}".format(e))


if __name__ == '__main__':
    start_task()