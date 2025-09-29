import urllib
import requests
import xmltodict
from app.config import Config
from app.argparse_singleton import args

class XMLParser:

    filename = Config.XML_PATH
    exporter_handler = Config.XML_CREATOR_PATH


    def __init__(self) -> None:
        self.product_id = None
        self.limit = None
        self.site = None
        self.data = []

        if args.force_update:
            self.__run_exporter()


    def get_products(self):
        file = urllib.request.urlopen(self.filename)
        data = file.read()
        file.close()
        self.data = xmltodict.parse(data).get("products").get("product")
        self.__filter_parent()
        self.__apply_parameters()
        return self.data


    def __run_exporter(self) -> None:
        requests.get( self.exporter_handler, timeout=120 )
        return None


    def __filter_parent(self) -> None:
        self.data = [product for product in self.data if product['type'] == 'parent']


    def __apply_parameters(self) -> None:
        if args.product_id:
            self.__get_product(args.product_id)
        if args.limit:
            self.__limit_products(args.limit)


    def __limit_products(self, n_limit) -> None:
        self.data = self.data[:n_limit]


    def __get_product(self, product_id):
        self.data = [product for product in self.data if product['product_id'] == product_id]
