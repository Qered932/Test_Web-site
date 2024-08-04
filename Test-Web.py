import requests
from bs4 import BeautifulSoup

class TestWeb:
    def __init__(self, url, stop_links=[]):
        self.url = url
        self.stop_links = stop_links
    def test(self):
        links_end = []
        response = requests.get(self.url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find_all('a')
            for a in content:
                link = a.get('href')
                if link in stop_links:
                    print('Запрешенная ссылка!!!')
                    links_end.append(link)
                else:
                    print(f'Ссылка: {link}')
            return links_end
        else:
            print('Сайт не отвечает')

url = input('ВВедите ссылку для проверки: ')
print('Введите запрешенные ссылки\nДля запуска проверки сайта нажмите пробел')
stop_links = []

while True:
    link = input('-')
    if link == ' ':
        break
    else:
        stop_links.append(link)

web = TestWeb(url, stop_links)
links = web.test()

with open('FileTheEnd.txt', 'w') as file:
    for i in links:
        file.write('Запрещенная ссылка: ' + i + '\n')