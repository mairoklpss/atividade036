#Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

listNotas = []

nomeAluno = input('qual o nome do aluno? ')

#ler as notas.
for i in range(1, 5):
    notas = float(input(f"digite a {i}° nota do(a) {nomeAluno}: "))
    listNotas.append(notas)

print("as notas dele(a) são:", listNotas)

media = sum(listNotas)/len(listNotas) 

print(f"a média do(a) aluno(a) {nomeAluno} é:", media)

