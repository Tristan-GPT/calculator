def calcul():
  
  try:
    calc=input("Quel est le calcul à effectuer ? ")
    result = eval(calc)
    print(str(result))
  except:
    print("Une erreur est survenue.")
    exit()
  
def parite():
  
  try:
    x=int(input("Quel est le nombre à tester ? "))
    if x % 2 == 0:
      print("Ce nombre est pair.")
    elif x % 2 == 1:
      print("Ce nombre est impair.")
  except: 
    print("Une erreur est survenue.")
    exit()
    
def verif():
  
  calc=input("Quel est l'affirmation mathématique à tester ? ")
  result=eval(calc)
  if result == True:
    print("Cette affirmation est juste.")
  elif result == False:
    print("Cette affirmation est fausse.")
    
def choice():

  try:
    print("Calculer une équation: 1\n\nVérifier si un nombre est pair ou impair: 2\n\nVérifier une affirmation mathématique: 3\n\nQuitter: exit")
    choice= int(input("Quel est la fonction à choisir ?"))
  
    if choice == 1:
      calcul()
      
    elif choice == 2:
      parite()
      
    elif choice == 3:
      verif()
    elif choice == "exit":
      exit()
  except Exception:
    print("Une erreur est survenue.")
 
choice() 
