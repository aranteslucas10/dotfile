#!/usr/bin/python
# -*- coding: utf-8 -*-

# Download and set background image from the picture of the day
# Author: Lucas Arantes <lucas_arantes10@hotmail.com>

import requests
import urllib
import os
import subprocess
import argparse

from bs4 import BeautifulSoup
from datetime import date


NASA_URL = "https://apod.nasa.gov/apod/"


def set_image_backgroud(image_path):
    """ Set a background image using feh """
    subprocess.call(['feh', '--bg-scale', image_path])


def image_download(url, path):
    """ Download image in path """
    urllib.urlretrieve(url, path)


def get_image_url_from_nasa_url():
    """ Find image url from nasa site """
    response = requests.get(NASA_URL)
    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            link_image = soup.find(name="img").get_attribute_list("src")[0]
            return "%s%s" % (NASA_URL, link_image)
    except AttributeError:
        print("No image today.")
        return None


def main(local_path):
    """ Main function, find, download, and set background image """
    current_date = date.today()
    path_image_name = "%s/imagem_%s.jpg" % (local_path,
                                            current_date.strftime("%Y%m%d"))
    if not os.path.exists(path_image_name):
        url_image = get_image_url_from_nasa_url()
        if url_image:
            image_download(url_image, path_image_name)
        else:
            path_image_name = local_path
    set_image_backgroud(path_image_name)


parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True,
                    dest="path", help="local path to put the images")

if __name__ == '__main__':
    args = parser.parse_args()
    main(args.path)
