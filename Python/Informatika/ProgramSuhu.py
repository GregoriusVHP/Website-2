# Fungsi built-in untuk menghitung panjang sebuah list
data = [1, 2, 3, 4, 5]
panjang_data = len(data)
print(f"Panjang data adalah {panjang_data}")

# Fungsi user-defined untuk menghitung luas persegi
def hitung_luas_persegi(sisi):
    luas = sisi*4 # Menghitung luas persegi
    return luas

# Contoh penggunaan
sisi = 4
luas = hitung_luas_persegi(sisi)
print(f"Luas persegi dengan sisi {sisi} adalah {luas}")


