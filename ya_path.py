import requests


token = ''
path = ''

def ya_folder(path, token):
    url = f"https://cloud-api.yandex.net/v1/disk/resources?path={path}"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Authorization': token }
    response = requests.put(url=url, headers=headers)
    return str(response)

def check_folder(path, token,v='v1', preview_size='', Accept = 'application/json'):
    url = f'https://cloud-api.yandex.net/{v}/disk/resources?path={path}&preview_size={preview_size}'
    headers = {'Accept': Accept , 'Authorization': token }
    response = requests.get(url=url, headers= headers)
    return str(response)


