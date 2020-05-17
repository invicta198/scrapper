import bs4
import requests
import urllib


def display_data(products):
    for i in products:
        title = i.find("h3", {"class": "s-item__title"})
        print(title.text)

        price = i.find("span", {"class": "s-item__price"})
        print(price.text)

        print("********************")


def start_task(product):
    # product = input("ENTER PRODUCT : ").strip()
    product = urllib.parse.quote_plus(
        product, safe="", encoding=None, errors=None)
    my_url = "https://www.ebay.com/sch/i.html" \
             "?_from=R40&_trksid=m570.l1313&_nkw={}&_sacat=0".format(product)

    html = None

    try:
        response = requests.get(my_url)
        if response.status_code == 200:
            html = response.content.decode()

        page = bs4.BeautifulSoup(html, "html.parser")
        all_products = page.find_all(
            "div", {"class": "s-item__wrapper clearfix"})

        print("Total Products : {}".format(len(all_products)))
        display_data(all_products)

    except Exception as e:
        print("Error Occurred {}".format(e))


if __name__ == '__main__':
    start_task("earphone")
