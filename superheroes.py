import random

class Ability:
    def __init__(self, name, attack_strength):
        # Set Ability name
        self.name = name
        # Set attack strength
        self.attack_strength = attack_strength

    def attack(self):

        # Calculate lowest attack value as an integer. "should be half of highest possible attack value"
        lowest_attack_value = self.attack_strength // 2

        # Use random.randint(a, b) to select a random attack value.
        attack_value = random.randint(lowest_attack_value, self.attack_strength)

        # Return attack value between 0 and the full attack.
        return attack_value

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength

class Hero:
    def __init__(self, name):
        # Initialize starting values
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        # Run attack() on every ability hero has
        total_damage = 0

        for ability in self.abilities:
            # ability.attack()
            total_damage += ability.attack()

        return total_damage

class Weapon(Ability):
    def attack(self):
        weapon_attack_value = random.randint(0, self.attack_strength)

        return weapon_attack_value
        # return a random value between 0 and the full attack power of the weapon. Hint: The attack power is inherited.

class Team:
    def init(self, team_name):
        # Instantiate resources
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        # Add Hero object to heroes list
        self.heroes.append(Hero)

    def remove_hero(self, name):
        # Remove hero from heroes list.
        # If Hero isn't found return 0.
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                return 0

    def find_hero(self, name):
        # Find and return hero from heroes list.
        # If Hero isn't found return 0.
        for hero in self.heroes:
            return hero
        else:
            return 0

    def view_all_heroes(self):
        # Print out all heroes to the console.
        for hero in self.heroes:
            print hero

if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
