import random

characterHP = 100
enemyHP = 100

curAtk = 10
curDef = 20
curHeal = 10

enemyAtk = 20
enemyDef = 15
enemyHeal = 5

playerShield = 0
enemyShield = 0


def attack(atkAmount, targetHP, shield):
  damage = max(0, atkAmount - shield)
  targetHP = max(0, targetHP - damage)
  print(f"Dealt {damage} damage! Target HP: {targetHP}")
  return targetHP


def defend(defAmount):
  print(f"Defended! Blocking up to {defAmount} damage next attack.")
  return defAmount


def heal(healAmount, currentHP):
  newHP = min(100, currentHP + healAmount)
  print(f"Healed {newHP - currentHP} HP! Current HP: {newHP}")
  return newHP


while characterHP > 0 and enemyHP > 0:
  print(f"\nYour HP: {characterHP} | Enemy HP: {enemyHP}")
  answer = input("Choose attack, defend, or heal: ").strip().lower()

  if answer == "attack":
    print("You attacked!")
    enemyHP = attack(curAtk, enemyHP, enemyShield)
    enemyShield = 0
  elif answer == "defend":
    playerShield = defend(curDef)
  elif answer == "heal":
    characterHP = heal(curHeal, characterHP)
  else:
    print("Invalid answer. Try again")
    continue

  if enemyHP <= 0:
    break

  print("\nEnemy Turn!")
  enemyChoice = random.randint(1, 4)

  if enemyChoice == 1:
    print("Enemy attacked!")
    characterHP = attack(enemyAtk, characterHP, playerShield)
    playerShield = 0
  elif enemyChoice == 2:
    print("Enemy is defending.")
    enemyShield = defend(enemyDef)
  elif enemyChoice == 3:
    print("Enemy is healing.")
    enemyHP = heal(enemyHeal, enemyHP)
  else:
    print("Enemy does nothing!")

if characterHP <= 0:
  print("You Lose")
else:
  print("You Win!")
