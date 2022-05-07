from Menu import *
import sys
def Combat(Playerlife,Playershield,Monsterlife,sworddamage,arcdamage,Monsterdamage,Monstername):
#cette fonction est le combat de nos 3 premiers monstres
#d'abord on a un peu de texte nous présentant l'ennemi(ses points de vies et ses dégats), et
#nos informations(pv et points de vies de notre bouclier et dégats)
    print("\x1b[1m\x1b[31;49mIl s'agit de",Monstername,"qui a",Monsterlife,"pv et vous enlève",Monsterdamage,"pv par coups.\x1b[0m")
    print("\x1b[1m\x1b[32;49mVous avez",Playerlife,"pv et un bouclier avec",Playershield,"pv\x1b[0m")
    print("\x1b[1mQue souhaitez vous faire ? \x1b[0m")
#possibilité soit de se battre soit de fuir le combat
    choice = input("\x1b[1m\x1b[34;49m[combattre] ou [fuir]: \x1b[0m")
    if choice == "combattre":
        print("Votre épée fait",sworddamage,"de dégats par coups et votre arc fait",arcdamage,"de dégats.")
#choix de l'arme que l'on souhaite faire usage
        choiceweapon = input("\x1b[1m\x1b[31;49m[épée] ou [arc]: \x1b[0m")
        
        if choiceweapon == "épée" or choiceweapon == "epee":
            while Monsterlife > 0 or Playerlife > 0:
                input("\x1b[1m\x1b[31;49mAppuyez sur la touche Entrée pour le frapper\x1b[0m")
                Monsterlife = Monsterlife - sworddamage
                
                if Monsterlife <= 0:
                    break
                print("Vous avez mis un coup à",Monstername,", il lui reste",Monsterlife,"pv.")
                
                if Playershield > 0:
                    Playershield = Playershield - Monsterdamage
                    print(Monstername,"a tapé sur votre bouclier, il reste",Playershield,"pv à votre bouclier.")
                    if Playershield <= 0:
                        print(Monstername,"a détruit votre bouclier!")
                    
                    if Monsterlife <= 0:
                        break
                    Monsterlife = Monsterlife - sworddamage
                    print("Vous avez mis un coup à",Monstername,", il lui reste",Monsterlife,"pv.")
                elif Playershield <= 0:
                    Playerlife = Playerlife - Monsterdamage
                
                if Playerlife <= 0:
                    break
                print(Monstername,"contre-attaque et il vous reste",Playerlife,"pv.")
            
            if Monsterlife < Playerlife :
#cas où l'on gagne le combat
                print("\x1b[1m\x1b[32;49mVous avez dézingué",Monstername,"!\x1b[0m")
                print("\x1b[3m\x1b[33;49mVos points de vie on été remis à 100\x1b[0m")
                print("-"*50)
                return True
            
            elif Playerlife < Monsterlife:
#cas où l'on perd le combat
                print(Monstername,"\x1b[31;49mVous a défoncé! Vous êtes mort\x1b[0m")
                print("\x1b[1m\x1b[31;49mGAME OVER\x1b[0m")
                second_menu()
                #appel de la fonction second_menu qui sauvegarde notre niveau et nous
                #demande de continuer ou quitter

                
        
        elif choiceweapon == "arc":
            while Monsterlife > 0 or Playerlife > 0:
                input("\x1b[1m\x1b[31;49mAppuyez sur la touche Entrée pour le frapper\x1b[0m")
                Monsterlife = Monsterlife - arcdamage
                
                if Monsterlife <= 0:
                    break
                print("Vous avez mis un coup à",Monstername,", il lui reste",Monsterlife,"pv.")
                
                if Playershield > 0:
                    Playershield = Playershield - Monsterdamage
                    print(Monstername,"a tapé sur votre bouclier, il reste",Playershield,"pv à votre bouclier.")
                    if Playershield <= 0:
                        print(Monstername,"a détruit votre bouclier!")
                    
                    if Monsterlife <= 0:
                        break
                    Monsterlife = Monsterlife - arcdamage
                    print("Vous avez mis un coup à",Monstername,", il lui reste",Monsterlife,"pv.")
                elif Playershield <= 0:
                    Playerlife = Playerlife - Monsterdamage
                
                if Playerlife <= 0:
                    break
                print(Monstername,"contre-attaque et il vous reste",Playerlife,"pv.")
            
            if Monsterlife < Playerlife :
#cas où l'on gagne le combat
                print("\x1b[1m\x1b[32;49mVous avez dézingué",Monstername,"!\x1b[0m")
                print("\x1b[3m\x1b[33;49mVos points de vie on été remis à 100\x1b[0m")
                print("-"*50)
                return True
            
            elif Playerlife < Monsterlife:
#cas où l'on perd le combat
                print("\x1b[31;49mVous êtes mort\x1b[0m")
                print("\x1b[1m\x1b[31;49mGAME OVER\x1b[0m")
                second_menu()
                #appel de la fonction second_menu qui sauvegarde notre niveau et nous
                #demande de continuer ou quitter
        else:
#permet de ne pas faire bugé le jeu si l'on saisi un arme non existante
            print("\x1b[1m\x1b[31;49mCette arme existe pas\x1b[0m")
            Combat(Playerlife,Playershield,Monsterlife,sworddamage,arcdamage,Monsterdamage,Monstername)

    
    elif choice == "fuir":
#si l'on fuit le combat
        print("\x1b[1mVous avez fuit le combat...Revenez mieux équipé !")
        print("-"*50)
        return False
    else:
#pemet d'éviter le plantage du jeu, si on saisit une action non cohérente
        print("\x1b[1m\x1b[31;49mCette action n'existe pas\x1b[0m")
        Combat(Playerlife,Playershield,Monsterlife,sworddamage,arcdamage,Monsterdamage,Monstername)


#c'est exactement la même fonction que celle d'au dessus
#sauf que dans celle là lorsqu'on gagne, le jeu se fini et on quitte le jeu(l.155 et l.195)
def Combat_Boss(Playerlife,Playershield,Monsterlife,sworddamage,arcdamage,Monsterdamage,Monstername):
    print("\x1b[1m\x1b[31;49mIl s'agit de",Monstername,"qui a",Monsterlife,"pv et vous enlève",Monsterdamage,"pv par coups.\x1b[0m")
    print("\x1b[1m\x1b[32;49mVous avez",Playerlife,"pv et un bouclier avec",Playershield,"pv\x1b[0m")
    print("\x1b[1mQue souhaitez vous faire ? \x1b[0m")
    
    choice = input("\x1b[1m\x1b[34;49m[combattre] ou [fuir]: \x1b[0m")
    if choice == "combattre":
        print("Votre épée fait",sworddamage,"de dégats par coups et votre arc fait",arcdamage,"de dégats.")
        choiceweapon = input("\x1b[1m\x1b[31;49m[épée] ou [arc]: \x1b[0m")
        
        if choiceweapon == "épée" or choiceweapon == "epee":
            while Monsterlife > 0 or Playerlife > 0:
                input("\x1b[1m\x1b[31;49mAppuyez sur la touche Entrée pour le frapper\x1b[0m")
                Monsterlife = Monsterlife - sworddamage
                
                if Monsterlife <= 0:
                    break
                print("Vous avez mis un coup à",Monstername,", il lui reste",Monsterlife,"pv.")
                
                if Playershield > 0:
                    Playershield = Playershield - Monsterdamage
                    print(Monstername,"a tapé sur votre bouclier, il reste",Playershield,"pv à votre bouclier.")
                    if Playershield <= 0:
                        print(Monstername,"a détruit votre bouclier!")
                    
                    if Monsterlife <= 0:
                        break
                    Monsterlife = Monsterlife - sworddamage
                    print("Vous avez mis un coup à",Monstername,", il lui reste",Monsterlife,"pv.")
                elif Playershield <= 0:
                    Playerlife = Playerlife - Monsterdamage
                
                if Playerlife <= 0:
                    break
                print(Monstername,"contre-attaque et il vous reste",Playerlife,"pv.")
            
            if Monsterlife < Playerlife :
                print("\x1b[1m\x1b[32;49mVous avez dézingué",Monstername,"!\x1b[0m")
                print("\x1b[32;49mVous êtes sorti de la forêt\x1b[0m")
                print("\x1b[1m\x1b[32;49mYOU WIN !!!\x1b[0m")
                return
            
            elif Playerlife < Monsterlife:
                print("\x1b[31;49mVous êtes mort\x1b[0m")
                print("\x1b[1m\x1b[31;49mGAME OVER\x1b[0m")
                second_menu()
                #appel de la fonction second_menu qui sauvegarde notre niveau et nous
                #demande de continuer ou quitter                
        
        elif choiceweapon == "arc":
            while Monsterlife > 0 or Playerlife > 0:
                input("\x1b[1m\x1b[31;49mAppuyez sur la touche Entrée pour le frapper\x1b[0m")
                Monsterlife = Monsterlife - arcdamage
                
                if Monsterlife <= 0:
                    break
                print("Vous avez mis un coup à",Monstername,", il lui reste",Monsterlife,"pv.")
                
                if Playershield > 0:
                    Playershield = Playershield - Monsterdamage
                    print(Monstername,"a tapé sur votre bouclier, il reste",Playershield,"pv à votre bouclier.")
                    if Playershield <= 0:
                        print(Monstername,"a détruit votre bouclier!")
                    
                    if Monsterlife <= 0:
                        break
                    Monsterlife = Monsterlife - arcdamage
                    print("Vous avez mis un coup à",Monstername,", il lui reste",Monsterlife,"pv.")
                elif Playershield <= 0:
                    Playerlife = Playerlife - Monsterdamage
                
                if Playerlife <= 0:
                    break
                print(Monstername,"contre-attaque et il vous reste",Playerlife,"pv.")
            
            if Monsterlife < Playerlife :
                print("\x1b[1m\x1b[32;49mVous avez dézingué",Monstername,"!")
                print("\x1b[32;49mVous êtes sorti de la forêt\x1b[0m")
                print("\x1b[1m\x1b[32;49mYOU WIN !!!\x1b[0m")
                sys.exit()
            
            elif Playerlife < Monsterlife:
                print("\x1b[31;49mVous êtes mort\x1b[0m")
                print("\x1b[1m\x1b[31;49mGAME OVER\x1b[0m")
                second_menu()
        else:
            print("\x1b[1m\x1b[31;49mCette arme existe pas\x1b[0m")
            Combat_Boss(Playerlife,Playershield,Monsterlife,sworddamage,arcdamage,Monsterdamage,Monstername)
    
    elif choice == "fuir":
        print("\x1b[1mVous avez fuit le combat...Revenez mieux équipé !")
        print("-"*50)
        return
    
    else:
        print("\x1b[1m\x1b[31;49mCette action n'existe pas\x1b[0m")
        Combat_Boss(Playerlife,Playershield,Monsterlife,sworddamage,arcdamage,Monsterdamage,Monstername)