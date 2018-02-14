# Вы можете расположить сценарий своей игры в этом файле.

# Объявляйте изображения здесь, используя оператор image.
# например, image eileen happy = "eileen_happy.png"


init -3 python: 
    development = 1 #Режим разработчика
    point = 0
    disclamer_speak = 0
    last_eat = 0 # Инициализация времени с последнего обеда
    noEventTime = 0 # Время без эвентов
    reaction = '' # Инициализация реакции
    curloc = 'loc_home' # Инициализация стартовой локации
    stat_loy = 0
    waitRequest = None
    ageDistribution = {'young':80,'old':20}
    last_sleeped = -99
    currRequest = ''
    filteredEffect = ''
    lastUsed = []
    aaronAssortiment = []
    strengthAdj = 25
    empathyAdj = 0
    # currPotion = defaultPotion # Инициализация пустой бутылки
    aaronWeekly = 0 #Еженедельный секс с Аароном
    infusionMod = 10
    newPos = 1
    globalArr = []
    globalChange = []
    soldItems = []
    
# Определение персонажей игры.   
init:
    image white = "#FFFFFF"
    define me = Character("Злая Вальда", who_color="#9E0002", show_side_image = im.Scale("images/picto/me.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define father = Character("Отец", who_color="#79AEE8")
    define man = Character("Парень", who_color="#79AEE8")
    define merc = Character("Наёмник", who_color="#79AEE8")
    define perv = Character("Извращенец", who_color="#79AEE8")
    define witch = Character("Старушка", who_color="#E8E1E0")
    define deflower = Character("Фридрих", who_color="#E8E1E0")
    define drinker = Character("Пьяница", who_color="#E8E1E0")
    define guard1 = Character("Стражник 1", who_color="#E8E1E0", show_side_image = im.Scale("images/picto/guard.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define guard2 = Character("Стражник 2", who_color="#E8E1E0", show_side_image = im.Scale("images/picto/guard.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define guard3 = Character("Стражница", who_color="#E8E1E0", show_side_image = im.Scale("images/picto/guard.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define girl = Character("Девочка", who_color="#E8E1E0", show_side_image = im.Scale("images/picto/girl.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define boy = Character("Мальчик", who_color="#79AEE8", show_side_image = im.Scale("images/picto/boy.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define incubus = Character("Инкуб", who_color="#9e0601", show_side_image = im.Scale("images/picto/incub.png",160, 160, xalign=0.0, yalign= 1.0), window_left_padding = 170)
    define band1 = Character("Старый бандит", who_color="#79AEE8")
    define band2 = Character("Молодой разбойник", who_color="#79AEE8")
    define leader = Character("Главарь", who_color="#79AEE8")
    #9e0601

# Игра начинается здесь.
label start:
    show white
    python:
        for x in locations:
            if x.name == 'UNKNOWN':
                renpy.say('CREATOR','WRONG LOCATION! ADD TO LOCATIONS LIST! LABEL = [x.id]. LOOK IN locations.rpy AT TOP!')
    jump disclaimer
    
label after_load:
    python:
        for x in allChars:
            for effect in x.effects:
                for newEffect in allEffects:
                    if effect.id == newEffect.id:
                        effect =  newEffect
                        
            for item in x.inventory:
                if item.type in ['food','ingredient']:
                    for effect in item.effects:
                        for newEffect in allEffects:
                            if effect.id == newEffect.id:
                                item.effects[newEffect] =  item.effects.pop(effect)
                                
        if isinstance(currRequest, Request):
            for x in allEffects:
                if currRequest.effect.keys()[0].id == x:
                    currRequest.effect[x] =  currRequest.effect.pop(currRequest.effect.keys()[0])
                    
        if waitRequest != None:
            waitRequest = {currRequest:waitRequest.values()[0]}
        # player.skills['empathy'] = max(30, player.skills['empathy'])
    return

    
# А тут, как всегда, моды и команды, которые я нашёл, но ещё не поюзал:
# http://www.nexusmods.com/skyrim/mods/10870/? - Puppeteer Master - говно
# setav mood 2 (0-7)
# http://www.nexusmods.com/skyrim/mods/42626/? - Must have for me!!!
# http://www.nexusmods.com/skyrim/mods/21491/?
# http://www.nexusmods.com/skyrim/mods/77396/? - Particle Field by Keung 
# http://www.nexusmods.com/skyrim/mods/72039/? - head
# http://www.nexusmods.com/skyrim/mods/2812/? - beter females
# http://www.nexusmods.com/skyrim/mods/74638/? - better cities
# http://www.nexusmods.com/skyrim/mods/71054/? - Bijin NPC
# http://www.nexusmods.com/skyrim/mods/61995/?

# http://www.nexusmods.com/skyrim/mods/75861/? - uunp armor
# Посмотреть, что там с OSA за плюшки.
# http://www.nexusmods.com/skyrim/mods/65146/ - robes
# http://www.nexusmods.com/skyrim/mods/63581/? - hagraven outfit
# http://www.nexusmods.com/skyrim/mods/63473/? - bijin wifes
# http://www.nexusmods.com/skyrim/mods/63353/? - rustic children
# http://www.nexusmods.com/skyrim/mods/60475/? - peeing
# http://www.nexusmods.com/skyrim/mods/60625/? - wenches
# http://www.nexusmods.com/skyrim/mods/59451/? - thief armor
# http://www.nexusmods.com/skyrim/mods/59048/? - idle animatons
# http://www.nexusmods.com/skyrim/mods/57959/? - riverwood
# http://www.nexusmods.com/skyrim/mods/57693/? - pregnant
# http://www.nexusmods.com/skyrim/mods/57371/? - house
# http://www.nexusmods.com/skyrim/mods/55924/? - unp armor
# http://www.nexusmods.com/skyrim/mods/55568/? - ndh animations run/walk

#http://www.loverslab.com/files/file/1255-ill-take-the-display-model/ - zaz poser

# 105 поза - просьба
# 154 - 
# 397 - chains
# 3884 - метла
# 3574 - плавание