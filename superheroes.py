import random


class Ability:
    def __init__(self, name, attack_strength):
        # Set Ability name
        self.name = name
        # Set attack strength
        self.attack_strength = int(attack_strength)

    def attack(self):
        # Calculate lowest attack value as an integer. "should be half of highest possible attack value"
        lowest_attack_value = self.attack_strength // 2

        # Use random.randint(a, b) to select a random attack value.
        attack_value = random.randint(
            lowest_attack_value, self.attack_strength)

        # Return attack value between 0 and the full attack.
        return attack_value

    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack_strength


class Hero:
    def __init__(self, name, health=100):
        # Initialize starting values
        self.name = name
        self.health = health
        self.abilities = list()
        self.armors = list()
        self.weapons = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        # Add ability to abilities list
        self.weapons.append(weapon)

    def add_armor(self, armor):
        # Add ability to abilities list
        self.weapons.append(armor)

    def attack(self):
        # Run attack() on every ability hero has
        total_damage = 0

        for ability in self.abilities:
            # ability.attack()
            total_damage += ability.attack()

        return total_damage

    def defend(self):
        # This method should run the defend method on each piece of armor and calculate the total defense.
        # If the hero's health is 0, the hero is out of play and should return 0 defense points.
        total_defense = 0

        if self.health == 0:
            return total_defense

        else:
            for armor in self.armors:
                total_defense += armor.defend()
                return total_defense

    def take_damage(self, damage_amt):
        # This method should subtract the damage amount from the
        # hero's health.
        # If the hero dies update number of deaths.
        self.health -= damage_amt

        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        # This method should add the number of kills to self.kills
        self.kills += 1


class Weapon(Ability):
    def attack(self):
        # return a random value between 0 and the full attack power of the weapon. Hint: The attack power is inherited.
        weapon_attack_value = random.randint(0, self.attack_strength)

        return weapon_attack_value


class Team:
    def __init__(self, team_name):
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
            print(hero)

    def attack(self, other_team):
        # This method should total our teams attack strength and
        # call the defend() method on the rival team that is passed in.
        # It should call add_kill() on each hero with the number of kills made.
        total_team_damage = 0

        for hero in self.heroes:
            total_team_damage += hero.attack()

        print(total_team_damage)
        other_team.defend(total_team_damage)

    def defend(self, damage_amt):
        # This method should calculate our team's total defense.
        # Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
        total_team_defense = 0

        for hero in self.heroes:
            total_team_defense += hero.defend()

        if damage_amt > total_team_defense:
            net_damage = damage_amt - total_team_defense
            self.deal_damage(net_damage)

    def deal_damage(self, damage):
        # Divide the total damage amongst all heroes.
        # Return the number of heros that died in attack.
        damage_per_hero = damage / len(self.heroes)
        number_of_dead_heroes = 0

        for hero in self.heroes:
            hero.health -= damage_per_hero

            if hero.health <= 0:
                number_of_dead_heroes += 1

        return number_of_dead_heroes

    def revive_heroes(self, health=100):
        # This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.health = 100

    def stats(self):
        # This method should print the ratio of kills/deaths for each member of the team to the screen.
        # This data must be output to the terminal.
        for hero in self.heroes:
            print("{}:{} is your Kill:Death ratio".format(
                self.kills, self.deaths))

    def update_kills(self):
        # This method should update each hero when there is a team kill.

        for hero in self.heroes:

            if hero.health <= 0:  # check hero isn't dead
                hero.kills += 1


class Armor:
    def __init__(self, name, defense):
        # Instantiate name and defense strength.
        self.name = name
        self.defense = defense

    def defend(self):
        # Return a random value between 0 and the
        # initialized defend strength.
        defense_value = random.randint(0, self.defense)
        return defense_value


class Arena:
    def __init__(self, good_guys_team_name, villains_team_name):
        self.good_guys_team = Team(good_guys_team_name)
        self.villains_team = Team(villains_team_name)

    def build_good_guys_team(self):
        # This method should allow a user to build team one.
        building_good_guys_team = True
        good_guys_team_size = 1

        while building_good_guys_team:

            good_guy_index = 0

            while good_guy_index < (good_guys_team_size):
                self.good_guys_team.add_hero(
                    Hero(input("Name one of your favorite heroes (you'll get to name {} total): ".format(good_guys_team_size))))
                self.good_guys_team.heroes[good_guy_index].add_ability(Ability(
                    input("What's their superpower?: "), input("How powerful is it? (0-80): ")))
                self.good_guys_team.heroes[good_guy_index].add_weapon(Weapon(
                    input("Do they have a weapon, too? If so, what is it: "), input("How powerful is it? (0-60): ")))
                self.good_guys_team.heroes[good_guy_index].add_armor(Armor(
                    input("What kind of armor do they have: "), input("How powerful is it? (0-40): ")))
                good_guy_index += 1

            else:
                building_good_guys_team = False

    def build_villains_team(self):
        # This method should allow user to build team two.
        building_villains_team = True
        villains_team_size = 1

        while building_villains_team:

            villain_index = 0

            while villain_index < (villains_team_size):
                self.villains_team.add_hero(
                    Hero(input("Name one of your favorite villains (you'll get to name {} total): ".format(villains_team_size))))
                self.villains_team.heroes[villain_index].add_ability(Ability(
                    input("What's their superpower?: "), input("How powerful is it? (0-80): ")))
                self.villains_team.heroes[villain_index].add_weapon(Weapon(
                    input("Do they have a weapon, too? If so, what is it: "), input("How powerful is it? (0-60): ")))
                self.villains_team.heroes[villain_index].add_armor(Armor(
                    input("What kind of armor do they have: "), input("How powerful is it? (0-40): ")))
                villain_index += 1

            else:
                building_villains_team = False

    def team_battle(self):
        # This method should continue to battle teams until
        # one or both teams are dead.
        battling = True
        print("Attack commencing shortly")

        while battling == True:
            print("the good guys are about to attack!")
            self.good_guys_team.attack(self.villains_team)
            print("ohh the good guys did damaage")
            print("the villains look pissed. they're going to retaliate!")
            self.villains_team.attack(self.good_guys_team)
            print("yup, that looked like it hurt. sorry, we're not sorry, good guys!")

            winning_team = ""

            good_guys_team_dead = False
            villains_team_dead = False

            good_guys_team_deaths = 0
            villains_team_deaths = 0

            for hero in self.good_guys_team.heroes:
                if hero.health <= 0:
                    good_guys_team_deaths += 1

            for hero in self.villains_team.heroes:
                if hero.health <= 0:
                    villains_team_deaths += 1

            if good_guys_team_deaths == len(self.good_guys_team.heroes):
                good_guys_team_dead = True
                winning_team = self.villains_team.name

            if villains_team_deaths == len(self.good_guys_team.heroes):
                villains_team_dead = True
                winning_team = self.good_guys_team.name

            if good_guys_team_dead == True or villains_team_dead == True:
                battling = False

        print("Team {} won!".format(winning_team))

    def show_stats(self):
        # This method should print out the battle statistics
        # including each heroes kill/death ratio.
        print("Team {} stats:".format(self.good_guys_team_name))
        print(self.good_guys_team.stats())

        print("Team {} stats:".format(self.villains_team_name))
        print(self.villains_team.stats())


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
    arena = Arena("Marvel", "DC")
    arena.build_good_guys_team()
    arena.build_villains_team()
    arena.team_battle()
