#import _src.desertedIsland
#from app import play
import os
from islandTiles.beach import tile as beach
from islandTiles.temple import tile as temple
from islandTiles.camp import tile as camp
from islandTiles.ravine import tile as ravine
from islandTiles.spring import tile as spring
from islandTiles.monster import monster
import numpy as np
import os
#from IPython.display import clear_output

#alive = True
#days = 0
#inventory = []

class GameController:

    island_map = {"temple": temple, 
                "spring": spring, 
                "beach": beach, 
                "ravine": ravine, 
                "camp": camp}

    def __init__(self):
        self.alive = True
        self.days = 0
        self.inventory = [] 
        self.life = 100
        self.food_life = 0
        self.drink = 0
        self.no_answer = 0

#I've used a dictionary here to access the classes above by their names. This is called a map, and common in coding.
    
    def play(self):
        while(self.alive):
            if self.days == 0:
                print("You have washed up on a Deserted Island! You must search the island for Food and Water to survive until rescue...")
            print("Days on the deserted island: "+str(self.days))
            #print('Your life percentage: '+str(self.life))
            #print('Your hungry percentage: '+str(self.food_life))
            #print('Your thirst percentage: '+str(self.drink))

            # An function for player life

            def player_life(self):                
                if self.life < 100:
                    recup = input('Oh no, you are injured !! would you like cure yourself? (Y/N)')
                    if recup == 'Y':
                        if 'fabric' in self.inventory:
                            dife = 100 - self.life
                            self.life = self.life + dife
                            print("Oh, amazing. Now you can survive more time in the Island")
    
                        else:
                            print('You do not have items to cure yourself yet. Continue searching')
                            
                    elif recup == 'N':
                        print('Take carefull !! You are injured')
                        
                    else:
                        print('I did not understand')
                return self.life

            # An function for Food system

            def food_system(self):
                # my_monster = monster(self)
                # my_monster.monster_movement()
                print('Life percentage: '+str(self.life))

                print('Hungry percentage: '+str(self.food_life)) 
                print('thirst percentage: '+str(self.drink))

                #print('Your level of hungry and thirst is growing up !! You need to find water and food quickly')

                if self.days > 0:
                    self.food_life = self.food_life + 5  
                    if (self.food_life > 60 and self.food_life < 100):
                        food_ask = input('You need to eat ! do it now? (Y/N)')
                        if food_ask == 'Y':
                            #quantity = input('how much times do you prefer? ')
                            food_count = self.inventory.count('Food')
                            
                            if 'Food' in self.inventory:
                                self.food_life = self.food_life - food_count*10
                                print('Awesome !! now you can survive for more time in the Island.\nYour current hungry status: '+str(self.food_life))
                                while 'Food' in self.inventory:
                                    self.inventory.remove('Food')
                                    

                            else:
                                print(" You don't have Food in your loots, continue searching")
                                
                        elif food_ask == 'N':
                            print('Ok. Just take carefull')
                            
                        else:
                            print('I did not understand')
                
                return self.food_life
            
            # A function for Water system

            def water_system(self):
                #print('thirst percentage: '+str(self.drink)) 

                #print('Your level of hungry and thirst is growing up !! You need to find water and food quickly')

                if self.days > 0:
                    self.drink = self.drink + 5  
                    if (self.drink > 60 and self.drink < 100):
                        water_ask = input('You need to drink ! do it now? (Y/N)')
                        if water_ask == 'Y':
                            #quantity1 = input('how much times do you prefer? ')
                            water_count = self.inventory.count('Water')
                            
                            if 'Water' in self.inventory:
                                self.drink = self.drink - water_count*10
                                print('Awesome !! now you can survive for more time in the Island.\nYour current thirst status: '+str(self.drink))
                                while 'Water' in self.inventory:
                                    self.inventory.remove('Water')

                            else:
                                print(" You don't have Water in your loots, continue searching")
                        elif water_ask == 'N':
                            print('Ok. Just take carefull')
                        else:
                            print('I did not understand')
                
                return self.drink
            
            self.food_life = food_system(self)
            self.drink = water_system(self)
            self.life = player_life(self)
            #print('Hungry percentage: '+str(self.food_life))
            # my_monster.monster_movement()

            #if self.no_answer == 2:
                

            if self.life <= 0:
                print('Game over !! Your history in this Island arrived in the end')
                self.alive = False

            if self.food_life >= 100:
                print('Game over !! Your hungry killed you')
                self.alive = False
            if self.drink >= 100:
                print('Game over !! Your thirst killed you')  
                self.alive = False

            if self.days == 40:
                print('Congratulations !! You survived the desert island ')
                break
            
            def ask_for_location():
        
                location = input("Where would you like to search today? (temple, spring, beach, ravine, camp): ")
                while not location in self.island_map:
                    print('invalid, try again !')
                    location = input("Where would you like to search today? (temple, spring, beach, ravine, camp): ")

                return location

            Water_Food = ['Water', 'Food']
            location = ask_for_location()
            tile = self.island_map[location]

            my_monster = monster(self)
            self.position = my_monster.monster_movement()

            #self.bla = my_monster.monster_growing_up()
            #self.vida = my_monster.monster_die() 
            
            #Our code to search the Island goes here
            #tile = self.island_map[input("Where would you like to search today? (temple, spring, beach, ravine, camp): ")]
            tile.enterTile()
            loot, encounter = tile.search()

            if self.position == location:

                print("Oh no, The monster and you are in the same place.")
                #if monster_finding == 'Y' or monster_finding == 'y':
                self.damage = my_monster.monster_damage_player()

                    #if 'knife' in self.inventory:


                if self.damage < 100:
                    print('You suffered a damage of: '+str(self.damage)+'. Take carefful and heal yourself !')
                    self.life = self.life - self.damage
                else:
                    print('Game over ! The monster killed you.')
                    break
                #elif monster_finding == 'N' or monster_finding =='n':
                    #print('Just remembering: You just can say NO 2 times')
                    #self.no_answer += 1
                #else:
                    #self.no_answer += 1

            if encounter == "Crocodile":
                #self.alive = False
                #print("You are eaten by a Crocodile")
                fight = input('You found a crocodile, would you like fight to have food ?(Y/N)\nYou need to know that if you would like to kill the crocodile without die, you need to have at least an knife:  ')
                #print("You need to know that if you would like to kill the crocodile without die, you need to have at least an knife")
                if fight == 'Y':
                    if not 'knife' in self.inventory:
                        self.life = self.life - 20 
                        print('you were brutally injured !! The crocodile took '+str(100 - self.life)+' of damage')
                        
                        
                        
                    else:
                        print('You killed the crocodile and now have more food')
                        x = 0
                        while x < 2:
                            self.inventory.append('Food')
                            x += 1
                        
                if fight == 'N':
                    print('Well done. You need to guarantee your life')
    
            
            elif encounter == "Big monkey":
                alert = input("You're so near of an Big monkey. Are you sure that you want continue to search here? (Y/N)")
                if alert == 'Y':
                    fight_monkey = input('Oh no, the Big monkey found you. run or fight ? ')
                    if fight_monkey == 'run':
                        continue
                    elif fight_monkey == 'fight':
                        if 'spear' in self.inventory:
                            print('Congratulations !! You killed the Big monkey and now have a lot of Food')
                            xx = 0
                            while xx < 3:
                                self.inventory.append("Food")
                                xx += 1
                        else:
                            self.life = self.life - 20
                            print('you were brutally injured !! The Big monkey took '+str(100 - self.life)+'of damage')
                    else:
                        print('Ops! Try again !')

            
            elif encounter == "ancestral soldier":
                alert = input("You're so near of an ancestral soldier. Are you sure that you want continue to search here? (Y/N)")
                if alert == 'Y':
                    fight_monkey = input('Oh no, the ancestral soldier found you. run or fight ? ')
                    if fight_monkey == 'run':
                        continue
                    elif fight_monkey == 'fight':
                        if 'spear' in self.inventory:
                            print('Congratulations !! You killed the ancestral soldier and now you have armor level 3')
                        
                            self.inventory.append("armor level 3 ")
                                
                        elif ('knife' in self.inventory) and (not 'spear' in self.inventory):
                            self.life = self.life - 10
                            print("You killed the ancestral soldier but you suffered a damage of "+str(100 - self.life)+'. But now, you have armor level 3')
                            self.inventory.append("armor level 3 ")

                        else:
                            self.life = self.life - 20
                            print('you were brutally injured !! The ancestral soldier took '+str(100 - self.life)+'of damage')
                    else:
                        print('Ops! Try again !')


            elif encounter == "the guardian":
                alert = input("You're so near of an guardian. Are you sure that you want continue to search here? (Y/N)")
                if alert == 'Y':
                    fight_monkey = input('Oh no, the guardian found you. run or fight ? ')
                    if fight_monkey == 'run':
                        continue
                    elif fight_monkey == 'fight':
                        if ('spear' in self.inventory):
                            print('Congratulations !! You killed the guardian and now have a armor level 2')
                            
                            
                            self.inventory.append("armor level 2")
                                
                        elif ('knife' in self.inventory) and (not 'spear' in self.inventory):
                            self.life = self.life - 10
                            print("You killed the guardian but you suffered a damage of "+str(100 -self.life))
                            self.inventory.append("armor level 2")
                        else:
                            self.life = self.life - 20
                            print('you were brutally injured !! The guardian took '+str(100 -self.life)+' of damage')
                    else:
                        print('Ops! Try again !')


            elif encounter == "Crumbling Cliffs":
                self.alive = False
                print("The cliffs below you crumble and you fall to your death")
                break

            
            if encounter == None:
                #print("Your search yields nothing...")
                old = Water_Food[np.random.randint(len(Water_Food))]
                print('You have find: '+old)
                self.inventory.append(old)
            else:
                if loot != None:
                    print("You encounter "+str(encounter)+" and find "+str(loot))
                    self.inventory.append(loot)
                else:
                    print("You encounter "+str(encounter)+" but find nothing...")
                
            tile.leaveTile()
                
            #This is the start of our player input section. We'll modify this code to make the gameplay fun.
            decision = input("Keep searching the Deserted Island? (Y/N) ")

            if decision == 'quit':
                break
            elif decision == 'Y':
                print("Good choice, maybe you'll survive another day.")
                os.system("cls")
            elif decision == 'N':
                print("Too bad! You're stuck here... Gotta keep searching.")
                break
            else:
                print("I didn't understand. Maybe you've been stuck on this Island for too long...")
            self.days += 1
        else:
            print("Game over. You survived for "+str(self.days)+" days.")