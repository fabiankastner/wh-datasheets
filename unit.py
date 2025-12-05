from typing import Optional, List
import yaml

class Unit:
    def __init__(
            self,
            name: Optional[str] = None,
            statline: dict = {"M": None, "T": None, "SV": None, "W": None, "LD": None, "OC": None},
            invulnerable_save: Optional[bool] = None,
            keywords: List[str] = [],
            abilities: dict = {},
            melee_weapons: List[dict] = [
                {"Range": None, "A": None, "WS": None, "S": None, "AP": None, "D": None}
            ],
            ranged_weapons: List[dict] = [
                {"Range": None, "A": None, "BS": None, "S": None, "AP": None, "D": None}
            ]
            ):
        self.name = name
        self.statline = statline
        self.invulnerable_save = invulnerable_save
        self.keywords = keywords
        self.abilities = abilities
        self.melee_weapons = melee_weapons
        self.ranged_weapons = ranged_weapons

    def to_yaml(self) -> None:

        filename = f"{self.name}.yaml" if self.name else "unit.yaml"
        with open(filename, "w") as file:
            yaml.dump(self.__dict__, file, sort_keys=False)
