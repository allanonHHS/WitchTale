init 10 python:
    locations = []
    global loc_btn, loc_txt
    loc_btn = []
    loc_txt = []
    class Location:
        def __init__(self, id, name, base_prob, position):
            self.id = id
            self.name = name
            self.base_prob = base_prob
            self.events = []
            self.qwests = []
            self.position = position
            self.items = []
            self.__statuses = []

        def getprob(self):
            global hour
            rez = self.base_prob # Иначе настоящая вероятность
            return rez

        def __repr__(self):
            return '<{} name: "{}">'.format(self.__class__.__name__,
                                            self.__name__('utf-8'))

        def getPeople(self):
            rez = []
            for x in allChars:
                try:
                    if x.getLocation().id==self.id:
                        rez.append(x)
                except AttributeError:
                    pass
            return rez

        def getItems(self):
            rez = []
            for x in self.items:
                rez.append(x)
            return rez

    class Event:
        def __init__(self,id,corr):
            self.id = id
            self.corr = corr

    class Qwest:
        def __init__(self,id):
            self.id = id
            self.done = False

    def getLoc(id):
        for x in locations:
            if x.id == id:
                return x
        return False

    def getQwest(id):
        for loc in locations:
            for qwest in loc.qwests:
                if qwest.id == id:
                    return qwest
        return False

# Функция добавления эвентов в локации
    def getEvents():
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'event_': # находим тот, что с евентом
                locEventId = eventLabel.split("_")[2]
                for location in locations: # начинаем перебирать локации
                    locPureId = location.id.split("_")[1]
                    if locEventId == locPureId: # Если имя локации содержится в имени эвента
                        index = eventLabel.rfind(location.id) # находим правый индекс имени локации
                        corr = eventLabel[index:] # режем по нему
                        temp = corr.split("_") # разбиваем строку по_
                        corr = int(temp[2]) # находим развратность
                        event = Event(id = eventLabel, corr = corr) # создаём эвент
                        location.events.append(event) # добавляем его в массив эвентов локации
        return 0

    def getQwests():
        for eventLabel in _locs: # перебираем все лейблы
            if eventLabel[:6] == 'qwest_': # находим тот, что с квестом
                for location in locations: # начинаем перебирать локации
                    if eventLabel.find(location.id) > 0: # Если имя локации содержится в имени эвента
                        qwest = Qwest(id = eventLabel) # создаём эвент
                        qwests = []
                        for q in location.qwests:
                            qwests.append(q.id)
                        if qwest.id not in qwests:
                            location.qwests.append(qwest) # добавляем его в массив эвентов локации
        return 0
    _locs = renpy.get_all_labels()
    
# Создание массива всех локаций
    def genLocs():
        for x in _locs:
            if x[:4] == 'loc_':
                if x == 'loc_home': loc = Location(id = x, name = 'дом', base_prob = -1, position = ['home','safe'])
                elif x == 'loc_cellar': loc = Location(id = x, name = 'подвал', base_prob = -1, position = ['home','safe'])
                elif x == 'loc_village': loc = Location(id = x, name = 'хутор', base_prob = 10, position = ['city'])
                elif x == 'loc_tavern': loc = Location(id = x, name = 'трактир', base_prob = 5, position = ['city'])
                elif x == 'loc_smith': loc = Location(id = x, name = 'кузнец', base_prob = 2, position = ['city'])
                elif x == 'loc_carpenter': loc = Location(id = x, name = 'плотник', base_prob = -1, position = ['city'])
                elif x == 'loc_shop': loc = Location(id = x, name = 'лавка', base_prob = 2, position = ['city'])
                
                elif x == 'loc_forest': loc = Location(id = x, name = 'лес', base_prob = -1, position = ['outside'])
                elif x == 'loc_hotSprings': loc = Location(id = x, name = 'чёртовы озёра', base_prob = -1, position = ['outside'])
                elif x == 'loc_river': loc = Location(id = x, name = 'река', base_prob = 5, position = ['outside'])
                elif x == 'loc_hills': loc = Location(id = x, name = 'горы', base_prob = -1, position = ['outside'])
                
                elif x == 'loc_harvestingForest': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_dreams': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_swim': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_swimNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_harvestingHills': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_harvestinghotSprings': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_villageNight': loc = Location(id = x, name = '', base_prob = 1, position = ['city'])
                elif x == 'loc_smithNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_carpenterNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_shopNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_forestNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_hotSpringsNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_riverNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_hillsNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_aaronSex': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_houses': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_housesNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_heromancyMale': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_heromancyFemale': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_mastur': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_masturNight': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_baseInteractM': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                elif x == 'loc_baseInteractF': loc = Location(id = x, name = '', base_prob = -1, position = ['tech'])
                
                elif x == 'loc_cave': loc = Location(id = x, name = '', base_prob = -1, position = ['outside'])
                else: loc = Location(id = x, name = 'UNKNOWN', base_prob = -1, position = ['other'])
                locations.append(loc)

    genLocs() # генерирую локации
    getEvents() # добавляю всем эвенты
    getQwests() # добавляю квесты
    
######################################################
# Объявление всех картинок локаций
init:
    image village = ConditionSwitch(
        "hour >= 5 and hour < 9", "images/locations/village_m.png",
        "hour >= 9 and hour < 17", "images/locations/village_d.png",
        "hour >= 17 and hour < 22", "images/locations/village_m.png",
        "hour >= 22 or hour < 5", "images/locations/village_n.png"
        )
    image cellar = 'images/locations/cellar.png'
    image home = ConditionSwitch(
        "hour >= 5 and hour < 9", "images/locations/home_m.png",
        "hour >= 9 and hour < 17", "images/locations/home_d.png",
        "hour >= 17 and hour < 22", "images/locations/home_m.png",
        "hour >= 22 or hour < 5", "images/locations/home_n.png"
        )
    image forest = ConditionSwitch(
        "hour >= 5 and hour < 9", "images/locations/forest_m.png",
        "hour >= 9 and hour < 17", "images/locations/forest_d.png",
        "hour >= 17 and hour < 22", "images/locations/forest_m.png",
        "hour >= 22 or hour < 5", "images/locations/forest_n.png"
        )
    image hotSprings = ConditionSwitch(
        "hour >= 5 and hour < 9", "images/locations/hotSprings_m.png",
        "hour >= 9 and hour < 17", "images/locations/hotSprings_d.png",
        "hour >= 17 and hour < 22", "images/locations/hotSprings_m.png",
        "hour >= 22 or hour < 5", "images/locations/hotSprings_n.png"
        )
    image river = ConditionSwitch(
        "hour >= 5 and hour < 9", "images/locations/river_m.png",
        "hour >= 9 and hour < 17", "images/locations/river_d.png",
        "hour >= 17 and hour < 22", "images/locations/river_m.png",
        "hour >= 22 or hour < 5", "images/locations/river_n.png"
        )
    image hills = ConditionSwitch(
        "hour >= 5 and hour < 9", "images/locations/hills_m.png",
        "hour >= 9 and hour < 17", "images/locations/hills_d.png",
        "hour >= 17 and hour < 22", "images/locations/hills_m.png",
        "hour >= 22 or hour < 5", "images/locations/hills_n.png"
        )
        
    image tavern = "images/locations/tavern.png"
    image smith = "images/locations/smith.png"
    image carpenter = "images/locations/carpenter.png"
    image shop = "images/locations/shop.png"
    image cave = "images/locations/cave.png"
        
    image movie = Movie(size=(1440, 810), xpos=0.5, ypos=0, xanchor=0.5, yanchor=0)

##############################################################
# Home
##############################################################

label loc_home:
    # if ptime == 0:
        # $ ptime += 1
        # $ move ('intro')
    show home
    python:
        loc_btn = [
            ('Подвал', Function(move, 'loc_cellar'), True),
            ('Река', Function(move, 'loc_river', 10), True),
            ('Хутор', Function(move, 'loc_village', 30), True),
            ('Лес', Function(move, 'loc_forest', 20), True),
            ('{i}Спать{/i}', Jump('sleep'), ((ptime - last_sleeped >= 4) or (player.getEnergy() < 200))),
            ('{i}Мастурбировать{/i}', Jump('masturbation'), (player.getLust() > 80 and lt() != 1)),
            ('{i}Принять селянина{/i}', [Function(clrscr),Jump('getRequest')], (waitRequest == None and lt() == 1 and rand(1,10) > 5))
            ]
        loc_txt = ['Ваш дом. Он довольно скромно обставлен, но для начинающей сельской ведьмы это неудивительно. Важно лишь то, что вам есть где поспать и на чём приготовить свои снадобья. Остальное, безусловно, приложится.']
    screen home:
        fixed:
            if development == 1:
                textbutton 'Test':
                    xalign 0.0 yalign 0.2
                    action [Function(clrscr), Show('sellScreen')]
        if waitRequest != None:
            frame xpos 0.0 ypos 0.7:
                vbox:
                    $ char = waitRequest.keys()[0].char
                    text _('Вас ждёт [char.fname]') style style.my_text
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(char.picto,0.9), im.matrix.opacity(0.9))
                        hover im.MatrixColor(im.FactorScale(char.picto,0.9), im.matrix.opacity(1.0))
                        action Jump('getRequest')
                    
    call screen home
    
label loc_cellar:
    show cellar
    python:
        loc_btn = [
            ('Домой', Function(move, 'loc_home'), True),
            ('{i}Варить зелье{/i}', [SetVariable('last_stage','stage1'), Show('brewing')], True),
            ('{i}Вспоминать уроки{/i}', Jump('brewTutorial'), True)
            ]
        loc_txt = ['Подвал вашей избушки. Судя по каменным стенам, он появился здесь задолго до того, как избушка была построена. Здесь темновато, но это не помешает вам готовить свои снадобья и проводить некоторые ритуалы.']
    screen cellar:
        null
    call screen cellar
    
label loc_village:
    show village
    python:
        loc_btn = [
            ('Домой', Function(move, 'loc_home', 30), True),
            ('Река', Function(move, 'loc_river', 20), True),
            ('Таверна', Function(move, 'loc_tavern'), True),
            ('Кузнец', Function(move, 'loc_smith'), (lt() == 1)),
            ('Плотник', Jump('speakFransSmith'), (lt() == 1 and trigger[14] + 10 < ptime)),
            ('Лавка', Function(move, 'loc_shop'), (lt() == 1)),
            ('{i}Подойти к гуляке{/i}', Jump('tavernDrinker'), (math.fabs(getPar(slaves, 'loy')) <= 20 and trigger[2] == 1 and lt() == 1)),
            ('{i}Гадать у таверны{/i}', Jump('heromancy'), lt() == 1),
            ('{i}Проникнуть в хату{/i}',  Function(tryEvent, 'loc_houses'), (player.hasElexir(etheral)))
            ]
        loc_txt = ['Хутор, рядом с которым вы поселились. У него по сути нет собственного названия. Местные называют его просто хутор, а приезжие Флюссхоф, что и переводится как хутор на реке. Подобных хуторов по всей стране не сосчитать.']
        loc_txt += ['Здесь есть лавка торговца, кузнец, портной и много крестьянских домов. Именно эти люди являются вашими основными посетителями.']
    screen village:
        null
    call screen village

label loc_shop:
    if trigger[21] + 24 > ptime:
        $ clrscr()
        jump laterAaron
    if trigger[20] == 5 and trigger[21] + 24 < ptime:
        $ clrscr()
        jump speakAaron
    show shop
    python:
        loc_btn = [
            ('Назад', Function(move, 'loc_village'), True),
            ('{i}Поговорить{/i}', [Function(clrscr), Jump('speakAaron')], True)
            ]
        loc_txt = ['Лавка Аарона Иудея. Или ломбард. Или ростовщическая контора. Или всё это вместе взятое. Непонятно, почему её до сих пор не сжёг Святой Официум, но почему-то не сжёг. Видимо тоже должны.']
        loc_txt += ['Тут можно прикупить всякий скарб и разные ингредиенты. Ассортимент каждый день меняется.']
    screen shop:
        null
    call screen shop
    
label loc_carpenter:
    show carpenter
    if trigger[13] < 3:
        $ clrscr()
        jump speakFransSmith
    python:
        loc_btn = [
            ('Назад', Function(move, 'loc_village'), True),
            ('{i}Поговорить{/i}', [Function(clrscr), Jump('speakFrans')], True)
            ]
        loc_txt = ['Местный плотник. У него нет определённого дома, где он занимается своими плотницкими делами, он просто перемещается со всеми инструментами по деревне и делает свою работу. Каждый раз его приходится подолгу искать.']
    screen carpenter:
        null
    call screen carpenter
    
label loc_smith:
    show smith
    python:
        loc_btn = [
            ('Назад', Function(move, 'loc_village'), True),
            ('{i}Поговорить{/i}', [Function(clrscr), Jump('speakOtto')], True)
            ]
        loc_txt = ['Кузница кузнеца, что кузнечит в своей кузнечной кузне. Честно, я не особо разбираюсь, что он там делает с этими кузнечными штуками.']
        loc_txt += ['Даже не знаю, чем он может быть мне полезен.']
    screen smith:
        null
    call screen smith
    
label loc_tavern:
    show tavern
    python:
        loc_btn = [
            ('Назад', Function(move, 'loc_village'), True),
            ('{i}К трактирщику{/i}', [Function(clrscr), Jump('speakKonrad')], True),
            ('{i}К шлюхе{/i}', [Function(clrscr), Jump('speakWhore')], (trigger[29] == 3 and player.hasElexir(fertilityCure))),
            ]
        loc_txt = ['Деревенская таверна. Всегда полна крестьян, что собираются уйти в поля, пришли с полей или просто не пошли сегодня на поля.']
        loc_txt += ['Здесь можно купить спиртное и еды.']
    screen tavern:
        null
    call screen tavern
    
label loc_forest:
    show forest
    python:
        loc_btn = [
            ('Домой', Function(move, 'loc_home', 20), True),
            ('Чёртовы озёра', Function(move, 'loc_hotSprings', 20), True),
            ('Белые горы', Function(move, 'loc_hills', 40), True),
            ('{i}Собирать ингредиенты{/i}', Jump('initHarvest'), True),
            ('{i}Искать место силы{/i}', Jump('koven1end'), trigger[40] == 2 and lt() == 0)
            ]
        loc_txt = ['Тихий лес с берёзками. Он не очень густой и довольно красивый, но жители деревни всё равно редко заходят сюда.']
        loc_txt += ['Если я пойду на восток, то окажусь у чёртовых озёр. На западе лежат белые горы.']
    screen forest:
        null
    call screen forest
    
label loc_hotSprings:
    show hotSprings
    if trigger[16] == 0:
        $ trigger[16] = 1
        jump hotSpringsBoots
            
    python:
        loc_btn = [
            ('Домой', Function(move, 'loc_home', 20), True),
            ('Лес', Function(move, 'loc_forest', 20), True),
            ('Логово разбойников', Function(move, 'loc_cave', 20),  trigger[45] >= 2),
            ('{i}Корни акации{/i}', Jump('koven1tent1'), trigger[42] == 1),
            ('{i}Собирать ингредиенты{/i}', Jump('initHarvest'), True)
            ]
        loc_txt = ['Передо мной Чёртовы Озёра. Земля пышет жаром, а в воздухе пахнет серой. От многочисленных озёр поднимается пар.']
        loc_txt += ['Отсюда я могу спуститься напрямую к дому, либо отправиться обратно в лес.']
    screen hotSprings:
        null
    call screen hotSprings
    
label loc_hills:
    show hills
    python:
        loc_btn = [
            ('Лес', Function(move, 'loc_forest', 20), True),
            ('{i}Собирать ингредиенты{/i}', Jump('initHarvest'), True)
            ]
        loc_txt = ['Белые Горы. Даже не поднимаясь сюда, совершенно очевидно, что у первооткрывателя не было никакой фантазии.']
        loc_txt += ['Это горы, и они действительно белые.']
    screen hills:
        null
    call screen hills
    
label loc_river:
    show river
    python:
        loc_btn = [
            ('Домой', Function(move, 'loc_home', 10), True),
            ('Хутор', Function(move, 'loc_village', 20), True),
            ('{i}Купаться{/i}', Jump('wash'), True),
            ('{i}Медитировать{/i}', Jump('meditation'), True),
            ('{i}Набрать воды{/i}', [Function(player.addItem, water), Function(changetime, 30), Function(move, curloc)], True),
            ('{i}Подойти к рыбаку{/i}', Jump('fisher'), rand(1,5) == 1 and lt() == 1)
            ]
        loc_txt = ['Река на которой стоит хутор, до которого ещё 20 минут. Сюда можно придти помедитировать или искупаться.']
        loc_txt += ['Здесь часто можно встретить деревенских рыбаков.']
    screen river:
        null
    call screen river
    
label loc_cave:
    show cave
    python:
        loc_btn = [
            ('Чёртовы озёра', Function(move, 'loc_hotSprings', 20), True),
            ('{i}Торговать{/i}', [Function(clrscr), Show('sellScreen')] , True)
            ]
        loc_txt = ['Логово бандитов в пещере. Не надо быть большого ума, чтобы понять, чем они занимаются.']
        loc_txt += ['Работорговля, контрабанда, разбой. И что я тут забыла?']
    screen river:
        null
    call screen river
    
label test:
    # python:
        # startTime = time.time()
        # testArray = []
        # for x in range(1,100000):
            # testArray[:] = []
            # for y in range(1,200):
                # testArray.append(y)
        # endtime = time.time() - startTime
    # 'Готово! [endtime] секунд!'
    # $ visibleItem = []
    # $ addedItem  = []
    # $ selectionArr = []
    # $ itemSelection = []
    # $ preRandom = []
    # $ harvested = ''
    # python:
        # global selectionArr
        # for x in range(0,100):
            # selectionArr.append(rand(0,10))
            # itemSelection.append(choice(ingForest))
            # preRandom.append(rand(0,40))
    # call screen harvesting
    # jump harvestingFail
    $ clrscr()
    # call screen showPeople
    # jump konradBuy
    python:
        currRequest = copy.copy(choice(allRequests))
        currRequest.char = getChar(currRequest.sex)
        if currRequest.patient == True:
            if currRequest.align == 'bad' and currRequest.char.getEnemy(currRequest.patientSex) != False:
                currRequest.patient = currRequest.char.getEnemy(currRequest.patientSex)
            elif currRequest.align == 'good' and currRequest.char.getFriend(currRequest.patientSex) != False:
                currRequest.patient = currRequest.char.getFriend(currRequest.patientSex)
            else:
                currRequest.patient = getChar(currRequest.patientSex)
    jump requestSperm
    
# label loc_baseLocation:
    # show expression '[location_pic]' as bg
    # screen baseLocation:
        # textbutton _('Вверх'):
                    # action[Function(move, location1)]
        # textbutton _('Вниз'):
                    # action[Function(move, location2)]
        # textbutton _('Влево'):
                    # action[Function(move, location3)]
        # textbutton _('Вправо'):
                    # action[Function(move, location4)]
        # text '[location_desription]'
    # call screen baseLocation
    
# python -1:
    # def move(location):
        # И вот тут мы меняем переменные location1, location2, location3, location4, location_pic и location_desription
        # А потом просто выполняем джамп на базовую локацию
        # renpy.jump('loc_baseLocation')
        
    
    
############################################################################################
#tech Locations
############################################################################################
label loc_harvestingForest:
    jump loc_home
label loc_harvestingHills:
    jump loc_home
label loc_harvestinghotSprings:
    jump loc_home
label loc_swim:
    jump loc_home
label loc_swimNight:
    jump loc_home
label loc_villageNight:
    jump loc_home
label loc_smithNight:
    jump loc_home
label loc_carpenterNight:
    jump loc_home
label loc_shopNight:
    jump loc_home
label loc_forestNight:
    jump loc_home
label loc_hotSpringsNight:
    jump loc_home
label loc_riverNight:
    jump loc_home
label loc_hillsNight:
    jump loc_home
label loc_aaronSex:
    jump loc_home
label loc_houses:
    jump loc_home
label loc_housesNight:
    jump loc_home
label loc_mastur:
    jump loc_home
label loc_masturNight:
    jump loc_home
label loc_heromancyMale:
    jump loc_home
label loc_heromancyFemale:
    jump loc_home
label loc_baseInteractM:
    jump loc_home
label loc_baseInteractF:
    jump loc_home