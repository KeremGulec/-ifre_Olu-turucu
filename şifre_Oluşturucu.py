import random
karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi=int(input("karakter sayısı seçin"))
parola=""
for i in range(sayi):
  parola=parola.random.choise(karakterler)
print("oluşturulan karakterler",parola)
