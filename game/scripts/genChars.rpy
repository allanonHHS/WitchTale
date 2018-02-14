init -10 python:
    config.use_cpickle = True
    dynpicto = ''
    

init -2 python:
    #объявление массивов
    picto_m = []
    picto_mOld = []
    picto_f = []
    picto_fOld = []

    # Загружаем все имеющиеся картинки
    import os
    for path in config.searchpath:
        # Ищем каталоги с картинками во всех возможных RenPy каталогах ресурсов
        try:
            for x in os.listdir(os.path.join(path, 'images/picto/male/')):
                picto_m.append(os.path.join('images/picto/male/', x))
                
            for x in os.listdir(os.path.join(path, 'images/picto/maleOld/')):
                picto_mOld.append(os.path.join('images/picto/maleOld/', x))
                
            for x in os.listdir(os.path.join(path, 'images/picto/female/')):
                picto_f.append(os.path.join('images/picto/female/', x))
                
            for x in os.listdir(os.path.join(path, 'images/picto/femaleOld/')):
                picto_fOld.append(os.path.join('images/picto/femaleOld/', x))

        except OSError:
            pass
            
    def genChars(amount):
        tempArr = []
        for x in range(0,amount):
            if rand(1,2) == 1:
                sex = 'male'
                tempCharBody = MaleBody(rand(160,180))
            else:
                sex = 'female'
                tempCharBody = FemaleBody(rand(170,190))
                
            tempCharStats = Stats(
                corr = randf(0,100),
                lust = randf(0,100),
                prana = randf(10,100),
                mana = randf(0,100),
                loyalty = randf(-10,10),
                energy = 1000,
                beauty = randf(0,100),
                fun = 50.0,
                maxlust = 100,
                maxmana = 100
            )
            if weightChoice(ageDistribution) == 'young':
                age = rand(25,35)
            else:
                age = rand(45,60)
            
            if sex == 'male':
                fname = choice(Char.maleNames)
                lname = weightChoice(Char.maleLastNames)
                color = "#79AEE8"
                if age < 40:
                    picto = choice(picto_m)
                else:
                    picto = choice(picto_mOld)
            else:
                fname = choice(Char.femaleNames)
                lname = weightChoice(Char.femaleLastNames)
                color = '#D98EE4'
                if age < 40:
                    picto = choice(picto_f)
                else:
                    picto = choice(picto_fOld)
                
            tempChar = Char(
                fname = fname,
                lname = lname,
                age = age,
                body = tempCharBody,
                stats = tempCharStats,
                color = color,
                inventory = [],
                wear = [],
                picto = picto,
                location = curloc,
                money = 100,
                skills = {
                    'interaction':0,
                    'interactTime':0, 
                    'health':rand(10,100),
                    'will':rand(0,100)
                    },
                friends = [],
                enemies = []
            )
            tempArr.append(tempChar)
        return tempArr
        
    def genFriends(tempArr):
        for x in tempArr:
            rnd = rand(0,10)
            for y in range(0,rnd):
                x.friends.append(choice(tempArr))
                
            rnd = rand(0,10)
            for y in range(0,rnd):
                x.enemies.append(choice(tempArr))
                
            x.friends = list(set(x.friends))
            x.enemies = list(set(x.enemies))
        return tempArr
            
    def genFriendsNewchar(char, tempArr):
        rnd = rand(0,10)
        for y in range(0,rnd):
            char.friends.append(choice(tempArr))
            
        rnd = rand(0,10)
        for y in range(0,rnd):
            char.enemies.append(choice(tempArr))
            
        char.friends = list(set(char.friends))
        char.enemies = list(set(char.enemies))
        return char

            
    

label skipall:
    python:
#####################################################
#Создание директора
#####################################################
        playerBody = FemaleBody(175)
        playerBody.parts['грудь'].size = 3
        playerBody.parts['анус'].size = 0
        playerBody.parts['вагина'].size = 0

        playerStats = Stats(
            corr = 0.0,
            lust = 0.0,
            prana = 100.0,
            energy = 1000,
            beauty = 70,
            fun = 50.0,
            mana = 100.0,
            maxlust = 100,
            maxmana = 100
        )

        player = Char(
            fname = 'Вальда',
            lname = 'Сибель',
            age = 20,
            body = playerBody,
            stats = playerStats,
            color = '#EE6A38',
            inventory = [],
            wear = [],
            picto = 'images/picto/gg.png',
            location = curloc,
            money = 100,
            skills = {'alchemy':20,'harvesting':20,'succubus':0,'empathy':30}
        )
        if development == 1:
            for x in allItems:
                for y in range(0,10):
                    player.addItem(x)
            for x in range(1,50):
                player.addItem(meatChickenCooked)
            player.skills = {'alchemy':100,'harvesting':100,'succubus':0,'empathy':100}
        else:
            for x in range(0,10):
                player.addItem(meatChickenCooked)
                player.addItem(spiritus)
                for y in ingForest:
                    player.addItem(y)
                for y in ingHills:
                    player.addItem(y)
                for y in ingHot:
                    player.addItem(y)
                for y in ingHunter:
                    player.addItem(y)
                    
        maleBody = MaleBody(180)
        konradStats = Stats(
            corr = 80,
            lust = 0,
            prana = 100,
            energy = 1000,
            beauty = 30,
            fun = 50.0,
            mana = 0.0,
            maxlust = 150
        )
        konrad = Char(
            fname = 'Конрад',
            lname = 'Трактирщик',
            age = 45,
            body = maleBody,
            stats = konradStats,
            color = '#77E47E',
            inventory = [],
            wear = [],
            picto = 'images/picto/konrad.png',
            location = curloc,
            money = 1000,
            skills = {}
        )
        
        maleBody = MaleBody(165)
        aaronStats = Stats(
            corr = 80,
            lust = 0,
            prana = 100,
            energy = 1000,
            beauty = 30,
            fun = 50.0,
            mana = 0.0,
            maxlust = 150
        )
        aaron = Char(
            fname = 'Аарон',
            lname = 'Иудей',
            age = 35,
            body = maleBody,
            stats = aaronStats,
            color = '#77E47E',
            inventory = [],
            wear = [],
            picto = 'images/picto/aaron.png',
            location = curloc,
            money = 1000,
            skills = {}
        )
        
        maleBody = MaleBody(160)
        ottoStats = Stats(
            corr = 50,
            lust = 0,
            prana = 120,
            energy = 1000,
            beauty = 50,
            fun = 50.0,
            mana = 0.0,
            maxlust = 120
        )
        otto = Char(
            fname = 'Отто',
            lname = 'Кузнец',
            age = 30,
            body = maleBody,
            stats = ottoStats,
            color = '#77E47E',
            inventory = [],
            wear = [],
            picto = 'images/picto/otto.png',
            location = curloc,
            money = 1000,
            skills = {}
        )  
            
        maleBody = MaleBody(180)
        ottoStats = Stats(
            corr = 50,
            lust = 0,
            prana = 120,
            energy = 1000,
            beauty = 50,
            fun = 50.0,
            mana = 0.0,
            maxlust = 120
        )
        
        oldman = Char(
            fname = 'Старик',
            lname = 'Рыбак',
            age = 70,
            body = maleBody,
            stats = ottoStats,
            color = '#77E47E',
            inventory = [],
            wear = [],
            picto = 'images/picto/oldman.png',
            location = curloc,
            money = 1000,
            skills = {}
        )
        
        maleBody = MaleBody(170)
        fransStats = Stats(
            corr = 90,
            lust = 0,
            prana = 90,
            energy = 1000,
            beauty = 80,
            fun = 50.0,
            mana = 0.0,
            maxlust = 200
        )
        
        frans = Char(
            fname = 'Франс',
            lname = 'Плотник',
            age = 35,
            body = maleBody,
            stats = fransStats,
            color = '#77E47E',
            inventory = [],
            wear = [],
            picto = 'images/picto/frans.png',
            location = curloc,
            money = 1000,
            skills = {}
        ) 
        
        helmaBody = FemaleBody(175)

        helmaStats = Stats(
            corr = 0.0,
            lust = 0.0,
            prana = 100.0,
            energy = 1000,
            beauty = 70,
            fun = 50.0,
            mana = 0.0,
            maxlust = 100
        )

        helma = Char(
            fname = 'Хельма',
            lname = 'Селянка',
            age = 20,
            body = helmaBody,
            stats = helmaStats,
            color = '#D98EE4',
            inventory = [],
            wear = [],
            picto = 'images/picto/helma.png',
            location = curloc,
            money = 100,
            skills = {}
        )
        
        saraBody = FemaleBody(175)
        saraStats = Stats(
            corr = 0.0,
            lust = 0.0,
            prana = 100.0,
            energy = 1000,
            beauty = 70,
            fun = 50.0,
            mana = 0.0,
            maxlust = 100
        )

        sara = Char(
            fname = 'Сара',
            lname = 'Иудейка',
            age = 20,
            body = saraBody,
            stats = saraStats,
            color = '#D98EE4',
            inventory = [],
            wear = [],
            picto = 'images/picto/sara.png',
            location = curloc,
            money = 100,
            skills = {}
        )
        
        whoreStats = Stats(
            corr = 100.0,
            lust = 0.0,
            prana = 100.0,
            energy = 1000,
            beauty = 70,
            fun = 50.0,
            mana = 0.0,
            maxlust = 100
        )

        whore = Char(
            fname = 'Хуре',
            lname = 'Шлюха',
            age = 30,
            body = saraBody,
            stats = whoreStats,
            color = '#D98EE4',
            inventory = [],
            wear = [],
            picto = 'images/picto/whore.png',
            location = curloc,
            money = 100,
            skills = {}
        ) 
     
# endBlc
#######################################################
#Пересохранение этого добра для того, чтобы сохранялось.
#######################################################
    python:
        trigger = []
        for x in range(0,1000):
            trigger.append(0)
        slaves = genChars(100)
        special = []
        # allChars = []
        special.append(konrad)
        special.append(otto)
        special.append(oldman)
        special.append(helma)
        special.append(frans)
        special.append(aaron)
        special.append(sara)
        special.append(whore)
        
        slaves = genFriends(slaves)
        special = genFriends(slaves)
        
        allChars = copy.copy(slaves)
        allChars.append(player)
        allChars += special
        if development == 0:
            renpy.jump('myintro')
        else:
            move('loc_home')
        # move('loc_home')
