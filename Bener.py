import os
import datetime
import csv
import pandas as pd
from pathlib import Path

def Login():
    os.system('cls')
    print("="* 115)
    print('LOGIN'.center(115) )
    print('=' * 115)
    Username = input("Masukkan Nama Pengguna Anda: ")
    Password = input("Masukkan Kata Sandi Anda: ")
    with open('akun.csv', 'r') as filecsv:
        reader = csv.DictReader(filecsv)
        for row in reader:
            if row['Username'] == Username and row['Password'] == Password:
                print("LOGIN Berhasil!")
                return True
    print("Username atau Password salah")
    input('Tekan Enter Untuk Melanjutkan')
    Login ()

def Register():
     os.system('cls')
     print("="* 115)
     print('REGISTER'.center(115) )
     print('=' * 115)
     Username = input('Masukkan Nama Pengguna Anda: ')
     Password = input('Masukkan Kata Sandi Sesuai Keinginan Anda: ')
     with open("akun.csv", mode='r') as filecsv:
          reader = csv.DictReader(filecsv)
          for row in reader:
               if row['Username'] == Username:
                    print('Usename Sudah Digunakan!')
                    return
     with open('akun.csv', mode='a') as filecsv:
          writer = csv.writer(filecsv)
          writer.writerow([Username, Password])
     print('Register Berhasil!')
    
def LoginAdmin():
     os.system('cls')
     print("="* 115)
     print('LOGIN ADMIN'.center(115) )
     print('=' * 115)
     Username = input('Masukkan Nama Pengguna Anda: ')
     Password = input('Masukkan Kata Sandi Anda: ')
     with open('admin.csv', mode='r') as filecsv:
          reader = csv.DictReader(filecsv)
          for row in reader:
               if row["Username"] == Username and row['Password'] == Password:
                    print("LOGIN Anda Sebagai Admin Berhasil")
                    input('Tekan Enter Untuk Melanjutkan')
               else:
                    print('Usename atau Password yang anda masukkan salah')
                    input('Tekan Enter Untuk Melanjutkan ')
                    LoginAdmin()

def cekAkunRegister():
     if not(Path("akun.csv").is_file()):
          with open('akun.csv', mode='w', newline=' ') as filecsv:       
               header = csv.DictWriter(filecsv, fieldnames=['Username', 'Password'], delimiter= ",")
               header.writeheader()
               filecsv.close()
               Register()
               input("\n Enter untuk melanjutkan")
               tampilanAwal()
     else:
          Register()
          input('\n Enter Untuk Melanjutkan')
          tampilanAwal()
    
def cekAkunAdmin():
     if not(Path('admin.csv').is_file()):
          with open('admin.csv', mode='w' , newline=" ") as filecsv:
               header = csv.DictWriter(filecsv, fieldnames=['Username','Password' ], delimiter= ",")
               header.writeheader()
               writer = csv.writer(filecsv)
               writer.writerow(["admin","admin987"])
               filecsv.close()
     LoginAdmin()

riwayatpembelian = []

def pesanan():
     global pilihan_jasa, harga, input_jasa,waktu_jam,total, total_semua
     os.system('cls')
     print('=' * 50)
     print('|','SELAMAT DATANG DI APLIKASI "GARAP"'.center(52), '|')
     print('=' * 50)
     print(" \n Apakah Ada yang Bisa Saya Bantu Untuk Merawat Lahan Pertanian Anda?")
     print("=" * 50)
     print('| ','NO |','      Pilihan Jasa      |Harga (per 2 jam)|')
     print("=" * 50)
     print('| ','1. | Pembajakan (traktor)    | Rp. 200.000    |')  
     print('| ','2. | Penggemburan (traktor)  | Rp. 175.000    |')
     print('| ','3. | Pemanenan (traktor)     | Rp. 400.000    |')
     print('| ','4. | penanaman Bibit         | Rp.  50.000    |')
     print('| ','5. | Pemupukan               | Rp.  50.000    |')
     print('| ','6. | Irigasi                 | Rp.  50.000    |')
     print('| ','7. | Penyemprotan pestisida  | Rp.  75.000    |')
     print('| ','8. | Pemangkasan             | Rp.  50.000    |')
     print('| ','9. | Penyiangan Gulma        | Rp.  30.000    |')
     print("| ","0. | Keluar                                   |")
     print('=' * 50)
     total = 0
     try:
        input_jasa = int(input('Masukkan pilihan Anda [1-9]: '))
        waktu_jam = int(input("Masukkan lama waktu perawatan (dalam jam): "))
        if input_jasa not in range(1, 10):
         raise ValueError("Pilihan jasa tidak valid!")
     except ValueError as e:
      print(f"Input tidak valid: {e}")
      input("Tekan Enter untuk mengulang.")
      pesanan()
     if input_jasa == 1 :
          pilihan_jasa = 'Pembajakan (traktor)'
          harga = waktu_jam * 200000
          total += harga
     elif input_jasa == 2:
          pilihan_jasa = 'Penggemburan (traktor)'
          harga = waktu_jam * 175000
          total += harga
     elif input_jasa == 3:
          pilihan_jasa = 'Pemanenan (traktor)'
          harga = waktu_jam * 400000
          total += harga
     elif input_jasa == 4:
          pilihan_jasa = 'penanaman Bibit'
          harga = waktu_jam *  50000
          total += harga
     elif input_jasa == 5:
          pilihan_jasa = 'Pemupukan'
          harga = waktu_jam *  50000
          total += harga
     elif input_jasa == 6:
          pilihan_jasa = 'Irigasi'
          harga = waktu_jam *  50000
          total += harga
     elif input_jasa == 7:
          pilihan_jasa = 'Penyemprotan pestisida '
          harga = waktu_jam *  75000
          total += harga
     elif input_jasa == 8:
          pilihan_jasa = 'Pemangkasan'
          harga = waktu_jam *  50000
          total += harga
     elif input_jasa == 9:
          pilihan_jasa = 'Penyiangan Gulma'
          harga = waktu_jam *  30000
          total += harga
     elif input_jasa == 0:
          tampilanAwal()
     else:
          print('Inputan Anda Salah')
          return
     riwayatpembelian.append({ 
          'pilihan jasa' : pilihan_jasa,
          'pesanan_hari' : '',
          'pesanan_waktu' : '',
          'harga': harga
        })

def pilihHari():
     global hari
     hari = input("Silahkan masukkan hari yang anda butuhkan untuk merawat lahan pertanian anda [ketik 0 jika tidak ada]:  ").lower()
     riwayatpembelian[-1]['pesanan_hari'] = hari
     if hari == "senin":
          jadwalSenin()
     elif hari == 'selasa':
          jadwalSelasa()
     elif hari == 'rabu':
          jadwalRabu()
     elif hari == 'kamis':
          jadwalKamis()
     elif hari == 'jumat':
          jadwalJumat()
     elif hari == 'sabtu':
          jadwalSabtu()
     elif hari == 'Minggu':
          jadwalMinggu()
     else:
          print("Inputan salah, Silahkan Ulangi Lagi")
          return
     jam = input('\nAnda Ingin Memesan pada Jam berapa, [ex: 04:00-06.00]:  ') #jika memilih 2 jam (jika memlih 1 jam tinggal menyesuaikan)
     riwayatpembelian[-1]['pesanan_waktu'] = jam
         
global jam,df,mydata
def jadwalSenin():
     os.system('cls')
     print("=" * 58) 
     print('|','JADWAL KOSONG BURUH TANI DI HARI SENIN'.center(54), "|" )   
     print('=' * 58)
     df = pd.read_csv('jadwalSenin.csv')
     df.index+=1
     print(df)
     print('-'*58)

def jadwalSelasa():
     os.system('cls')
     print("=" * 58) 
     print('|','JADWAL KOSONG BURUH TANI SDI HARI SELASA'.center(54), "|" )   
     print('=' * 58)
     df = pd.read_csv('jadwalSelasa.csv')
     df.index+=1
     print(df)
     print('-'*58)

def jadwalRabu():
     os.system('cls')
     print("=" * 58) 
     print('|','JADWAL KOSONG BURUH TANI DI HARI RABU'.center(54), "|" )   
     print('=' * 58)
     df = pd.read_csv('jadwalRabu.csv')
     df.index+=1
     print(df)
     print('-'*58)

def jadwalKamis():
     os.system('cls')
     print("=" * 58) 
     print('|','JADWAL KOSONG BURUH TANI DI HARI KAMIS'.center(54), "|" )   
     print('=' * 58)
     df = pd.read_csv('jadwalKamis.csv')
     df.index+=1
     print(df)
     print('-'*58)

def jadwalJumat():
     os.system('cls')
     print("=" * 58) 
     print('|','JADWAL KOSONG BURUH TANI DI HARI JUMAT'.center(54), "|" )   
     print('=' * 58)
     df = pd.read_csv('jadwalJumat.csv')
     df.index+=1
     print(df)
     print('-'*58)

def jadwalSabtu():
     os.system('cls')
     print("=" * 58) 
     print('|','JADWAL KOSONG BURUH TANI DI HARI SABTU'.center(54), "|" )   
     print('=' * 58)
     df = pd.read_csv('jadwalSabtu.csv')
     df.index+=1
     print(df)
     print('-'*58)

def jadwalMinggu():
     os.system('cls')
     print("=" * 58) 
     print('|','JADWAL KOSONG BURUH TANI DI HARI MINGGU'.center(54), "|" )   
     print('=' * 58) 
     df = pd.read_csv('jadwalMinggu.csv')
     df.index+=1
     print(df)
     print('-'*58)

def simpanRiwayatPembelian():
     nama_file = 'riwayat_pembelian.csv'
     file_baru = not os.path.exists(nama_file)
     with open(nama_file, mode='a', newline='', encoding='utf-8') as file:
          fieldnames = ['pilihan jasa', 'pesanan_hari', 'pesanan_waktu', 'harga']
          writer = csv.DictWriter(file, fieldnames=fieldnames)
          if file_baru:
            writer.writeheader()
          for pembelian in riwayatpembelian:
            writer.writerow(pembelian)

def rincianPesanan():
    os.system('cls')
    print('Nama Pemesan Jasa: ', nama)
    print('nomor handphone yang dapat di hubungi: ',hp)
    print('Lokasi atau alamat: ', lokasi)
    waktu = datetime.datetime.now()
    print('waktu pemesanan: ', waktu)
    print('=' * 115)
    print('| ',"RINCIAN PESANAN ANDA".center(111), '|')
    print('=' * 115)  
    global riwayatpembelian, total
    if not riwayatpembelian:
        print("Belum ada jasa yang dipesan.")
        return
    print(f"{'No.':<5} {'Jasa':<30} {'Hari':<15} {'Waktu':<20} {'Harga':<10}")
    print('-' * 115)
    total = 0
    for index, pembelian in enumerate(riwayatpembelian, start=1):
        print(f"{index:<5} {pembelian['pilihan jasa']:<30} {pembelian['pesanan_hari']:<10}    {pembelian['pesanan_waktu']:<20}  Rp{pembelian['harga']:<10}")
        total += pembelian['harga']
    print('=' * 115)
    print(f"Total Keseluruhan: Rp{total}")
    print('=' * 115)
    print('Jika ada kesalahan inputan dalam memesan jasa garap kami, kami akan mengkonfirmasi melalui nomor handphone anda')

#admin
def admin():
     os.system('cls')
     print("=" * 115)
     print('Selamat datang admin'.center(115))
     print('=' * 115)
     print('Apa yang ingin anda lakukan: ')
     print("1. LIHAT RIWAYAT PEMBELIAN PEMBELI")
     print("2. MENGUBAH STATUS KETERSEDIAAN ")
     print('0. KELUAR')
     inputan_admin = int(input("Masukkan pilihan anda, [1], [2] : "))
     if inputan_admin == 1 :
          lihatRiwayatPembelian()
     elif inputan_admin == 2 :
          Ubah_Status()
          
     elif inputan_admin == 0:
         tampilanAwal()
     else:
          print('Inputan yang anda masukkan salah')

def lihatRiwayatPembelian():
     os.system('cls')
     print('=' * 60)
     print('Riwayat Pembelian Pembeli'.center(60))
     print('=' * 60)
     df = pd.read_csv('riwayat_pembelian.csv')
     df.index+=1
     print(df)
     print('=' * 60)
     input('Tekan Enter Untuk Keluar! ')
     admin()
   
def Ubah_Status():
    os.system('cls')
    print('=' * 60)
    print('Ubah Status Ketersediaan'.center(60))
    print('=' * 60)
    # Menentukan hari
    hari_admin = input('Masukkan hari yang ingin diubah jadwalnya (senin-minggu): ').capitalize()
    if hari_admin not in ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']:
        print('Hari tidak valid, silakan coba lagi.')
        input('Tekan Enter untuk kembali ke menu.')
        return admin()
    nama_file = f"jadwal{hari_admin}.csv"
    if not Path(nama_file).is_file():
        print(f"File untuk jadwal {hari_admin} tidak ditemukan!")
        input('Tekan Enter untuk kembali.')
        return admin()
    
    with open(nama_file, 'r', newline='', encoding='utf-8') as file:
        reader = list(csv.reader(file))
        inputan_index = int(input('Masukkan nomor baris yang ingin diubah (1-10): ')) - 1
    if inputan_index < 1 or inputan_index > len(reader) - 1:
        print(f"Baris {inputan_index} tidak valid. File hanya memiliki {len(reader) - 1} data (header tidak dihitung).")
        return
    header = reader[0]
    data = reader[1:]  
    data.pop(inputan_index - 1)

    with open(nama_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)  
        writer.writerows(data)
        print(f"Baris {inputan_index} berhasil dihapus dari file {nama_file}.")

    jam_ubah = input('Masukkan jam yang akan di ubah statusnya [04:00-05:00]: ')
    status_baru = input('Masukkan status baru (Tersedia/Tidak Tersedia): ').capitalize()

# nambah index
    with open(nama_file, 'r', newline='', encoding='utf-8') as file:
        reader = list(csv.reader(file))

    baris_baru = [hari_admin, jam_ubah, status_baru ]
    header = reader[0]
    data = reader[1:]
    data.insert(inputan_index - 1, baris_baru)

    with open(nama_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Menulis header kembali
        writer.writerows(data)
    print(f"Baris baru berhasil ditambahkan di indeks {inputan_index} pada file {nama_file}.")

def tampilanAwal():
    global lokasi, hp, nama
    os.system('cls')
    print("=" * 115)
    print("SELAMAT DATANG DI GARAP".center(115))
    print('APLIKASI JASA PERAWATAN LAHAN PERTANIAN'.center(115))
    print("=" * 115)
    print("Silahkan Pilih melakukan register atau login terlebih dahulu :")
    print("1. LOGIN")
    print("2. REGISTER")
    print("3. LOGIN ADMIN")
    
    input_login = int(input("Masukkan pilihan anda, [1], [2], [3] : "))
    if input_login == 1:
        Login()
        input("Enter Untuk Melanjutkan")
        os.system('cls')
        nama = input('Masukkan nama anda: ')
        hp = input('Masukkan nomor handphone Anda: ')
        pesanan()
        pilihHari()
        while True:
            lanjut = input('Apakah ada pesanan lagi? (ya/tidak): ').lower()
            if lanjut == 'ya':
                pesanan()
                pilihHari()
            elif lanjut == 'tidak':
                lokasi = input('Masukkan lokasi dan alamat lahan pertanian anda: ')
                print('Baiklah, berikut rincian pesanan Anda:')
                rincianPesanan()
                simpanRiwayatPembelian()
                print('Terima Kasih Sudah Memesan Jasa Kami!')
                break
            else:
                print("Input tidak valid, harap masukkan 'ya' atau 'tidak'.")

    elif input_login == 2: 
        cekAkunRegister()
    elif input_login == 3:
        cekAkunAdmin()
        admin()
    else:
        input('\n Yang Anda Masukkan Tidak Valid, Enter Jika Ingin Melanjutkan')
tampilanAwal()


