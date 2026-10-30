from mahasiswa import Mahasiswa

class Menu:
    def __init__(self, data_mahasiswa):
        self.data_mahasiswa = data_mahasiswa

    def jalankan(self):
        while True:
            print("=== DATA MAHASISWA ===")
            print("1. Tambah Mahasiswa")
            print("2. Cari Mahasiswa")
            print("3. Hapus Mahasiswa")
            print("0. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                nim = input("NIM: ")
                nama = input("Nama: ")

                mahasiswa = Mahasiswa(nim, nama)

                if self.data_mahasiswa.tambah(mahasiswa):
                    print("Data berhasil ditambahkan")
                else:
                    print("NIM sudah terdaftar")

            elif pilihan == "2":
                nim = input("NIM yang dicari: ")
                mahasiswa = self.data_mahasiswa.cari(nim)

                if mahasiswa:
                    print(mahasiswa.tampilkan_info())
                else:
                    print("Data tidak ditemukan")

            elif pilihan == "3":
                nim = input("NIM yang dihapus: ")

                if self.data_mahasiswa.hapus(nim):
                    print("Data berhasil dihapus")
                else:
                    print("Data tidak ditemukan")

            elif pilihan == "0":
                print("Program selesai")
                break

            else:
                print("Pilihan tidak valid")
