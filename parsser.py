import requests # Import biblioteki
from bs4 import BeautifulSoup
import csv
from datetime import datetime

start = datetime.now() # записываем время начала работы

url = 'http://kenesh.kg/ru/deputy/list/35'

# получаем основную страницу
def get_html(url):
    response = requests.get(url)
    return response.text


def get_links():
    html = get_html(url) # вызываем функцию для получения главной страницы
    soup = BeautifulSoup(html, 'html.parser') # заготовим суп
    tds = soup.find('table').find_all('td') # получаем элемент страницы
    links = []

    for td in tds: # проходимся по каждому элементу и сохраняес список
        try:
            a = td.find('a').get('href')
            if "deputy" in a:
                links.append('http://kenesh.kg' + a)
        except Exception as ex:
            print(ex) # остовляем только уникальные ссылки
    links = set(links) # f
    return links


def get_page_data(): # вызываем функцию для получения данных ч каждой страницы
    links = get_links()
    for link in links: # запускаем цикл
        response = requests.get(link).text
        try:
            soup = BeautifulSoup(response, 'html.parser') # готовим суп для обработки страницы

            try:
                name = soup.find('h3', class_='deputy-name').text.strip() # пробуем получить имя
                phone = soup.find('p', class_='mb-10').text.strip() # пробуем получить номер телефона
                # print(phone)
            except Exception as ex:
                print(ex)
                phone = 'Нет данных'

            try:
                bio = soup.find('div', id='biography').text.strip() # пробуем получить биография
                # print(len(bio))
            except Exception as ex:
                print(ex)

            with open('data.csv', 'a') as file: # записываем данные в файл
                data = (name, phone, bio)
                writer = csv.writer(file)
                writer.writerow((name,phone,bio))
                print(f'{name} записан в файл')

        except Exception as ex:
            print(ex)
    print('finish')

get_page_data()
# высчитывам время работы
stop = datetime.now()
print(stop - start)