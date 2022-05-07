from Menu import menu
from Moove import *
def game():
#ceci est notre fonction de jeu, ou il y a d'abord le menu,
#puis un petit texte qui nous introduis brièvement le jeu,
#ensuite on demande le pseudo au joueur ensuite on appelle une petite fonction qui,
#nous montre à quoi correspondent chaque objet sur notre map
    menu()
    print_presentation_du_jeu()
    ask_name()
    info()
    moove(1,1,Map)
    

def print_presentation_du_jeu():
#cette fonction nous affiche la présenation du jeu    
    print("""
    Vous allez apparaître dans un gigantesque forêt.
    Vous pourrez vous baladez dans cette forêt, et votre but est de sortir de cette dernière.
    Tout au long de votre balade vous allez trouvé des objets que vous pourrez décider de ramasser ou non.
    Vous allez tombez sur des Maladies qui voudront vous anéantir, vous devrez alors tous les tués,
    pour avancer dans le jeu, et devenir plus fort et peut-être un jour sortir de la forêt.
    Bonne chance, amusez vous bien !! 
    """)



def ask_name():
#cette fonction nous demande de saisir un pseudo et cette fonction retourne ce pseudo saisi
    nom_de_joueur = input("\x1b[3m\x1b[34;49mQuel est le nom de votre perso ?: \x1b[0m")
    print(f"\x1b[1mQue le jeu commence {nom_de_joueur} !\x1b[0m")
    return nom_de_joueur
game()