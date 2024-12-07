idade_nadador = int(input("Digite a idade do nadador: "))

if idade_nadador < 5:
    print(f"O nadador não se enquadra em nenhuma categoria")
elif 5 <= idade_nadador <= 7:
    print(f"O nadador se enquadra na categoria: Infantil A")
elif 8 <= idade_nadador <= 11:
    print(f"O nadador se enquadra na categoria: Infantil B")
elif 12 <= idade_nadador <= 13:
    print(f"O nadador se enquadra na categoria: Juvenil A")
elif 14 <= idade_nadador <= 17:
    print(f"O nadador se enquadra na categoria: Juvenil B")
elif idade_nadador >= 18:
    print(f"O nadador se enquadra na categoria: Adulto")
