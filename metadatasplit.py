import csv
import json


#Generate Metadata

f = open('./all-traits.json',) 
data = json.load(f)

PROJECT_NAME = "Evo Kid Army"
DESCRIPTION = "The Evo Kid Army is a collection of 9,292 NFTs that give the holder access to the Evo Kid Army, the official fan club of the band Less Than Jake. Members get access to exclusive merch, special giveaways, behind-the-scenes looks at recording sessions, advance peeks at new music, and plenty more! It's the ultimate VIP pass to all things Less Than Jake!"
EXTERNAL_URL = "https://lessthanjake.com/"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    image = "https://nervous.mypinata.cloud/ipfs/QmVdafQABqczynVEJkxTTFY5uQReS86VQPR7BDebf1KJNq/" + str(token_id) + '.png'
    token = {
        "attributes": [],
        "tokenId": token_id,
        "name": PROJECT_NAME + ' #' + str(token_id),
        "description": DESCRIPTION,
        "external_url": EXTERNAL_URL,
        "image": image


    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Shirts", i["Shirts"]))
    token["attributes"].append(getAttribute("Candy Dispenser", i["Candy Dispenser"]))
    token["attributes"].append(getAttribute("Heads", i["Heads"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()