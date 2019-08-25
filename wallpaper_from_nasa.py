#!/usr/bin/python
# -*- coding: utf-8 -*-

# Script para buscar imagens do dia do site da nasa e colocar como fundo
# Author: Lucas Arantes <lucas_arantes10@hotmail.com>

import requests
import urllib
import os
import subprocess

from bs4 import BeautifulSoup
from datetime import date


def set_image_backgroud(image_name):
    """
    Coloca a imagem como papel de parede.
    """
    subprocess.call(['feh', '--bg-scale', image_name])


def download_imagem(url_imagem, destino):
    """
    Realiza o donwload da imagem na caminho de destino.
    """
    urllib.urlretrieve(url_imagem, destino)


def get_url_imagem_from_nasa_url():
    """
    Busca a url da imagem do dia no site da nasa.
    """
    url_nasa = "https://apod.nasa.gov/apod/"
    resp = requests.get(url_nasa)
    try:
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            image_link = soup.find(name="img").get_attribute_list("src")[0]
            return "%s%s" % (url_nasa, image_link)
    except AttributeError:
        print("Sem imagens para o dia de hoje.")
        return None


def main():
    """
    Função principal, busca, baixa e colcoa como papel de parede a
    'Picture of the day' disponível no site da nasa.
    """
    image_path = "/home/lucas/Imagens/nasa_imagens"
    current_date = date.today()
    path_image_name = "%s/imagem_%s.jpg" % (image_path,
                                            current_date.strftime("%Y%m%d"))
    if not os.path.exists(path_image_name):
        image_url = get_url_imagem_from_nasa_url()
        if image_url:
            download_imagem(image_url, path_image_name)
        else:
            path_image_name = image_path

    set_image_backgroud(path_image_name)


if __name__ == '__main__':
    main()
