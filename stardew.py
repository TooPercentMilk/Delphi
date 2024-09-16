class Person:
    def __init__(self, name, courtable: bool, gifts, workplace, birthday):
        self.name = name
        self.courtable = courtable
        self.gifts = gifts
        self.workplace = workplace
        self.birthday = birthday

class Crop:
    def __init__(self, name, base_price: int, grow_time: int, regrow_time: int, fruit: bool, 
                 production:int=1, quality:float=1, proliferate:bool=False):
        self.name = name
        self.fruit = fruit
        self.base_price = base_price
        self.grow_time = grow_time
        self.regrow_time = regrow_time
        self.proliferate = proliferate
        self.quality = quality
        self.production = production
        def raw_sell(self):
            return self.base_price * self.quality

        def preserve_sell(self):
            return self.base_price * 2 + 50

        def keg_sell(self):
            if self.fruit:
                return self.base_price * 3
            else:
                return self.base_price * 2.25
            
        def best_sell():
            best_price = 0
            best_choice = None
            if self.raw_sell() > best_price:
                best_price = self.raw_sell()
                best_choice = "Raw"
            if self.preserve_sell() > best_price:
                best_price = self.preserve_sell()
                best_choice = "Preserve"
            if self.keg_sell() > best_price:
                best_price = self.keg_sell()
                best_choice = "Keg"
            return best_price, best_choice