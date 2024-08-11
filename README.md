# EN
**GenZoomEyeIoTSearch** is a Python tool for searching IoT devices using the ZoomEye API. The tool allows users to search for hosts and web resources, providing detailed information based on various filters.

## Features
- **Host Search**: Find IoT devices using IP, hostname, ports, etc.
- **Web Search**: Discover websites and web services using filters like site, keywords, titles, and more.
- **Save Results**: Save your search results in JSON format.
- **Colorful CLI**: Uses colorama for enhanced command-line visuals.

## Installation
1. **Clone the Repository**:
```bash
git clone https://github.com/geniuszlyy/GenZoomEyeIoTSearch.git
cd GenZoomEyeIoTSearch
```
2. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

## Configuration
- **API key**: Create a `config.json` file in the root directory with your ZoomEye API key:
```json
{
    "api_key": "your_zoomeye_api_key"
}
```

## Usage
Run the program:
```bash
python GenZoomEyeIoTSearch.py
```

![image](https://github.com/user-attachments/assets/55931845-9370-4112-bc5e-2b2b44984005)


## Search Options
1. **Host Search**:
- Example Query: `country:russia +port:22`
2. **Web Search**:
- Example Query: `site:example.com +title:login`

![image](https://github.com/user-attachments/assets/1b2a4f06-c449-487d-a0b0-5bf917fac073)


## Steps
- Select the search type (1 for Host, 2 for Web)
- Enter your search query with appropriate filters
- Choose to save results if needed

## Dependencies
- `requests`: For making HTTP requests to the ZoomEye API.
- `colorama`: For colored terminal output.
- `tabulate`: For displaying data in a table format.



# RU
**GenZoomEyeIoTSearch** — это инструмент на Python для поиска IoT-устройств с использованием API ZoomEye. Инструмент позволяет пользователям искать хосты и веб-ресурсы, предоставляя подробную информацию на основе различных фильтров.

## Особенности
- **Поиск хостов**: Найдите IoT-устройства по IP, имени хоста, портам и другим параметрам.
- **Поиск веб-ресурсов**: Исследуйте сайты и веб-сервисы с использованием фильтров, таких как сайт, ключевые слова, заголовки и другие.
- **Сохранение результатов**: Сохраните результаты поиска в формате JSON.
- **Цветной интерфейс CLI**: Использует colorama для улучшенной визуализации в командной строке.

## Установка
1. **Клонирование репозитория**:
```bash
git clone https://github.com/geniuszlyy/GenZoomEyeIoTSearch.git
cd GenZoomEyeIoTSearch
```
2. **Установка зависимостей**:
```bash
pip install -r requirements.txt
```

## Конфигурация
- **API key**: Создайте файл `config.json` в корневой директории с вашим API-ключом ZoomEye:
```json
{
    "api_key": "your_zoomeye_api_key"
}
```

## Использование
Запустите программу:
```bash
python GenZoomEyeIoTSearch.py
```

![image](https://github.com/user-attachments/assets/a5718fef-1825-4a8d-a79a-b5d34a6cadbd)


## Варианты поиска
1. **Поиск хостов**:
- Пример запроса: `country:russia +port:22`
2. **Поиск веб-ресурсов**:
- Пример запроса: `site:example.com +title:login`

![image](https://github.com/user-attachments/assets/f87ab4ef-e9c2-4ef3-8eca-3d8949e68515)


## Шаги
- Выберите тип поиска (1 для хостов, 2 для веб)
- Введите ваш запрос с соответствующими фильтрами
- Выберите, хотите ли сохранить результаты

## Зависимости
- `requests`: Для выполнения HTTP-запросов к API ZoomEye.
- `colorama`: Для цветного вывода в терминале.
- `tabulate`: Для отображения данных в табличном формате.
