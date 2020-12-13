#Program Sederhana Pendataan Ekonomi OrangTua Berdasarkan Gaji dan Pengeluaran.
import pandas as pd

# inisialisasi class
class Orangtua():
    
    def __init__(self):
        # constructor class
        self.data =[]
        self.jumlah = 0
        
    def tambah_data(self, nama, jabatan, gaji):
        """
        Menambah data pada list objek
        """
        self.data.append({'Nama':nama,
                    'Jabatan':jabatan,
                    'Gaji':gaji,
                    'Kategori':''})
        self.jumlah += 1
        
    def hitung_tingkat(self, pengeluaran):
        """
        Menghitung tingkat kesejahteraan berdasarkan
        hasil pengurangan gaji dengan rata-rata pengeluaran/bulan
        """
        
        index = self.jumlah - 1
        
        if (self.data[index]['Gaji'] - pengeluaran >= 1000000):
            self.data[index]['Kategori'] = 'Sangat mampu'
            
        elif (self.data[index]['Gaji'] - pengeluaran >= 500000):
            self.data[index]['Kategori'] = 'Mampu'
            
        elif (self.data[index]['Gaji'] - pengeluaran == 0):
            self.data[index]['Kategori'] = 'Berkecukupan'
            
        else:
            self.data[index]['Kategori'] = 'Kurang mampu'
            
    def tampilkan_data(self):
        """
        Menampilkan data dari Orangtua
        """
        df = pd.DataFrame(self.data)
        
        print("="*50)
        print("Data Karyawan".center(50,' '))
        print("="*50)
        print(df)
        print("="*50)
        
        pilih = int(input("Masukkan pilihan : "))
    
    print()
    return pilih

def tambah():
    print("1. Tambahkan data")
    nama = input("Masukkan nama\t\t\t: ")
    jabatan = input("Masukkan jabatan\t\t: ")
    gaji = int(input("Masukkan gaji\t\t\t: "))
    pengeluaran = int(input("Masukkan pengeluaran/bulan\t: "))
    
    orangtua.tambah_data(nama, jabatan, gaji)
    orangtua.hitung_tingkat(pengeluaran)
    print()
        
# main program
orangtua = Orangtua() # instance dari class Karyawan
pilih = 0
while (pilih != 3):
    pilih = get_option()
    
    if (pilih == 1):
        tambah()
        
    elif (pilih == 2):
        orangtua.tampilkan_data()
        
    elif (pilih == 3):
        print("Keluar dari program!")
        
    else:
        print("Tidak ada pilihan!")
        print()
