list_operation = ["+", "-", "*","/", "//", "%","**"]
list_multiplication = ["*","x","X"]
list_puissance = ["**","xx","XX"]

while True: #permet de relancer le programe directement apres qu'il ai trouver un resultat !
    
    print("Je suis une calculatrice 9000, et je suis prête à tout calculer pour toi!")
    
    #Demande le nombre et verifie que la valeur saisie par l'utilisateur est bien un nombre
    def demander_nombre():
        chiffre = 0
        while chiffre == 0:
            nombre= input("Entrez un nombre ?: ")
            try:        
                chiffre= float(nombre) +1
            except:
                if "," in nombre:
                    print ("Erreur : Veuillez remplacer la , par un .")
                else: 

                    print ("Erreur: Veuillez rentrer un nombre !")
        return float (nombre)

    #Demande l'opération a réaliser
    def demander_calcul():
        calcul = input ("Quelle type d'opération souhaitez-vous effectuer ? : ")    
        while calcul not in list_operation and calcul not in list_multiplication and calcul not in list_puissance:
            print ("Erreur, veuillez saisir une opération valide")
            calcul = input("Quelle type d'opération souhaitez-vous effectuer ? : ")
        return calcul


    nombre1 = demander_nombre()
    calcul = demander_calcul()
    nombre2 = demander_nombre()

    #Effectue l'operation
    if calcul == "+":
        resultats = nombre1 + nombre2
    elif calcul == "-":
        resultats = nombre1 - nombre2
    elif calcul in list_multiplication:
        resultats = nombre1 * nombre2
    elif calcul == "/":
        if nombre2 == 0:
            resultats = "Erreur, division par 0 impossible" #Exclusion de la division par O
        else :
            resultats = nombre1 / nombre2
    elif calcul == "//":
        resultats = nombre1 // nombre2
    elif calcul == "%":
        resultats = nombre1 % nombre2
    elif calcul in list_puissance:
        resultats = nombre1 ** nombre2

    # Vérifie si le résultat est un nombre entier
    if resultats.is_integer():
        resultats = int(resultats)

    print(resultats)
