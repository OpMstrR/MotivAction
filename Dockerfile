# 1. Базовий образ Python
FROM python:3.10-slim

# 2. Встановлення робочої директорії
WORKDIR /app

# 3. Копіюємо файл залежностей
COPY app/requirements.txt .

# 4. Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копіюємо весь код у контейнер
COPY app/ .

# 6. Запуск застосунку
CMD ["python", "main.py"]
