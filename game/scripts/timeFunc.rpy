init -3 python:
    #Start time
    minute = 0
    check_minute = 0
    hour = 6
    ptime = 0
    mtime = 0
    timeMoved = 0
    ltMoved = 0
    weekday = 1
    month = 5
    number = 1
    year = 1220
    ptime = 0
    last_sleeped = 0
    
    def gettime(*args):
        #Дни недели
        if weekday == 1: _weekday = 'Понедельник'
        if weekday == 2: _weekday = 'Вторник'
        if weekday == 3: _weekday = 'Среда'
        if weekday == 4: _weekday = 'Четверг'
        if weekday == 5: _weekday = 'Пятница'
        if weekday == 6: _weekday = 'Суббота'
        if weekday == 7: _weekday = 'Воскресенье'

        #Месяца
        if month == 1: _month = 'Января'
        if month == 2: _month = 'Февраля'
        if month == 3: _month = 'Марта'
        if month == 4: _month = 'Апреля'
        if month == 5: _month = 'Мая'
        if month == 6: _month = 'Июня'
        if month == 7: _month = 'Июля'
        if month == 8: _month = 'Августа'
        if month == 9: _month = 'Сентября'
        if month == 10: _month = 'Октября'
        if month == 11: _month = 'Ноября'
        if month == 12: _month = 'Декабря'
        
        if minute < 10:
            output = '%d %s %d, %s. %s:0%s' % (number, _month, year, _weekday, hour, minute)
        else:
            output = '%d %s %d, %s. %s:%s' % (number, _month, year, _weekday, hour, minute)
            
        if 'day' in args:
            output = '%d %s %d, %s.' % (number, _month, year, _weekday)
            
        return output
    
    def advancetime(change):
        global minute, check_minute, hour, ptime, weekday, number, year, month, mtime, ltMoved, timeMoved, flagIncome, noEventTime
        x = 0
        while x < change:
            if hour >= 5 and hour < 9:
                hour = 5
                advance = 4
            elif hour >= 9 and hour < 17:
                hour = 9
                advance = 8
            elif hour >= 17 and hour < 22:
                hour = 17
                advance = 5
            else:
                hour = 22
                advance = 7
            changetime(advance*60)
            x += 1

    def getcurrtime():
        if hour >= 5 and hour < 9:
            return 1
        elif hour >= 9 and hour < 17:
            return 2
        elif hour >= 17 and hour < 22:
            return 3
        else:
            return 4
    
    def changetime(change):
        global minute, check_minute, hour, ptime, weekday, number, year, month, mtime, ltMoved, timeMoved, flagIncome, noEventTime
        
        if player.hasEffect('boost'):
            change = int(change/2)
        elif player.hasEffect('boostCure'):
            change = int(change*2)
        while change != 0:
            tempChange = min(10,change)
            change -= min(10,change)
            minute += tempChange
            mtime += tempChange
            counter = 0
            if minute >= 60:
                hourlyRecount()
                minute -= 60
                hour += 1
                noEventTime += 10
                ptime += 1
                if hour >= 24:
                    hour -= 24
                    weekday += 1
                    if weekday >=8: weekday -=7
                    number += 1
                    if number >= 31:
                        number -= 30
                        month += 1
                        if month == 13:
                            month -=12
                            year += 1
        return counter
    
    def getWeekday(day):
        if day == 1: return 'Понедельник'
        if day == 2: return 'Вторник'
        if day == 3: return 'Среду'
        if day == 4: return 'Четверг'
        if day == 5: return 'Пятницу'
        if day == 6: return 'Субботу'
        if day == 7: return 'Воскресенье'
    
    def lt():
        if hour in range(5,22):
            return 1
        else:
            return 0
        return result

    def hourlyRecount():
        global hour, trigger, allChars, aaronWeekly, weekday, aaronAssortiment, ptime
        if trigger[29] == 4 and trigger[30] + 120 < ptime:
            trigger[29] = 3
            
        if weekday == 7 and hour == 12:
            trigger[49] = 0
            
        if hour == 12 and trigger[38] > 0:
            for x in range(0, trigger[38]):
                if trigger[37] == 1:
                    setLoy(3, rand(1,5))
                else:
                    setLoy(3, rand(-5,-1))
                    
        if hour == 0: 
            trigger[21] = -99
            if weekday == 1:
                aaronWeekly = 0
                soldItems[:] = []
            aaronAssortiment = []
            if weekday == 5:
                trigger[47] = 0
            for x in ingForest:
                if rand(1,5) == 1:
                    ing = choice(ingForest)
                    for y in range(1,100):
                        aaronAssortiment.append(ing)
            for x in ingForest:
                if rand(1,5) == 1:
                    ing = choice(ingHills)
                    for y in range(1,100):
                        aaronAssortiment.append(ing)
            for x in ingForest:
                if rand(1,5) == 1:
                    ing = choice(ingHot)
                    for y in range(1,100):
                        aaronAssortiment.append(ing)
            for x in ingForest:
                if rand(1,5) == 1:
                    ing = choice(ingHunter)
                    for y in range(1,100):
                        aaronAssortiment.append(ing)
                
                
        #adding new npc
        while len(slaves) < 110:
            newChar = genFriendsNewchar(genChars(1)[0], slaves)
            slaves.append(newChar)
            allChars.append(newChar)
        
        for char in allChars:
            getCharDesc(char)
            
            if char != player:
                if char.hasItem(meatChickenCooked.name) == False:
                    char.addItem(meatChickenCooked)
                    
            if char.hasItem(meatChickenCooked.name):
                if char.hasEffect(hunger):
                    char.applyEffects(meatChickenCooked.effects)
                    char.removeItem(meatChickenCooked)
                elif char.hasEffect(hungerCure):
                    if char.getEffect(hungerCure).strength < 25:
                        char.applyEffects(meatChickenCooked.effects)
                        char.removeItem(meatChickenCooked)
            
            if char.lname in ['Старый'] and char.getSkill('interaction') >= 10:
                trigger[39] = 1
            
            char.incMana(max(0, int((char.getLust()-50)/10)))
            
            for effect in char.effects: # Применяем все эффекты к чару.
                if char.hasEffect('spellBreakerCure') and effect.id not in ['hunger','hungerCure','spellBreakerCure','faith']:
                    effect.strength += effect.strength
                
                if effect.id == 'faith':
                    char.incMana(effect.strength/10)
                
                if effect.id == 'hunger':
                    if effect.strength <= 25:
                        char.incEnergy(-25)
                    elif effect.strength <= 50:
                        char.incEnergy(-50)
                        char.incLust(-50)
                    elif effect.strength <= 75:
                        char.incEnergy(-100)
                        char.incLust(-100)
                        char.incMana(-5)
                    else:
                        char.incEnergy(-100)
                        char.incLust(-100)
                        char.incMana(-5)
                        char.incPrana(-1)
                        
                elif effect.id == 'hungerCure':
                    if effect.strength >= 75:
                        player.incEnergy(50)
                        player.incPrana(1)
                    elif effect.strength >= 50:
                        player.incEnergy(25)
                        
                elif effect.id == 'diarea':
                    char.applyEffects({hunger:10})
                    
                elif effect.id == 'diareaCure':
                    char.incLust(-5)
                    char.incEnergy(-25)
                    
                elif effect.id == 'intoxication':
                    char.incMana(-5)
                    char.applyEffects({hunger:5})
                    
                elif effect.id == 'intoxicationCure':
                    char.incMana(1)
                    
                elif effect.id == 'fertility':
                    char.incLust(5)
                    
                elif effect.id == 'fertilityCure':
                    char.incLust(-5)
                    
                elif effect.id == 'bleeding':
                    char.incPrana(-2.5)
                    
                elif effect.id == 'regeneration':
                    char.incPrana(10)
                    
                elif effect.id == 'regenerationCure':
                    char.incPrana(-0.5)
                    
                elif effect.id == 'concentration':
                    char.incMana(5)
                    
                elif effect.id == 'concentrationCure':
                    char.incMana(-2)
                    char.incFun(1)
                    
                elif effect.id == 'poison':
                    char.incPrana(-10)
                    
                elif effect.id == 'impotence' and char.getSex() != 'female':
                    char.incLust(-25)
                    
                elif effect.id == 'impotenceCure' and char.getSex() != 'female':
                    char.incLust(25)
                    
                effect.strength += effect.increment
                char.checkEffect(effect)
                    
                
                
                