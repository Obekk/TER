# Ouvrir le fichier original en lecture
with open('dog.txt', 'r') as f:
    # Lire le contenu du fichier dans une chaîne de caractères
    original_content = f.read()

# Créer une nouvelle chaîne de caractères sans les chiffres ni les caractères 'N'
new_content = ''.join([c for c in original_content if c not in '0123456789Nn'])

# Ouvrir le fichier de destination en écriture
with open('dog_flawless.txt', 'w') as f:
    # Écrire le nouveau contenu dans le fichier de destination
    f.write(new_content)