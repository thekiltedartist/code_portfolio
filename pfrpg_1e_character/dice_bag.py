from random import randint


def d20(mod=0):
    return randint(1,20 + mod)


def d6(mod=0):
    return randint(1,6) + mod
