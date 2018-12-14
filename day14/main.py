#!/usr/bin/env python3

def p1(nb_recipes):
    recipes = [3,7]
    elf0 = 0
    elf1 = 1
    while len(recipes) <= nb_recipes + 10:
        new_recipe = recipes[elf0] + recipes[elf1]
        if new_recipe > 9:
            recipes.append(new_recipe//10)
        recipes.append(new_recipe%10)
        elf0 = (elf0 + 1 + recipes[elf0]) % len(recipes)
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    return "".join(map(str, recipes[nb_recipes:nb_recipes+10]))

def p2(recipe_str):
    recipes = [3,7]
    elf0 = 0
    elf1 = 1
    recipe_length = len(recipe_str)
    while "".join(map(str, recipes[-recipe_length:])) != recipe_str:
        new_recipe = recipes[elf0] + recipes[elf1]
        if new_recipe > 9:
            recipes.append(new_recipe//10)
            if "".join(map(str, recipes[-recipe_length:])) == recipe_str:
                break
        recipes.append(new_recipe%10)
        elf0 = (elf0 + 1 + recipes[elf0]) % len(recipes)
        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    return len(recipes) - recipe_length

if __name__ == "__main__":
    print("part1(5): {}".format(p1(5)))
    print("part1(18): {}".format(p1(18)))
    print("part1(2018): {}".format(p1(2018)))
    print("part1(909441): {}".format(p1(909441)))
    print("part2(\"51589\"): {}".format(p2("51589")))
    print("part2(\"01245\"): {}".format(p2("01245")))
    print("part2(\"92510\"): {}".format(p2("92510")))
    print("part2(\"59414\"): {}".format(p2("59414")))
    print("part2(\"909441\"): {}".format(p2("909441")))

