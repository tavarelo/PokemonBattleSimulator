import random

from pokemon_data import create_pokemon
from player import Player
from battle import Battle


def choose_pokemon(pokemon_list):

    print("\n===================================")
    print("     Pokemon Battle Simulator")
    print("===================================")

    print("\nChoose your Pokemon:\n")

    for i, pokemon in enumerate(pokemon_list, start=1):
        print(
            f"{i}. {pokemon.name}"
            f" ({pokemon.pokemon_type})"
        )

    while True:

        try:

            choice = int(input("\nEnter a number: "))

            if 1 <= choice <= len(pokemon_list):
                return pokemon_list.pop(choice - 1)

            print("Please choose a valid number.")

        except ValueError:

            print("Please enter a number.")


def main():

    pokemon = create_pokemon()

    player_pokemon = choose_pokemon(pokemon)

    computer_pokemon = random.choice(pokemon)

    print(f"\nYou chose {player_pokemon.name}!")

    print(f"Computer chose {computer_pokemon.name}!")

    player = Player("Player", player_pokemon)

    computer = Player("Computer", computer_pokemon)

    battle = Battle(player, computer)

    battle.start_battle()


if __name__ == "__main__":
    main()