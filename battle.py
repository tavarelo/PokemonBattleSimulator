import random

from type_chart import get_type_multiplier


class Battle:
    """
    Controls the entire battle.
    """

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    # -------------------------------------------------
    # Damage Calculation
    # -------------------------------------------------

    def calculate_damage(self, attacker, defender, move):

        if not move.hits():
            print(f"\n{attacker.name}'s {move.name} missed!")
            return 0

        multiplier = get_type_multiplier(
            move.move_type,
            defender.pokemon_type
        )

        critical = 1

        if random.randint(1, 100) <= 10:
            critical = 1.5

        base_damage = (
            attacker.attack
            + move.power
            - defender.defense
        ) / 2

        if base_damage < 1:
            base_damage = 1

        damage = int(base_damage * multiplier * critical)

        print(f"\n{attacker.name} used {move.name}!")

        if multiplier == 2:
            print("It's super effective!")

        elif multiplier == 0.5:
            print("It's not very effective...")

        if critical > 1:
            print("Critical Hit!")

        return damage

    # -------------------------------------------------
    # Attack
    # -------------------------------------------------

    def attack(self, attacker, defender, move):

        damage = self.calculate_damage(
            attacker,
            defender,
            move
        )

        defender.take_damage(damage)

        print(f"{defender.name} lost {damage} HP.")

        print(
            f"{defender.name}: "
            f"{defender.current_hp}/"
            f"{defender.max_hp} HP"
        )

    # -------------------------------------------------
    # Player Turn
    # -------------------------------------------------

    def player_turn(self):

        pokemon = self.player.pokemon

        while True:

            print("\n==========================")
            print(f"{pokemon.name}'s Turn")
            print("==========================")

            print("1. Attack")
            print("2. Use Potion")
            print("3. View Stats")

            choice = input("\nChoose an option: ")

            if choice == "1":

                print()

                for i, move in enumerate(pokemon.moves):

                    print(f"{i + 1}. {move}")

                try:

                    move_choice = int(
                        input("\nChoose a move: ")
                    ) - 1

                    if move_choice not in range(
                        len(pokemon.moves)
                    ):
                        raise ValueError

                    move = pokemon.moves[move_choice]

                    self.attack(
                        pokemon,
                        self.computer.pokemon,
                        move
                    )

                    break

                except ValueError:

                    print("Invalid choice.")

            elif choice == "2":

                if self.player.use_potion():
                    break

            elif choice == "3":

                pokemon.display_stats()

            else:

                print("Invalid choice.")

    # -------------------------------------------------
    # Computer Turn
    # -------------------------------------------------

    def computer_turn(self):

        pokemon = self.computer.pokemon

        if (
            pokemon.current_hp <= pokemon.max_hp // 3
            and self.computer.potions > 0
            and random.randint(1, 100) <= 40
        ):

            self.computer.use_potion()
            return

        move = pokemon.choose_random_move()

        print("\nComputer's Turn...")

        self.attack(
            pokemon,
            self.player.pokemon,
            move
        )
    # -------------------------------------------------
    # Speed Order
    # -------------------------------------------------

    def first_turn_is_player(self):
        """
        Returns True if the player's Pokemon is faster.
        """

        return (
            self.player.pokemon.speed
            >= self.computer.pokemon.speed
        )

    # -------------------------------------------------
    # Check Winner
    # -------------------------------------------------

    def battle_over(self):

        if self.player.pokemon.is_fainted():
            return True

        if self.computer.pokemon.is_fainted():
            return True

        return False

    # -------------------------------------------------
    # Display Winner
    # -------------------------------------------------

    def display_winner(self):

        print("\n================================")
        print("Battle Finished!")
        print("================================")

        if self.player.pokemon.is_fainted():

            print("\nYou Lost!")

            print(
                f"{self.computer.pokemon.name} wins the battle!"
            )

        else:

            print("\nCongratulations!")

            print(
                f"{self.player.pokemon.name} wins the battle!"
            )

    # -------------------------------------------------
    # Start Battle
    # -------------------------------------------------

    def start_battle(self):

        print("\n================================")
        print("Pokemon Battle Begins!")
        print("================================")

        print(
            f"\nYou sent out {self.player.pokemon.name}!"
        )

        print(
            f"Computer sent out {self.computer.pokemon.name}!"
        )

        player_first = self.first_turn_is_player()

        while not self.battle_over():

            print("\n--------------------------------")
            print(
                f"{self.player.pokemon.name}: "
                f"{self.player.pokemon.current_hp}/"
                f"{self.player.pokemon.max_hp}"
            )

            print(
                f"{self.computer.pokemon.name}: "
                f"{self.computer.pokemon.current_hp}/"
                f"{self.computer.pokemon.max_hp}"
            )
            print("--------------------------------")

            if player_first:

                self.player_turn()

                if self.battle_over():
                    break

                self.computer_turn()

            else:

                self.computer_turn()

                if self.battle_over():
                    break

                self.player_turn()

        self.display_winner()       