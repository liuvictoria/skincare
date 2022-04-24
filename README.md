### About
This script checks skincare products for potentially bad ingredients. Get that glowing skin without feeling like you are compromising your sanity! This product is not FDA approved. Do not sue me.

### Quick Tutorial
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

### How to modify ingredients lists
#### ingredients.txt
* Each product should take up two lines. 
* The first line is of the format "====PRODUCT NAME HERE====". Please do not forget the four equal signs on each side of the product name.
* The second line consists of a comma-separated list of ingredients. The ingredients should be ONE LINE (i.e. don't return carriage anywhere in the list. The script will not work if there is a return carriage in the middle of the list).
* Different products should be separated by a blank line.
* Please refer to the example .txt file.

An example ingredients txt file:
====BELIF THE TRUE CREAM - AQUA BOMB====
Water, Dipropylene Glycol, Glycerin, Methl Trimethicone, Alcohol Denat, Dimethicone, Cyclopentasiloxane, 1,2-Hexanediol, Malakite Extract, Caprylic/Capric Triglyceride, Pentaerythrityl Tetraethylhexanoate, PEG/PPG/Polybutylene Glycol-8/5/3 Glycerin, Alchemilla Vulgaris Leaf Extract*, Equisetum Arvense Leaf Extract*, Stellaria Media (Chickweed) Extract*, Urtica Dioica (Nettle) Leaf Extract*, Plantago Lanceolata Leaf Extract*, Avena Sativa (Oat) Kernel Extract**, Calendula Officinalis Flower Extract**, Nepeta Cataria Extract**, Rubus Idaeus (Raspberry) Leaf Extract**, Baptisia Tinctoria Root Extract**, Dimethiconol, Polymethylsilsesquioxane, Sodium Acrylate/Acryloyldimethyltaurate/Dimethylacrylamide Crosspolymer, Isohexadecane, Polysorbate 60, Ceramide 3, Cholesterol, Butyrospermum Parkii (Shea) Butter, Phenl Trimethicone, Pentaerythrityl Tetraisostearate, Panthenol, Squalane, Triethylhexanoin, Macadamia Ternifolia Seed Oil, PEG-150, PEG-40 Hydrogenated Castor Oil, Acrylates/C10-30 Alkyl Acrylate Crosspolymer, C14-22 Alcohols, Arachidyl Glucoside, Hydrogenated Lecithin, PEG-100 Stearate, Stearic Acid, Glyceryl Stearate, Carbomer, Tromethamine, Trisodium EDTA, Fragrance+, Citronellol, Limonene, Citral, Geraniol, Linalool

====WELL PEOPLE Dewy Juice Hydrating Aloe Essence====
water (aqua), aloe barbadensis leaf juice, rosa damascena flower water, glycerin, butylene glycol, vaccinium myrtillus fruit/leaf extract, trehalose, tris(hydroxymethyl)aminomethane, panthenol, hydroxyacetophenone, 1/2-hexanediol, saccharum officinarum (sugar cane) extract/ saccharum officinarum extract, xanthan gum, citrus limon (lemon) fruit extract/citrus limon fruit extract, citrus aurantium dulcis(orange) fruit extract/citrus aurantium dulcis fruit extract, acer saccharum (sugar maple) extract/ acer saccharum extract, sodium hyaluronate, hydroxypropyl methylcellulose, citric acid, caprylyl/capryl glucoside, potassium sorbate, sodium benzoate, artemisia princeps leaf extract, polyglyceryl-3 cocoate, polyglyceryl-10 laurate, sodium chloride.

====Clinique Dramatically Different Moisturizing Lotion+====
Water\Aqua\Eau, Mineral Oil\Paraffinum Liquidum\Huile Minérale, Glycerin, Petrolatum, Stearic Acid, Glyceryl Stearate, Sesamum Indicum (Sesame) Oil, Urea, Lanolin Alcohol, Triethanolamine, Hordeum Vulgare (Barley) Extract\Extrait D'Orge, Cucumis Sativus (Cucumber) Fruit Extract, Helianthus Annuus (Sunflower) Seedcake, Propylene Glycol Dicaprate, Sodium Hyaluronate, Butylene Glycol, Pentylene Glycol, Trisodium Edta, Phenoxyethanol, Yellow 6 (Ci 15985), Yellow 5 (Ci 19140), Red 33 (Ci 17200).

#### bad_actors.txt
* Each bad ingredient should be on its own line. 
* Each bad ingredient must be lower-case; otherwise, the program will not pick up a match.
* Please refer to the example .txt file.

An example bad actors txt file:
fragrance
perfume
parfum
phthalate
dbp
dehp
dep
paraben
peg
polyethylene glycol
ethylene oxide
14-dioxane
retinol
formaldehyde
quaternium-15
dmdm hydantoin
imidazolidinyl urea
diazolidinyl urea
hydroxymethylglycinate
2-bromo-2-nitropropane-13 diol
bronopol
sls
lauryl sulfate
sles
sodium laureth sulfate
triclosan
triclocarban
bha
bht
coal
edta
mea
dea
hydroquinone
methylisothiazolinone
methylchloroisothiazolinone
toluene
lead
octinoxate
oxybenzone
avobenzone
benzalkonium chloride

