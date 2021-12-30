class etudiant :
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
 #list de type etudiant        
etudiant = [
{'nom' : 'karret','prenom' : 'ayoub', 'age': 22,'cne': 1523648, 'moyenne': 16},
{'nom' : 'bouhazama','prenom' : 'ibrahim', 'age': 20,'cne': 15268943, 'moyenne': 17},
{'nom': 'ibn tahaikt','prenom' : 'anass', 'age': 23,'cne': 144060438, 'moyenne': 19},
{'nom' : 'benbreghit','prenom' : 'hamza', 'age': 23,'cne': 14068952, 'moyenne': 18},
]

#trie par age
etudiant.sort(key=lambda x: x.get('age'))
print("le Trie par age :\n")
print(etudiant)
#trie par moyenne
etudiant.sort(key=lambda x: x.get('moyenne'))
print("le Trie par moyenne :\n")
print(etudiant)



