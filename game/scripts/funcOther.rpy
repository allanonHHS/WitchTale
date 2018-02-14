init -5 python:
    import random
    from random import choice
    import time
    from operator import attrgetter

    dublicationChar = []
    classrooms = []
    
    def rand(a, b):
        if a - b >= 0 or b == 0:
            return a
        else :
            return random.randint(a,b)

    def randf(a, b):
        return random.uniform(a,b)


    def getPar(list, *args):
        temp = 0
        if args[0] == 'loy':
            for x in list:
                temp = temp + x.getLoy()
            return round(temp/len(list),2)

        if args[0] == 'fun':
            for x in list:
                temp = temp + x.getFun()
            return round(temp/len(list),2)

        if args[0] == 'corr':
            for x in list:
                temp = temp + x.getCorr()
            return round(temp/len(list),2)

        if args[0] == 'lust':
            for x in list:
                temp = temp + x.getLust()
            return round(temp/len(list),2)

        if args[0] == 'edu':
            for x in list:
                temp = temp + x.getEdu()
            return round(temp/len(list),2)

        if args[0] == 'rep':
            for x in list:
                temp = temp + x.getRep()
            return round(temp/len(list),2)
        return 'error'

    def waiting(t):
        player.stats.energy -= randf(t/2,t)
        changetime(t)
        move(curloc)
        
#Динамическая картинка
    def dynImage(st,at): 
        return dynpicto, None

    def clrscr():
        renpy.scene(layer='screens')

    def skipEvent():
        tryEvent(curloc)

    def setLoy(count,amount):
        for x in range(0, count):
            getChar().incLoy(amount)
            
    def setCorr(count,amount):
        for x in range(0, count):
            getChar().incCorr(amount) 
            
    def setLust(count,amount):
        for x in range(0, count):
            getChar().incLust(amount)
            
    def setFun(count,amount):
        for x in range(0, count):
            getChar().incFun(amount)   

           
    def getDays(number):
        if number == 0 or number >= 5:
            return str(number) + ' дней'
        elif number == 1:
            return str(number) + ' день'
        else:
            return str(number) + ' дня'

    def clearLocations():
        for x in locations:
            x.removePeoples([])
        
    def hasLocationsItem(item):
        for x in locations:
            if item in x.items:
                return True
        return False
        
    def getChar(*args):
        global slaves, lastUsed
        tempArr = []
        if not args:
            # Gather all slaves
            tempArr += slaves
        else:
            for x in slaves:
                if x.getSex() in args or args[0] == 'all':
                    tempArr.append(x)
            if len(args) > 1:
                if args[1] == 'young':
                    tempArr[:] = [x for x in tempArr if x.age < 40]
                if args[1] == 'old':
                    tempArr[:] = [x for x in tempArr if x.age >= 40]
        for x in range(0,10):
            selected = choice(tempArr)
            if selected not in lastUsed:
                break
            if x == 5:
                del lastUsed[:]
        lastUsed.append(selected)
        return selected
        
    def getCharByWork(gender, work):
        global slaves
        tempArr = []
        for x in slaves:
            if x.getSex() == gender and x.lname == work:
                tempArr.append(x)
        return choice(tempArr)
        
    def checkAntiEffect(effect1, effect2):
        if effect1.id[-4:] == 'Cure':
            if effect2.id == effect1.id[:-4]:
                return True
        else:
            if effect2.id[:-4] == effect1.id:
                return True
        return False
        
    def getAntiEffect(effect):
        if effect.id[-4:] == 'Cure':
            for pEffect in allEffects:
                if pEffect.id == effect.id[:-4]:
                    return pEffect
        else:
            for pEffect in allEffects:
                if pEffect.id[:-4] == effect.id:
                    return pEffect
        return False
        
    def getAlignment(char):
        align = len(char.friends) - len(char.enemies)
        if align < -8:
            return 'Ужасный человек'
        elif align < -5:
            return 'Плохой человек'
        elif align < -2:
            return 'Нехороший человек'
        elif align < 2:
            return 'Обычный человек'
        elif align < 5:
            return 'Неплохой человек'
        elif align < 8:
            return 'Хороший человек'
        else:
            return 'Отличный человек'
            
            
    def weightChoice(dict):
        allWeight = sum(dict.values())
        rnd = rand(0,allWeight-1)
        upto = 0
        for element in dict:
            upto += dict.get(element)
            if rnd in range(0,upto):
                return element
        return None
        
    def cheatIng():
        for x in allItems:
            for y in range(1,100):
                player.addItem(x)
