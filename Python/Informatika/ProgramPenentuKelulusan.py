def main(): # pembuataan fungsi
    print("-------------------------------")
    print("Program Penentuan Kelulusan")
    print("-------------------------------")

    # input
    x = float(input("Silahkan masukan  nilai akhir: ")) # float agar dapat memasukkan nilai desimal

    # kondisi
    if x >= 75: # jika di atas 75
        print("Anda lulus!")
    elif x >= 50 and x <= 74: # jika di antara 50 dan 69
        print("Anda harus mengikuti remidial")
    elif x < 50: # jika di bawah 50
        print("Anda tidak lulus")
    else:
        print("KESALAHAN INPUT")

main() # pemanggilan fungsi

# pengulangan 
y = True
while y == True:
    z = str(input("Mau cek lagi?ya/tidak "))
    if z == "ya" or z == "y":
        main()
    else:
        print("Terimakasih!")
        break