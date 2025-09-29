import os
import shutil

from app.classes.XMLParser import XMLParser
from app.classes.ImagesPipe import ImagesPipe


try:
    os.mkdir('tmp')
except FileExistsError:
    shutil.rmtree('tmp')
    os.mkdir('tmp')

products = XMLParser().get_products()

for product in products:
    product = ImagesPipe(product)
    product.set_gallery()
    product.do_operations()
    continue

shutil.rmtree('tmp')
