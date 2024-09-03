from mitmproxy import http
import json

# Файл, в который будет записан генерируемый Python-код
output_file = "replay_history.py"

# Открываем файл для записи сгенерированного кода
with open(output_file, 'w', encoding='utf-8') as f:
    # Начало файла с импортами
    f.write("import requests\n\n")
    f.write("# Воспроизведение истории запросов\n\n")


# Функция, которая будет сохранять каждый перехваченный запрос и генерировать код
def request(flow: http.HTTPFlow) -> None:
    entry = {
        "url": flow.request.url,
        "method": flow.request.method,
        "headers": dict(flow.request.headers),
        "body": flow.request.text
    }

    # Открываем файл для дозаписи сгенерированного кода
    with open(output_file, 'a', encoding='utf-8') as f:
        # Получаем индекс запроса на основе текущего размера файла
        # Он используется для создания переменных ответа, уникальных для каждого запроса
        i = sum(1 for line in open(output_file, 'r', encoding='utf-8') if 'response_' in line)

        f.write(f"# Запрос {i + 1}: {entry['method']} {entry['url']}\n")

        # Запись метода и URL
        f.write(f"response_{i + 1} = requests.{entry['method'].lower()}(\n")
        f.write(f"    url='{entry['url']}',\n")

        # Добавление заголовков, если они есть
        if entry['headers']:
            f.write(f"    headers={json.dumps(entry['headers'], indent=4, ensure_ascii=False)},\n")

        # Добавление тела запроса, если оно есть
        if entry['body']:
            f.write(f"    data={json.dumps(entry['body'], ensure_ascii=False)}\n")
        else:
            f.write("\n")

        # Завершение записи запроса
        f.write(f")\n\n")

        # Опционально: добавляем вывод статуса и содержимого ответа для отладки
        f.write(f"print(f'Status: {{response_{i + 1}.status_code}}')\n")
        f.write(f"print(response_{i + 1}.text)\n\n")

    print(f"Запрос {i + 1} сохранен в {output_file}")

