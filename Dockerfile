# Gunakan Python 3.10 versi slim agar ringan dan cepat
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Install dependency sistem yang WAJIB ada untuk library 'tgcrypto' dan 'psutil'
# Kami juga menambahkan 'ffmpeg' karena bot Telegram biasanya memerlukannya untuk media
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

# --- BAGIAN PENTING UNTUK KECEPATAN ---
# Copy requirements.txt DULUAN sebelum copy file lain.
# Ini agar Docker melakukan "Caching". Saat Anda cuma ganti .env,
# Docker TIDAK AKAN install ulang pip (hemat waktu 2-3 menit).
COPY requirements.txt .

# Install library Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy sisa semua file, TERMASUK .env dan main.py Anda
COPY . .

# Set variabel PORT default ke 8080 (sesuai script Anda)
ENV PORT=8080

# Buka port 8080 agar Koyeb bisa mendeteksi bot "Healthy"
EXPOSE 8080

# Jalankan script (Pastikan nama file script Anda sudah diubah jadi main.py)
CMD ["python", "main.py"]