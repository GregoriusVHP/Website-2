import math

def Tambah(x, y):
    return x + y

def Kurang(x, y):
    return x - y

def  Kali(x, y):
    return x * y

def  Bagi(x, y):
    return x / y

def  Modulus(x, y):
     return x % y

def AkarKuadrat(x):
     return  math.sqrt(x) 

def Pangkat(x, y):
     return x ** y
     

def main():
    while True:
        print()
        print()
        print()
        print("="*60)
        print("\tSelamat datang di kalkulator sederhana!")
        print("="*60)
        print()
        print("Mau hitung apa?")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Modulus")
        print("6. Akar Kuadrat")
        print("7. Pangkat")
        print("8. Keluar")
        print()
    
        #  Menerima input dari user
        d = int(input("SILAHKAN PILIH (ketik angka 1-8): "))
        if d == 1:
            x  = float(input("Masukkan angka pertama: "))
            y  = float(input("Masukkan angka kedua: "))
            print(f"Hasilnya adalah: {round(Tambah(x, y))}")
        elif d == 2:
            x  = float(input("Masukkan angka pertama: "))
            y  = float(input("Masukkan angka kedua: "))
            print(f"Hasilnya adalah: {round(Kurang(x, y))}")
        elif  d == 3:
            x  = float(input("Masukkan angka pertama: "))
            y  = float(input("Masukkan angka kedua: "))
            print(f"Hasilnya adalah: {round(Kali(x, y))}")
        elif  d == 4:
            x  = float(input("Masukkan angka pertama: "))
            y  = float(input("Masukkan angka kedua: "))
            print(f"Hasilnya adalah: {Bagi(x, y)}")
        elif d == 5:
            x = float(input("Masukkan angka pertama: "))
            y = float(input("Masukkan angka kedua: "))
            print(f"Hasilnya adalah: {round(Modulus(x, y))}")
        elif d == 6:
            x =  float(input("Masukkan angka pertama: "))          
            print(f"Hasilnya adalah: {round(AkarKuadrat(x))}")
        elif d == 7:
            x  =  float(input("Masukkan angka pertama: "))
            y  =  float(input("Masukkan derajat pangkat: "))
            print(f"Hasilnya adalah: {round(Pangkat(x, y))}")
        elif  d == 8:
            print("Terimakasih telah menggunakan program ini! :)")
            break
        else:
            print(ValueError)
    

if  __name__ == "__main__":
            main()