def classificar_nadador(idade):

  if 5 <= idade <= 7:
    return "Infantil A"
  elif 8 <= idade <= 11:
    return "Infantil B"
  elif 12 <= idade <= 13:
    return "Juvenil A"
  elif 14 <= idade <= 17:
    return "Juvenil B"
  elif idade >= 18:
    return "Adulto"

idade_nadador = int(input("Digite a idade do nadador: "))
categoria = classificar_nadador(idade_nadador)

print(f"O nadador se enquadra na categoria: {categoria}")
