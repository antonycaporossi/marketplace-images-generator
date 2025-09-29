# Marketplace Images Generator

Automated image processing tool that parses XML product feeds, downloads images, and generates marketplace-specific versions based on configurable requirements.

## Features

- 📦 Parse XML product feeds with product data
- 🖼️ Batch download product images
- 🔄 Apply marketplace-specific transformations (mirror, resize, enhance)
- ⚙️ Fully configurable operations per marketplace
- 🎯 Support for multiple aggregators/marketplaces
- 🚀 CLI arguments for testing and specific product updates

## Supported Operations

- **Mirror**: Flip images horizontally
- **Fit**: Resize images to specific dimensions
- **Enhance**: Adjust image brightness

## Requirements

- Python 3.7+
- See `requirements.txt` for package dependencies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/marketplace-images-generator.git
cd marketplace-images-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your settings:
```bash
cp config.sample.py config.py
```

4. Edit `config.py` with your marketplace settings:
```python
class Config:
    MAIN_URL = "https://yoursite.com"
    XML_PATH = f"{MAIN_URL}/path/to/feed.xml"
    AGGREGATORS = ('marketplace1', 'marketplace2')
    OPERATIONS = {
        "marketplace1": {
            "mirror": True,
            "enhance": 1.05
        },
        "marketplace2": {
            "fit": (1571, 2000),
            "enhance": 1.05
        }
    }
```

## Usage

### Basic Usage

Process all products from the XML feed:
```bash
python xml_parser.py
```

### CLI Arguments

**Limit products for testing:**
```bash
python xml_parser.py --limit 10
```

**Process a specific product:**
```bash
python xml_parser.py --product PRODUCT_SKU
```

**Force XML feed update before processing:**
```bash
python xml_parser.py --force_update
```

**Combine arguments:**
```bash
python xml_parser.py --force_update --limit 5
```

## Configuration

### Config Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `MAIN_URL` | string | Your main website URL |
| `XML_CREATOR_PATH` | string | URL to trigger XML feed creation |
| `XML_PATH` | string | XML feed URL |
| `TEMP_DIR` | string | Temporary directory for processing |
| `AGGREGATORS` | tuple | List of marketplace identifiers |
| `IMAGES_FOLDER` | string | Base directory for saving images |
| `FIRST_IMAGE` | string | Key for the first product image |
| `IMAGE_FILTER` | string | Prefix to filter image keys |
| `OPERATIONS` | dict | Image operations per marketplace |

### Operations Configuration

Define custom operations for each marketplace:

```python
OPERATIONS = {
    "marketplace_name": {
        "mirror": True,           # Boolean: flip horizontally
        "fit": (width, height),   # Tuple: resize to dimensions
        "enhance": 1.05           # Float: brightness factor (1.0 = no change)
    }
}
```

## Project Structure

```
marketplace-images-generator/
├── app/
│   ├── classes/
│   │   ├── ImagesPipe.py      # Image processing pipeline
│   │   └── XMLParser.py        # XML feed parser
├── images/                     # Generated images (created automatically)
├── tmp/                        # Temporary files (created automatically)
├── argparse_singleton.py       # CLI argument parser
├── config.py                   # Your configuration (create from sample)
├── config.sample.py            # Configuration template
├── requirements.txt            # Python dependencies
└── xml_parser.py              # Main entry point
```

## How It Works

1. **Parse XML**: Reads product data from configured XML feed
2. **Filter Products**: Extracts only parent products with images
3. **Download Images**: Downloads all product images to temporary directory
4. **Process Images**: Applies marketplace-specific operations
5. **Save Results**: Organizes processed images by marketplace and SKU

## Example Output

```
images/
├── marketplace1/
│   ├── PRODUCT_SKU_001/
│   │   ├── image1.jpg
│   │   └── image2.jpg
│   └── PRODUCT_SKU_002/
│       └── image1.jpg
└── marketplace2/
    ├── PRODUCT_SKU_001/
    │   ├── image1.jpg
    │   └── image2.jpg
    └── PRODUCT_SKU_002/
        └── image1.jpg
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For issues, questions, or contributions, please open an issue on GitHub.

## Changelog

### v1.0.0
- Initial release
- XML parsing support
- Image download and processing
- Configurable marketplace operations
- CLI arguments for testing