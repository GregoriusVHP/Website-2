#PRAKTIK INFROMATIKA
def main():
    x = int(input("Silahkan ketik umur anda: ")) # INPUT USIA
    print()
    print("\tSTATUS")
    print("1.Pelajar\n2.Pekerja\n3.Pengangguran")
    y = int(input("Apa status anda?(angka)->  ")) # INPUT STATUS

    if x < 18: # JIKA USIA DIBAWAH 18 TAHUN
        if y == 1: 
            print("Anda adalah pelajar dibawah umur")
        elif y == 2:
            print("Anda terlalu muda untuk bekerja")
        else:
            pass
    elif x >= 18 or x <= 60: # JIKA USIA DIANTARA 18-60 TAHUN
        if y == 1:
            print("Anda adalah pelajar di usia produktif.")
        elif y == 2:
            print("Anda adalah seorang pekerja di usia produktif.")
        elif y == 3:
            print("Anda adalah pengangguran di usia produktif, carilah pekerjaan.")
        else:
            pass
    elif x > 60: # JIKA USIA DIATAS 60 TAHUN
        if y == 1:
            print("Usia lanjut tetapi masih menjadi pelajar.")
        elif y == 2:
            print("Anda masih bekerja di usia lanjut.")
        elif y == 3:
            print("Anda sudah pensiun dan menganggur")
        else:
            pass
    else:
        pass
main() # PEMANGGILAN OUTPUT MENGGUNAKAN KELAS