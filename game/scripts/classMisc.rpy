init -50 python:
    class Item:
        def __init__ (self, name, id, durability, picto, type):
            self.durability = durability
            self.name = name
            self.id = id
            self.picto = picto
            self.type = type

    class Ingredient(Item):
        def __init__ (self, effects):
            self.effects = effects
            
        def getEffect(self):
            for x in self.effects:
                return x
        
        def getEffectStrength(self):
            for x in self.effects:
                return self.effects.get(x)
    
    class Clothing(Item):
        def __init__ (self, covers, resist):
            self.covers = covers
            self.resist = resist
    
    class Effect:
        def __init__ (self, name, id, increment, type, description):
            self.name = name
            self.id = id
            self.strength = 0
            self.increment = increment
            self.type = type
            self.description = description
        
        def normalize(self):
            self.strength = max(0, min(self.strength, 100))
            
        def reset(self):
            self.normalize()
            
    class Potion(Item):
        def __init__ (self, mult, mainEffect, subEffects):
            self.mult = mult
            self.mainEffect = mainEffect
            self.subEffects = subEffects
            
        def hasMainEffect(self, item):
            for x in item.effects:
                if x in self.mainEffect:
                    return True
            return False
            
        def getMainEffect(self):
            for x in self.mainEffect:
                return x
                
        def getMainEffectStrength(self):
            for x in self.mainEffect:
                return self.mainEffect.get(x)
            
        def getAntiSubEffect(self, effect):
            if effect.id[-4:] == 'Cure':
                for pEffect in self.subEffects:
                    if pEffect.id == effect.id[:-4]:
                        return pEffect
            else:
                for pEffect in self.subEffects:
                    if pEffect.id[:-4] == effect.id:
                        return pEffect
            return False
            
        def hasAntiSubEffect(self, effects):
            for effect in effects:
                if effect.id[-4:] == 'Cure':
                    for pEffect in self.subEffects:
                        if pEffect.id == effect.id[:-4]:
                            return True
                else:
                    for pEffect in self.subEffects:
                        if pEffect.id[:-4] == effect.id:
                            return True
            return False
            
    class Request:
        def __init__ (self, description, effect, sex, adviceG, adviceB, align, patient = False, patientSex = 'all'):
            self.description = description
            self.effect = effect
            self.char = Char()
            self.patient = patient
            self.patientSex = patientSex
            self.sex = sex
            self.name = self.char.name
            self.adviceG = adviceG
            self.adviceB = adviceB
            self.align = align
            self.empathy = False
            self.empathyTry = False
            