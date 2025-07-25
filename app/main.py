class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.health = health
        self.name = name
        self.hidden = False
        if health > 0:
            self.alive.append(self)

    def __repr__(self) -> str:
        return \
            "{"\
            f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}"\
            "}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = bool(abs(self.hidden - 1))


class Carnivore(Animal):
    @staticmethod
    def bite(target: Herbivore) -> None:
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)
                target.health = 0
