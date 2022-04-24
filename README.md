## About
This script checks skincare products for potentially bad ingredients. Get that glowing skin without feeling like you are compromising your sanity! This product is not FDA approved. Do not sue me. :relaxed:

## Quick Tutorial
Here is what you need to modify:
* ingredients.txt
* bad_actors.txt

Make sure `ingredient_checker.py`, `bad_actors.txt`, and `ingredients.txt` are all in the same directory. From the command line, run
```
python ingredient_checker.py
```
OR 
```
python3 ingredient_checker.py
```

Your results will be created in a new file (same directory) called `alarms_results.txt`

## How to modify ingredients lists
#### ingredients.txt
* Each product should take up two lines. 
* The first line is of the format "====PRODUCT NAME HERE====". Please do not forget the four equal signs on each side of the product name.
* The second line consists of a comma-separated list of ingredients. The ingredients should be ONE LINE (i.e. don't return carriage anywhere in the list. The script will not work if there is a return carriage in the middle of the list). For example, you may need to copy/paste active vs inactive ingredients together, on the same line.
* Different products should be separated by a blank line.
* Please refer to the [example ingredients.txt file](https://github.com/liuvictoria/skincare/blob/master/ingredients.txt)

#### bad_actors.txt
* Each bad ingredient should be on its own line. 
* Each bad ingredient must be lower-case; otherwise, the program will not pick up a match.
* Please refer to the [example bad_actors.txt file](https://github.com/liuvictoria/skincare/blob/master/bad_actors.txt)

## Results
Please refer to the [example alarms_results.txt file](https://github.com/liuvictoria/skincare/blob/master/alarms_results.txt). This is the result from the example bad_actors.txt file, linked above.

__NOTE: You might notice that "Meadowfoam Estolide" is raised as a potential alarm for SUPERGOOP Unseen Sunscreen SPF 40. This is because "MEA" was detected in the string "Meadowfoam Estolide". However, by visual inspection, it's pretty obvious that "Meadowfoam Estolide" is not MEA. So take the results with a grain of salt!__
