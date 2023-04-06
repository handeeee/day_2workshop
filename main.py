
vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.


if final<40:
    print("kullanıcı kaldı")

elif ortalama<50:
    print("kullanıcı kaldı")

elif vize==(2*final):
    print("kullanıcı kaldı")

else:
    print("kullanıcı geçti")