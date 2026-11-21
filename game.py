import random

characterHP = 100
enemyHP = 100
curAtk = 10
curDef = 20
curHeal = 10
enemyAtk = 20
enemyDef = 15
enemyHeal = 5
prevDef = 0
prevEnemyDef = 0

history = []

def attack(atkAmount, enemyHP):
  enemyHP -= atkAmount
  print("Attacked!")
  print(f"Enemy HP is {enemeyHP}")
def defend(defAmount, characterHP):
  characterHP += defAmount
  print("Defended!")
  print(f"Current defending point: {defAmount}")
  prevDef = curDef
def heal(healAmount, characterHP):
  characterHP += healAmount
  print("Healed!")
  print(f"Current HP: {characterHP})

while True:
  if characterHP != 0 and enemyHP != 0:
  
    answer = input("Enter your decision: ")
    
    if answer == "attack":
      attack(curAtk, enemyHP)
    elif answer == "defend":
      defend(curDef, characterHP)
    elif answer == "heal":
      heal(curHeal, characterHP)
    else:
      ("Invalid answer. Try again")
  
    print("Enemy Turn!")
  
    if enemyHP - prevEnemyDef >= 1:
      enemyHP = enemyHP - prevEnemyDef
    else:
      enemyHP = 1
  
    enemyChoice = random.randint(1, 4)
    if enemyChoice == 1:
      print("Enemy attacked!")
      print(f"Enemy dealt {enemyAtk} damage - {characterHP - enemyAtk}HP remaining")
      characterHP -= enemyAtk
    elif enemyChoice == 2:
      print("Enemy defended!")
      enemyHP += enemyDef
      prevEnemyDef = enemyDef
    elif enemyChoice == 3:
      print("Enemy healed!")
      enemyHP += enemyHeal
    elif enemyChoice == 4:
      print("Enemy doesn't know what to do! Your turn comes!")
  
    if characterHP - prevDef >= 1:
      characterHP -= prevDef
    else:
      characterHP = 1
  
  elif characterHP <= 0:
    print("You Lose")
    break
  elif enemyHP <= 0:
    print("You Win!")
    break
    
