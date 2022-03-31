from imaplib import IMAP4_SSL
from PIL import Image 
from IPython.display import display 
import random
import json

#Inject all the shapes and set their weights

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Aqua", "Royal Blue", "Purple", "Cyan", "Pink", "Red", "Yellow", "Lemon", "Lime", "Green", "Full Aqua", "Full Royal Blue", "Full Maroon", "Full Orange", "Full Green", "Gold", "Silver"]
background_weights = [0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.06379681446,0.02152389152,0.02152389152]

shirts = ["Red PEZ", "Losing Streak", "Pezcore", "Hello Rockview", "Borders & Boundaries", "Anthem", "In With The Out Crowd", "GNV FLA", "See The Light", "Silver Linings", "Sound The Alarm", "Losers, Kings, and Things We Don\'t Understand", "Greased", "Making Fun of Things You Don't Understand", "Smoke Spot"]
shirts_weights = [0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667,0.06666666667]

candy_dipenser = ["Evo Kid", "Roger Lima", "Chris DeMakes", "Buddy Schaub", "J.R. Wasilewski", "Matt Yonker", "Losing Streak", "Hello Rockview", "Losers, Kings, and Things We Don\'t Understand", "Saddest Clown", "Frank"]
candy_dipenser_weights = [0.09090909091,0.09090909091,0.09090909091,0.09090909091,0.09090909091,0.09090909091,0.09090909091,0.09090909091,0.09090909091,0.09090909091,0.09090909091]

heads = ["Evo Kid", "Merchtastic", "Hell Looks A Lot Like L.A.", "Glorious Moustache", "Who is that masked man?", "Ghost of Tours Past", "Howdy Howdy Howdy", "Space Cadet", "Go Gators!", "Mohawk"]
heads_weights = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

background_files = {
    "Aqua": "LTJ_NFT_BG_1",
    "Royal Blue": "LTJ_NFT_BG_2",
    "Purple": "LTJ_NFT_BG_3",
    "Cyan": "LTJ_NFT_BG_4",
    "Pink": "LTJ_NFT_BG_5",
    "Red": "LTJ_NFT_BG_6",
    "Yellow": "LTJ_NFT_BG_7",
    "Lemon": "LTJ_NFT_BG_8",
    "Lime": "LTJ_NFT_BG_9",
    "Green": "LTJ_NFT_BG_10",
    "Full Aqua": "LTJ_NFT_BG_11",
    "Full Royal Blue": "LTJ_NFT_BG_12",
    "Full Maroon": "LTJ_NFT_BG_13",
    "Full Orange": "LTJ_NFT_BG_14",
    "Full Green": "LTJ_NFT_BG_15",
    "Gold": "LTJ_NFT_BG_GOLD",
    "Silver": "LTJ_NFT_BG_SILVER"
}

shirts_files = {
    "Red PEZ": "LTJ_NFT_2_shirt_1",
    "Losing Streak": "LTJ_NFT_2_shirt_2",
    "Pezcore": "LTJ_NFT_2_shirt_3",
    "Hello Rockview": "LTJ_NFT_2_shirt_4",
    "Borders & Boundaries": "LTJ_NFT_2_shirt_5",
    "Anthem": "LTJ_NFT_2_shirt_6",
    "In With The Out Crowd": "LTJ_NFT_2_shirt_7",
    "GNV FLA": "LTJ_NFT_2_shirt_8",
    "See The Light": "LTJ_NFT_2_shirt_9",
    "Silver Linings": "LTJ_NFT_2_shirt_10",
    "Sound The Alarm": "LTJ_NFT_2_shirt_11",
    "Losers, Kings, and Things We Don't Understand": "LTJ_NFT_2_shirt_12",
    "Greased": "LTJ_NFT_2_shirt_13",
    "Making Fun of Things You Don't Understand": "LTJ_NFT_2_shirt_14",
    "Smoke Spot": "LTJ_NFT_2_shirt_15"
}

candy_dipenser_files = {
    "Evo Kid": "LTJ_NFT_3_pez_1",
    "Roger Lima": "LTJ_NFT_3_pez_2",
    "Chris DeMakes": "LTJ_NFT_3_pez_3",
    "Buddy Schaub": "LTJ_NFT_3_pez_4",
    "J.R. Wasilewski": "LTJ_NFT_3_pez_5",
    "Matt Yonker": "LTJ_NFT_3_pez_6",
    "Losing Streak": "LTJ_NFT_3_pez_7",
    "Hello Rockview": "LTJ_NFT_3_pez_8",
    "Losers, Kings, and Things We Don't Understand": "LTJ_NFT_3_pez_9",
    "Saddest Clown": "LTJ_NFT_3_pez_10",
    "Frank": "LTJ_NFT_3_pez_11"
}

heads_files = {
    "Evo Kid": "LTJ_NFT_4_head_1",
    "Merchtastic": "LTJ_NFT_4_head_2",
    "Hell Looks A Lot Like L.A.": "LTJ_NFT_4_head_3",
    "Glorious Moustache": "LTJ_NFT_4_head_4",
    "Who is that masked man?": "LTJ_NFT_4_head_5",
    "Ghost of Tours Past": "LTJ_NFT_4_head_6",
    "Howdy Howdy Howdy": "LTJ_NFT_4_head_7",
    "Space Cadet": "LTJ_NFT_4_head_8",
    "Go Gators!": "LTJ_NFT_4_head_9",
    "Mohawk": "LTJ_NFT_4_head_10"
}

#Create a function to generate unique image combinations
TOTAL_IMAGES = 100 # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = [] 

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Shirts"] = random.choices(shirts, shirts_weights)[0]
    new_image ["Candy Dispenser"] = random.choices(candy_dipenser, candy_dipenser_weights)[0]
    new_image ["Heads"] = random.choices(heads, heads_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)

#Return true if all images are unique

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

#add token id

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

#print all images

print(all_images)

#get trait count

background_count = {}
for item in background:
    background_count[item] = 0

shirts_count = {}
for item in shirts:
    shirts_count[item] = 0

candy_dipenser_count = {}
for item in candy_dipenser:
    candy_dipenser_count[item] = 0

heads_count = {}
for item in heads:
    heads_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    shirts_count[image["Shirts"]] += 1
    candy_dipenser_count[image["Candy Dispenser"]] += 1
    heads_count[image["Heads"]] += 1

print(background_count)
print(shirts_count)
print(candy_dipenser_count)
print(heads_count)

#Generate Metadata for all Traits

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#Generate Images

for item in all_images:

    im1 = Image.open(f'./layers/backgrounds/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/shirts/{shirts_files[item["Shirts"]]}.png').convert('RGBA')
    im3 = Image.open(f'./layers/pez/{candy_dipenser_files[item["Candy Dispenser"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/heads/{heads_files[item["Heads"]]}.png').convert('RGBA')
    
    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)

    #Convert to RGB
    rgb_im = com3.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/LTJ_images_100/" + file_name)
    print(file_name)

#Generate Metadata

#f = open('./metadata/all-traits.json',) 
#data = json.load(f)

#IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE/"
#PROJECT_NAME = "Balloon Animals"

#def getAttribute(key, value):
#    return {
#        "trait_type": key,
#        "value": value
#    }
#for i in data:
#    token_id = i['tokenId']
#    token = {
#        "image": IMAGES_BASE_URI + str(token_id) + '.png',
#        "tokenId": token_id,
#        "name": PROJECT_NAME + ' ' + str(token_id),
#        "attributes": []
#    }
#    token["attributes"].append(getAttribute("Background", i["Background"]))
#    token["attributes"].append(getAttribute("Back Legs", i["Back Legs"]))
#    token["attributes"].append(getAttribute("Background", i["Background"]))
#    token["attributes"].append(getAttribute("Ears", i["Ears"]))
#    token["attributes"].append(getAttribute("Front Legs", i["Front Legs"]))
#    token["attributes"].append(getAttribute("Head", i["Head"]))
#    token["attributes"].append(getAttribute("Eyelids", i["Eyelids"]))
#    token["attributes"].append(getAttribute("Tail", i["Tail"]))
#    token["attributes"].append(getAttribute("Outline", i["Outline"]))

#    with open('./metadata/' + str(token_id), 'w') as outfile:
#        json.dump(token, outfile, indent=4)
#f.close()