import random


class Pokemon:
    """
    Base Pokemon class.
    """

    def __init__(self, name, pokemon_type, max_hp, attack, defense, speed, moves):
        self.name = name
        self.pokemon_type = pokemon_type
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves

    def is_fainted(self):
        return self.current_hp <= 0

    def heal(self, amount):
        self.current_hp += amount

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def take_damage(self, damage):
        self.current_hp -= damage

        if self.current_hp < 0:
            self.current_hp = 0

    def choose_random_move(self):
        return random.choice(self.moves)

    def display_stats(self):
        print(f"\n===== {self.name} =====")
        print(f"Type: {self.pokemon_type}")
        print(f"HP: {self.current_hp}/{self.max_hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print("Moves:")

        for i, move in enumerate(self.moves, start=1):
            print(f"{i}. {move}")

    def __str__(self):
        return f"{self.name} ({self.pokemon_type})"


class FirePokemon(Pokemon):
    """
    Fire-type Pokemon
    """

    def __init__(self, name, max_hp, attack, defense, speed, moves):
        super().__init__(
            name,
            "Fire",
            max_hp,
            attack,
            defense,
            speed,
            moves
        )


class WaterPokemon(Pokemon):
    """
    Water-type Pokemon
    """

    def __init__(self, name, max_hp, attack, defense, speed, moves):
        super().__init__(
            name,
            "Water",
            max_hp,
            attack,
            defense,
            speed,
            moves
        )


class GrassPokemon(Pokemon):
    """
    Grass-type Pokemon
    """

    def __init__(self, name, max_hp, attack, defense, speed, moves):
        super().__init__(
            name,
            "Grass",
            max_hp,
            attack,
            defense,
            speed,
            moves
        )