import numpy as np
from statistics import mean
import matplotlib.pyplot as plt

"""
class MarkovChain(object):
  def __init__(self, transition_proba):
    self.transition_prob = transition_prob
    self.states = list(transition_prob.keys())

  def next_state(self, current_state):
    return np.random.choise(
      self.states, p=[self.transition_prob[current_state][next_state]
      for next_state in self.states]
      )
  def generate_states(self, current_state, no=10):
    futur_states = []
    for i in range(no):
      next_state = self.next_state(current_state)
      furure_states = next_state
      current_state = next_state
    return futur_states

"""

class ChaineMarkov:
    
    def __init__(self, etat_initial, matrice_transition):
        self.etat_initial = etat_initial
        self.matrice_transition = matrice_transition
        self.etat_actuel = self.etat_initial
        self.elements_chaine = [self.etat_initial]
    
    def passer_etapes(self, nb_etapes):
        for i in range(nb_etapes):
            self.etat_actuel = np.random.choice(['A', 'C', 'G', 'T'], p=self.matrice_transition[self.etat_actuel])
            self.elements_chaine.append(self.etat_actuel)
        return self.etat_actuel
    def vider_chaine(self):
        self.elements_chaine = []

  # Définir l'état initial et la matrice de transition



tab_Tableau_graphe = []
#nombre de simulation : n
for elem in ['A','C','G']:
  etat_initial = elem
  matrice_transition = {
    'A': [0.5, 0.4, 0.1,   0],
    'C': [0.5, 0.4,   0, 0.1],
    'G': [  0, 0.1, 0.7, 0.2],
    'T': [   0,  0,   0,   1]}
  # Créer une instance de la classe ChaineMarkov
  chaine = ChaineMarkov(etat_initial, matrice_transition)

  n = 10000
  nbr_pas_par_simulation = []
  for i in range(n):
    chaine.vider_chaine()
    chaine = ChaineMarkov(etat_initial, matrice_transition)
    while chaine.etat_actuel != 'T':
      chaine.passer_etapes(1)
    #Le nombre de pas est le nombre d'élements de la chaine - 1
    nbr_pas_par_simulation.append(len(chaine.elements_chaine)-1)
  print(mean(nbr_pas_par_simulation))

  Tableau_graphe =[]
  for k in range(1,50):
    summ = 0
    for elem in nbr_pas_par_simulation:
      if elem == k:
        summ = summ+1
    Tableau_graphe.append(summ/n)
  tab_Tableau_graphe.append(Tableau_graphe)



    
x = [i for i in range(1,50)]

plt.plot(x, tab_Tableau_graphe[0], "-.")
plt.plot(x, tab_Tableau_graphe[1], "-.")
plt.plot(x, tab_Tableau_graphe[2], "-.")
plt.show()
plt.close()



# Passer 10 étapes dans la chaîne
#etat_final = chaine.passer_etapes(20)

#print("L'état final de la chaîne est :", etat_final)
#print("chaine :", chaine.elements_chaine)
"""
Q = np.array([[0.5,0.4,0.1],[0.5,0.4,0],[0,0.1,0.7]])
print((Q.transpose()@Q).trace()**(1/2))
"""