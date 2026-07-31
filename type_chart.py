"""
Pokemon type effectiveness chart.
"""

TYPE_CHART = {
    "Fire": {
        "Fire": 1,
        "Water": 0.5,
        "Grass": 2,
        "Normal": 1
    },

    "Water": {
        "Fire": 2,
        "Water": 1,
        "Grass": 0.5,
        "Normal": 1
    },

    "Grass": {
        "Fire": 0.5,
        "Water": 2,
        "Grass": 1,
        "Normal": 1
    },

    "Normal": {
        "Fire": 1,
        "Water": 1,
        "Grass": 1,
        "Normal": 1
    }
}


def get_type_multiplier(attacking_type, defending_type):
    """
    Returns the effectiveness multiplier.
    """

    return TYPE_CHART.get(attacking_type, {}).get(defending_type, 1)