notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João": 5.5}
soma = 0

for alunos in notas:
    soma= soma + notas[alunos]
media= soma/4

print("A média geral da turma é", media)