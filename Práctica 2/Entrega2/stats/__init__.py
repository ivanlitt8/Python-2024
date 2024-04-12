

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
