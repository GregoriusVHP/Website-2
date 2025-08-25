# Daftar Menu
makanan = [
    ["Nasi Goreng", 12000],
    ["Mie Goreng", 10000],
    ["Gado-Gado", 8000],
    ["Spaghetti", 25000]
]

minuman = [
    ["Jus Jeruk", 5000],
    ["Jus Apel", 6000],
    ["Kopi", 4000],
    ["Teh", 3000],
    ["Thai Tea", 8000]
]

def menu(): # Fungsi untuk menampilkan menu
    print("="*32)
    print("\tDaftar Menu Makanan")
    print("="*32)
    print("\nMAKANAN\n")
    for item in makanan:
        print(f"{item[0]} - Rp. {item[1]}")
    print()
    print("\nMINUMAN\n")
    for item in minuman:
        print(f"{item[0]} - Rp. {item[1]}")
    print()

def input_item(): # Fungsi untuk menginput item
    while True:
        pilih = input("\nPilih item (atau ketik 'selesai' untuk selesai): ").title()
        if pilih == "Selesai" or cari_harga(pilih) is not None:
            return pilih
        print("Item tidak tersedia. Coba lagi!")

def cari_harga(item): # Fungsi untuk mencari harga item
    for kategori in (makanan, minuman):
        for menu_item in kategori:
            if menu_item[0] == item:
                return menu_item[1]
    return None # Jika item tidak ditemukan

def input_jumlah(): # Fungsi untuk menginput jumlah
    while True:
        jumlah = input("Masukkan jumlah: ")
        if jumlah.isdigit() and int(jumlah) > 0:
            return int(jumlah)
        print("Jumlah harus berupa angka lebih dari 0.")

def hitung_total(pesanan): # Fungsi untuk menghitung total harga
    total = 0
    for item, jumlah in pesanan:
        harga = cari_harga(item)
        total += harga * jumlah
    return total

def tampilkan_pesanan(pesanan): # Fungsi untuk menampilkan pesanan
    print("\nPesanan Anda:")
    for item, jumlah in pesanan:
        harga = cari_harga(item)
        print(f"{item}: {jumlah} x Rp{harga} = Rp{harga * jumlah}")

def input_uang(total_harga): # Fungsi untuk menginput uang
    while True:
        uang = input(f"Total harga adalah Rp{total_harga}. Masukkan uang yang dibayarkan: ")
        if uang.isdigit() and int(uang) >= total_harga:
            return int(uang)
        print("Uang tidak cukup atau input tidak valid. Coba lagi!")

def kasir(): # Fungsi untuk menampilkan program kasir
    pesanan = [] # Daftar pesanan kosong
    while True: # Loop hingga user memilih 'selesai'
        menu()# Tampilkan menu
        item = input_item()# Input item
        if item == "Selesai":# Jika user memilih 'selesai'
            break
        jumlah = input_jumlah() # Input jumlah
        
        # Perbarui pesanan jika item sudah ada
        for pesanan_item in pesanan:
            if pesanan_item[0] == item:
                pesanan_item[1] += jumlah
                break
        else:
            pesanan.append([item, jumlah])
    
    if not pesanan:
        print("\nTidak ada pesanan. Terima kasih!")
        return

    total_harga = hitung_total(pesanan)
    tampilkan_pesanan(pesanan)
    print(f"Total Harga: Rp{total_harga}")

    uang_dibayar = input_uang(total_harga)
    kembalian = uang_dibayar - total_harga

    print("\n--- Struk Pembayaran ---")
    tampilkan_pesanan(pesanan)
    print(f"Total Harga: Rp{total_harga}")
    print(f"Uang Dibayarkan: Rp{uang_dibayar}")
    print(f"Kembalian: Rp{kembalian}")
    print("\nTerima kasih telah berbelanja!")

# Menjalankan program
kasir()