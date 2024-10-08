# Скрипт для перехвата и воспроизведения HTTP-запросов

Этот репозиторий содержит скрипт на Python, который использует `mitmproxy` для перехвата HTTP(S) запросов, сделанных браузером, и сразу генерирует Python-скрипт (`replay_history.py`), который можно использовать для воспроизведения этих запросов. Сгенерированный скрипт использует библиотеку `requests` для выполнения запросов.

## Требования

- Python 3.7+
- `mitmproxy`
- Библиотека `requests` (для выполнения сгенерированного скрипта)

## Установка

1. **Установите зависимости:**

   В репозитории есть файл `requirements.txt`. Используйте следующую команду для установки всех необходимых пакетов:

   ```bash
   pip install -r requirements.txt
   ```

2. Клонируйте или загрузите этот репозиторий на ваш локальный компьютер.

## Использование

1. Запустите скрипт с использованием `mitmproxy`:

   Используйте следующую команду, чтобы запустить `mitmproxy` со скриптом:
   
   ```bash
   mitmproxy -s main.py
   ```
2. Настройте браузер на использование `mitmproxy` как прокси:

   Откройте настройки прокси в вашем браузере.
   Установите прокси-сервер на 127.0.0.1 и порт 8080

3. Выполняйте действия в браузере:

   По мере того, как вы будете пользоваться браузером, скрипт будет перехватывать HTTP(S) запросы и сразу генерировать Python-код для их воспроизведения.
   Сгенерированный код будет сохранен в файл replay_history.py.

4. Воспроизведите перехваченные запросы:

   После того как запросы будут перехвачены, вы можете запустить сгенерированный скрипт для их воспроизведения:

   ```bash
   python replay_history.py
   ```
Этот скрипт отправит все перехваченные запросы в том же порядке, в каком они были выполнены, и выведет статус-коды и текст ответа для каждого запроса.

## Как это работает
   Перехват запросов: Скрипт использует `mitmproxy` для перехвата всего HTTP(S) трафика, проходящего через него. Для каждого перехваченного запроса сохраняются URL, метод HTTP, заголовки и тело (если оно присутствует).
   
   Генерация кода на Python: Для каждого перехваченного запроса скрипт добавляет блок кода на Python в файл replay_history.py. Этот код использует библиотеку requests для отправки HTTP-запроса, аналогичного перехваченному.
   
   Воспроизведение запросов: Сгенерированный скрипт replay_history.py можно выполнить для воспроизведения всех перехваченных запросов в том же порядке.

## Пример
   Ниже приведен пример того, как может выглядеть сгенерированный код на Python:

   ```python
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
   ```
## Примечания
   При перехвате HTTPS-трафика mitmproxy действует как посредник, что позволяет ему расшифровывать и анализировать зашифрованный трафик. Для того чтобы избежать предупреждений о безопасности, вам нужно установить CA-сертификат mitmproxy в браузере.
