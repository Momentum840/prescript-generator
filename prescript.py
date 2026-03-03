import json
import random
import time
import os

def generatePrescript():
    with open('conditions.json', 'r') as file:
        words = json.load(file)
        
    num = random.randint(1,500)
    suffix = "th" if 11 <= num % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(num % 10, "th")
    numStr = f"{num}{suffix}"
    
    condition = random.choice(words["conditions"])
    act1 = random.choice(words["firstAct"])
    adj = random.choice(words["adjectives"])
    noun = random.choice(words["nouns"])
    act2 = random.choice(words["secondAct"])
    closing = random.choice(words["closing"])
    
    prescript = f"{condition} {act1} and find the {numStr} {adj} {noun} you see and {act2}. {closing}"
    
    return prescript.strip()

print (generatePrescript())