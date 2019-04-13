import os
import atexit
import urllib.request
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def exit_handler():
	print(f"\n[Status] Finished downloading images")


def get_image(target):
	if not os.path.exists("./downloaded_images/"):
		os.makedirs("./downloaded_images/")
		print(f"[Status] Creating directory: '/downloaded_images'")

	print(f"[Status] Downloading following images:")
	for i in range(1, 32):
		page_url = target + str(i).zfill(2) + ".html"
		page = requests.get(page_url)
		img_elements = BeautifulSoup(page.text, 'html.parser').find_all("img")
		for img in img_elements:
			img_url = target[:-6] + img["src"]
			split = urllib.parse.urlsplit(img_url)
			img_name = split.path.split('/')[-1]
			dl_dir = "./downloaded_images/" + img_name
			urllib.request.urlretrieve(img_url, dl_dir)
			print(f"{img_name}")
		
get_image("https://apod.nasa.gov/apod/ap1901")  # January 2019

atexit.register(exit_handler)