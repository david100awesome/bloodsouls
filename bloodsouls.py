minimum_age = 10
x = ("vsvnsnvosobsnbo")
print(x)
name = input("what is your name?")
print("your name is" , name , )

choice = input("do you like blood? (y or n)") 
if choice == "y" or choice == "Y":
    print("you can play!here is the pass code 1551")
else:
    print("get out!")
print("This is your first fight")
minimum_number = 1550
maximum_number = 1552
x = ("sound volume")
number = 0
print(x)
while number != 1551:
    number = int(input("what is the passcode?"))
    if number != 1551:
        print ("wrong number")
        continue
    else:
        break
        

while True:
    weapon = ("fist")
    health = 100
    fist = 1
    Enemy_health = 100
    damage =  weapon
    wooden_sword = 10
    stone_sword = 20
    print("you are in TN!")
    
    choice = input("You find a wooden sword. pick it up? (y or n)")
    if choice == "y" or choice == "Y":
        weapon = wooden_sword
        print("You picked it up!")
    print("Someone hits you")
    health -= 10
    print("You took 10 damage")
    print("Health:", health)
    print("you hit him")
    Enemy_health -= 10
    print("enemy retreated") 
     
    choice = input("you find a health potion drink it? (y or n)")
    if choice == "y" or choice == "Y":
        health += 10
    print("the enemy came back!")
    
    choice = input("would you like to attack? (y or n)")
    if choice == "y" or choice == "Y":
        Enemy_health -= 10
        print ("the enemy fell in a hole and died!hooray!")
        Enemy_health -= 80
    else:
        print("the enemy hit you and you fell in a hole and died! NO!")
        health -=  90
        continue
        
    choice = input("you find a house. go in?(y or n)")
    if choice == "y" or choice == "Y":
        print("you are in the house")
    else:
        print("you are not in the house")
        
    choice = input("you find a chest.open it?(y or n)")        
    if choice == "y" or choice == "Y":
            weapon = stone_sword
            print("you now have a stone_sword")
            break
       
