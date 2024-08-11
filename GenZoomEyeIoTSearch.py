import requests
import urllib.parse
import json
import os
import logging
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

# Инициализация логирования
logging.basicConfig(level=logging.INFO)

# Логотип и команда помощи
LOGO = f"""
{Fore.LIGHTRED_EX}
   _____            ______                     ______           _____   _______ _____                     _     
  / ____|          |___  /                    |  ____|         |_   _| |__   __/ ____|                   | |    
 | |  __  ___ _ __    / / ___   ___  _ __ ___ | |__  _   _  ___  | |  ___ | | | (___   ___  __ _ _ __ ___| |__  
 | | |_ |/ _ \ '_ \  / / / _ \ / _ \| '_ ` _ \|  __|| | | |/ _ \ | | / _ \| |  \___ \ / _ \/ _` | '__/ __| '_ \ 
 | |__| |  __/ | | |/ /_| (_) | (_) | | | | | | |___| |_| |  __/_| || (_) | |  ____) |  __/ (_| | | | (__| | | |
  \_____|\___|_| |_/_____\___/ \___/|_| |_| |_|______\__, |\___|_____\___/|_| |_____/ \___|\__,_|_|  \___|_| |_|
                                                      __/ |                                                     
                                                     |___/                                                      
{Style.RESET_ALL}
"""

HELP_TEXT = f"""
{Fore.LIGHTYELLOW_EX}╭────────────────────────━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━────────────────────╮
| {Fore.LIGHTGREEN_EX}Usage: python {os.path.basename(__file__)}                                                    {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}Description: Search IoT data with ZoomEye API.                           {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}Commands:                                                                {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}  1) Host search: Search by IP, hostname, port, etc.                     {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}     Example: country:russia +port:22                                    {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}  2) Web search: Search websites, headers, keywords, etc.                {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}     Example: site:example.com +title:login                              {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}Instructions:                                                            {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}  - Choose search type (1 or 2)                                          {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}  - Enter query with filters                                             {Fore.LIGHTYELLOW_EX}| 
| {Fore.LIGHTGREEN_EX}  - Save results if needed                                               {Fore.LIGHTYELLOW_EX}| 
╰────────────────────────━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━────────────────────╯
"""

# Загружает API-ключ из конфигурационного файла
def load_api_key(config_file='config.json'):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config.get('api_key')
    except FileNotFoundError:
        logging.error(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Конфигурационный файл не найден.")
        raise
    except json.JSONDecodeError:
        logging.error(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Ошибка чтения конфигурационного файла.")
        raise

# Формирует URL для поиска на основе запроса и типа поиска
def build_url(query, search_type):
    base_url = "https://api.zoomeye.org/"
    search_path = "host/search" if search_type == 1 else "web/search"
    encoded_query = urllib.parse.quote_plus(query)
    return f"{base_url}{search_path}?query={encoded_query}&page=1"

# Выводит на экран доступные фильтры для поиска
def display_filters(filters, filter_type):
    print(tabulate(filters, headers=['Параметр', 'Описание']))
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» ПРИМЕР: {Fore.LIGHTGREEN_EX}{filter_type}:russia +port:21 +service:http")

# Отправляет запрос и получает результаты поиска
def fetch_results(url, api_key):
    headers = {"Authorization": f"JWT {api_key}"}
    try:
        response_data = requests.get(url, headers=headers)
        print(f"Request URL: {response_data.url}")
        print(f"Request Headers: {response_data.request.headers}")
        response_data.raise_for_status()  # Проверка на успешный запрос
        return response_data.json()
    except requests.RequestException as e:
        logging.error(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Ошибка запроса: {Fore.LIGHTRED_EX}{e}")
        print(f"Response Status Code: {response_data.status_code}")
        print(f"Response Content: {response_data.text}")
        raise

# Выводит результаты поиска на экран
def display_results(results):
    matches = results.get("matches", [])
    for index, match in enumerate(matches):
        ip_address = match.get("ip", "Неизвестно")
        port_info = match.get("portinfo", {})
        port = port_info.get("port", "Неизвестно")
        app = port_info.get("app", "Неизвестно")
        print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» "
              f"{Fore.LIGHTGREEN_EX}{index + 1}) {Fore.LIGHTBLUE_EX}IP-адрес: {Fore.LIGHTGREEN_EX}{ip_address}, {Fore.LIGHTBLUE_EX}Порт: {Fore.LIGHTGREEN_EX}{port}, {Fore.LIGHTBLUE_EX}Приложение: {Fore.LIGHTGREEN_EX}{app}")

# Сохраняет результаты поиска в файл JSON
def save_results(results, filename='results.json'):
    try:
        with open(filename, 'w') as file:
            json.dump(results, file, ensure_ascii=False, indent=4)
        logging.info(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Результаты сохранены в файл {Fore.LIGHTGREEN_EX}{filename}")
    except IOError as e:
        logging.error(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Ошибка при сохранении файла: {Fore.LIGHTRED_EX}{e}")

def main():
    print(LOGO)
    print(HELP_TEXT)
    
    # Списки фильтров для хостов и веб-ресурсов
    host_filters = [
        ["Приложение", 'app:proftd'], 
        ["Версия", 'ver:2.1'], 
        ['IP', 'ip:1.1.1.1'], 
        ['Сервис', 'service:http'],
        ['CIDR', '1.2.3.4/21'], 
        ['Имя хоста', 'google.com'], 
        ['Порт', 'port:53'], 
        ['Город', 'city:moscow'], 
        ['Страна', 'country:russia'], 
        ['ASN', 'asn:1234'], 
        ['Устройство', 'device:router'], 
        ['ОС', 'os:windows']
    ]
    web_filters = [
        ["Приложение", 'app:proftd'], 
        ['Заголовок', 'header:server'], 
        ['Ключевые слова', 'keywords:google.com'], 
        ['Описание', 'desc:github'],
        ['Название', 'title:github'], 
        ['IP', 'ip:192.168.1.1'], 
        ['Сайт', 'site:google.com'], 
        ['Город', 'city:moscow'],
        ['Страна', 'country:russia']
    ]

    # Загрузка API-ключа
    api_key = load_api_key()

    # Выбор типа поиска
    search_choice = int(input(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Что вы хотите искать?\n1) Хост 2) Веб\n=======>>>>> "))
    if search_choice == 1:
        display_filters(host_filters, "country")
    elif search_choice == 2:
        display_filters(web_filters, "country")

    search_query = input(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Введите строку поиска: ")
    request_url = build_url(search_query, search_choice)

    # Выполнение запроса и вывод результатов
    print(request_url)
    search_results = fetch_results(request_url, api_key)
    display_results(search_results)

    # Сохранение результатов
    save_choice = input(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenZoomEyeIoTSearch {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Хотите сохранить результаты? (y/n): ").lower()
    if save_choice == 'y':
        save_results(search_results)

if __name__ == "__main__":
    main()
