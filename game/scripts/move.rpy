init:
    image daytime = ConditionSwitch(
        "hour < 5 or hour > 20", "#646464",
        "hour >=5  and hour <= 8", "#FFD6BD",
        "hour > 8  and hour <= 18", "#FFFFFF",
        "hour > 18  and hour <= 20", "#EB9191",
        )
    image black = '#000000'
    $ lastEventTime = 0

init python:
#базовая функция перемещения. Использовать всегда и всюду
    from random import shuffle
    def move(where,*args):
        global curloc, hour, prevloc, same_loc, defaultSymbol, school, noEventTime, development, interactionObj, mtime, lastEventTime, allChars #объявление глобальных переменных
        if development == 1:    
            player.setEnergy(2000)
        interactionObj = '' # Сбрасываем человека с которым разговаривали
        if renpy.has_label(where) == True: #Проверка на то, что локация существует. Если нет, прыгаем домой.
            renpy.scene(layer='master') # Сброс картинок
            renpy.scene(layer='screens') # Сброс скринов
            renpy.show('daytime') # Базовый фон
            player.incEnergy(-randf(2,5)) #расход энергии
            resetStats(allChars) #Сброс статов
            updateEffects(allChars) #Сброс статов
            player.checkDur() # Удаление использованных предметов
            resetVars() # Сброс переменных
            checkTriggers(where) # Проверка переменных квестов
            
            moveChars(where) #Размещение крестьян на локации
            
            changetime(rand(1, 3)) #изменение времени
            if where[:4] == 'loc_' and 'tech' not in getLoc(where).position: #Если локация - локация и если она не техническая
                checkDeath() # проверка на смерть
                if where != curloc and 'self' not in getLoc(where).position:
                    prevloc = curloc
                    curloc = where
                    same_loc = 0
                else:
                    same_loc = 1
                if 'self' not in getLoc(where).position:
                    renpy.show_screen('stats_screen') #При перемещении всегда появляется интерфейс
                    renpy.show_screen('locationChars') #При перемещении всегда появляется интерфейс
                tempLoc = getLoc(where)
                checkUnconscious(tempLoc) # потеря сознания
                checkDrunk(tempLoc) # потеря сознания

            if rand(1,100) < 10 and lastEventTime + 40 < mtime: # Если на локации кто-то есть и локация поменялась, дёргаем эвент по рандому
                tryEvent(where) # попытка дёрнуть рандомный эвент с локации. Ожидание не даёт эвентов.
                
            renpy.retain_after_load() # чтобы сохранялся интерфейс, иначе ошибка
            
            if  where[:4] == 'loc_': trySpecialEvent(where) # спец эвент
            if len(args) > 0:
                changetime(args[0])
                player.incEnergy(-randf(args[0],args[0]*2))

            renpy.jump(where) #Переход на локу
        else:
            renpy.jump('loc_home')

    def resetVars():
        global waitRequest
        currPotion = defaultPotion
        last_stage = 'stage1'
        usedIngredients[:] = []
        # failedIngredients[:] = []
        if waitRequest != None:
            if waitRequest.values()[0] + 120 < mtime:
                waitRequest = None
                        
#Просто дёргает всех людей и сбрасывает выделющиеся статы
    def resetStats(input):
        player.inventory.sort(key=lambda x: x.name)
        for x in input:
            x.normalize()
            for y in x.effects:
                y.normalize()
        if player.hasEffect('faith'):
            player.setMaxMana(100 + player.getEffect('faith').strength)
        player.normalize()
        for x in player.effects:
            x.normalize()
        for x in player.skills:
            player.skills[x] = min(max(player.skills[x], 0),100)
                

#Вызов эвента
    def tryEvent(location):
        global noEventTime, mtime, lastEventTime, same_loc
        tempEv = []
        if lt() != 1:
            location += 'Night'
        for x in locations: #перебираем локи и ищем подходящие эвенты
            if x.id == location:
                for event in x.events:
                    if event.corr <= player.getCorr():
                        tempEv.append(event)

        if len(tempEv) > 0:
            # renpy.hide_screen('stats_screen')
            clrscr()
            callEvent = choice(tempEv).id
            lastEventTime = mtime #запоминаем время
            noEventTime = 0 # Сбрасываем переменную "время без эвентов"
            renpy.jump(callEvent) #эвент
        # else:
            # move(curloc)

    def trySpecialEvent(location):
        if len(getLoc(location).qwests) > 0:
            qArr = []
            for q in getLoc(location).qwests:
                if q.done == False:
                    qArr.append(q)
            if len(qArr) > 0:
                renpy.jump(choice(qArr).id)
 
# бессознательное состояние
    def checkUnconscious(location):
        if player.getEnergy() < 10 and rand(1,3) == 1:
            if 'safe' in location.position:
                renpy.jump('sleep')
            else:
                renpy.jump('unconscious')
                
    def checkDrunk(location):
        if player.getEnergy() < 400 and rand(1,3) == 1 and player.hasEffect(intoxication):
            if player.getEffect(intoxication).strength > 50:
                if 'safe' in location.position:
                    renpy.jump('sleep')
                else:
                    renpy.jump('drunk')
             
    def checkDeath():
        if player.getPrana() <= 0:
            renpy.jump('death')
            
    def updateEffects(chars):
        for char in chars:
            if char.hasEffect('hungerCure') == False: #Если мы не сыты, значит голодны
                char.applyEffects({hunger:0})
                
            for effect in char.effects:
                if char.hasEffect('spellBreaker'): # Если чаролом, сносим эффект, если он не сам чаролом
                    if effect.id not in ['hunger','hungerCure','faith','spellBreaker']:
                        char.effects.remove(effect)
                        
    def checkTriggers(where):
        global hour, aaronWeekly, trigger
        if trigger[20] == 3 and aaronWeekly == 0 and hour > 20:
            aaronWeekly = 1
            tryEvent('loc_aaronSex')
        if trigger[20] == 8 and where == 'loc_home' and lt() == 0 and weekday == 1 and trigger[49] == 0:
            renpy.jump('saraCome')
        
        if where == 'loc_smith' and trigger[41] == 1:
            renpy.jump('koven1smith')
            
        if where == 'loc_smith' and trigger[41] == 4:
            renpy.jump('koven1smith1')
            
        if where == 'loc_smith' and trigger[41] == 23 and trigger[43] + 24 < ptime:
            renpy.jump('koven1smith2')
            
        if where == 'loc_hotSprings' and trigger[41] == 10 and trigger[42] == 0:
            renpy.jump('koven1tent1')
            
        if where == ('loc_smith') and trigger[41] == 12 and trigger[43] + 24 < ptime:
            renpy.jump('koven1tent3')
            
        if where == ('loc_village') and trigger[41] == 20 and trigger[43] + 24 < ptime and lt() == 1:
            renpy.jump('koven1whore2')
            
        if where == ('loc_village') and trigger[44] == 1 and trigger[43] + 15 < ptime and lt() == 1:
            renpy.jump('koven1whoreFail')

        if where == ('loc_forest') and trigger[45] == 1 and lt() == 1 and rand(1,3) == 1:
            renpy.jump('koven1bandit1')
            
        if where == ('loc_cave') and trigger[45] == 2:
            renpy.jump('koven1bandit2')
            
        if where == 'loc_hotSprings' and player.hasItem(boots.name) == False:
            renpy.jump('hotSpringsNoBoots')
            
        if where == 'loc_hills' and player.hasItem(furArmor.name) == False:
            renpy.jump('hillsNoFur')
            
        if where == 'loc_cellar' and trigger[26] == 0 and player.hasElexir(impotenceCure):
            renpy.jump('horsePower')
            
        if where == 'loc_village' and trigger[29] == 2 and trigger[30] + 3 < ptime:
            renpy.jump('whoreAsk')
            
        if where == 'loc_village' and trigger[39] == 1 and lt() == 0 and weekday == 7:
            renpy.jump('ghostSearch')
            
    def moveChars(location):
        for x in slaves:
            x.location = ''
            if rand(1, 100) < getLoc(location).base_prob:
                x.location = location
                        

                
                
                