# Gunakan base image Python
FROM python:3.8.0-slim

# Set working directory
WORKDIR /app

# Copy file requirements.txt dulu biar cache install nggak ke-reset tiap ada perubahan kecil
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua file project ke dalam container
COPY . .

# Jalankan bot
CMD ["python", "bot.py"]
