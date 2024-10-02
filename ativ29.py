# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.
def verificar_presenca(alunos_presentes):
    # Contar o número de alunos presentes
    total_presentes = len(alunos_presentes)
    
    # Exibir a quantidade de alunos presentes
    print(f"Alunos presentes: {total_presentes}")
    
    # Exibir a lista de alunos presentes
    print("Lista de alunos presentes:", ', '.join(alunos_presentes))
    
    # Verificar se o total de alunos presentes é menor que 5
    if total_presentes < 5:
        print("Aviso: Poucos alunos presentes. Revisar lista de chamada.")

# Exemplo de uso
alunos_presentes = ['Ana', 'Bruno', 'Carlos', 'Daniela']
verificar_presenca(alunos_presentes)
