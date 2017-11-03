import random
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

number = 0
print(x)
while number != '1551':
    number = (input("what is the passcode?"))
    if number != '1551':
        print ("wrong passcode")
        continue
    else:
        break
 
print("you are in TN")
print("you are a knight with a iron_sword")
while True:
    
    weapon = ("iron_sword")
    health = 100
    fist = 1
    Enemy_health = 100
    wolf_health = 20
    damage =  weapon
    choice = input("you find a enemy attack?you have to say yes sorry(y)")
    if choice =="y" or choice =="Y":
        while Enemy_health > 0 and health > 0:
            p_damage = random.randint(1,  20)
            e_damage = random.randint(1,  15)
            
            # player attacks
            if p_damage < 5:
                print("you missed")
            else:
                print("you hit him!" , p_damage)
                Enemy_health -= p_damage 
            print("enemy health" , Enemy_health)
            if Enemy_health < 1:
                continue
            
            # enemy attacks
            if e_damage < 5:
                print("the enemy missed")
            else:
                print("the enemy hit you",  e_damage) 
                health -= e_damage 
            print("your health" , health , )
    else:
        print("I told you you can't do that!")
        continue
    print("you kiled the enemy!")
    choice = input("you find a health potion drink it? (y or n)")
    if choice == "y" or choice == "Y":
        health = 100
    
    
    
        
    
    
        
    
        
    choice = input("you find a house. go in?(y or n)")
    if choice == "y" or choice == "Y":
            print("you are in the house")
            print("ther is nothing in the house you leave the house.")
    else:  
            print("you are not in the house")
            
            print("you got shot by a enemy NO!")
            continue
        
        
    choice = input("you find a wolf.attack?(y or n)")
    if choice == "y"or choice == "Y":
            print("you hit the wolf in the head and it died!")
            print("you win! or did you?")
            break
    else:
            print("the wolf hit it's head on accident")
            print("you win! or did you?")
            break
