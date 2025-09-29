class Config:
    MAIN_URL = "" # Main website URL
    XML_CREATOR_PATH = "" # URL to trigger XML feed creation
    XML_PATH = "" # XML feed URL
    TEMP_DIR = "tmp" # Temporary directory for image processing
    AGGREGATORS = () # e.g., ('marketplace1', 'marketplace2')
    IMAGES_FOLDER = "images" # Base directory for saving images
    FIRST_IMAGE = "image_URL_1" # Key for the first image in the product data
    IMAGE_FILTER = "image_URL" # Prefix to filter image keys in product data
    """
    OPERATIONS is a dictionary that defines image processing operations
    for each aggregator.

    The dictionary should be of the following structure:

    {
        "aggregator_name": {
            "operation_name": value,
            ...
        },
        ...
    }

    Supported operations are:
    - "mirror": Boolean indicating whether to mirror the image or not.
    - "fit": Tuple of two integers indicating the size to fit the image to.
    - "enhance": Float indicating the brightness enhancement factor.

    Example:
    {
        "marketplace1":
            {
                "mirror": True,
                "enhance": 1.05
            },
        "marketplace2":
            {
                "fit": (1571, 2000),
                "enhance": 1.05
            }
    }
    """
    OPERATIONS = {}
