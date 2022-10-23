# contoh class sederhana

class Mahasiswa:
    nama = None
    nim = None
    
    def hello(self):
        print(f'hallo {self.nama} {self.nim}')

nizar= Mahasiswa()
nizar.nama = "nizar"
nizar.nim = "20210801373"

nizar.hello()

class Abc:

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def __del__(self):
        print("delete")  

    def data(self):
        print("hello", self.nama, self.nim)

a = Abc("nizar", "20210801373")
#print(a.__dict__)

a.data()
del a