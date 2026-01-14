import asyncio
import sys
import os

async def run_bot():
    print("🚀 Pemicu Logika Biner Dimulai...")
    
    try:
        # --- SOLUSI: Import di dalam fungsi ---
        import core_logic 
        
        print("🔗 Menghubungkan ke fungsi utama biner...")
        # Memanggil fungsi main() yang ada di dalam core_logic.so
        await core_logic.main() 
        
    except ImportError as e:
        print(f"❌ File 'core_logic.so' tidak ditemukan atau rusak: {e}")
        sys.exit(1)
    except AttributeError:
        print("❌ Error: Fungsi 'main()' tidak ditemukan di dalam core_logic.so")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error saat menjalankan biner: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Menjalankan loop utama
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass
