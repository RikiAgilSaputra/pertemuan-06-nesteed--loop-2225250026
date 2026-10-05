#input data-n
n = int(input ("n:"))

#pengkondisian jika n <= 0
while n <= 0:
    print ("n harus positif")
    n = int(input ("n:"))

#deklarasi variabel untuk menghitung total hasil dan total bilangan genap
total_semua = 0
count_genap = 0

#perulangan untuk menghitung perkalian
for i in range (1, n + 1):
    total_baris = 0
    for j in range (1, n + 1):
        hasil = i * j
        print (f"{hasil:4}", end = "  ")
        total_baris += hasil
        total_semua += hasil
        if hasil % 2 == 0:
            count_genap += 1

    #menampilkan jumlah baris
    print (f"    | jumlah baris = {total_baris}")
print ()

#menmapilkan total seluruh hasil dan banyak hasil genap
print (f"total seluruh hasil = {total_semua}")
print (f"banyak hasil genap = {count_genap}")



