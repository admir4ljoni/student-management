import sys
import types

modul = types.ModuleType("mahasiswa")
modul.Mahasiswa = object
sys.modules["mahasiswa"] = modul

from menu import Menu

class DataSementara:
    pass

menu = Menu(DataSementara())
menu.jalankan()
