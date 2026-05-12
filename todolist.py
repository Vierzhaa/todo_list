import json
import os
import time

FILE_NAME = 'tugas.json'
jd=0.5

def muat_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def simpan_data(daftar_tugas):
    with open(FILE_NAME, 'w') as file:
        json.dump(daftar_tugas, file, indent=4)

def main():
    while True:
        daftar_tugas = muat_data()
        print("\n=== DAFTAR TUGAS ===")
        if not daftar_tugas:
            print("Belum ada tugas.")
        else:
            for t in daftar_tugas:
                status = "[V]" if t['selesai'] else "[ ]"
                print(f"{t['id']}. {status} {t['nama']}")
        
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Selesaikan Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama tugas baru: ")
            id_baru = daftar_tugas[-1]['id'] + 1 if daftar_tugas else 1
            daftar_tugas.append({"id": id_baru, "nama": nama, "selesai": False})
            simpan_data(daftar_tugas)
            print("Tugas ditambahkan!")
            time.sleep(jd)
            os.system("cls")
            
        elif pilihan == '2':
            try:
                id_target = int(input("ID tugas yang selesai: "))
                for t in daftar_tugas:
                    if t['id'] == id_target:
                        t['selesai'] = True
                        break
                simpan_data(daftar_tugas)
                print(f"Tugas {id_target} selesai!")
                time.sleep(jd)
                os.system("cls")
            except ValueError:
                print("Masukkan ID berupa angka.")
                time.sleep(jd)
                os.system("cls")

        elif pilihan == '3':
            try:
                id_hapus = int(input("Masukkan ID tugas yang ingin dihapus: "))
                daftar_baru = [t for t in daftar_tugas if t['id'] != id_hapus]
                if len(daftar_baru) < len(daftar_tugas):
                    simpan_data(daftar_baru)
                    print(f"Tugas ID {id_hapus} berhasil dihapus.")
                    time.sleep(jd)
                    os.system("cls")
                else:
                    print("ID tidak ditemukan.")
                    time.sleep(jd)
                    os.system("cls")
            except ValueError:
                print("Masukkan ID berupa angka.")
                time.sleep(jd)
                os.system("cls")
            
        elif pilihan == '4':
            os.system("cls")
            print("bye")
            break
        else:
            print("Pilihan tidak valid.")
            time.sleep(jd)
            os.system("cls")

if __name__ == '__main__':
    main()
