# Kode Warna Teks
MERAH    = '\033[31m'
HIJAU    = '\033[32m'
KUNING   = '\033[33m'
BIRU     = '\033[34m'
MAGENTA  = '\033[35m'
CYAN     = '\033[36m'
# Style Font
TEBAL         = '\033[1m'
REDUP         = '\033[2m'  # Bikin teks agak abu-abu/tipis
MIRING        = '\033[3m'  # Catatan: Gak semua terminal dukung miring
GARIS_BAWAH   = '\033[4m'
BERKEDIP      = '\033[5m'  # Bikin teks kedip-kedip (retro abis!)
NEGATIF       = '\033[7m'  # Tukar posisi warna teks ama warna background
GARIS_BAWAH = '\033[4m'

RESET    = '\033[0m'

print(f'\n\n\n\n{TEBAL}SELAMAT DATANG DI Croissant Doré{RESET}')
print(f'\n\n{TEBAL}    ----- DAFTAR MENU -----{RESET}\n\n')
mastermenu = []
menumakanan = {

    "NK" : {"nama": 'Nasi Kebuli', "harga": 15000},
    "AR" : {"nama": 'Ayam Rica', "harga": 10000},
    "AB" : {"nama": 'Ayam Balado', "harga": 10000},
    "FF" : {"nama": 'French Fries', "harga": 7000},
    "NP" : {"nama": 'Nasi Padang', "harga": 15000},
    "NG" : {"nama": 'Nasi Goreng', "harga": 13500},
    "MG" : {"nama": 'Mie Goreng', "harga": 7500},
    "MR" : {"nama": 'Mie Rebus', "harga": 7500},
    "KG" : {"nama": 'Kwetiau Goreng', "harga": 8000},
    "KR" : {"nama": 'Kwetiau Rebus', "harga": 8000},
    "LG" : {"nama": 'Lele Goreng', "harga": 8000},
    "AG" : {"nama": 'Ayam Goreng', "harga": 8000},
    "GK" : {"nama": 'Nasi Goreng Kambing', "harga": 16500},
    "MA" : {"nama": 'Mie Ayam', "harga": 12500},
    "AF" : {"nama": 'Ayam Fillet', "harga": 10000}
    }
menuminuman = {

    "ET": {"nama": 'Es Teh', "harga": 4500},
    "EK": {"nama": 'ES Kelapa', "harga": 5000},
    "AD": {"nama": 'Air Putih Dingin', "harga": 3500},
    "LT": {"nama": 'Lemon Tea', "harga": 7500},
    "TH": {"nama": 'Teh Hangat', "harga": 4500},
    "AH": {"nama": 'Air Putih Hangat', "harga": 3500},
    "JJ": {"nama": 'Jus Jeruk', "harga": 5000},
    "SD": {"nama": 'Susu Putih Dingin', "harga": 5000},
    "SH": {"nama": 'Susu Putih Hangat', "harga": 5000},
    "MD": {"nama": 'Susu Milo Dingin', "harga": 5000},
    "EC": {"nama": 'Es Cappucino', "harga": 5000}
    }
keranjangmenumak = []
keranjangmenumin = []
mastermenu.append(menumakanan)
mastermenu.append(menuminuman)

while True:

        print(f"\n         {GARIS_BAWAH}{TEBAL}{MIRING}MENU MAKANAN{RESET}\n")
        while True:

                for kodemak , detailmak in mastermenu[0].items():
                    harga_idrmak = f"{detailmak['harga']:,}".replace(",", ".")
                    print(f'{TEBAL}[{kodemak}]{RESET} {MIRING}{detailmak["nama"].ljust(25)}{RESET} : {TEBAL}{HIJAU}Rp{harga_idrmak}{RESET}')

                while True:
                    pesanmak = input('\nMASUKAN KODE MAKANAN :  ').upper()
                    if pesanmak in mastermenu[0]:
                        break
                    else:
                       print('MASUKAN KODE YANG TERDAFTAR! ')

                while True:
                    try:
                        porsimak = int(input('BERAPA PORSI :  '))
                        if porsimak > 0:
                            break
                        else:
                           print('MASUKAN JUMLAH PORSI DENGAN BENAR!  ')
                    except ValueError:
                        print(f'MASUKAN DENGAN ANGKA!  ')
                pmakanan = {

                            "nama" : pesanmak,
                            "porsi" : porsimak
                        }
                keranjangmenumak.append(pmakanan)
                
                print(f'\n{TEBAL}KERANJANG ANDA SAAT INI:\n{RESET}')
                jumtotmak = 0
                for menumak in keranjangmenumak:
                    nama_makanan = mastermenu[0][menumak["nama"]]['nama']
                    porsi_makanan = menumak["porsi"]
                    subtmak = mastermenu[0][menumak['nama']]['harga'] * porsi_makanan
                    idrsubtmak = f'{subtmak:,}'.replace(",", ".")
                    jumtotmak += subtmak
                    print(f'{TEBAL}[     {nama_makanan.ljust(20)} {porsi_makanan}p = {HIJAU}Rp{idrsubtmak}{RESET}    ]{RESET}')
                idrjumtotmak = f'{jumtotmak:,}'.replace(",", ".")
                print(f'{TEBAL}                         TOTAL = {GARIS_BAWAH}{HIJAU}Rp{idrjumtotmak}{RESET}')
                print(f'\n[ {TEBAL}{KUNING}N{RESET} > {TEBAL}{KUNING}(LANJUTKAN PESANAN){RESET}  | {TEBAL}{KUNING}Y{RESET} > {TEBAL}{KUNING}(EDIT MENU){RESET} ]')
                while True:                   
                            editmak = input(f'\n{TEBAL}APAKAH INGIN MENAMBAH MENU LAIN?  {RESET}').upper()
                            if editmak == "Y" or editmak == "N":
                                break
                            else:
                                print(f'MASUKAN INPUT DENGAN BENAR!  ')
                                print(f'\n[ {TEBAL}{KUNING}N{RESET} > {TEBAL}{KUNING}(LANJUTKAN PESANAN){RESET}  | {TEBAL}{KUNING}Y{RESET} > {TEBAL}{KUNING}(EDIT MENU){RESET} ]')
                if editmak == "N":
                    break
                elif editmak == "Y":
                    print(f'\n         {TEBAL}PILIH MENU ANDA :  ){RESET}\n')

            #PEMBATAS MENU, SUPAYA TIDAK BINGUNG

        print(f'\n\n\n{TEBAL}           -- FIX ORDER --{RESET}\n')
        for menumak in keranjangmenumak:
                    nama_makanan = mastermenu[0][menumak["nama"]]['nama']
                    porsi_makanan = menumak["porsi"]
                    subtmak = mastermenu[0][menumak['nama']]['harga'] * porsi_makanan
                    idrsubtmak = f'{subtmak:,}'.replace(",", ".")
                    print(f'{TEBAL}{nama_makanan.ljust(20)} {porsi_makanan}p = {HIJAU}Rp{idrsubtmak}{RESET}')
        print(f'{TEBAL}      TOTAL = {HIJAU}{GARIS_BAWAH}Rp{idrjumtotmak}{RESET}')

        print(f"\n\n\n\n         {GARIS_BAWAH}{TEBAL}{MIRING}MENU MINUMAN{RESET}\n")
        while True:
                for kodemin , detailmin in mastermenu[1].items():
                    harga_idrmin = f"{detailmin["harga"]:,}".replace(",", ".")
                    print(f'{TEBAL}[{kodemin}]{RESET} {MIRING}{detailmin["nama"].ljust(25)}{RESET} : {TEBAL}{HIJAU}Rp{harga_idrmin}{RESET}')

        
                while True:
                    pesanmin = input('\nMASUKAN KODE MINUMAN :  ').upper()
                    if pesanmin in mastermenu[1]:
                        break
                    else:
                        print('MASUKAN KODE YANG TERDAFTAR!  ')

                while True:
                    try:
                        porsimin = int(input('BERAPA PORSI :  '))
                        if porsimin > 0:
                            break
                        else:
                            print('MASUKAN JUMLAH PORSI DENGAN BENAR!  ')
                    except ValueError:
                        print('MASUKAN DENGAN ANGKA!  ')


                pminuman = {
                    "nama" : pesanmin,
                    "porsi" : porsimin
                    }
                keranjangmenumin.append(pminuman)

                print(f'\n{TEBAL}KERANJANG ANDA SAAT INI :{RESET}\n')
                jumtotmin = 0
                for menumin in keranjangmenumin:
                    nama_minuman = mastermenu[1][menumin['nama']]['nama']
                    porsi_minuman = menumin['porsi']
                    subtmin = mastermenu[1][menumin['nama']]['harga'] * porsi_minuman
                    idrsubtmin = f'{subtmin:,}'.replace(",", ".")
                    jumtotmin += subtmin
                    print(f'{TEBAL}[     {nama_minuman.ljust(20)} {porsi_minuman}p = {HIJAU}Rp{idrsubtmin}{RESET}     ]{RESET}')
                idrjumtotmin = f'{jumtotmin:,}'.replace(",", ".")
                print(f'{TEBAL}                         TOTAL = {HIJAU}{GARIS_BAWAH}{idrjumtotmin}{RESET}')
                print(f'\n[ {TEBAL}{KUNING}N{RESET} > {TEBAL}{KUNING}(LANJUTKAN PESANAN){RESET}  | {TEBAL}{KUNING}Y{RESET} > {TEBAL}{KUNING}(EDIT MENU){RESET} ]')
                while True:                   
                            editmin = input(f'\n{TEBAL}APAKAH INGIN MENAMBAH MENU LAIN?  {RESET}').upper()
                            if editmin == "Y" or editmin == "N":
                                break
                            else:
                                print(f'MASUKAN INPUT DENGAN BENAR!  ')
                                print(f'\n[ {TEBAL}{KUNING}N{RESET} > {TEBAL}{KUNING}(LANJUTKAN PESANAN){RESET}  | {TEBAL}{KUNING}Y{RESET} > {TEBAL}{KUNING}(EDIT MENU){RESET} ]')
                if editmin == "N":
                    break
                elif editmin == "Y":
                    print(f'\n         {TEBAL}PILIH MENU ANDA :  ){RESET}\n')

        hargamak = jumtotmak
        hargamin = jumtotmin
        totalharga = hargamak + hargamin
        totalharga_idr = f'{totalharga:,}'.replace(",", ".")

        print(f'\n\n{TEBAL}{GARIS_BAWAH} ----- PESANAN ANDA ----- {RESET}\n')
        print(f'{TEBAL}MAKANAN : \n{RESET}')
        for pesananandamak in keranjangmenumak:
            nama_makanan_nota = mastermenu[0][pesananandamak['nama']]['nama']
            porsi_makanan_nota = pesananandamak['porsi']
            hargamak_nota = mastermenu[0][pesananandamak['nama']]['harga'] * porsi_makanan_nota
            idrhargamaknota = f'{hargamak_nota:,}'.replace(",", ".")
            print(f'{TEBAL}[ {nama_makanan_nota.ljust(25)} {porsi_makanan_nota}p = {HIJAU}Rp{idrhargamaknota}{RESET} ]{RESET}')
        print(f'\n{TEBAL}MINUMAN : \n{RESET}')
        for pesananandamin in keranjangmenumin:
            nama_minuman_nota = mastermenu[1][pesananandamin['nama']]['nama']
            porsi_minuman_nota = pesananandamin['porsi']
            hargamin_nota = mastermenu[1][pesananandamin['nama']]['harga'] * porsi_minuman_nota
            idrhargaminnota = f'{hargamin_nota:,}'.replace(",", ".")
            print(f'{TEBAL}[ {nama_minuman_nota.ljust(25)} {porsi_minuman_nota}p = {HIJAU}Rp{idrhargaminnota}{RESET} ]{RESET}')
        
        print(f'{TEBAL}\n               TOTAL = {GARIS_BAWAH}{HIJAU}Rp{totalharga_idr}{RESET}')

        print(f'\n[ {TEBAL}{HIJAU}{GARIS_BAWAH}Y{RESET} > {GARIS_BAWAH}{TEBAL}{HIJAU}(LANJUTKAN PESANAN){RESET}  | {TEBAL}{MERAH}{GARIS_BAWAH}N{RESET} > {GARIS_BAWAH}{TEBAL}{MERAH}(EDIT PESANAN){RESET} ]')
        while True:
            konfirmasi = input(f'\n{TEBAL}APAKAH ANDA INGIN MELANJUTKAN PESANAN?{RESET} ').upper()
            if konfirmasi == "Y" or konfirmasi == "N":
                break
            else:
                print(f'\n{GARIS_BAWAH}{TEBAL}{MERAH}MASUKAN INPUT DENGAN BENAR!{RESET} ')
                print(f'[ {TEBAL}{HIJAU}{GARIS_BAWAH}Y{RESET} > {GARIS_BAWAH}{TEBAL}{HIJAU}(LANJUTKAN PESANAN){RESET}  | {TEBAL}{MERAH}{GARIS_BAWAH}N{RESET} > {GARIS_BAWAH}{TEBAL}{MERAH}(EDIT PESANAN){RESET} ]')
        if konfirmasi == "Y":
            break
        elif konfirmasi == "N":
            print(f'{TEBAL}{KUNING}PESANAN DIBATALKAN SILAHKAN PILIH MENU{RESET}')
            keranjangmenumak.clear()
            keranjangmenumin.clear()