import json
import random
import string
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
    
    prescript = f"{condition}, {act1} and find the {numStr} {adj} {noun} you see and {act2}. {closing}"
    
    return prescript.strip()

def typewriting(text, speed=0.05):
    for char in text:
        print(char, end='', flush=False) # set flush to True for instant output
        time.sleep(speed)
    print()

# cool shit zone
def charSpamShow(targetText, speed=0.05):
    spamChar = string.ascii_letters + string.punctuation + string.digits
    currentText = [random.choice(spamChar) for _ in range(len(targetText))]
    
    for i in range(len(targetText)):
        for j in range(i, len(targetText)):
            currentText[j] = random.choice(spamChar)
            
        currentText[i] = targetText[i]
        
        print('\r' + "".join(currentText), end='', flush=True) 
        time.sleep(speed)
        
    
def charSpamHide(targetText, speed=0.05):
    spamChar = string.ascii_letters + string.punctuation + string.digits
    currentText = list(targetText)
    
    for i in range(len(targetText)):
        for j in range(i + 1):
            currentText[j] = random.choice(spamChar)
            
        print('\r' + "".join(currentText), end='', flush=True)
        time.sleep(speed)
        
    time.sleep(0.5)
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # --- The _CLEAR._ Effect ---
    clearText = "_CLEAR._"
    
    for _ in range(15): 
        pureChaos = "".join(random.choice(spamChar) for _ in range(len(clearText)))
        print('\r' + pureChaos, end='', flush=True)
        time.sleep(0.03) 
                
    currentClear = [random.choice(spamChar) for _ in range(len(clearText))]
    
    for i in range(len(clearText)):
        for j in range(i, len(clearText)):
            currentClear[j] = random.choice(spamChar)
        currentClear[i] = clearText[i]
        print('\r' + "".join(currentClear), end='', flush=True)
        time.sleep(0.1) 
        
    time.sleep(1)
    print("\n") 
    
# --- OUTPUT ---
finalPrescript = generatePrescript()
charSpamShow(finalPrescript, speed=0.02)
time.sleep(3)
charSpamHide(finalPrescript, speed=0.02)