while True: 

    print("kalkoelator")

    a = float(input("masukan angka: "))
    b = float(input("masukan angka: "))

    print("pilih operasai")
    print("1.tambah (+)")
    print("2.kurang (-)")
    print("3.kali (X)")
    print("4.bagi (%)")

    pilih = input("masukan pilihan (1/2/3/4): ")

    if pilih == "1":
        Hasil = a + b
        print("hasilnya", Hasil)
    elif pilih == "2":
        Hasil = a - b
        print("hasilnya", Hasil)
    elif pilih == "3":
        Hasil = a * b
        print("hasilnya", Hasil)
    elif pilih == "4":
        if b == 0:
            print("tidak bisa di bagi 0")

        else:
            Hasil = a / b
            print("hasilnya", Hasil)

    else:
        print("input tidak valid")

    ulang = input("ulang ngga? (y/g): ")
    if ulang != "y":
        print("oke")
        break    