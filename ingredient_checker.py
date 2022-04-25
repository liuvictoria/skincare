# read in bad ingredients file
# MAKE SURE ALL BAD INGREDIENTS ARE LOWER CASE!!!!! OTHERWISE IT WILL NOT MATCH
with open("bad_actors.txt") as bad_actors_file:
    bad_actors = bad_actors_file.read().splitlines()

# read in product ingredients file
# don't worry about lowercase / uppercase for this files
with open("ingredients.txt") as in_file:
    lines = in_file.readlines()

# check ingredients txt file is formatted correctly
for idx_line, line in enumerate(lines):
    if "====" in line:
        assert idx_line + 1 < len(lines), "no ingredients after product name"
        assert "====" not in lines[idx_line + 1], "ingredients need to be listed in the line after product name"
        assert "," in lines[idx_line + 1], "ingredients need to be listed in the line after product name"
        if idx_line + 2 < len(lines):
            assert "\n" == lines[idx_line + 2], "Two possible errors: 1) ingredients need to fit in one line OR 2) need a new line after ingredients list"

# extract product name and ingredients
products = dict()
for idx_line, line in enumerate(lines):
    if "====" in line:
        products[line] = lines[idx_line + 1]

# create file for results
with open('alarms_results.txt', 'w') as out_file:
    # iterate thru products
    for product in products:
        
        ingredients = products[product]
        # everything lowercase for string matching
        lowercase_ingredients = ingredients.lower()
        ingredients = ingredients.split(",")
        lowercase_ingredients = lowercase_ingredients.split(",")

        has_alarms = False
        out_file.write(f"{product}")
        for idx_ingredient, lowercase_ingredient in enumerate(lowercase_ingredients):
            for bad_actor in bad_actors:
                if bad_actor in lowercase_ingredient:
                    has_alarms = True
                    out_file.write(f"Ingredient Name: {ingredients[idx_ingredient].rstrip().lstrip()}\n")
                    out_file.write(f"    Potential Alarm: {bad_actor}\n")
                    continue
        if not has_alarms:
            out_file.write("None of the ingredients raise alarms")
        out_file.write("\n\n")
