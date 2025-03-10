# 1. Kullanıcının girdiği metni bir dosyaya yazma
file_name = "metin_dosyasi.txt"

with open(file_name, "w") as file:
    metin = input("Bir metin girin: ")
    file.write(metin)

print("\nMetin dosyaya yazıldı.")

# 2. Dosyadaki içeriği okuma ve ekrana yazdırma
with open(file_name, "r") as file:
    icerik = file.read()
    print("\nDosyanın içeriği:")
    print(icerik)

# 3. Kullanıcıdan 5 satır veri alıp dosyaya ekleme
with open(file_name, "w") as file:
    print("\nLütfen 5 satır metin girin:")
    for i in range(1, 6):
        satir = input(f"{i}. satır: ")
        file.write(satir + "\n")

print("\n5 satır metin dosyaya kaydedildi.")

# 4. Dosyayı satır satır okuyarak ekrana yazdırma
print("\nDosyanın satır satır içeriği:")
with open(file_name, "r") as file:
    for line in file:
        print(line.strip())  # strip() boşlukları ve yeni satır karakterlerini temizler
