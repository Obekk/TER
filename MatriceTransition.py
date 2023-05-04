# Ouvrir le fichier en lecture
with open('dog_flawless.txt', 'r') as f:
    # Lire le contenu du fichier dans une chaîne de caractères
    content = f.read()

# Initialiser une matrice 4x4 pour stocker les pourcentages d'apparition des nucléotides
transition_matrix = [[0 for j in range(4)] for i in range(4)]

# Initialiser un dictionnaire vide pour stocker les comptages des nucléotides
counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# Compter les occurrences des nucléotides dans le fichier et mettre à jour la matrice de transition
for i in range(len(content) - 1):
    curr_char = content[i]
    next_char = content[i+1]
    if curr_char in counts and next_char in counts:
        counts[curr_char] += 1
        transition_matrix['ACGT'.index(curr_char)]['ACGT'.index(next_char)] += 1

# Calculer le pourcentage d'apparition de chaque nucléotide après chaque nucléotide
for i in range(4):
    total_count = sum(transition_matrix[i])
    for j in range(4):
        transition_matrix[i][j] = transition_matrix[i][j] / total_count 

# Afficher la matrice de transition
for row in transition_matrix:
    print(row)
