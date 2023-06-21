from random import shuffle
alunos = (input('Escreva o nome dos alunos com espaço: ').split(','))
shuffle(alunos)
print(f'Em ordem quem vai apresentar o trabalho: {alunos}')