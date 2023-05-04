# Ouvrir le fichier en lecture
with open('dog_flawless.txt', 'r') as f:
    # Lire le contenu du fichier dans une chaîne de caractères
    content = f.read()

# Initialiser un dictionnaire vide pour stocker les comptages des motifs à trois nucléotides
counts = {}

# Compter les occurrences des motifs à trois nucléotides dans le fichier
for i in range(len(content) - 2):
    motif = content[i:i+3]
    if motif not in counts:
        counts[motif] = 1
    else:
        counts[motif] += 1

# Calculer le pourcentage d'apparition de chaque motif à trois nucléotides
total_count = sum(counts.values())
for motif in counts:
    counts[motif] = counts[motif] / total_count * 100

# Afficher les résultats
for motif, percentage in counts.items():
    print(f"Le motif '{motif}' apparaît avec un pourcentage de {percentage:.2f}%")
