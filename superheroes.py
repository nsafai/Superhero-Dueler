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
        self.deaths = 0
        self.kills = 0

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

        return total_team_damage

    def defend(self, damage_amt):
        # This method should calculate our team's total defense.
        # Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.
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
    def __init__(self, team_one_name, team_two_name):
        self.team_one = Team(team_one_name)
        self.team_two = Team(team_two_name)

    def build_team_one(self):
        # This method should allow a user to build team one.
        building_team = True

        while building_team:
            print(len(self.team_one.heroes))
            team_one_instructions = "What heroes are part of team ONE? (When you're done, type 'done'):"

            # if list is not empty and last item of list is not "done"
            if (len(self.team_one.heroes) == 0):
                self.team_one.heroes.append(input(team_one_instructions))

            elif (len(self.team_one.heroes) != 0) and (self.team_one.heroes[-1] != "done"):
                self.team_one.heroes.append(input(team_one_instructions))

            # if user is done with input and has typed "done" as the last item of list
            elif (len(self.team_one.heroes) != 0) and self.team_one.heroes[-1] == "done":
                self.team_one.heroes.pop()
                break

            else:
                print("error building team_one")


    def build_team_two(self):
        # This method should allow user to build team two.
        building_team = True

        while building_team:
            team_two_instructions = "What heroes are part of team TWO? (When you're done, type 'done':)"

            # if list is not empty and last item of list is not "done"
            if (len(self.team_two.heroes) == 0):
                self.team_two.heroes.append(input(team_two_instructions))

            # if user has started input but not specified that they are "done", keep asking for input
            elif (len(self.team_two.heroes) != 0) and (self.team_two.heroes[-1] != "done"):
                self.team_two.heroes.append(input(team_two_instructions))

            # if user is done with input and has typed "done" as the last item of list
            elif (len(self.team_two.heroes) != 0) and self.team_two.heroes[-1] == "done":
                self.team_two.heroes.pop()
                break

            else:
                print("error building team_two")


    def team_battle(self):
        # This method should continue to battle teams until
        # one or both teams are dead.
        battling = True

        while battling == True:
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)

            winning_team = ""

            team_one_dead = False
            team_two_dead = False

            team_one_deaths = 0
            team_two_deaths = 0

            for hero in team_one.heroes:
                if hero.health <= 0:
                    team_one_deaths += 1

            for hero in team_two.heroes:
                if hero.health <= 0:
                    team_two_deaths += 1

            if team_one_deaths == len(self.team_one.heroes):
                team_one_dead = True
                winning_team = self.team_two.name

            if team_two_deaths == len(self.team_one.heroes):
                team_two_dead = True
                winning_team = self.team_one.name

            if team_one_dead == True or team_two_dead == True:
                battling = False

        print("Team {} won!".format(winning_team))

    def show_stats(self):
        # This method should print out the battle statistics
        # including each heroes kill/death ratio.
        print("Team {} stats:".format(self.team_one_name))
        print(self.team_one.stats())

        print("Team {} stats:".format(self.team_two_name))
        print(self.team_two.stats())


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
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
