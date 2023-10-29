# Boş bir dictionary yaradın
my_dict = {}

# İstifadəçinin 1 və ya 2 daxil etməsini sorun
choice = input("Daxil edin: 1 (Keys) və ya 2 (Values): ")

# Əgər boş bir şey daxil edilərsə, error mesajı verin
if not choice:
    print("Melumat daxil etmediniz")
else:
    if choice == '1':
        # 1 daxil ediləndə, dictionary-dəki keys-ləri yazdırın
        keys = list(my_dict.keys())
        print("Keys:", keys)
    elif choice == '2':
        # 2 daxil ediləndə, dictionary-dəki values-ləri yazdırın
        values = list(my_dict.values())
        print("Values:", values)
    else:
        # Əgər 1 və 2-dən başqa bir şey daxil edilsə, error mesajı verin
        print("Xəta: 1 və ya 2 daxil edin")
