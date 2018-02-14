init -5 python:
    import random
    from random import choice
    import time
    from operator import attrgetter
    
    def initPotion(item):
        global currPotion
        for effect in item.effects:
            if effect.id == 'intoxication':
                if item.effects.get(effect) == 100:
                    tempMult = 4
                elif item.effects.get(effect) >= 90:
                    tempMult = 3
                elif item.effects.get(effect) >= 40:
                    tempMult = 2
                elif item.effects.get(effect) >= 20:
                    tempMult = 1.5
                elif item.effects.get(effect) >= 5:
                    tempMult = 0.5
                else:
                    tempMult = 0.1
                
        tempPotion = Potion(
        mult = tempMult, 
        mainEffect = {},
        subEffects = {}
        )
        tempPotion.name = item.name
        tempPotion.id = rand(100000,999999)
        tempPotion.durability = 1
        tempPotion.picto = 'images/items/defaultPotion.png'
        tempPotion.type = 'hidden'
        currPotion = tempPotion
    
    def updatePotion(item):
        global currPotion, usedIngredients
        changetime(20)
        for effect in item.effects:
            if currPotion.mainEffect.has_key(effect):
                currPotion.mainEffect[effect] = min(100, currPotion.mainEffect.get(effect) + item.effects.get(effect)*currPotion.mult)
            else:
                if currPotion.subEffects.has_key(effect):
                    currPotion.subEffects[effect] = currPotion.subEffects.get(effect) + item.effects.get(effect)*currPotion.mult
                else:
                    currPotion.subEffects[effect] = item.effects.get(effect)*currPotion.mult
        
    def setMainEffectPotion(effect):
        global currPotion
        currPotion.name = 'Зелье: ' + effect.name
        currPotion.mainEffect = {effect : 0}
        
    def cleanPotion(item):
        global currPotion
        changetime(10)
        for x in item.effects:
            if currPotion.getAntiSubEffect(x):
                currPotion.subEffects.pop(currPotion.getAntiSubEffect(x))
                
    def getPotion(potion):
        global usedIngredients
        player.incMana(-10)
        tempPotion =  Ingredient(
        effects = potion.mainEffect
        )
        tempPotion.name = potion.name
        tempPotion.id = potion.getMainEffect().name
        tempPotion.durability = 1
        tempPotion.picto = 'images/items/' + potion.getMainEffect().id + '.png'
        tempPotion.type = 'food'
        player.addItem(tempPotion)
        for x in usedIngredients:
            player.removeItem(x)
        changetime(30)
            
    def getPotions(potion,amount):
        global usedIngredients, failedIngredients
        usedIngredients = usedIngredients + failedIngredients
        player.incMana(-10*amount)
        tempPotion =  Ingredient(
        effects = potion.mainEffect
        )
        tempPotion.name = potion.name
        tempPotion.id = potion.getMainEffect().name
        tempPotion.durability = 1
        tempPotion.picto = 'images/items/' + potion.getMainEffect().id + '.png'
        tempPotion.type = 'food'
        for x in range(0,amount):
            player.addItem(tempPotion)
        for y in range(0,amount):
            for x in usedIngredients:
                player.removeItem(x)
        changetime(30*amount)
    
    def checkAmount(amount):
        global usedIngredients, failedIngredients
        tempIngredients = usedIngredients + failedIngredients
        counter = 0
        if player.getMana() < 10*amount:
            return False
        for ing in tempIngredients:
            for x in player.inventory:
                if ing.name == x.name:
                    counter += 1
            if counter < amount:
                return False
            else:
                counter = 0
        return True