import asyncio
import core_logic # Nama file .so Anda (tanpa ekstensi)
import sys

async def run_bot():
    print("🚀 Pemicu Logika Biner Dimulai...")
    try:
        # Memanggil fungsi main() yang ada di dalam core_logic.so
        await core_logic.main()
    except Exception as e:
        print(f"❌ Error saat menjalankan biner: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Menjalankan loop utama
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass