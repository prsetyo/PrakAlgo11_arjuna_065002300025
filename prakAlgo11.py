import sys

def awal():
    awal = input('Masukan nama File: ')
    if awal == 'contoh.txt':
        main()
    else:
        print("File tidak ditemukan")

def baca_data():
    with open('contoh.txt', 'r') as f:
        print(f.read())
        main()

def cari_rata_rata():
    with open('contoh.txt', 'r') as f:
        nilai_mahasiswa = [float(line.strip().split()[-1]) for line in f.readlines()]
        if nilai_mahasiswa:
            rata_rata = sum(nilai_mahasiswa) / len(nilai_mahasiswa)
            print(f"Nilai rata-rata mahasiswa: {rata_rata:.2f}")
        else:
            print("Tidak ada data mahasiswa.")

def update_nilai_praktikum():
    nim = input("Masukkan NIM mahasiswa yang akan diupdate: ")
    nilai_baru = float(input("Masukkan nilai praktikum baru: "))

    with open('contoh.txt', 'r') as f:
        lines = f.readlines()

    found = False
    with open('contoh.txt', 'w') as f:
        for line in lines:
            data = line.strip().split()
            if data and data[0] == nim:
                line = f"{nim} {data[1]} {nilai_baru}\n"
                found = True
            f.write(line)

    if found:
        print(f"Nilai praktikum mahasiswa dengan NIM {nim} berhasil diupdate.")
    else:
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

def simpan():
    # Proses simpan data
    print("Perubahan nilai berhasil disimpan.")
    main()

def main():
    print('''
    [MENU]
    1. Baca Data
    2. Mencari Nilai Rata-rata Mahasiswa
    3. Update Nilai Praktikum
    4. Simpan Perubahan
    5. Exit
    ''')
    
    choose_menu = int(input('Silahkan Pilih: '))
    
    if choose_menu == 1:
        baca_data()
    elif choose_menu == 2:
        cari_rata_rata()
    elif choose_menu == 3:
        update_nilai_praktikum()
    elif choose_menu == 4:
        simpan()
    elif choose_menu == 5:
        sys.exit(0)
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-5.")
        main()

if __name__ == '__main__':
    awal()
