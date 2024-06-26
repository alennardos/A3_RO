# Nombre de camions disponibles
num_trucks = 2  

# Variables de décision
x = LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n)], cat=LpBinary)
u = LpVariable.dicts('u', [i for i in range(n)], lowBound=0, cat='Continuous')

# Créer le modèle de minimisation
vrp_model = LpProblem("VRP", LpMinimize)

# Fonction objectif : Minimiser la somme des distances
vrp_model += lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Contraintes
for i in range(n):
    vrp_model += lpSum(x[i, j] for j in range(n) if i != j) == 1  # Chaque ville est visitée exactement une fois
    vrp_model += lpSum(x[j, i] for j in range(n) if i != j) == 1  # Chaque ville est visitée exactement une fois

# Contraintes pour les camions (chaque camion doit partir et revenir à Paris, index 0)
vrp_model += lpSum(x[0, j] for j in range(1, n)) <= num_trucks
vrp_model += lpSum(x[i, 0] for i in range(1, n)) <= num_trucks

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            vrp_model += u[i] - u[j] + n * x[i, j] <= n - 1

# Résoudre le modèle
vrp_model.solve()

# Afficher la solution
solution = []
for i in range(n):
    for j in range(n):
        if x[i, j].varValue == 1:
            solution.append((i, j))

# Afficher la route optimale sur la carte
plt.figure(figsize=(10, 10))
plt.scatter(x_scaled, y_scaled)

# Annoter les villes
for i, (x, y) in enumerate(scaled_coordinates):
    plt.text(x, y, cities_df['ville'][i], fontsize=9)

# Tracer les lignes représentant les routes des camions
for route in solution:
    i, j = route
    plt.plot([x_scaled[i], x_scaled[j]], [y_scaled[i], y_scaled[j]], 'k-', lw=0.5)

plt.title('Routes des camions à partir de Paris')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()


