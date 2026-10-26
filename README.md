# Book Catalog API

Сервис для управления каталогом книг на **FastAPI**.  
Позволяет добавлять книги, просматривать список и искать по автору.  


## Запуск приложения

### 1. Клонирование репозитория

git clone https://github.com/OvcharovMichail/book-catalog-api.git
cd book-catalog-api

### 2. Создание и активация виртуального окружения

python -m venv .venv

Windows
.\.venv\Scripts\Activate.ps1

Linux / macOS
source .venv/bin/activate

### 3. Установка зависимостей

pip install -r requirements.txt

### 4. Запуск сервера

Режим разработки (с авто-перезагрузкой):
uvicorn app_final:app --reload

Обычный режим (без --reload, для стабильной работы):
uvicorn app_final:app --host 0.0.0.0 --port 8000

После запуска откройте в браузере:

Веб-интерфейс: http://127.0.0.1:8000/
Swagger UI (документация API): http://127.0.0.1:8000/docs

### 5. Запуск тестов

Установите зависимости для тестов:
pip install -r requirements-dev.txt

Запустите тесты:
python -m pytest -v

### Переменные окружения
APP_NAME - Название приложения
APP_VERSION - Версия приложения
APP_AUTHOR - Автор проекта
Для локальной настройки используйте .env.example как шаблон или передавайте переменные через терминал:

Windows
$env:APP_VERSION="2.0.0"; uvicorn app_final:app --reload
Linux / macOS
APP_VERSION=2.0.0 uvicorn app_final:app --reload

### Диагностика и логи
Логи: Все события выводятся в консоль в формате:
Время - Уровень - Сообщение

Проверка работоспособности: GET /health → {"status": "ok"}

Версия: GET /version → {"name": "...", "version": "...", "author": "..."}