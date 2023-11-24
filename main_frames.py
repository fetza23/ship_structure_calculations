def yuvarla_sayi(sayi):
    if sayi % 100 >= 50:
        return (sayi // 100 + 1) * 100
    else:
        return (sayi // 100) * 100 +50

# Test
sayi = int(input("Bir sayı girin: "))
yuvarlanmis_sayi = yuvarla_sayi(sayi)
print(f"{sayi} sayısı {yuvarlanmis_sayi} sayısına yuvarlandı.")