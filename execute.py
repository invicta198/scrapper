import flipkart
import ebay
if __name__ == '__main__':
    product = input("ENTER PRODUCT : ").strip()
    flipkart.start_task(product)
    ebay.start_task(product)