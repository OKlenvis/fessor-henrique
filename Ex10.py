boletim= {}
p= input("Quer adicionar um aluno(a)?: ")

while p == "sim" or p == "SIM" or p == "Sim":
    nome= input('Adicione o nome do(a) aluno(a): ')
    nota= float(input("Agora adicione a nota do(a) alono(a): "))
    
    boletim[nome] = nota
    
    p = input("Quer adicionar outro aluno(a)?: ")
    
    for a in boletim:
        n = boletim[a]
                
        if n >= 6.0:
            print(f"O(a) aluno(a) {a} está Aprovado(a) com  uma nota de {nota}")
        else:
            print(f"O(a) aluno(a) {a} está Reprovado(a) com  uma nota de {nota}")
print("Muito obrigado por usar o nosso sistema de notas!!")