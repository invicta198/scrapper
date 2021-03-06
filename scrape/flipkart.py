import bs4
import requests
import urllib


def first_method(product_details):
    for product_detail in product_details:
        data = product_detail.findAll("div", {"class": "col col-7-12"})
        for datum in data:

            name = datum.div
            # PRINTING NAME OF EACH PRODUCT FOUND
            print("Product : {}".format(name.text))

            try:
                rating = datum.find(
                    "div", {"class": "hGSR34"})
                # PRINTING RATING OF EACH PRODUCT FOUND
                print("Rating : {}".format(rating.text))
            except Exception as e:
                print("Error Occurred {}".format(e))

            detail = datum.findAll("li", {"class": "tVe95H"})
            for k in detail:
                # PRINTING DETAILS OF EACH PRODUCT FOUND
                print("Details : {}".format(k.text))

            print("********************")


def second_method(content):
    product_line = content.findAll("div", {"class": "_3O0U0u"})
    print("Total Products : {}".format(len(product_line)))
    for i in product_line:
        for j in i:

            product_name = j.div.find("a", {"class": "_2cLu-l"})['title']
            # PRINTING NAME OF EACH PRODUCT FOUND
            print("Product : {}".format(product_name))

            try:
                rating = j.div.find(
                    "div", {"class": "niH0FQ _36Fcw_"}).text
                # PRINTING RATING OF EACH PRODUCT FOUND
                print("Rating(Number) : {}".format(rating))

                details = j.div.find("a", {"class": "_1Vfi6u"}).text
                # PRINTING DETAILS OF EACH PRODUCT FOUND
                print("Details : {}".format(details))

            except Exception as e:
                print("Error Occurred {}".format(e))

            print("********************")


def start_task(product):
    product = urllib.parse.quote_plus(
        product, safe="", encoding=None, errors=None)
    my_url = "https://www.flipkart.com/search?q={}".format(product)
    html = None

    try:
        response = requests.get(my_url)

        if response.status_code == 200:
            html = response.content.decode()

        page = bs4.BeautifulSoup(html, "html.parser")

        details = page.find_all("div", {"class": "_1-2Iqu row"})

        print(len(details))
        print("*****")
        if len(details) != 0:
            first_method(details)
        else:
            second_method(page)

    except Exception as e:
        print("Error Occurred {}".format(e))


if __name__ == '__main__':
    start_task("earphone")
