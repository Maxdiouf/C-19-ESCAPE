#voici notre carte de jeu
Map = [
        ["!1","D","π²","π²","π²", "π²", "π²", "π²", "!2", "π²"],
        ["π²","X","π²","π²","π²", "π²", "π²", "π²", "π²", "π²"],
        ["V","π²","π²","π²","π²" , "π²", "π²", "B", "π²", "π²","π²"],
        ["π²","π²","π²","π²","π²", "π²", "π²", "π²", "π²", "π²"],
        ["π²","A","π²","π²","π²", "π²", "π²", "π²", "π²", "M","π²"],
        ["π²","π²","π²","π²","π²", "π²", "π²", "π²", "!3","π²"],
        ["P","π²","π²","π²","π²", "π²", "π²", "π²", "π²", "π²"],
        ["π²","π²","π²","π²","π²", "F", "π²", "π²", "π²", "$" ],
]

def show_map(carte):
#fonction nous affichant bien la map
    i = 0
    while i < len(carte):
        print(carte[i])
        i = i + 1    

def info():
#fonction qui nous montre Γ  quoi correspondent chaque objet sur notre map
    print("-"*50)
    print("""
    \x1b[4mVoici quelques informations Γ  propos de la Carte:\x1b[0m
    π² == il y a rien 
    X == Vous 
    $ == la sortie de la fΓ΄ret 
    ! == une maladie /3
    D == Doliprane (Vous ajoute 50 pv.)  
    V == Vitamine C (Vous ajoute 25 pv.)  
    A ==  vaccin Astra zanΓ©ca (Permet de bloquer 1 coup du monstre avec votre bouclier)
    M == vaccin Moderna (Permet de bloquer 2 coups du monstre avec votre bouclier)
    P == vaccin Pfizer (Permet de bloquer 3 coups du monstre avec votre bouclier)
    B == Barre Γ©nergΓ©tique Boost Attack (Permet de faire 15 de dΓ©gats en plus par coups)
    F == fiole remΓ¨de Γ  appliquer sur son arme (Permet de faire 30 de dΓ©gats en plus par coups)
    """)

def add_2inventory(Liste,objet):   
#fonction qui permet d'ajouter des objets dans l'inventaire
    #Γ  chaque fois il y a un objet si oui 
    #alors faire la fonction en parametre avec l'objet de la case
    if objet in Liste:
        print("\x1b[1mVous avez dΓ©ja",objet,"dans votre sac.\x1b[0m")
        return
    print(f"\x1b[1m\x1b[32;49mSouhaitez-vous mettre {objet} dans votre sac ?\x1b[0m")
    choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
    if choice == "oui":
        Liste.append(objet)
        print(f"\x1b[1m{objet} Γ  bien Γ©tΓ© mis dans votre sac.\x1b[0m")
        return Liste
    elif choice == "non":
        print(f"\x1b[1m{objet} a Γ©tΓ© laissΓ© sur le sol.\x1b[0m")
        return Liste
    else:
        print("\x1b[31;49mrΓ©ponse inconnue")
        add_2inventory(Liste,objet)

def use_inventory():
#fonction qui permet d'afficher du texte si oui ou non, pon utilise un objet
#ensuite selon la rΓ©ponse de cette fonction, on lancera une fonction Combat
#avec les paramΓͺtres associΓ©s avec l'objet utilisΓ©
#ex: si on utilise le Doliprane alors on met en paramΓͺtre Γ  Combat que on a 150 pv au lieu de 100pv
    print("\x1b[1m\x1b[33;49mVoici le contenu de votre sac: \x1b[0m",inventaire)
    print("\x1b[1mQue voulez vous utiliser?\x1b[0m")
    choice_object = input("\x1b[1m\x1b[34;49mEntrez le nom exacte de l'objet que vous voulez ou bien entrez 'rien' si vous voulez rien: \x1b[0m")
    if choice_object == "rien":
        return choice_object
    else:
        print("\x1b[33;49mVous utilisΓ©\x1b[0m",choice_object)
        return choice_object

def Dr_raoult():
#petit personnage surprise qui apparaΓ?t seulement si on gagne au 3Γ¨me combat
#ce personnage nous indiqueras le chemin pour aller vers la sortie
    print("-"*50)
    print("\x1b[1m\x1b[33;49mDr Raoult est apparΓ»t et semble vouloir vous parlez\x1b[0m")
    input("\x1b[3m\x1b[34;49mAppuyez sur EntrΓ©e pour afficher la suite\x1b[0m")
    print("")
    print("\x1b[1m\x1b[33;49mDr Raoult: Salut aventurier(Γ¨re).\x1b[0m")
    input("\x1b[3m\x1b[34;49mAppuyez sur EntrΓ©e pour afficher la suite\x1b[0m")
    print("")
    print("\x1b[1m\x1b[33;49mDr Raoult: Il paraΓ?t qu' Γ  la sortie, il s'y cachait une grosse maladie!\x1b[0m")
    input("\x1b[3m\x1b[34;49mAppuyez sur EntrΓ©e pour afficher la suite\x1b[0m")
    print("")
    print("\x1b[1m\x1b[33;49mDr Raoult: Il vous faudra un des trois vaccins pour pouvoir battre cette crΓ©ature car elle est surpuissante et imbattable sans vaccin.\x1b[0m")
    input("\x1b[3m\x1b[34;49mAppuyez sur EntrΓ©e pour afficher la suite\x1b[0m")
    print("")
    print("\x1b[1m\x1b[33;49mDr Raoult: Bonne chance aventurier(Γ¨re) !\x1b[0m")
    print("-"*50)
    return

from Combat import Combat
from Combat import Combat_Boss
inventaire = []
def moove(y,x,map): # config y et x a la position oΓΉ on se trouve avant de vouloir bouger.
    print("-"* 50)
    show_map(Map)
    print("\x1b[1mVous Γͺtes ici: \x1b[0m",map[y][x]) #position du joueur initiale
#si la case oΓΉ on se trouve il y a n'importe qu'elle lettre alors 
#l'objet associΓ© Γ  la lettre est ajouter Γ  l'inventaire
#c'est pareil pour tous les autres objets
    if map[y][x] == "D":
        objet = "Doliprane"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])
        
    elif map[y][x] == "V":
        objet = "Vitamine C"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])
        
    elif map[y][x] == "A":
        objet = "vaccin Astra zanΓ©ca"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])
        
    elif map[y][x] == "M":
        objet = "vaccin Moderna"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])
        
    elif map[y][x] == "P":
        objet = "vaccin Pfizer"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])
        
    elif map[y][x] == "B":
        objet = "Barre Γ©nergΓ©tique Boost Attack"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])
        
    elif map[y][x] == "F":
        objet = "Fiole remΓ¨de"
        add_2inventory(inventaire,objet)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])
    
#premier combat   
    elif map[y][x] == "!1":
#on determine un Monstername afin de le rΓ©utilisΓ© pour lancer notre fonction Combat
        Monstername = "Rhu-meuh"
        print("\x1b[1m\x1b[37;45mUN ENNEMI EST APPARΓT !\x1b[0m")
        print("\x1b[1m\x1b[33;49mSouhaitez-vous parcourir votre sac juste avant le combat ? Vous pourrez choisir qu'un seul objet! \x1b[0m")

        choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
#input qui demande si on veut parcourir l'inventaire
        if choice == "oui":
#si oui ce que l'on va rentrΓ© dans le input,Γ§a lancera Combat mais avec des paramΓ¨tres diffΓ©rents
            objet = use_inventory()
            if objet == "Doliprane":
                Combat(150,0,100,20,40,15,Monstername) # + 50 pv pour notre joueur
            
            elif objet == "Vitamine C":
                Combat(125,0,100,20,40,15,Monstername) # + 25 pv pour notre joueur
            
            elif objet == "Fiole remΓ¨de" or objet == "Fiole remede":
                Combat(100,0,100,50,70,15,Monstername) # +30 de dΓ©gats
            
            elif objet == "Barre Γ©nergΓ©tique Boost Attack" or objet == "Barre energetique Boost Attack":
                Combat(100,0,100,35,55,15,Monstername) #+15 de dΓ©gats
            
            elif objet == "vaccin Pfizer":
                Combat(100,45,100,20,40,15,Monstername) # (bloc 3 attaques de l'ennemi)
            
            elif objet == "vaccin Moderna":
                Combat(100,30,100,20,40,15,Monstername) # (bloc 2 attaques de l'ennemi)
            
            elif objet == "vaccin Astra zanΓ©ca" or objet == "vaccin Astra zaneca":
                Combat(100,15,100,20,40,15,Monstername) # (bloc 1 attaques de l'ennemi)
#si jamais on est dans l'inventaire mais non veut rien alors Γ§a lance la fonction Combat de base 
            elif objet == "rien":
                Combat(100,0,100,20,40,15,Monstername)
#si jamais on veut pas parcourir l'inventaire alors Γ§a lance la fonction Combat de base
        elif choice == "non":
            Combat(100,0,100,20,40,15,Monstername)
        
        print("-"*50)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])

#2Γ¨me combat (mΓͺme commentaire que le premier combat)
    elif map[y][x] == "!2":
        Monstername = "Pal-hue"
        print("\x1b[1m\x1b[37;45mUN ENNEMI EST APPARΓT !\x1b[0m")
        print("\x1b[1m\x1b[33;49mSouhaitez-vous parcourir votre sac juste avant le combat ? Vous pourrez choisir qu'un seul objet! \x1b[0m")
        
        choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
        if choice == "oui":
            objet = use_inventory()
            if objet == "Doliprane":
                Combat(150,0,125,20,40,30,Monstername) # + 50 pv pour notre joueur
            
            elif objet == "Vitamine C":
                Combat(125,0,125,20,40,30,Monstername) # + 25 pv pour notre joueur
            
            elif objet == "Fiole remΓ¨de" or objet == "Fiole remede":
                Combat(100,0,125,50,70,30,Monstername) # +30 de dΓ©gats sur toutes nos armes
            
            elif objet == "Barre Γ©nergΓ©tique Boost Attack" or objet == "Barre energetique Boost Attack":
                Combat(100,0,125,35,55,30,Monstername) #+15 de dΓ©gats sur toutes nos armes
            
            elif objet == "vaccin Pfizer":
                Combat(100,90,125,20,40,30,Monstername) # (bloc 3 attaques de l'ennemi)
            
            elif objet == "vaccin Moderna":
                Combat(100,60,125,20,40,30,Monstername) # (bloc 2 attaques de l'ennemi)
            
            elif objet == "vaccin Astra zanΓ©ca" or objet == "vaccin Astra zaneca":
                Combat(100,30,125,20,40,30,Monstername) # (bloc 1 attaques de l'ennemi)
            
            elif objet == "rien":
                Combat(100,0,125,20,40,30,Monstername)

        elif choice == "non":
            Combat(100,0,125,20,40,30,Monstername)
        print("-"*50)
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])

#3Γ¨me combat(mΓͺme commentaire que le deuxiΓ¨me et premier combat)
    elif map[y][x] == "!3":
        Monstername = "Grippex"
        print("\x1b[1m\x1b[37;45mUN ENNEMI EST APPARΓT !\x1b[0m")
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
            
            elif objet == "Fiole remΓ¨de" or objet == "Fiole remede":
                result = Combat(100,0,150,50,70,45,Monstername) # +30 de dΓ©gats sur toutes nos armes
                if result == True:
                    Dr_raoult()
            
            elif objet == "Barre Γ©nergΓ©tique Boost Attack" or objet == "Barre energetique Boost Attack":
                result = Combat(100,0,150,35,55,45,Monstername) #+15 de dΓ©gats sur toutes nos armes
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

            elif objet == "vaccin Astra zanΓ©ca" or objet == "vaccin Astra zaneca":
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
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])

#combat contre le boss(mΓͺme commentraire que les combats prΓ©cΓ©dents)
    elif map[y][x] == "$":
        print("FΓ©licitation, vous avez touvΓ© la sort...")
        Monstername = "Koronah-virusse"
        print("\x1b[1m\x1b[37;45mUN ENNEMI EST APPARΓT !\x1b[0m")
        print("\x1b[1m\x1b[33;49mSouhaitez-vous parcourir votre sac juste avant le combat ? Vous pourrez choisir qu'un seul objet! \x1b[0m")

        choice = input("\x1b[3m\x1b[34;49m[oui] ou [non]: \x1b[0m")
        if choice == "oui":
            objet = use_inventory()
            if objet == "Doliprane":
                Combat_Boss(150,0,200,20,40,60,Monstername) # + 50 pv pour notre joueur
            
            elif objet == "Vitamine C":
                Combat_Boss(125,0,200,20,40,60,Monstername) # + 25 pv pour notre joueur
            
            elif objet == "Fiole remΓ¨de" or objet == "Fiole remede":
                Combat_Boss(100,0,200,50,70,60,Monstername) # +30 de dΓ©gats sur toutes nos armes
            
            elif objet == "Barre Γ©nergΓ©tique Boost Attack" or objet == "Barre energetique Boost Attack":
                Combat_Boss(100,0,200,35,55,60,Monstername) #+15 de dΓ©gats sur toutes nos armes
            
            elif objet == "vaccin Pfizer":
                Combat_Boss(100,180,200,20,40,60,Monstername) # (bloc 3 attaques de l'ennemi)
            
            elif objet == "vaccin Moderna":
                Combat_Boss(100,120,200,20,40,60,Monstername) # (bloc 2 attaques de l'ennemi)
            
            elif objet == "vaccin Astra zanΓ©ca" or objet == "vaccin Astra zaneca":
                Combat_Boss(100,60,200,20,40,60,Monstername) # (bloc 1 attaques de l'ennemi)
            
            elif objet == "rien":
                Combat_Boss(100,0,200,20,40,60,Monstername)     

        elif choice == "non":
            Combat_Boss(100,0,200,20,40,60,Monstername)     
        input("\x1b[3mAppuyez sur EntrΓ©e pour afficher de nouveau la map: \x1b[0m")
        show_map(Map)
        print("Vous Γͺtes ici:",map[y][x])

    elif map[y][x] == "_":
        print("Il n'y a rien ici")
#ici c'est les dΓ©placements
    print("\x1b[1m\x1b[3mPour vous dΓ©placer, veuillez juste saisir la direction oΓΉ vous souhaitez allΓ©.\x1b[0m")
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
        print("Vous avez quittΓ© le jeu")
        print("Au revoir, Γ  bientΓ΄t !")
        return
#permet d'Γ©viter le plantage du jeu, si on rentre une direction impossible        
    else:
        print("\x1b[1m\x1b[31;49mdirection non connue \x1b[0m")
        moove(y,x,Map)
    moove(y,x,Map)
