import stats.__init__ as stats

# Datos
names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica, FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]

# Función 1
structure = stats.create_stats(names, goals, goals_avoided, assists)

# Función 2
player_max_goals, max_goals = stats.max_goals(structure)
print("El/la jugador/a con el máximo de goles es", player_max_goals, "con", max_goals, "goles.")

# Función 3
influential_player = stats.most_influential(structure)
print("El/la jugador/a mas influyente es",influential_player,".")

# Función 4
goal_average = stats.calculate_goal_average(structure)
print("El promedio de goles por partido del equipo es", goal_average)

# Función 5
player_name, goal_average , state= stats.player_goal_average(structure)
if(state):
    print("El promedio de goles por partido de", player_name, "es", goal_average)
