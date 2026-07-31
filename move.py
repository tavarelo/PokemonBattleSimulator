import random

class Move:
    """
    Represents a Pokemon move.
    """

    def __init__(self, name, move_type, power, accuracy):
        self.name = name
        self.move_type = move_type
        self.power = power
        self.accuracy = accuracy

    def hits(self):
        """
        Returns True if the move hits based on its accuracy.
        """
        return random.randint(1, 100) <= self.accuracy

    def __str__(self):
        return (
            f"{self.name} "
            f"(Type: {self.move_type}, "
            f"Power: {self.power}, "
            f"Accuracy: {self.accuracy}%)"
        )