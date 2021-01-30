# DEF DASHBOARD
def dashboard():
    print('+-------------------------------------------------+')
    print('|                SELAMAT DATANG DI                |')
    print('|    SELAMAT DATANG DI RENTAL MOBIL KELOMPOK      |')
    print('|                    CARE CAR                     |')
    print('+-------------------------------------------------+')

# DEF tabel harga
def tabel():
    print('\n ')
    print('+-------------------------------------------------+')
    print('|             LIST HARGA RENTAL MOBIL             |')
    print('+-------------------------------------------------+')
    print('| Kode | Nama Mobil                | Tarif/hari   |')
    print('|   a  | HONDA BRIO                | RP.100k/hari |')
    print('|   b  | YAMAHA SUPRA              | RP.200k/hari |')
    print('|   c  | MITSHUBITSI XPANDER       | RP.200k/hari |')
    print('|   d  | SUZUKI CARRY              | RP.80k/hari  |')
    print('|   e  | DAIHATSU SIGRA            | RP.150k/hari |')
    print('+-------------------------------------------------+')

# DEF struct
def struct():
    print('\n ')
    print('+-------------------------------------------------+')
    print('|                   DATA PENYEWA                  |')
    print('+-------------------------------------------------+')
    print("Nama           : "+str(nama))
    print("Alamat         : "+str(alamat))
    print("Merk Mobil     : "+str(merk))
    print('+-------------------------------------------------+')
    print('Total Biaya    : Rp.',"{:,}".format(int(total)).replace(',','.'))
    print('+-------------------------------------------------+')

#DASHBOARD
dashboard()


ulang='y'
while ulang=='y':

    # input question 1
    qs1 = input ( 'Ada yang bisa kami bantu ? (y/n) : ')
    # akhir input question 1
   
    # kondisi 1 (qs1)
    if qs1 == "y":
        print('\n ')
        print('+-------------------------------------------------+')
        print('|            Apa Yang Akan Anda Lakukan           |')
        print('+-------------------------------------------------+')
        print('| a. Rental Langsung                              |')
        print('| b. Booking Mobil                                |')
        print('+-------------------------------------------------+')

        # input question 2   
        qs2 = input( 'Apa yang ingin anda lakukan         : ')
        # akhir input question 2

        # input pilihan Mobil RENTAL LANGSUNG
        if qs2 == "a":
            tabel()

            # INPUTAN PILIHAN MOBIL
            mobil = input ('Input Kode mobil  : ')

            # INPUTAN DATA DIRI (rental)
            nama = input  ('Input nama anda   : ')
            alamat = input('Input alamat anda : ')
            lama = int(input( 'Input jumlah hari : '))
            # akhir INPUTAN DATA DIRI (rental)

            # MOBIL YANG DI PILIH
            if mobil == "a" :
                merk ="HONDA BRIO"
                harga = 100000
            elif mobil == "b" :
                merk ="YAMAHA SUPRA"
                harga = 200000
            elif mobil == "c":
                merk ="MITSHUBITSI XPANDER"
                harga = 200000
            elif mobil == "d":
                merk ="SUZUKI CARRY"
                harga = 80000
            elif mobil == "e":
                merk ="SUZUKI CARRY"
                harga = 150000
            else :
                print('OKE')

            # PROSES
            total= harga * lama 

            # OTPUT STRUCT
            struct()
            print('Bagi penyewa kami mengucapkan terima kasih atas ')
            print('kepercayaannya Dan silahkan mengambil mobil yang \nsudah diswa di Parkiran depan Terima kasih')
            print('\n ')

        # input pilihan Mobil BOOKING
        elif qs2 =="b":
            tabel()

            # INPUTAN PILIHAN MOBIL
            mobil = input ('Input Kode mobil  : ')

            # INPUTAN DATA DIRI
            nama = input  ('Input nama anda   : ')
            alamat = input('Input alamat anda : ')
            lama = int(input( 'Input jumlah hari : '))
            tanggal = input("Masukan Tanggal Booking : ")

            # MOBIL YANG DI PILIH
            if mobil == "a" :
                merk ="HONDA BRIO"
                harga = 100000
            elif mobil == "b" :
                merk ="YAMAHA SUPRA"
                harga = 200000
            elif mobil == "c":
                merk ="MITSHUBITSI XPANDER"
                harga = 200000
            elif mobil == "d":
                merk ="SUZUKI CARRY"
                harga = 80000
            elif mobil == "e":
                merk ="SUZUKI CARRY"
                harga = 150000
            else :
                print('oky')

            # PROSES
            dp = harga * lama * 0.2
            total= harga * lama - dp

            # OTPUT STRUCT
            struct()

            print('Bagi penyewa kami mengucapkan terima kasih atas ')
            print('kepercayaannya Dan silahkan mengambil mobil yang \nsudah dibooking pada tanggal',str(tanggal))
            print('\n ')

        else :
            print('pilihan tidak ada')
                    
        ulang=input("Input Data Baru (y/n)?     : ")
        if ulang=="n":
                print('Baik Terimakasih')
                break
    # akhir kondisi 1 (qs1)


    # kondisi 2 (qs2)
    elif qs1 == "n":
        print('Baik Terimakasih')
        break


    # kondisi 3
    else :
        print('pilihan tidak ada')
     
    

