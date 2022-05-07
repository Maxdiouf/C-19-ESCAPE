#voici notre carte de jeu
Map = [
        ["!1","D","🌲","🌲","🌲", "🌲", "🌲", "🌲", "!2", "🌲"],
        ["🌲","X","🌲","🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲"],
        ["V","🌲","🌲","🌲","🌲" , "🌲", "🌲", "B", "🌲", "🌲","🌲"],
        ["🌲","🌲","🌲","🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲"],
        ["🌲","A","🌲","🌲","🌲", "🌲", "🌲", "🌲", "🌲", "M","🌲"],
        ["🌲","🌲","🌲","🌲","🌲", "🌲", "🌲", "🌲", "!3","🌲"],
        ["P","🌲","🌲","🌲","🌲", "🌲", "🌲", "🌲", "🌲", "🌲"],
        ["🌲","🌲","🌲","🌲","🌲", "F", "🌲", "🌲", "🌲", "$" ],
]

def show_map(carte):
#fonction nous affichant bien la map
    i = 0
    while i < len(carte):
        print(carte[i])
        i = i + 1    

def info():
#fonction qui nous montre à quoi correspondent chaque objet sur notre map
    print("-"*50)
    print("""
    \x1b[4mVoici quelques informations à propos de la Carte:\x1b[0m
    🌲 == il y a rien 
    X == Vous 
    $ == la sortie de la fôret 
    ! == une maladie /3
    D == Doliprane (Vous ajoute 50 pv.)  
    V == Vitamine C (Vous ajoute 25 pv.)  
    A ==  vaccin Astra zanéca (Permet de bloquer 1 coup du monstre avec votre bouclier)
    M == vaccin Moderna (Permet de bloquer 2 coups du monstre avec votre bouclier)
    P == vaccin Pfizer (Permet de bloquer 3 coups du monstre avec votre bouclier)
    B == Barre énergétique Boost Attack (Permet de faire 15 de dégats en plus par coups)
    F == fiole remède à appliquer sur son arme (Permet de faire 30 de dégats en plus par coups)
    """)

def add_2inventory(Liste,objet):   
#fonction qui permet d'ajouter des objets dans l'inventaire
    #à chaque fois il y a un objet si oui 
    #alors faire la fonction en parametre avec l'objet de la case
    if objet in Liste:
        print("\x1b[1mVous avez déja",objet,"dans votre sac.\x1b[0m")
        return
    print(f"\x1b[1m\x1b[32;49mSouhaitez-vous mettre {objet} dans votre sac ?\x1b[0m")
    choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
    if choice == "oui":
        Liste.append(objet)
        print(f"\x1b[1m{objet} à bien été mis dans votre sac.\x1b[0m")
        return Liste
    elif choice == "non":
        print(f"\x1b[1m{objet} a été laissé sur le sol.\x1b[0m")
        return Liste
    else:
        print("\x1b[31;49mréponse inconnue")
        add_2inventory(Liste,objet)

def use_inventory():
#fonction qui permet d'afficher du texte si oui ou non, pon utilise un objet
#ensuite selon la réponse de cette fonction, on lancera une fonction Combat
#avec les paramêtres associés avec l'objet utilisé
#ex: si on utilise le Doliprane alors on met en paramêtre à Combat que on a 150 pv au lieu de 100pv
    print("\x1b[1m\x1b[33;49mVoici le contenu de votre sac: \x1b[0m",inventaire)
    print("\x1b[1mQue voulez vous utiliser?\x1b[0m")
    choice_object = input("\x1b[1m\x1b[34;49mEntrez le nom exacte de l'objet que vous voulez ou bien entrez 'rien' si vous voulez rien: \x1b[0m")
    if choice_object == "rien":
        return choice_object
    else:
        print("\x1b[33;49mVous utilisé\x1b[0m",choice_object)
        return choice_object

def Dr_raoult():
#petit personnage surprise qui apparaît seulement si on gagne au 3ème combat
#ce personnage nous indiqueras le chemin pour aller vers la sortie
    print("-"*50)
    print("\x1b[1m\x1b[33;49mDr Raoult est apparût et semble vouloir vous parlez\x1b[0m")
    input("\x1b[3m\x1b[34;49mAppuyez sur Entrée pour afficher la suite\x1b[0m")
    print("")
    print("\x1b[1m\x1b[33;49mDr Raoult: Salut aventurier(ère).\x1b[0m")
    input("\x1b[3m\x1b[34;49mAppuyez sur Entrée pour afficher la suite\x1b[0m")
    print("")
    print("\x1b[1m\x1b[33;49mDr Raoult: Il paraît qu' à la sortie, il s'y cachait une grosse maladie!\x1b[0m")
    input("\x1b[3m\x1b[34;49mAppuyez sur Entrée pour afficher la suite\x1b[0m")
    print("")
    print("\x1b[1m\x1b[33;49mDr Raoult: Il vous faudra un des trois vaccins pour pouvoir battre cette créature car elle est surpuissante et imbattable sans vaccin.\x1b[0m")
    input("\x1b[3m\x1b[34;49mAppuyez sur Entrée pour afficher la suite\x1b[0m")
    print("")
    print("\x1b[1m\x1b[33;49mDr Raoult: Bonne chance aventurier(ère) !\x1b[0m")
    print("-"*50)
    return

from Combat import Combat
from Combat import Combat_Boss
inventaire = []
def moove(y,x,map): # config y et x a la position où on se trouve avant de vouloir bouger.
    print("-"* 50)
    show_map(Map)
    print("\x1b[1mVous êtes ici: \x1b[0m",map[y][x]) #position du joueur initiale
#si la case où on se trouve il y a n'importe qu'elle lettre alors 
#l'objet associé à la lettre est ajouter à l'inventaire
#c'est pareil pour tous les autres objets
    if map[y][x] == "D":
        objet = "Doliprane"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])
        
    elif map[y][x] == "V":
        objet = "Vitamine C"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])
        
    elif map[y][x] == "A":
        objet = "vaccin Astra zanéca"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])
        
    elif map[y][x] == "M":
        objet = "vaccin Moderna"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])
        
    elif map[y][x] == "P":
        objet = "vaccin Pfizer"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])
        
    elif map[y][x] == "B":
        objet = "Barre énergétique Boost Attack"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])
        
    elif map[y][x] == "F":
        objet = "Fiole remède"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])
    
#premier combat   
    elif map[y][x] == "!1":
#on determine un Monstername afin de le réutilisé pour lancer notre fonction Combat
        Monstername = "Rhu-meuh"
        print("\x1b[1m\x1b[37;45mUN ENNEMI EST APPARÛT !\x1b[0m")
        print("\x1b[1m\x1b[33;49mSouhaitez-vous parcourir votre sac juste avant le combat ? Vous pourrez choisir qu'un seul objet! \x1b[0m")

        choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
#input qui demande si on veut parcourir l'inventaire
        if choice == "oui":
#si oui ce que l'on va rentré dans le input,ça lancera Combat mais avec des paramètres différents
            objet = use_inventory()
            if objet == "Doliprane":
                Combat(150,0,100,20,40,15,Monstername) # + 50 pv pour notre joueur
            
            elif objet == "Vitamine C":
                Combat(125,0,100,20,40,15,Monstername) # + 25 pv pour notre joueur
            
            elif objet == "Fiole remède" or objet == "Fiole remede":
                Combat(100,0,100,50,70,15,Monstername) # +30 de dégats
            
            elif objet == "Barre énergétique Boost Attack" or objet == "Barre energetique Boost Attack":
                Combat(100,0,100,35,55,15,Monstername) #+15 de dégats
            
            elif objet == "vaccin Pfizer":
                Combat(100,45,100,20,40,15,Monstername) # (bloc 3 attaques de l'ennemi)
            
            elif objet == "vaccin Moderna":
                Combat(100,30,100,20,40,15,Monstername) # (bloc 2 attaques de l'ennemi)
            
            elif objet == "vaccin Astra zanéca" or objet == "vaccin Astra zaneca":
                Combat(100,15,100,20,40,15,Monstername) # (bloc 1 attaques de l'ennemi)
#si jamais on est dans l'inventaire mais non veut rien alors ça lance la fonction Combat de base 
            elif objet == "rien":
                Combat(100,0,100,20,40,15,Monstername)
#si jamais on veut pas parcourir l'inventaire alors ça lance la fonction Combat de base
        elif choice == "non":
            Combat(100,0,100,20,40,15,Monstername)
        
        print("-"*50)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])

#2ème combat (même commentaire que le premier combat)
    elif map[y][x] == "!2":
        Monstername = "Pal-hue"
        print("\x1b[1m\x1b[37;45mUN ENNEMI EST APPARÛT !\x1b[0m")
        print("\x1b[1m\x1b[33;49mSouhaitez-vous parcourir votre sac juste avant le combat ? Vous pourrez choisir qu'un seul objet! \x1b[0m")
        
        choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
        if choice == "oui":
            objet = use_inventory()
            if objet == "Doliprane":
                Combat(150,0,125,20,40,30,Monstername) # + 50 pv pour notre joueur
            
            elif objet == "Vitamine C":
                Combat(125,0,125,20,40,30,Monstername) # + 25 pv pour notre joueur
            
            elif objet == "Fiole remède" or objet == "Fiole remede":
                Combat(100,0,125,50,70,30,Monstername) # +30 de dégats sur toutes nos armes
            
            elif objet == "Barre énergétique Boost Attack" or objet == "Barre energetique Boost Attack":
                Combat(100,0,125,35,55,30,Monstername) #+15 de dégats sur toutes nos armes
            
            elif objet == "vaccin Pfizer":
                Combat(100,90,125,20,40,30,Monstername) # (bloc 3 attaques de l'ennemi)
            
            elif objet == "vaccin Moderna":
                Combat(100,60,125,20,40,30,Monstername) # (bloc 2 attaques de l'ennemi)
            
            elif objet == "vaccin Astra zanéca" or objet == "vaccin Astra zaneca":
                Combat(100,30,125,20,40,30,Monstername) # (bloc 1 attaques de l'ennemi)
            
            elif objet == "rien":
                Combat(100,0,125,20,40,30,Monstername)

        elif choice == "non":
            Combat(100,0,125,20,40,30,Monstername)
        print("-"*50)
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])

#3ème combat(même commentaire que le deuxième et premier combat)
    elif map[y][x] == "!3":
        Monstername = "Grippex"
        print("\x1b[1m\x1b[37;45mUN ENNEMI EST APPARÛT !\x1b[0m")
        print("\x1b[1m\x1b[33;49mSouhaitez-vous parcourir votre sac juste avant le combat ? Vous pourrez choisir qu'un seul objet! \x1b[0m")

        choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
        if choice == "oui":
            objet = use_inventory()
            if objet == "Doliprane":
                result = Combat(150,0,150,20,40,45,Monstername) # + 50 pv pour notre joueur
                if result == True:
                    Dr_raoult()

            elif objet == "Vitamine C":
                result = Combat(125,0,150,20,40,45,Monstername) # + 25 pv pour notre joueur
                if result == True:
                    Dr_raoult()
            
            elif objet == "Fiole remède" or objet == "Fiole remede":
                result = Combat(100,0,150,50,70,45,Monstername) # +30 de dégats sur toutes nos armes
                if result == True:
                    Dr_raoult()
            
            elif objet == "Barre énergétique Boost Attack" or objet == "Barre energetique Boost Attack":
                result = Combat(100,0,150,35,55,45,Monstername) #+15 de dégats sur toutes nos armes
                if result == True:
                    Dr_raoult()
            
            elif objet == "vaccin Pfizer":
                result = Combat(100,135,150,20,40,45,Monstername) # (bloc 3 attaques de l'ennemi)
                if result == True:
                    Dr_raoult()
            
            elif objet == "vaccin Moderna":
                result = Combat(100,90,150,20,40,45,Monstername) # (bloc 2 attaques de l'ennemi)
                if result == True:
                    Dr_raoult()

            elif objet == "vaccin Astra zanéca" or objet == "vaccin Astra zaneca":
                result = Combat(100,45,150,20,40,45,Monstername) # (bloc 1 attaques de l'ennemi)
                if result == True:
                    Dr_raoult()
            
            elif objet == "rien":
                result = Combat(100,0,150,20,40,45,Monstername)
                if result == True:
                    Dr_raoult()
            
        elif choice == "non":
            result = Combat(100,0,150,20,40,45,Monstername)
            if result == True:
                Dr_raoult()
        
        print("-"*50)    
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])

#combat contre le boss(même commentraire que les combats précédents)
    elif map[y][x] == "$":
        print("Félicitation, vous avez touvé la sort...")
        Monstername = "Koronah-virusse"
        print("\x1b[1m\x1b[37;45mUN ENNEMI EST APPARÛT !\x1b[0m")
        print("\x1b[1m\x1b[33;49mSouhaitez-vous parcourir votre sac juste avant le combat ? Vous pourrez choisir qu'un seul objet! \x1b[0m")

        choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
        if choice == "oui":
            objet = use_inventory()
            if objet == "Doliprane":
                Combat_Boss(150,0,200,20,40,60,Monstername) # + 50 pv pour notre joueur
            
            elif objet == "Vitamine C":
                Combat_Boss(125,0,200,20,40,60,Monstername) # + 25 pv pour notre joueur
            
            elif objet == "Fiole remède" or objet == "Fiole remede":
                Combat_Boss(100,0,200,50,70,60,Monstername) # +30 de dégats sur toutes nos armes
            
            elif objet == "Barre énergétique Boost Attack" or objet == "Barre energetique Boost Attack":
                Combat_Boss(100,0,200,35,55,60,Monstername) #+15 de dégats sur toutes nos armes
            
            elif objet == "vaccin Pfizer":
                Combat_Boss(100,180,200,20,40,60,Monstername) # (bloc 3 attaques de l'ennemi)
            
            elif objet == "vaccin Moderna":
                Combat_Boss(100,120,200,20,40,60,Monstername) # (bloc 2 attaques de l'ennemi)
            
            elif objet == "vaccin Astra zanéca" or objet == "vaccin Astra zaneca":
                Combat_Boss(100,60,200,20,40,60,Monstername) # (bloc 1 attaques de l'ennemi)
            
            elif objet == "rien":
                Combat_Boss(100,0,200,20,40,60,Monstername)     

        elif choice == "non":
            Combat_Boss(100,0,200,20,40,60,Monstername)     
        input("\x1b[3mAppuyez sur Entrée pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous êtes ici:",map[y][x])

    elif map[y][x] == "_":
        print("Il n'y a rien ici")
#ici c'est les déplacements
    print("\x1b[1m\x1b[3mPour vous déplacer, veuillez juste saisir la direction où vous souhaitez allé.\x1b[0m")
    choice = input("\x1b[1m\x1b[32;49m[nord][sud][est][ouest][quit game]: \x1b[0m")
    if choice == "nord":
        y = y - 1
            
    elif choice == "sud":    
        y = y + 1
            
    elif choice == "est":
        x = x + 1
            
    elif choice == "ouest":
        x = x - 1
    
    elif choice == "quit game":
        print("Vous avez quitté le jeu")
        print("Au revoir, à bientôt !")
        return
#permet d'éviter le plantage du jeu, si on rentre une direction impossible        
    else:
        print("\x1b[1m\x1b[31;49mdirection non connue \x1b[0m")
        moove(y,x,Map)
    moove(y,x,Map)
