characterHP = 100
enemyHP = 100
curAtk = 10
curDef = 20
curHeal = 10

def attack(atkAmount, enemyHP):
  enemyHP -= atkAmount
  print("Attacked!")
  print(f"Enemy HP is {enemeyHP}")
def defend(defAmount, characterHP):
  characterHP += defAmount
  print("Defended!")
  print(f"Current defending point: {defAmount}")
def heal(healAmount, characterHP):
  characterHP += healAmount
  print("Healed!")
  print(f"Current HP: {characterHP})
  
while characterHP != 0 and enemyHP != 0:

  answer = input("Enter your decision: ")
  
  if answer == "attack":
    attack(curAtk, enemyHP)
  elif answer == "defend":
    defend(curDef, characterHP)
  elif answer == "heal":
    heal(curHeal, characterHP)

  print("Enemy Turn!")
  
