import argparse
import time

# Argparse
parser = argparse.ArgumentParser()
parser.add_argument("--template", help="")
args = parser.parse_args()

while True:
	print("test")
	time.sleep(1)
