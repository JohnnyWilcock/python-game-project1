# Setting classes for characters and enemys

class Fighter:
  def __init__(self, name, level=1,):
    self.name = name
    self.level = level
    self.experience = 0
    self.health = level * 10
    self.max_health = level * 10
    self.stamina = level * 5
    self.gold = 20
    self.knocked_out = False
  def __repr__(self):
    return "{name} is a level {level} fighter. {name} has {health} hit points and {stamina} stamina points.".format(name = self.name, level = self.level, health = self.health, stamina = self.stamina)
  
  def lose_health(self, amount):
    self.health -= amount
    if self.health < 0:
      self.health = 0
      self.knock_out()

  def knock_out(self):
    self.knocked_out = True
    print("You have been knocked out!")

  
  def lose_stamina(self, amount):
    self.stamina -= amount

  def gain_stamina(self, amount):
    self.stamina += amount

  def gain_health(self, amount):
    self.health += amount
    if self.health >= self.max_health:
        self.health = self.max_health 

  def gain_level(self):
    if self.experience >= self.level * 10:
      self.level += 1
      print("Level Up! You are now level {level}!".format(level = self.level))
    
  def attack(self, opponent):
     print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = opponent.name, damage = self.level *2))
     opponent.lose_health(self.level * 2)
  
  def special_attack(self, opponent):
    print("{my_name} performed a mighty sword attack on {other_name}! For {damage} damage.".format(my_name = self.name, other_name = opponent.name, damage = self.level * 4 ))
    opponent.lose_health(self.level * 4)
    self.lose_stamina(round(self.level))


class Wizard:
  def __init__(self, name, level=1):
    self.name = name
    self.level = level
    self.experience = 0
    self.health = level * 5
    self.max_health = level * 5
    self.mana = level * 10
    self.max_mana = level * 10
    self.gold = 20
    self.knocked_out = False
  def __repr__(self):
    return "{name} is a level {level} wizard. {name} has {health} hit points and {mana} mana points.".format(name = self.name, level = self.level, health = self.health, mana = self.mana)

  def lose_health(self, amount):
    self.health -= amount
    if self.health < 0:
      self.health = 0
      self.knock_out()

  def knock_out(self):
    self.knocked_out = True
    print("You have been knocked out!")

  def gain_health(self, amount):
    self.health += amount
    if self.health >= self.max_health:
      self.health = self.max_health

  def lose_mana(self, amount):
    self.mana -= amount

  def gain_mana(self, amount):
    self.mana += amount

  def gain_experience(self, amount):
    self.experience += amount
    self.gain_level()

  def gain_level(self):
    if self.experience >= self.level * 10:
      self.level += 1
      self.health = self.max_health
      self.mana = self.max_mana
      print("Level Up! You are now level {level}!".format(level = self.level))

  def attack(self, opponent):
    print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = opponent.name, damage = self.level))
    opponent.lose_health(self.level)

  def cast_lightning(self, opponent):
    if self.mana > self.level:
      print("{my_name} cast lightning on {other_name} for {damage} damage.".format(my_name = self.name, other_name = opponent.name, damage = self.level * 2))
      opponent.lose_health(self.level * 2)
      self.lose_mana(self.level)
    else:
      print("You don't have enough mana")

  def cast_healing(self):
    self.gain_health(self.level * 2)
    self.lose_mana(self.level * 2)
    print("{my_name} cast healing on themself. It cures {hit_points} of health.".format(my_name = self.name, hit_points = self.level * 2))


class Enemy:
  def __init__(self, name, type, level=1, armour='',):
    self.name = name
    self.type = type
    self.level = level
    self.armour_type = armour
    self.health = level * 5
    self.max_health = level * 5
    self.gold = 20
    self.knocked_out = False
  def __repr__(self):
    return "A level {level} {type} wearing {armour} armour.".format(level = self.level, type = self.type, armour = self.armour_type)
  
  def attack(self, opponent):
    print("{my_name} attacked {other_name} for {damage} damage.".format(my_name = self.name, other_name = opponent.name, damage = self.level))
    opponent.lose_health(self.level)

  def lose_health(self, amount):
    self.health -= amount
    if self.health < 0:
      self.health = 0
      self.knock_out()

  def knock_out(self):
    self.knocked_out = True
    print("The {enemy} has been knocked out!".format(enemy = self.type))
  
# Functions
    




# fighter_one = Fighter("Juan", 5)
# fighter_two = Fighter("Bob", 4)
wizard_one = Wizard("Eugene", 1)
print(wizard_one)
# print(fighter_one)
# print(fighter_two)
# print(wizard_one)
# fighter_one.attack(fighter_two)
# print(fighter_one)
# print(fighter_two)
# wizard_one.cast_lightning(fighter_one)
# print(fighter_one)
# fighter_one.special_attack(wizard_one)
# print(fighter_one)
# print(wizard_one)
# wizard_one.cast_healing()
# print(wizard_one)
enemy_one = Enemy("skeleton", "skeleton", 3, "leather")
print(enemy_one)
# Getting player input for character creation

# player_name = input("What is your characters name? ")
# player_class = input("What class of character would you like to play? A Fighter or Wizard? ")

# if player_class == Fighter:
#   player_character = Fighter(player_name, 1)
# elif player_class == Wizard:
#   player_character = Wizard(player_name, 1)


# # player_character = player_character_creation(player_name, player_class)

# print(player_name)
# print(player_class)
# player_character = Fighter(player_name)
# print(player_character)
