class DataMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah(self, mahasiswa):
        if mahasiswa.nim in self.data:
            return False

        self.data[mahasiswa.nim] = mahasiswa
        return True

    def cari(self, nim):
        return self.data.get(nim)

    def hapus(self, nim):
        if nim in self.data:
            del self.data[nim]
            return True

        return False

if __name__ == "__main__":
    from types import SimpleNamespace

    data = DataMahasiswa()
    mhs = SimpleNamespace(nim="23001", nama="Budi")

    print("Tambah:", data.tambah(mhs))
    print("Cari:", data.cari("23001").nama)
    print("Hapus:", data.hapus("23001"))
    print("Cari lagi:", data.cari("23001"))
