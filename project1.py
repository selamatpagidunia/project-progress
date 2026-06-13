print('\n\n\n\nSELAMAT DATANG DI Croissant Doré')
print('\n\n ----- DAFTAR MENU -----\n\n')
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

mastermenu.append(menumakanan)
mastermenu.append(menuminuman)

print("         MENU MAKANAN\n")
for kodemak , detailmak in mastermenu[0].items():
    harga_idrmak = f"{detailmak['harga']:,}".replace(",", ".")
    print(f'[{kodemak}] {detailmak["nama"].ljust(25)} - Rp{harga_idrmak}')

while True:
    pesanmak = input('\nMASUKAN KODE MAKANAN : ').upper()
    if pesanmak in mastermenu[0]:
        break
    else:
        print('MASUKAN KODE YANG TERDAFTAR! ')

while True:
    try:
        porsimak = int(input('BERAPA PORSI : '))
        if porsimak > 0:
            break
        else:
            print('MASUKAN JUMLAH PORSI DENGAN BENAR! ')
    except ValueError:
        print(f'MASUKAN DENGAN ANGKA! ')

print("\n\n         MENU MINUMAN\n")
for kodemin , detailmin in mastermenu[1].items():
    harga_idrmin = f"{detailmin["harga"]:,}".replace(",", ".")
    print(f'[{kodemin}] {detailmin["nama"].ljust(25)} - Rp{harga_idrmin}')

while True:
    pesanmin = input('\nMASUKAN KODE MINUMAN : ').upper()
    if pesanmin in mastermenu[1]:
        break
    else:
        print('MASUKAN KODE YANG TERDAFTAR! ')

while True:
    try:
        porsimin = int(input('BERAPA PORSI : '))
        if porsimin > 0:
            break
        else:
            print('MASUKAN JUMLAH PORSI DENGAN BENAR! ')
    except ValueError:
        print('MASUKAN DENGAN ANGKA! ')

hargamak = mastermenu[0][pesanmak]["harga"] * porsimak
hargamin = mastermenu[1][pesanmin]["harga"] * porsimin
totalharga = hargamak + hargamin

print(f'\n\n ----- PESANAN ANDA ----- ')
print(f'MAKANAN : {mastermenu[0][pesanmak]["nama"]} - {porsimak}p - TOTAL = Rp{f'{hargamak:,}'.replace(",", ".")}')
print(f'MINUMAN : {mastermenu[1][pesanmin]["nama"]} - {porsimin}p - TOTAL = Rp{f'{hargamin:,}'.replace(",", ".")}')
print(f'          TOTAL = Rp{f'{totalharga:,}'.replace(",", ".")}\n')