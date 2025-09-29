import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
	'--limit',
	dest='limit',
	type=int,
	help='Max product number for tests'
)

parser.add_argument(
	'--product',
	dest='product_id',
	type=str,
	help='Insert product ID for a specific images update'
)

parser.add_argument(
	'--force_update',
	dest='force_update',
	action='store_true',
	help='Force remote XML update'
)

args = parser.parse_args()
