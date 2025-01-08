#Fighter Classes/Attributes
#Code Written by Matthew Rivers

#creates the class for boxers
class Boxer:
    def __init__(self, n, h, p, d):
        self._name = n
        self._health = h
        self._power = p
        self._defense = d
        #whether or not the fighter has been knocked out (dead) or not (alive)
        self._knockedOut = False
        #creates placeholder for boxers inventory
        self._inventory = []
    #getters/setters
    def _get_name(self):
        return self._name
    def _get_health(self):
        return self._health
    def _get_power(self):
        return self._power
    def _get_defense(self):
        return self._defense
    def _get_knockedOut(self):
        return self._knockedOut
    def _get_inventory(self):
        return self._inventory
    def _set_name(self, n):
        self._name = n
    def _set_health(self, h):
        self._health = h
    def _set_power(self, p):
        self._power = p
    def _set_defense(self, d):
        self._defense = d
    def _set_knockedOut(self, d):
        self._knockedOut = d
    def _set_inventory(self, newInventory):
        self._inventory = newInventory

    #properties
    name = property(_get_name, _set_name)
    health = property(_get_health, _set_health)
    power = property(_get_power, _set_power)
    defense = property(_get_defense, _set_defense)
    knockedOut = property(_get_knockedOut, _set_knockedOut)
    inventory = property(_get_inventory, _set_inventory)

    #function for fighters to take damage, and if their health is 0 they lose
    def takeDamage(self, damage):
        self.health = max(0, self.health - damage)
        if self.health == 0:
            self.defeat()

    #adds items to inventory
    def addToInventory(self, item):
        self._inventory.append(item)
        print(f"{item} has been added to your inventory.")

    #shows what is in boxers inventory
    def showInventory(self):
        if self._inventory:
            print("Your inventory contains:")
            for item in self._inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

    #if a fighter loses/is defeated, the boolean of knocked out (dead) switches from false to true
    def defeat(self):
        self._knockedOut = True

    #shows new desctiption of a knocked out boxer
    def newDescription(self):
        if self._knockedOut:
            return f"{self.name} is knocked out."
        return f"{self.name}"