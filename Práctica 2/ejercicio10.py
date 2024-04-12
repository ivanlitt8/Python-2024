def create_stats(names, goals, goals_avoided, assists):
    # Lista se genera eliminando espacios en blanco, formateando la primer mayuscula de los nombres
    # eliminando una comilla y por ultimo separando todos los nombres.
    list_names = [nombre.strip().capitalize() for nombre in names.replace("'", "").split(',')]
    # Combino los elementos de las listas, y almanceno todo en otra lista
    stats = list(zip(list_names, goals, goals_avoided, assists))
    # Retorno la lista
    return stats

def max_goals(stats):
    max = 0
    player_max_goals = ''
    # Recorro la lista usando name y goals, el guion bajo se utiliza
    # para ignorar variables que no se desempaquetan
    for name, goals, _, _ in stats:
        if goals > max:
            max = goals
            player_max_goals = name
    # Retorno dos variables
    return player_max_goals, max

def most_influential(stats):
    max_influence = 0
    for name, goals, goals_avoided, assists in stats:
        # Recorro la lista calculando la influencia
        influence = (goals * 1.5)+ (goals_avoided * 1.25) + assists
        if influence > max_influence:
            max_influence = influence
            most_influential_player = name
    # Devuelvo jugador con influencia maxima
    return most_influential_player

def calculate_goal_average(stats):
    # Hago la suma de todos los goles, nuevamente uso _ y divido por el total de partidos
    goal_average  = sum(goals for _, goals, _, _ in stats)/25

    return goal_average

def player_goal_average(stats):
    name = ' '
    average = 0
    # Elijo por numero para simplificar
    player = int(input("Seleccione número de jugador 1-20:")) - 1
    if player < 1 or player > 20:
        print("Error: el número ingresado no es válido.")
        state = False
    else:
        # Accedo al nombre del jugador con numero elegido
        name = stats[player][0]
        # Accedo a su cantidad de goles y divido por el total de partidos
        average = stats[player][1] / 25
        state = True
    return name, average, state

# Datos
names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica, FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]

# Función 1
stats = create_stats(names, goals, goals_avoided, assists)

# Función 2
player_max_goals, max_goals = max_goals(stats)
print("El/la jugador/a con el máximo de goles es", player_max_goals, "con", max_goals, "goles.")

# Función 3
influential_player = most_influential(stats)
print("El/la jugador/a mas influyente es",influential_player,".")

# Función 4
goal_average = calculate_goal_average(stats)
print("El promedio de goles por partido del equipo es", goal_average)

# Función 5
player_name, goal_average , state= player_goal_average(stats)
if(state):
    print("El promedio de goles por partido de", player_name, "es", goal_average)
