p = input("Digite uma palavra: ")
v= []
c= []

for letras in p:
    if letras in "ãõÃÕaeiouAEIOUáéíóúÁÉÍÓÚ":
        v.append(letras)
    if letras in "bBcCdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ":
        c.append(letras)
print(v)
print(c)