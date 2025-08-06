
# Курсовая по ООП
import requests
import os
import json

token = input("Введите токен Яндекс_диска: ")
text = 'PY-130'
filename = f'{text}.jpeg'

# Функция скачивания картинки с сайта кошки
def download_cat_foto(text):
    url_foto_cat = f'https://cataas.com/cat/says/{text}'
    response = requests.get(url_foto_cat)
    with open ('PY-130.jpeg', 'wb') as f:
        f.write(response.content)

# Функция создания папки на яндекс диске
def create_folder_YD():
    url_folder = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {
            'path': 'PY-130'
    }
    headers = {
        'Authorization': f'OAuth {token}'
    }
    response1 = requests.put(url_folder, params=params, headers=headers)

# Функция создания запроса загрузки файла в созданную папку яндекс диска
def response_upload_in_folder():
    url_load = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    params = {
        'path': f'PY-130/{filename}'
    }

    headers = {
        'Authorization': f'OAuth {token}'
    }

    response2 = requests.get(url_load, params=params, headers=headers)
    url_load_pic = response2.json()['href']

    # Загружаем файл на Яндекс Диск
    with open(f'{filename}', 'rb') as f:
        response3 = requests.put(url_load_pic, files={'file': f})
        response3.raise_for_status()
    print("Файл успешно загружен на Яндекс.Диск")

download_cat_foto(text)
create_folder_YD()
response_upload_in_folder()

# Собираем информацию о файле
file_info = {
    'filename': filename,
    'size_bytes': os.path.getsize(filename)
        }
with open('file_info.json', 'w', encoding='utf-8') as json_file:
    json.dump(file_info, json_file, ensure_ascii=False, indent=4)

print("Информация о файле сохранена в file_info.json")


