import random
class Monster:
    def __init__(self, monster, initative, endurance, attack, agility, common):
        self.monster = monster
        self.initiative = initative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.common = common
        self.allstats = {'Class': f'{monster}', 'Initative': f'{initative}', 'Endurance': f'{endurance}', 'Attack': f'{attack}', 'Agility': f"{agility}", "Common": f"{common}"}

class GiantSpider(Monster):
    def __init__(self):
        super().__init__('GiantSpider', 7, 1, 2, 3, 0.20)

class Skeletton(Monster):
    def __init__(self):
        super().__init__('Skeletton', 4, 2, 3, 3, 0.15)

class Orc(Monster):
    def __init__(self):
        super().__init__('Orc', 6, 3, 4, 4, 0.10)

class Troll(Monster):
    def __init__(self):
        super().__init__('Troll', 2, 4, 7, 2, 0.05)


shuffle_spider =[str(GiantSpider), "No monster"]
shuffle_skeletton = [str(Skeletton), "No Monster"]
shuffle_orc = [str(Orc), "No Monster"]
shuffle_troll = [str(Troll), "No monster"]


def random_monsters():
    random_spider = random.choices(shuffle_spider, weights=[20, 80], k=1)
    random_skeletton = random.choices(shuffle_skeletton, weights=[15, 85], k=1)
    random_orc = random.choices(shuffle_orc, weights=[10, 90], k=1)
    random_troll = random.choices(shuffle_troll, weights=[0.05, 95], k=1)
    print(random_spider + random_skeletton + random_orc + random_troll)


class Treasures:
    def __init__(self, treasure, value):
        self.treasure = treasure
        self.value = value


coins = Treasures("Coins", 2)
money_pouch = Treasures("Money pouch", 6)
gold_jewelry = Treasures("Gold Jewelry", 10)
gems = Treasures("Gems", 14)
small_treasure_chest = Treasures("Small treasure chest", 20)


shuffle_coins = [str(coins.treasure), "No Treasure"]
shuffle_money_pouch = [str(money_pouch.treasure), "No Treasure"]
shuffle_gold_jewelry = [str(gold_jewelry.treasure), "No Treasure"]
shuffle_gems = [str(gems.treasure), "No Treasure" ]
shuffle_small_treasure_chest = [str(small_treasure_chest.treasure), "No Treasure"]


def random_treasurs():

        random_coins = random.choices(shuffle_coins, weights=[40, 60], k=1)
        random_money_pouch = random.choices(shuffle_money_pouch, weights=[20, 80], k=1)
        random_gold_jewelry = random.choices(shuffle_gold_jewelry, weights=[15, 85], k=1)
        random_gems = random.choices(shuffle_gems, weights=[10, 90], k=1)
        random_treasure_chest = random.choices(shuffle_small_treasure_chest, weights=[5, 95], k=1)
        print(random_coins + random_money_pouch + random_gold_jewelry + random_gems + random_treasure_chest)


random_monsters()
random_treasurs()