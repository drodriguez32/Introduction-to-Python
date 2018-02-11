import random as rm

class Pound: 
    
    # Define a constructor method
    def __init__(self, rare=False): # has as a parameter the particular instance (object) that was created
        
        # States to define coins
        self.value = 1.00
        self.color = "gold"
        self.num_edges = 1
        self.diam = 22.5 #mm
        self.thick = 3.15 #mm
        self.heads = True
        
        self.rare = rare
        
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
            
    
    def rust(self): # parameter has to be the same as in the constructor or it won't work
        self.color = "greenish"
        
    def clean(self):
        self.color = "gold"
        
    def flip(self):
        heads_options = [True,False]
        choice = rm.choice(heads_options)
        self.heads = choice
        
    def __del__(self): # when a coin is spent, it is destroyed with this destructor method
        print("Coin spent!")