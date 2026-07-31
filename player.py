class Player:
    """
    Represents a player in the Pokemon Battle Simulator.
    A player has a name, one Pokemon, and a limited number of potions.
    """

    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon
        self.potions = 3

    def use_potion(self):
        """
        Heal the player's Pokemon by 20 HP.
        """

        if self.potions <= 0:
            print("No potions left!")
            return False

        if self.pokemon.current_hp == self.pokemon.max_hp:
            print(f"{self.pokemon.name} already has full HP!")
            return False

        self.potions -= 1
        self.pokemon.heal(20)

        print(f"\n{self.name} used a Potion!")
        print(f"{self.pokemon.name} recovered 20 HP.")
        print(f"Potions remaining: {self.potions}")

        return True

    def show_status(self):
        """
        Display the player's current Pokemon status.
        """

        print("\n---------------------------")
        print(f"Trainer: {self.name}")
        print(f"Pokemon: {self.pokemon.name}")
        print(f"HP: {self.pokemon.current_hp}/{self.pokemon.max_hp}")
        print(f"Potions: {self.potions}")
        print("---------------------------")