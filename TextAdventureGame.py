import sys
import os
import random

intro1 = '''THE UNKNOWN FUTURE
BY: CHARLES EUDY
3/28/20016'''
intro2 = '''HELLO!! GET UP... CAN YOU HEAR ME... GET UP!!'''
intro3 = '''Hi %s My name is Charles your are sleeping on my floor'''
intro4 = '''How did you get here? Well that doesn't matter. Anyway I can help you find your way around
I haven't seen clothes like that before only in magazines. what year are you from?'''
intro5 = '''WHY! %s what a very long time ago. Well welcome to the year 3072!'''
intro6 = '''Well %s in the future a lot has changed. There are zombies everywhere. I have given you some
gear to put on to help you with your journey. The gear contains your stats, like health and attack power
you can get more stats by killing zombies.'''

weaponList = {"Rusty Knife": {"Gold": 2, "Attack": 10}, "Rusty Dagger": {"Gold": 5, "Attack": 7},
              "Rusty ShortSword": {"Gold": 7, "Attack": 10}, "Rusty LongSword": {"Gold": 7, "Attack": 13},
              "Rusty GreatSword": {"Gold": 7, "Attack": 10}}


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 120
        self.health = self.maxhealth
        self.attackpower = 20
        self.level = 1
        self.maxlevel = 10
        self.experience = 0
        self.maxexperience = 100
        self.gold = 30
        self.pots = 0
        self.weap = ["Rusty Knife"]
        self.currentweap = ["Rusty Knife"]

    @property
    def attack(self):
        attack = self.attackpower
        if self.currentweap == "Rusty Knife":
            attack += 5
        if self.currentweap == "Rusty Dagger":
            attack += 7
        if self.currentweap == "Rusty ShortSword":
            attack += 10
        if self.currentweap == "Rusty LongSword":
            attack += 13
        if self.currentweap == "Rusty GreatSword":
            attack += 15
        return attack


class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 40
        self.health = self.maxhealth
        self.attackpower = 7
        self.golddrop = random.randint(1, 3)
        self.potiondrop = 0


ZombieID = Zombie("Zombie")


class Bandit:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 40
        self.health = self.maxhealth
        self.attackpower = 10
        self.golddrop = random.randint(1, 10)
        self.potiondrop = 0


BanditID = Bandit("Bandit")


class Cannibal:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 30
        self.health = self.maxhealth
        self.attackpower = 5
        self.golddrop = random.randint(1, 2)
        self.potiondrop = 0


CannibalID = Cannibal("Cannibal")


class StrayDog:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attackpower = 2
        self.golddrop = 0
        self.potiondrop = 0
        self.chanceinfection = random.randint(1, 10)


StrayDogID = StrayDog("StrayDog")


def main():
    os.system('cls')
    print(intro1)
    print('1: Start')
    print('2: Load')
    print('3: Exit')
    option = input('What would you like to do?')
    if option == "1":
        start()
    elif option == "2":
        main()
    elif option == "3":
        sys.exit()
    else:
        main()


def start():
    os.system('cls')
    print(intro2)
    print("Hello what is your name?")
    option = input('Enter Name?')
    global playerID
    playerID = Player(option)
    start1()


def start1():
    global option
    print(intro3 % playerID.name)
    print(intro4)
    year = input('Type what year')
    print(intro5 % year)
    print(intro6 % playerID.name)
    print('Name: %s' % playerID.name)
    print('Level: %i' % playerID.level)
    print('Health: %i / %i' % (playerID.health, playerID.maxhealth))
    print('AttackPower: %i' % playerID.attackpower)
    print('Gold: %i' % playerID.gold)
    print('Potions: %i' % playerID.pots)
    print('Weapon: %s ' % playerID.currentweap)
    option = input('Press Enter')
    start2()


def start2():
    global option
    print('Where would you like to go? ')
    print('1.) Explore')
    print('2.) Fight')
    print('3.) Store')
    print('4.) Save')
    print('5.) Exit')
    option = input('What would you like to do?')

    if option == '1':
        explore()
    elif option == '2':
        prefight()
    elif option == '3':
        store()
    elif option == '4':
        pass
    elif option == '5':
        sys.exit()
    else:
        start2()


def explore():
    global option
    print('1.) The City')
    print('2.) The Zoo')
    print('3.) Walk')
    print('4.) Go Back')
    option = input('Where would you like to explore?')
    if option == '1':
        theCity()
    elif option == '2':
        theZoo()
    elif option == '3':
        walk()
    elif option == '4':
        goback()
    else:
        explore()


def theCity():
    print('You find a sign that says beware Enter if you are strong enough!')
    print('1.) ENTER the city')
    print('2.) Explore somewhere else')
    option = input('What would you like to do %s' % playerID.name)
    if option == '1':
        cityEntrance()
    elif option == '2':
        explore()


def cityEntrance():
    print("Something runs at you!")
    prefight()


def theZoo():
    pass


def walk():
    pass


def goback():
    print("Did you get scared? Go see what's going on outside")
    start2()


def prefight():
    global enemy
    enemyID = random.randint(1, 4)
    if enemyID == 1:
        enemy = ZombieID
    elif enemyID == 2:
        enemy = BanditID
    elif enemyID == 3:
        enemy = CannibalID
    elif enemyID == 4:
        enemy = StrayDogID
    fight()


'''  Combat Menu Layout

                       *******************************************
                       *   %s          VS           %s           *
                       *-----------------------------------------*
                       * %s Health %i/%i        %s Health %i/%i  *
                       *                                         *
                       *******************************************  '''


def fight():
    global option
    print(" %s        VS          %s " % (playerID.name, enemy.name))
    print(" %s Health %i/%i     %s health %i/%i" % (
    playerID.name, playerID.health, playerID.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print('1.) Attack')
    print('2.) Backpack')
    print('3.) Run')
    option = input('Press Enter')
    if option == '1':
        attack()
    elif option == '2':
        backpack()
    elif option == '3':
        run()


def attack():
    global option
    pAttack = random.uniform(playerID.attackpower / 2, playerID.attackpower)
    eAttack = random.uniform(enemy.attackpower / 2, enemy.attackpower)
    if pAttack == playerID.attackpower / 2:
        print(' You Miss!')
    else:
        enemy.health -= pAttack
        print(' You deal %i damage' % pAttack)
    if enemy.health <= 0:
        win()
    if eAttack == enemy.attackpower / 2:
        print(' %s Missed!' % enemy.name)
    else:
        playerID.health -= eAttack
        print(' %s deals %i damage' % (enemy.name, eAttack))
    if playerID.health <= 0:
        dead()
    else:
        fight()


def backpack():
    print('Name: %s' % playerID.name)
    print('Level: %i' % playerID.level)
    print('Gold: %i' % playerID.gold)
    print('Weapon: %s' % playerID.currentweap)
    print('1.) Potions')
    print('2.) Weapons')
    print('3.) Clothes')
    print('4.) Go Back')
    option = input('What would you like to do?')
    if option == '1':
        potionList()
    elif option == '2':
        weapons()
    elif option == '3':
        clothes()
    elif option == '4':
        fight()
    else:
        backpack()


def weapons():
    pass


def clothes():
    pass


def potionList():
    print('You have %i potions ' % playerID.pots)
    print('1.) Goback')
    option = input('What would you like to do?')
    if option == '1':
        backpack()


def drinkPotion():
    global option
    if playerID.pots == 0:
        print("Sorry.."
              " You don't have any potions!")
    else:
        playerID.health += 50
        if playerID.health > playerID.maxhealth:
            playerID.health = playerID.maxhealth

        print(' You consumed a potion!')
        option = input('Press Enter')
        fight()


def run():
    global option
    os.system('cls')
    runNum = random.randint(1, 3)
    if runNum == 1:
        print(' You ran away safely!')
        option = input('Press Enter')
        start2()
    else:
        print(' You failed to get away!')
        option = input('Press Enter')

        eAttack = random.uniform(enemy.attackpower / 2, enemy.attackpower)
        if eAttack == enemy.attackpower / 2:
            print(' %s Missed!' % enemy.name)
        else:
            playerID.health -= eAttack
            print(' %s deals %i damage' % (enemy.name, eAttack))
            option = input('Press Enter')
        if playerID.health <= 0:
            dead()
        else:
            fight()


def win():
    global option
    playerID.gold += enemy.golddrop
    print('You have defeated %s' % enemy.name)
    print(" %s has dropped %i gold, %i gold has been added to your coin purse" % (
    enemy.name, enemy.golddrop, enemy.golddrop))
    option = input('Press Enter')
    enemy.health = enemy.maxhealth
    start2()


def dead():
    global option
    print('You have died')
    option = input('Press Enter')
    start2()


def store():
    global option
    os.system('cls')
    print(''' +++++++++++++++++++++++++
              +-------Charles's-------+
              +---------SHOP----------+
              +---LOW PRICE'S DAILY---+
              +++++++++++++++++++++++++ ''')
    print("Go Ahead check out my gear in stock")
    print("Rusty Knife")
    print("Rusty Dagger")
    print("Rusty ShortSword")
    print("Rusty LongSword")
    print("Rusty GreatSword")
    option = input("Type the item would you like to buy?")
    if option in weaponList:
        if playerID.gold >= weaponList[option]:
            playerID.gold -= weaponList[option]
            playerID.weap.append(option)
            print("You have bought %s" % option)
            start1()
        else:
            print("You don't have enough gold")
            start1()
    else:
        print("I don't have that item in my inventory.. Sorry")
        start1()


main()