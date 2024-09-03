import requests

# Воспроизведение перехваченных запросов

# Запрос 1: GET https://example.com
response_1 = requests.get(
    url='https://example.com',
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html",
    }
)
print(f'Status: {response_1.status_code}')
print(response_1.text)

# Запрос 2: POST https://example.com/login
response_2 = requests.post(
    url='https://example.com/login',
    headers={
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
    },
    data='username=user&password=pass'
)
print(f'Status: {response_2.status_code}')
print(response_2.text)