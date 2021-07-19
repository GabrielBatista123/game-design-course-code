#import GameController as game
import numpy as np


class monster:

    island_list = ['temple']

    def __init__(self, gc):
        self.gc = gc
        self.monster_life = 60
        self.monster_alive = True
        self.monster_damage = 0  
        
    def monster_movement(self):
        if self.gc.days < 50:    
            
            return self.island_list[np.random.randint(len(self.island_list))]
            
        else:
            return 0


            #island_list = ['temple', 'spring', 'beach', 'ravine']
            #return self.gc.island_list[np.random.randint(len(self.gc.island_list))]
            #location2 = keys[np.random.randint(len(keys))]
            #position = self.gc[location2]

    
    # função para o monstro a cada dia que passa crescer mais o poder.
    def monster_growing_up(self):
        if self.gc.days < 50:
            self.monster_life = self.monster_life + 2
            # usar o days do Game controller   
        return self.monster_life
    
    def monster_die(self):
        if self.monster_life <= 0:
            print('YOU FINALLY KILLED THE MONSTER. Now you can walk in "peace" :) ')
            x = 0
            while x < 5:
                self.gc.inventory.append('coin')
                self.gc.inventory.append('Water')
                self.gc.inventory.append('Food')
                self.gc.inventory.append('armadura level 5')
                x += 1
            """y = 0
            while y < 3:
                self.gc.inventory.append('armadura')
                y += 1
            z = 0
            while z < 3:
                self.gc.inventory.append('Water')
                z += 1"""
            self.gc.inventory.append('sword')
        return self.gc.inventory


    def monster_damage_player(self):
        monster_damage = self.monster_damage + 90
        if ('armor level 2' in self.gc.inventory) and (not 'armor level 3' in self.gc.inventory ) : 
            monster_damage = self.monster_damage + 80
        elif (not 'armor level 2' in self.gc.inventory) and ('armor level 3' in self.gc.inventory ) :
            monster_damage = self.monster_damage + 60
        elif ('armor level 2' in self.gc.inventory) and ('armor level 3' in self.gc.inventory ) :
            monster_damage = self.monster_damage + 20
        return monster_damage
