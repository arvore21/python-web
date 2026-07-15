def calcular_combustivel(litros, preco):
    total = litros * preco
    mensagem = ""
    if total > 200:
        mensagem = "O gasto ultrapassou R$ 200,00!"
    return total, mensagem
 
def calcular_joias(valor, percentual):
    aumento = valor * (percentual / 100)
    final = valor + aumento
    return final
 
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
 
    if media > 6:
        resultado = "Maior que 6"
    elif media < 6:
        resultado = "Menor que 6"
    else:
        resultado = "Igual a 6"
   
    return media, resultado

        