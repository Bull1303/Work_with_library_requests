import requests

# Задача №1

list_heroes = ['Hulk', 'Captain America', 'Thanos']

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)

all_heroes = {}
heroes = {}

for item in response.json():
    all_heroes[item['name']] = item['powerstats']['intelligence']

for hero in list_heroes:
    intelligence = all_heroes.get(hero)
    heroes[hero] = intelligence

print(f'Самый умный супергерой из заданного списка - {max(heroes)}')

# Задача №2

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = '!!!!!ЗДЕСЬ ВСТАВИТЬ СВОЙ ТОКЕН ЯНДЕКС ДИСК!!!!!'
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'OAuth {TOKEN}'
}


def upload_file(loadfile, savefile, replace=True):
    """Загрузка файла.
    savefile: Путь к файлу на Диске
    loadfile: Путь к загружаемому файлу
    replace: true or false Замена файла на Диске"""
    res = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    if 'href' not in res.keys():
        print(f"Ошибка: {res['error']}")
    else:
        with open(loadfile, 'rb') as f:
            requests.put(res['href'], files={'file': f})
            print(f'Файл {file} загружен успешно!')


if __name__ == '__main__':
    files_list = ['test.txt', 'test2.txt']
    for file in files_list:
        upload_file(file, 'Netology/' + file)
