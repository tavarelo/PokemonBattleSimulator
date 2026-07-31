from move import Move
from pokemon import FirePokemon, WaterPokemon, GrassPokemon

# -----------------------------
# MOVE FACTORY
# -----------------------------

def create_moves():
    return {
        "Ember": Move("Ember", "Fire", 40, 100),
        "Flamethrower": Move("Flamethrower", "Fire", 90, 100),
        "Fire Fang": Move("Fire Fang", "Fire", 65, 95),
        "Fire Blast": Move("Fire Blast", "Fire", 110, 85),

        "Water Gun": Move("Water Gun", "Water", 40, 100),
        "Bubble": Move("Bubble", "Water", 40, 100),
        "Aqua Tail": Move("Aqua Tail", "Water", 90, 90),
        "Hydro Pump": Move("Hydro Pump", "Water", 110, 80),

        "Vine Whip": Move("Vine Whip", "Grass", 45, 100),
        "Razor Leaf": Move("Razor Leaf", "Grass", 55, 95),
        "Seed Bomb": Move("Seed Bomb", "Grass", 80, 100),
        "Solar Beam": Move("Solar Beam", "Grass", 120, 75),

        "Scratch": Move("Scratch", "Normal", 40, 100),
        "Tackle": Move("Tackle", "Normal", 40, 100),
        "Quick Attack": Move("Quick Attack", "Normal", 40, 100),
        "Slam": Move("Slam", "Normal", 80, 75),
        "Bite": Move("Bite", "Normal", 60, 100),
    }


def create_pokemon():
    moves = create_moves()

    return [

        FirePokemon(
            "Charmander",
            39,
            52,
            43,
            65,
            [
                moves["Scratch"],
                moves["Ember"],
                moves["Fire Fang"],
                moves["Flamethrower"]
            ]
        ),

        FirePokemon(
            "Vulpix",
            38,
            41,
            40,
            65,
            [
                moves["Ember"],
                moves["Quick Attack"],
                moves["Fire Fang"],
                moves["Fire Blast"]
            ]
        ),

        FirePokemon(
            "Growlithe",
            55,
            70,
            45,
            60,
            [
                moves["Bite"],
                moves["Ember"],
                moves["Flamethrower"],
                moves["Fire Blast"]
            ]
        ),

        WaterPokemon(
            "Squirtle",
            44,
            48,
            65,
            43,
            [
                moves["Tackle"],
                moves["Water Gun"],
                moves["Bubble"],
                moves["Aqua Tail"]
            ]
        ),

        WaterPokemon(
            "Psyduck",
            50,
            52,
            48,
            55,
            [
                moves["Scratch"],
                moves["Water Gun"],
                moves["Bubble"],
                moves["Hydro Pump"]
            ]
        ),

        WaterPokemon(
            "Poliwag",
            40,
            50,
            40,
            90,
            [
                moves["Bubble"],
                moves["Water Gun"],
                moves["Quick Attack"],
                moves["Hydro Pump"]
            ]
        ),

        GrassPokemon(
            "Bulbasaur",
            45,
            49,
            49,
            45,
            [
                moves["Tackle"],
                moves["Vine Whip"],
                moves["Razor Leaf"],
                moves["Seed Bomb"]
            ]
        ),

        GrassPokemon(
            "Oddish",
            45,
            50,
            55,
            30,
            [
                moves["Vine Whip"],
                moves["Razor Leaf"],
                moves["Seed Bomb"],
                moves["Solar Beam"]
            ]
        ),

        GrassPokemon(
            "Bellsprout",
            50,
            75,
            35,
            40,
            [
                moves["Vine Whip"],
                moves["Razor Leaf"],
                moves["Slam"],
                moves["Solar Beam"]
            ]
        )
    ]