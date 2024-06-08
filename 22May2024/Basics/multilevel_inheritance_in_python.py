"""
1.Multilevel Inheritance - A class can inherit attributes and methods from more than one class.
2.Method Resolution Order (MRO) - Search is done first in current class,
                                  then the search continues into parent classes in depth-first,
                                  left-right fashion without searching the same class twice.
"""


class Movecharacter:
    def move_fwd(self):
        print("Move forward 1 step")

    def move_bwd(self):
        print("Move backward 1 step")


class JumpCharacter(Movecharacter):
    def jump_level_1(self):
        print("jump_level_1")

    def jump_level_2(self):
        print("jump_level_2")


class pokemon(JumpCharacter):
    def move_bwd(self):  # overridden
        print("Pokemon moving")


p = pokemon()
p.move_fwd()
p.move_bwd()
p.jump_level_1()
p.jump_level_2()
print(pokemon.mro())