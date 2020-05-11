import click
from scrape import ebay, flipkart


@click.command()
@click.option('--product', default='laptop', prompt="ENTER PRODUCT ", help='Name of Item you Wish to Search')
def start_task(product):
    product = product.strip()
    flipkart.start_task(product)
    ebay.start_task(product)


if __name__ == '__main__':
    start_task()