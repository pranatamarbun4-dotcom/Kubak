# Gunakan Python 3.10 versi slim agar ringan dan cepat
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependency sistem (Wajib untuk tgcrypto, psutil, dan media)
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt duluan untuk Caching
COPY requirements.txt .

# Install library Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy semua file biner dan loader
# Pastikan di folder repo Anda ada: run.py, secrets.so, core_logic.so
COPY . .

# Set variabel PORT ke 8080
ENV PORT=8080

# Buka port 8080 untuk Health Check
EXPOSE 8080

# --- PERUBAHAN DI SINI ---
# Jalankan run.py (Loader) sebagai pintu masuk utama, 
# bukan main.py yang lama atau core_logic.so
CMD ["python", "main.py"]