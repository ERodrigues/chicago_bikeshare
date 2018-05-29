# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# TAREFA 3
def column_to_list(data, index):
    """
        Função que transforma o resultado de uma das colunas em uma nova lista
          Argumentos:
              data: recebe a lista utilizada como origem.
              index: recebe a coluna que deverá ser utilizada como referência.
          Retorna:
              Retorna uma nova lista contendo apenas os valores da coluna referenciada
              através do argumento index.
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a
    # feature pelo seu índice,e dar append para uma lista
    for line in data:
        column_list.append(line[index])
    return column_list

# TAREFA 5
def count_gender(data_list):
    """
        Função que retorna a quantidade de generos presentes na lista passada como parâmetro
          Argumentos:
              data_list: recebe a lista utilizada como origem.
          Retorna:
              Retorna uma tupla com a quantidade de generos masculinos e femininos
    """
    male = len([line[-2] for line in data_list if 'Male' == line[-2]])
    female = len([line[-2] for line in data_list if 'Female' == line[-2]])
    return [male, female]

# TAREFA 6
def most_popular_gender(data_list):
    """
        Função retorna qual o genero mais prevalente
          Argumentos:
              data_list: recebe a lista utilizada como origem.
          Retorna:
              Retorna uma string informando qual o genero mais prevalente
    """
    male, female = count_gender(data_list)
    if male > female:
        answer = "Masculino"
    elif male == female:
        answer = "Igual"
    else:
        answer = "Feminino"
    return answer

def count_items(column_list):
    """
        Função que identifica os valores únicos em uma lista passada por parâmetro
        e a quantidade de vezes que aquele valor se repete
        Argumentos
            column_list: lista em que os valores são identificados e contados
        retorna
            lista com os valores únicos e com a contagem de repetição deste valor
            na lista
    """
    item_types = []
    count_items = []
    for column in column_list:
        if item_types.count(column) == 0:
            item_types.append(column)

    for item in item_types:
        count_items.append(column_list.count(item))

    return item_types, count_items

def print_graph(y_position, x_label, y_label, title, quantity, types):
    """
        Função que imprime um gráfico de barra de acordo com os parametros passados
        Argumentos
            y_position:posicao do eixo Y
            x_label: rótulo do eixo X
            y_label: rótulo do eixo Y
            title: Título do gráfico
            quantity: Quantidade
            types: Tipos a serem apresentados no gráfico
    """
    plt.bar(y_position, quantity)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.xticks(y_position, types)
    plt.title(title)
    plt.show(block=True)

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
print (data_list[:20])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

input("Aperte Enter para continuar...")
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for line in data_list[:20]:
    print(line[-2])

input("Aperte Enter para continuar...")
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
male = len([line[-2] for line in data_list if 'Male' == line[-2]])
female = len([line[-2] for line in data_list if 'Female' == line[-2]])
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
print_graph(y_pos, 'Gênero', 'Quantidade', 'Quantidade por Gênero', quantity, types)

input("Aperte Enter para continuar...")
# TAREFA 7
#  Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
column_list = column_to_list(data_list, -3)
types, counts = count_items(column_list)
y_pos = list(range(len(types)))
print_graph(y_pos, 'Tipos', 'Quantidade', 'Quantidade por Tipos de Usuários', counts, types)


input("Aperte Enter para continuar...")
# TAREFA 8
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Existe um conjunto de dados com genero não informado, "
answer += "conforme apresentado:{}".format(len([line[-2] for line in data_list if line[-2] == '']))
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 9
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
values = 0.
new_trip_duration = [int (trip_duration) for trip_duration in trip_duration_list]
new_trip_duration.sort()
min_trip = new_trip_duration[0]
max_trip = new_trip_duration[-1]
for trip_duration in new_trip_duration:
    values += trip_duration

mean_trip = values/len(trip_duration_list)

if len(new_trip_duration) % 2 == 0:
    first_index = int(len(new_trip_duration)/2)
    second_index = int(len(new_trip_duration)/2)+1
    median_trip = (int(new_trip_duration[first_index]) + int(new_trip_duration[second_index]))/2
else:
    median_trip = int(new_trip_duration[int(len(new_trip_duration)/2)])

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
answer = input("Você vai encarar o desafio? (yes ou no)")
# TAREFA 12 - Desafio! (Opcional)
if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
