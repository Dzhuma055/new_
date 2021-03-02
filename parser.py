# import requests
# from bs4 import BeautifulSoup
#
# url = "http://kenesh.kg/ru/deputy/list/35"
#
# def get_html(url):
#
#     response = requests.get(url)
#     return response.text
#
# def get_links():
#     html = get_html(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     tds = soup.find('table', class_='table').find_all('td')
#     links = []
#
#     for td in tds:
#         try:
#             a = td.find('a').get('href')
#             if 'deputy' in a:
#                 links.append('http://kenesh.kg' + a)
#         except Exception as ex:
#             print(ex)
#     links = set(links)
#     return links
#
#
#     links = get_links()
#     for links in links:
#          response = requests.get(link).text
#         try:
#             soup = BeautifulSoup(response, 'html.parser')
#
#         try:
#             name = soup.find('h3', class_='deputy-name').text.strip()
#             print(name)
#         except Exception as ex:
#         print(ex)
#
#         try:
#             phone = soup.find('p', class_='mb-10').text.strip()
#             print(phone)
#         except Exception as ex:
#             print(ex)
#             phone = 'нет данных'
#         try:
#             bio = soup.find('div', id='biography').text.strip()
#             print(len(bio))
#         except Exception as ex:
#         print(ex)
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
import csv


url = 'http://kenesh.kg/ru/deputy/list/35'


def get_html(url):
    response = requests.get(url)
    return response.text


def get_links():
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.find('table').find_all('td')
    links = []

    for td in tds:
        try:
            a = td.find('a').get('href')
            if "deputy" in a:
                links.append('http://kenesh.kg' + a)
        except Exception as ex:
            print(ex)
    links = set(links)
    return links

def_get_page_data
links = get_links()
for link in links:
    response = requests.get(link).text
    try:
        soup = BeautifulSoup(response, 'html.parser')

        try:
            name = soup.find('h3', class_='deputy-name').text.strip()
            print(name)
        except Exception as ex:
            print(ex)

        try:
            phone = soup.find('p', class_='mb-10').text.strip()
            print(phone)
        except Exception as ex:
            print(ex)
            phone = 'Нет данных'

        try:
            bio = soup.find('div', id='biography').text.strip()
            print(len(bio))
        except Exception as ex:
            print(ex)

    except Exception as ex:
        print(ex)



