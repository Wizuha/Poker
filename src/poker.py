from random import randint
def turn():
  turn = randint(0,1)
  if turn == 0 :
    return 0
  elif turn == 1 :
    return 1

def suite(a,b,c) :
  if b == a + 1 and c == b + 1 :
    return True
  elif c == b + 1 and a == c + 1 :
    return True
  elif a == c + 1 and b == a + 1 :
    return True
  elif b == c + 1 and a == b + 1 :
    return True
  elif c == a + 1 and b == c + 1 :
    return True
  elif a == c + 1 and c == a + 1 :
    return True
  else : 
    return False

def compare_suite(a,b,c,d,e,f):
  y = a+b+c
  z = d+e+f
  if y < z :
    return True
  else :
    return False

def pair (a,b,c) :
  if a == b and c != b :
    return True
  elif c == b and a != b :
    return True
  elif a == c and b != c :
    return True
  else : 
    return False

def compare_pair(a,b,c,e,d,f):
  
  if a == b and e == d and a > e :
    return False
  elif a == b and e == d and a < e :
    return True
  elif a == b and e == d and a == e and c > f :
    return False
  elif a == b and e == d and a == e and c < f :
    return True
  
  elif a == c and e == f and a > e :
    return False
  elif a == c and e == f and a < e :
    return True
  elif a == c and e == f and a == e and b > d :
    return False
  elif a == c and e == f and a == e and b > d :
    return True

  elif b == c and d == f and b > d :
    return False
  elif b == c and d == f and b < d :
    return True
  elif b == c and d == f and b == d and a > e :
    return False
  elif b == c and d == f and b == d and a < e :
    return True
  
  elif a == c and d == e and a > d :
    return False
  elif a == c and d == e and a < d :
    return True
  elif a == c and d == e and a == d and b > f :
    return False
  elif a == c and d == e and a == d and b < f :
    return True
  
  elif a == c and d == f and a > d :
    return False
  elif a == c and d == f and a < d :
    return True
  elif a == c and d == f and a == d and b > e :
    return False
  elif a == c and d == f and a == d and b < e :
    return True

  elif e == f and a == b and e < a :
    return False
  elif e == f and a == b and e > a :
    return True
  elif e == f and a == b and a == e and d < c :
    return False
  elif e == f and a == b and a == e and d > c :
    return True

  elif b == c and e == f and b > e :
    return False
  elif b == c and e == f and b < e :
    return True
  elif b == c and e == f and b == e and a > d :
    return False
  elif b == c and e == f and b == e and a < d :
    return True

  elif a == c and d == f and a > d :
    return False
  elif a == c and d == f and a < d :
    return True
  elif a == c and d == f and a == d and b > e :
    return False
  elif a == c and d == f and a == d and b < e :
    return True

def brelan (a,b,c) :
  if a == b == c :
    return True
  else:
    return False

def compare_brelan(a,b,c,e,f,g):
  if a > e :
    return False
  else :
    return True

def comb_random(a,b,c):
  if brelan(a,b,c):
    return False
  elif suite(a,b,c):
    return False
  elif pair(a,b,c):
    return False
  else :
    return True

def compare_random(a,b,c,d,e,f):
  L = [a,b,c]
  V = [d,e,f]
  i = 0
  v = 0
  max = 0
  max1 = 0
  while i < len(L) :
    if L[i] > max :
      max = L[i]
    i += 1
  
  while v < len(V):
    if V[v] > max1 :
      max1 = V[v]
    v += 1
  
  if max > max1 :
    return False
  else :
    return True

from random import randint 
def poker():
  print("----------------------------- Bienvenue vous allez commencer à jouer au poker ----------------------------- ")
  
  reponse = input("Etes vous prêt à jouer ? \n oui ou non : ")
  tour = turn()
  sum_player = 100

  while reponse != "oui" and reponse != "non":
    reponse =input("Nous n'avons pas compris votre réponse\n oui ou non : ")

  while reponse == "oui" and sum_player > 0 :

    if tour == 1 :
      tour = 0
    elif tour == 0 :
      tour = 1
    
    
    print("Vous rentrez avec ",sum_player, "jetons\n")
    
    
    print("Vous allez à présent jouer 10 jetons pour commencer la partie")
    
    sum_player = sum_player - 10
    token_player = 10
    
    print("L'ia à jouer 10 jetons pour commencer la partie")
    token_ia = 10


    card1_ia = randint(1,10)
    card2_ia = randint(1,10)
    card3_ia = randint(1,10)

    print("Voici vos cartes :")
    card1_player = randint(1,10)
    print(card1_player)
    card2_player = randint(1,10)
    print(card2_player)
    card3_player = randint(1,10)
    print(card3_player,"\n")

    
    if tour == 1:
      choice_ia = randint(1,2)
      print("tour 1")
      if choice_ia == 1:        
        print("Vous avez gagné, l'ia à quitter la partie\n")
        token_player += token_ia
        sum_player += token_player
        print("Vos gains : +",token_player,"jetons")
        print("Votre somme :",sum_player,"jetons")
        reponse = input("Voulez vous rejouer une partie ? \noui ou non : ")
        while reponse != "oui" and reponse != "non":
          reponse = input("Nous avons mal compris votre réponse \n oui ou non : ")
        if reponse == "non":
          break
        if reponse == "oui":
          continue
      elif choice_ia == 2:
        
        print("L'ia à décidé de relancer et d'augmenter la mise\n")
        choice_bet_ia = randint(1,3)
        if choice_bet_ia == 1:
          choice_bet_ia = 20
          token_ia = token_ia + 20
        elif choice_bet_ia == 2:
          choice_bet_ia = 40
          token_ia = token_ia + 40
        elif choice_bet_ia == 3:
          choice_bet_ia = 60
          token_ia = token_ia + 60
        print("L'ia à misé",choice_bet_ia,"jetons")
        print("Mise total ia :",token_ia,"jetons\n")

        print("---------------------------------------------------------- ")

        choice = input(" 1 : Relaner et augmenter la mise \n 2 : S'arrêter \n 3 : Miser la même somme que l'ia\n Faite votre choix :  ")

        if choice == "1" and sum_player >= 60:
          choice_bet = input("Quel mise voulez-vous jouer ?\n 1 : 20 jetons\n 2 : 40 jetons\n 3 : 60 jetons \n Choisissez votre mise :  ")
          if choice_bet == "1" :
            choice_bet = 20
            sum_player = sum_player - 20
            token_player = token_player + 20
          elif choice_bet == "2":
            choice_bet = 40
            sum_player = sum_player - 40
            token_player = token_player + 40
          elif choice_bet == "3":
            choice_bet = 60
            sum_player = sum_player - 60
            token_player = token_player + 60
        elif choice == "1" and sum_player >= 40 and sum_player < 60 :
          choice_bet = input("Quel mise voulez-vous jouer ?\n 1 : 20 jetons\n 2 : 40 jetons \n Choisissez votre mise :  ")
          if choice_bet == "1" :
            choice_bet = 20
            sum_player = sum_player - 20
            token_player = token_player + 20
          elif choice_bet == "2":
            choice_bet = 40
            sum_player = sum_player - 40
            token_player = token_player + 40
        elif choice == "1" and sum_player >= 20 and sum_player < 40 :
          choice_bet = input("Quel mise voulez-vous jouer ?\n 1 : 20 jetons \n Choisissez votre mise :  ")
          if choice_bet == "1" :
            choice_bet = 20
            sum_player = sum_player - 20
            token_player = token_player + 20
        else :
          choice_bet = 10
          
        print("Mise :",choice_bet,"jetons")
        print("Mise total :",token_player,"jetons\n")

        if choice == "2":
          
          print("Vous avez perdu cette partie l'ia récupère vos jetons\n")
          token_ia = token_ia + token_player
          token_player = token_player - 10
          print("Vouys finissez la partie avec",sum_player,"jetons")
          reponse = input("Voulez-vous rejouer une partie ? \n oui ou non : ")
          while reponse != "oui" and reponse != "non":
            reponse = input("Nous avons mal compris votre réponse \n oui ou non : ")
          if reponse == "non":
            break
        
        elif choice == "3":
          if choice_bet_ia == 20:
            choice_bet = 20
            token_player = token_player + 20
            sum_player = sum_player - 20
          elif choice_bet_ia == 2:
            choice_bet = 40
            token_player = token_player + 40
            sum_player = sum_player - 40
          elif choice_bet_ia == 3:
            choice_bet = 60
            token_player = token_player + 60
            sum_player = sum_player - 60
        print("Vous avez décidé de miser ",choice_bet,"jetons la même somme que l'ia")
        print("Mise total:",token_player,"jetons\n")
    
    elif tour == 0:
      print("tour 0")
      choice = input(" 1 : S'arrêter \n 2 : Relaner et augmenter la mise\n En attente de votre choix :  ")
      
      if choice == "1":
        print("Vous avez décidé de vous arrêter l'ia recupère votre mise\n")
        token_ia = token_player + token_ia
        print("Vouys finissez la partie avec",sum_player,"jetons")
        reponse = input("Voulez-vous rejouer une partie ? \n oui ou non : ")
        while reponse != "oui" and reponse != "non":
          reponse = input("Nous avons mal compris votre réponse \n oui ou non : ")
        if reponse == "non":
          break

      elif choice == "2":
        choice_bet = input("Quel mise voulez-vous jouer ?\n 1 : 20 jetons\n 2 : 40 jetons\n 3 : 60 jetons \n  ")
        if choice_bet == "1" and sum_player >= 60:
          choice_bet = 20
          sum_player = sum_player - 20
          token_player = token_player + 20
        elif choice_bet == "2":
          choice_bet = 40
          sum_player = sum_player - 40
          token_player = token_player + 40
        elif choice_bet == "3":
          choice_bet = 60
          sum_player = sum_player - 60
          token_player = token_player + 60
        elif choice == "1" and sum_player >= 40 and sum_player < 60 :
          choice_bet = input("Quel mise voulez-vous jouer ?\n 1 : 20 jetons\n 2 : 40 jetons \n Choisissez votre mise :  ")
          if choice_bet == "1" :
            choice_bet = 20
            sum_player = sum_player - 20
            token_player = token_player + 20
          elif choice_bet == "2":
            choice_bet = 40
            sum_player = sum_player - 40
            token_player = token_player + 40
        elif choice == "1" and sum_player >= 20 and sum_player < 40 :
          choice_bet = input("Quel mise voulez-vous jouer ?\n 1 : 20 jetons \n Choisissez votre mise :  ")
          if choice_bet == "1" :
            choice_bet = 20
            sum_player = sum_player - 20
            token_player = token_player + 20
        elif choice == "1" and sum_player < 20 :
          choice_bet = 10
        print("Mise :",choice_bet,"jetons")
        print("Mise total :",token_player,"jetons")
      
      print("---------------------------------------------------------- ")

  # L'ia choisit sa mise
      choice_ia = randint(1,3)
      
      if choice_ia ==  1 :
        choice_bet_ia = randint(1,3)
        if choice_bet_ia == 1:
          choice_bet_ia = 20
          token_ia = token_ia + 20
        elif choice_bet_ia == 2:
          choice_bet_ia = 40
          token_ia = token_ia + 40
        elif choice_bet_ia == 3:
          choice_bet_ia = 60
          token_ia = token_ia + 60
        print("Mise ia :",choice_bet_ia,"jetons")
        print("Mise total ia :",token_ia,"jetons")
      elif choice_ia == 2 :
        print("Vous avez gagné l'ia à quitter la partie")
        token_player = token_ia + token_player
        sum_player += token_player
        print("Vos gains : +",token_player,"jetons")
        print("Votre somme :",sum_player)
        reponse = input("Voulez vous refaire une partie ?")
        while reponse != "oui" and reponse != "non":
          reponse = input("Voulez vous refaire une partie ?")
        if reponse == "oui":
          print("Vouys finissez la partie avec",sum_player,"jetons\n")
          continue
        else :
          print("Vouys finissez la partie avec",sum_player,"jetons\n")
          print("------------------ A bientot ------------------")
          break
        reponse = input("Voulez-vous rejouer une partie ? \n oui ou non : ")
        while reponse != "oui" and reponse != "non":
          reponse = input("Nous avons mal compris votre réponse \n oui ou non : ")
        if reponse == "non":
          break
      
      elif choice_ia == 3 :
        if choice_bet == 20 :
          choice_bet_ia = 20
          token_ia = token_ia + 20
        elif choice_bet == 40 :
          choice_bet_ia = 40
          token_ia = token_ia + 40
        elif choice_bet == 60 :
          choice_bet_ia = 60
          token_ia = token_ia + 60
        print("Mise ia: ",choice_bet_ia,"jetons")
        print("Mise total ia : ",token_ia,"jetons\n")

    print("---------------------------------------------------------- ")
    total = token_player + token_ia
    print("Gain total :",total,"jetons")
    print("---------------------------------------------------------- ")
    
    print("Voici les cartes de l'ia:")
    print(card1_ia)
    print(card2_ia)
    print(card3_ia,"\n")
    print("---------------------------------------------------------- ")
    print("Voici vos cartes :")
    print(card1_player)
    print(card2_player)
    print(card3_player,"\n")

    suite_ia = suite(card1_ia,card2_ia,card3_ia)
    suite_player = suite(card1_player,card2_player,card3_player)

    brelan_ia = brelan(card1_ia,card2_ia,card3_ia)
    brelan_player = brelan(card1_player,card2_player,card3_player)

    pair_ia = pair(card1_ia,card2_ia,card3_ia)
    pair_player = pair(card1_player,card2_player,card3_player)

    comb_random_ia = comb_random(card1_ia,card2_ia,card3_ia)
    comb_random_player = comb_random(card1_player,card2_player,card3_player)

    comb_ia = [suite_ia , brelan_ia , pair_ia,comb_random_ia]
    comb_player = [suite_player,brelan_player,pair_player,comb_random_player]

    
    if comb_ia[0] and comb_player[1]:
      print("L'ia a une suite | Vous avez un brelan")
      token_player = 0
      token_ia = total
      print("Vous avez perdu la partie\n")
    elif comb_ia[0] and comb_player[2]:
      print("L'ia a une suite | Vous avez une paire")
      token_player = 0
      token_ia = total
      print("Vous avez perdu la partie\n")
    elif comb_ia[1] and comb_player[2]:
      print("L'ia a un brelan | Vous avez une paire")
      token_player = 0
      token_ia = total
      print("Vous avez perdu la partie\n")
    elif comb_ia[1] and comb_player[0]:
      print("Vous avez une suite | L'ia a un brelan")
      token_ia = 0
      token_player = total
      sum_player += token_player
      print("Vous avez gagné la partie\n")
    elif comb_ia[2] and comb_player[0]:
      print("Vous avez une suite | L'ia a une paire")
      token_ia = 0
      token_player = total
      sum_player += token_player
      print("Vous avez gagné la partie\n")
    elif comb_ia[2] and comb_player[1]:
      print("Vous avez un brelan | L'ia a une paire")
      token_ia = 0
      token_player = total
      sum_player += token_player
      print("Vous avez gagné la partie\n")
    elif comb_ia[0] and comb_player[3]:
      print("L'ia a une suite | Vous avez des cartes randoms")
      token_player = 0
      token_ia = total
      print("Vous avez perdu la partie\n")
    elif comb_ia[3] and comb_player[0]:
      print("L'ia a des cartes randoms | Vous avez une suite")
      token_ia = 0
      token_player = total
      sum_player += token_player
      print("Vous avez gagné la partie\n")
    elif comb_ia[1] and comb_player[3]:
      print("L'ia a un brelan | Vous avez des cartes randoms")
      token_player = 0
      token_ia = total
      print("Vous avez perdu la partie\n")
    elif comb_ia[2] and comb_player[3]:
      print("L'ia a une paire | Vous avez des cartes randoms")
      token_player = 0
      token_ia = total
      print("Vous avez perdu la partie\n")
    elif comb_ia[3] and comb_player[1]:
      print("L'ia a des cartes randoms | Vous avez un brelan")
      token_ia = 0
      token_player = total
      sum_player += token_player
      print("Vous avez gagné la partie\n")
    elif comb_ia[3] and comb_player[2]:
      print("L'ia a des cartes randoms | Vous avez une paire")
      token_ia = 0
      token_player = total
      sum_player += token_player
      print("Vous avez gagné la partie\n")
    elif comb_ia[3] and comb_player[3]:
      print("L'ia a des cartes randoms | Vous avez des cartes randoms")
      compare_random(card1_ia,card2_ia,card3_ia,card1_player,card2_player,card3_player)
      if True :
        print("Vous avez gagné la partie\n")
        token_ia = 0
        token_player = total
        sum_player += token_player
      else :
        print("Vous avez perdu la partie\n")
        token_player = 0
        token_ia = total
    elif comb_ia[2] and comb_player[2]:
      print("L'ia a une paire | Vous avez une paire")
      compare_pair(card1_ia,card2_ia,card3_ia,card1_player,card2_player,card3_player)
      if True :
        print("Vous avez gagné la partie\n")
        token_ia = 0
        token_player = total
        sum_player += token_player
      else :
        print("Vous avez perdu la partie\n")
        token_player = 0
        token_ia = total
    elif comb_ia[1] and comb_player[1]:
      print("L'ia a un brelan | Vous avez un brelan")
      compare_brelan(card1_ia,card2_ia,card3_ia,card1_player,card2_player,card3_player)
      if True :
        print("Vous avez gagné la partie\n")
        token_ia = 0
        token_player = total
        sum_player += token_player
      else :
        print("Vous avez perdu la partie\n")
        token_player = 0
        token_ia = total
    elif comb_ia[0] and comb_player[0]:
      print("L'ia a une suite | Vous avez une suite")
      compare_suite(card1_ia,card2_ia,card3_ia,card1_player,card2_player,card3_player)
      if True :
        print("Vous avez gagné la partie\n")
        token_ia = 0
        token_player = total
        sum_player += token_player
      else :
        print("Vous avez perdu la partie\n")
        token_player = 0
        token_ia = total

    print("Gain final ia :",token_ia)
    print("Votre gain final :",token_player)
    print("Votre Somme:",sum_player)

    reponse = input("Voulez vous refaire une partie ? \noui ou non : ")
    while reponse != "oui" and reponse != "non" :
      reponse = input("Voulez vous refaire une partie ? \noui ou non : ")
    if reponse == "non":
      print("--------------------------------------- A Bientot --------------------------------------- ")  
      break

r = poker()