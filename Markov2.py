import collections

# Lire le fichier texte et stocker le contenu dans une chaîne de caractères
with open('dog_flawless.txt', 'r') as f:
    sequence = f.read()

# Calculer la fréquence des paires de nucléotides
pairs_freq = collections.defaultdict(lambda: collections.Counter())
for i in range(len(sequence) - 1):
    pair = sequence[i:i+2]
    pairs_freq[pair[0]][pair[1]] += 1

# Calculer les probabilités des paires de nucléotides
pairs_prob = collections.defaultdict(lambda: collections.defaultdict(float))
for nucleotide, counter in pairs_freq.items():
    total_count = sum(counter.values())
    for next_nucleotide, count in counter.items():
        pairs_prob[nucleotide][next_nucleotide] = count / total_count

# Afficher les probabilités des paires de nucléotides
for nucleotide, prob in pairs_prob.items():
    print("Probabilités pour la lettre", nucleotide)
    print(prob)

# Ouvrir le fichier en lecture
with open('nom_fichier.txt', 'r') as f:
    # Lire le contenu du fichier dans une chaîne de caractères
    content = f.read()

# Initialiser un dictionnaire vide pour stocker les comptages des nucléotides
counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# Compter les occurrences des nucléotides dans le fichier
for char in content:
    if char in counts:
        counts[char] += 1

# Calculer le pourcentage d'occurrence de chaque nucléotide
total_count = sum(counts.values())
percentages = {nuc: count / total_count * 100 for nuc, count in counts.items()}

# Afficher les résultats
for nuc, percent in percentages.items():
    print(f'{nuc}: {percent:.2f}%')