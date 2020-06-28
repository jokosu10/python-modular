import requests

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'\nSuccess access to {url} {response.status_code}')
        print(f'\nContent {response.text}')
    else:
        print(f'Oops, ada there is error about request {response.status_code}')
except Exception as e:
    print(f'There is an error {e}')
print('Program Ended')
