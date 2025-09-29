import os
import urllib
from PIL import Image, ImageOps, ImageEnhance
from app.config import Config



class ImagesPipe():
    """
    Class for downloading and processing images from a product gallery.
    """

    FIRST_IMAGE = Config.FIRST_IMAGE
    IMAGE_FILTER = Config.IMAGE_FILTER
    TEMP_FOLDER = Config.TEMP_DIR
    IMAGES_FOLDER = Config.IMAGES_FOLDER

    def __init__(self, product) -> None:
        self.product = product
        self.gallery = {}


    def do_operations(self) -> None:

        """
        Download images from the given product gallery.

        :return: None
        :rtype: None
        """
        self.download_images()


    def get_folder_name(self) -> str:
        """
        Return the folder name of the product.

        The folder name is determined by the product SKU.

        :return: The folder name of the product
        :rtype: str
        """
        return self.product.get("sku")


    def set_gallery(self) -> None:
        """
        Set the product gallery by filtering the product dictionary
        based on the image filter.

        :return: None
        """
        self.gallery = {
            key : value for key, value
            in self.product.items()
            if key.startswith( self.IMAGE_FILTER)
        }


    def download_images(self) -> None:
        """
        Download images from the given product gallery.

        The images are first downloaded to a temporary directory, then
        processed by the configured aggregators. The processed
        images are then saved to the configured images folder.

        :return: None
        :rtype: None
        """
        for image_key , image in self.gallery.items():
            print(image)
            file = urllib.parse.urlparse(image)

            temp_dir = os.path.join( self.TEMP_FOLDER, self.get_folder_name() )
            self.create_folder_tree( temp_dir )

            # Define the temporary file path
            tmp_file_path = os.path.join(
                temp_dir,
                os.path.basename(file.path)
            )

            urllib.request.urlretrieve(image, tmp_file_path)

            for aggregator in Config.AGGREGATORS:
                aggregator_folder = os.path.join(
                    self.IMAGES_FOLDER,
                    aggregator,
                    self.get_folder_name()
                )

                self.create_folder_tree( aggregator_folder )
                self._operation(
                    aggregator=aggregator,
                    image=Image.open(tmp_file_path),
                    image_key=image_key,
                    save_path=os.path.join( aggregator_folder, os.path.basename(file.path) )
                )


    def create_folder_tree(self, folder):
        """
        Create a folder tree at the specified directory.

        If the directory does not exist, then create it recursively.

        :param folder: The directory to create
        :return: None
        """
        if not os.path.exists(folder):
            os.makedirs(folder)


    def _operation(self, aggregator, image, image_key, save_path):
        operations = Config.OPERATIONS.get(aggregator)
        if operations.get("fit"):
            image = ImageOps.fit( image, operations.get("fit") )
        if operations.get("mirror"):
            image = ImageOps.mirror(image)
        if operations.get("enhance") and image_key == self.FIRST_IMAGE:
            image = self.__default_image_enhance(image, operations.get("enhance") )
        self.__save_image( image, save_path )


    def __default_image_enhance(self, image, factor=1.05):
        """
        Default image enhancement operation.

        Enhance the brightness of an image by the given factor.

        :param image: The image to be enhanced
        :param factor: The brightness enhancement factor. Defaults to 1.05
        :return: The enhanced image
        """
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(factor)
        return image


    def __save_image(self, image, save_path):
        """
        Save the given image to the specified path.

        :param image: The image to be saved
        :param save_path: The path to save the image to
        :return: None
        """
        image.save(save_path)
