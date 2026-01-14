import asyncio
import sys
import os

# --- PAKSA PYTHON MELIHAT FOLDER SAAT INI ---
# Langkah ini krusial agar file .so bisa ditemukan di server Linux
sys.path.append(os.getcwd()) 

async def run_bot():
    # Menampilkan daftar file untuk memastikan core_encrypted.so ada di sana
    print("📂 File di direktori saat ini:", os.listdir(os.getcwd()))
    print("🚀 Pemicu Logika Terenkripsi Dimulai...")
    
    try:
        # Import biner core_encrypted.so (tanpa ekstensi)
        import core_encrypted 
        print("✅ Modul 'core_encrypted' berhasil dimuat!")
        
        # Memicu fungsi utama di dalam biner secara eksplisit
        # Pastikan di kode asli Anda fungsi utamanya bernama 'main'
        await core_encrypted.main() 
        
    except ImportError as e:
        print(f"❌ Python gagal menemukan file .so: {e}")
        print("💡 Tips: Pastikan nama file di GitHub/Koyeb adalah 'core_encrypted.so'")
        sys.exit(1)
    except AttributeError:
        print("❌ Error: Fungsi 'main()' tidak ditemukan di dalam core_encrypted.so")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Kesalahan sistem saat menjalankan biner: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Menjalankan loop utama asyncio
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass
