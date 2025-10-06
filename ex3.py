valores = [
    10,
    3 + 2j,
    3.14,
    [1.2],
    "j",
    (1,2),
    None,
    True,
    {"chave": "valor", "idade": 25}
]

for valor in valores:
    print(f"Valor: {valor} - Tipo: {type(valor)}")