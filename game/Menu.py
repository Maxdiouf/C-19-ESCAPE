def menu():
#fonction qui pemet d'afficher un menu
#il y a 3 actions possible(jouer, info ou bien quitter le jeu)
#pour lancer l'action on a use un input et un 'if' ensuite on fait un appelle de la
#fonction associé aà notre choix
    print("\x1b[1m-"* 40)
    print("\x1b[1m\x1b[36;49m   Bienvenue au jeu 'C19 Escape'\x1b[0m")
    print("")
    print("\x1b[1m           MENU")
    print("\x1b[1m\x1b[32;49m       >1.start new game\x1b[0m")
    print("\x1b[1m\x1b[33;49m       >2.info\x1b[0m")
    print("\x1b[1m\x1b[31;49m       >3.quit game\x1b[0m")
    print("")
    choice = int(input("\x1b[3m\x1b[34;49mQue voulez vous faire ? [1] [2] [3]: \x1b[0m"))
    if  choice != 1 and choice != 2 and choice != 3 :
        choice = int(input("\x1b[3m\x1b[34;49mQue voulez vous faire ? [1] [2] [3]: \x1b[0m"))
    elif choice == 1:
        return
    elif choice == 2:
        info()
    elif choice == 3:
        quit()

def info():
#fonction nous affichant les règles du jeu et les créateurs de ce jeu
    print("-"* 40)
    print("\x1b[1m\x1b[4mLES RÈGLES :\x1b[0m")
    print("""
    Vous êtes dans une forêt et vous devez en sortir en trouvant la sortie. 
    Tout au long de votre balade dans la forêt vous trouverez des objets,
    vous rencontrerez des maladies que vous devrez tuer dans le bonne ordre du premier au dernier
    pour pouvoir tuer le boss final et enfin sortir de cette forêt. 
    """)
    print("""\x1b[1mCE JEU a été crée par: \x1b[0m
    LACES Vitomir
    DIARRA Abdramane
    DIOP Abdoulaye
    GUIRO Alex
    DIOUF Maguette
    FANE Yaya
    """)
    input("\x1b[3m\x1b[34;49mAppuyer sur Entrer pour afficher le menu: \x1b[0m")
    menu()

import sys
def quit() : 
#il s'agit ici de la fonction 
#qui nous permettra de quitter le jeu. aprés chaque 
#niveau, le programme demande au joueur s'il veut continuer 
#la npartie ou pas et quand celui ci saisi stop,
#le jeu se termine automatiquement
    
    print("-"* 50)
    print("\x1b[91;49mvoulez-vous quitter le jeu ?\x1b[0m")
    choice = input("\x1b[3m\x1b[34;49m[oui] [non]: \x1b[0m")

    if choice == "oui":
        print("Vous avez quitté le jeu")
        print("Au revoir, à bientôt !")
        sys.exit()
    elif choice == "non" :
        print("Vous êtes toujours sur le jeu")
        menu()
    elif choice != "oui" and choice != "non":
        print("veuillez entrez une bonne réponse")
        quit()
    else :
        print("réponse non comprise")

def second_menu(): 
#Il s'agit de la fonction qui permettra au joueur de pouvoir continuer
#le jeu même s'il pert un combat contre un monstre.
#ici, aprés chaque échec, un second menu est affiché en demandant au joueur 
#soit de continuer la partie, soit reveoir les infos ou quitter.
#il s'agit en quelque sorte de la fonction save
    print("\x1b[1m-"* 40)
    print("\x1b[1m\x1b[36;49m   Bienvenue au jeu 'C19 Escape'\x1b[0m")
    print("")
    print("\x1b[1m           MENU")
    print("\x1b[1m\x1b[32;49m       >1.continue old game\x1b[0m")
    print("\x1b[1m\x1b[33;49m       >2.info\x1b[0m")
    print("\x1b[1m\x1b[31;49m       >3.quit game\x1b[0m")
    print("")
    choice = int(input("\x1b[3m\x1b[34;49mQue voulez vous faire ? [1] [2] [3]: \x1b[0m"))
    if  choice != 1 and choice != 2 and choice != 3 :
        choice = int(input("\x1b[3m\x1b[34;49mQue voulez vous faire ? [1] [2] [3]: \x1b[0m"))
    elif choice == 1:
        return
    elif choice == 2:
        info()
    elif choice == 3:
        quit()