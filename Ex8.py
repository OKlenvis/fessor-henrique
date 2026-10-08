lista = [
    {"nome": "mouse", "preco": 50.00},
    {"nome": "computador", "preco": 2000.00},
    {"nome": "monitor", "preco": 20.00},
]
for i in lista:
    if i["preco"] >=50.00:
        print(f"O produto {i['nome']} é acima de R$50.00 com seu valor de {i['preco']}")