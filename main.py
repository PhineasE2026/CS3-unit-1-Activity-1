# Define ur functions here! ! ! ! ! ! !

#PART A functions with no args and no return

def bake_cake():
    print("Get your wet ingredients: eggs, vanilla extract, milk.")
    print("Get your dry ingredients: flour, baking powder, sugar.")
    print("Preheat the oven.")
    print("Combine your wet and dry ingredients. Mix thoroughly.")
    print("Lay out combined mixture in a baking pan. Place the pan inside the oven.")
    print("Let bake for 30 minutes at 350 degrees.")
    print("When complete, carefully remove baked cake from oven.")
    print("Slice the cake into multiple slices. Preferably eight.")
    print("Take one slice and eat it to check the flavor.")
    print("It will need some salt, so sprinkle a bit of salt on there.")
    print("Once the salt is sprinkled, your cake is done. Place it into fridge.")
    print("Once people are over the next day, you take cake from fridge. Serve it cold.")

def intro_to_baking():
    print("In Python baking we give arbitarily long explanations to baking simple home recipes")

#PART B functions with args and no return

def list_conceivable_cakes(vanilla, chocolate, red_velvet):
    print(f"Cake in the main recipe: {vanilla}")
    print(f"Cake in secondary recipe {chocolate}")
    print(f"Cake in tertiary recipe: {red_velvet}")

#PART C functions with args and return

def prepare_cake(cake, platter):
    return f"Place {cake} on {platter} wow looks great!"

#PART D functions with possible args and return

def salting(cake, salt="sprinkles of salt"):
    return f"Let's add some {salt} to the {cake}"


def the_bake():
    intro_to_baking()
    list_conceivable_cakes("vanilla cake", "chocolate cake", "red velvet cake")
    bake_cake()
    print(prepare_cake("vanilla cake", "fine china"))
    print("Cake baked.")
    print(salting("vanilla cake"))

def main():
    # Call your functions in the main here
    the_bake()


if __name__ == "__main__":
    main()
