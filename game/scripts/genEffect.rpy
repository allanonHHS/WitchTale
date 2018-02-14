init -1 python:
    allEffects = []
    randomEffects = []
    
    noEffect = Effect(
    name = 'Пустой эффект', 
    id = 'noEffect', 
    increment = 0,
    type = 'effect',
    description = '')
    
    hunger = Effect(
    name = 'Голод', 
    id = 'hunger',
    increment = 0.7, 
    type = 'effect',
    description = 'Степень недостатка пищи для организма. Чем выше, тем больше отрицательных эффектов.')
    allEffects.append(hunger)
    
    hungerCure = Effect(
    name = 'Сытость', 
    id = 'hungerCure', 
    increment = -2,
    type = 'effect',
    description = 'Величина насыщения организма едой. Чем выше, тем больше положительных эффектов.')
    allEffects.append(hungerCure)

    diarea = Effect(
    name = 'Диарея',
    id = 'diarea', 
    increment = -1,
    type = 'illness',
    description = 'Исторжение почти не переваренной пищи. Усиливает голод.')
    allEffects.append(diarea)
    randomEffects.append(diarea)
    
    diareaCure = Effect(
    name = 'Запор',
    id = 'diareaCure', 
    increment = -100,
    type = 'illness',
    description = 'Невозможность вывести отходы организма. Снижает желание и увеличивает усталость.')
    allEffects.append(diareaCure)
    randomEffects.append(diareaCure)
    
    intoxication = Effect(
    name = 'Опьянение',
    id = 'intoxication', 
    increment = -10,
    type = 'illness',
    description = 'Увеличивает настроение, но уменьшает связь с Изнанкой и усиливает голод.')
    allEffects.append(intoxication)
    randomEffects.append(intoxication)
    
    intoxicationCure = Effect(
    name = 'Ясность',
    id = 'intoxicationCure', 
    increment = -25,
    type = 'illness',
    description = 'Усиливает связь с изнанкой, но отрицательно сказывается на настроении.')
    allEffects.append(intoxicationCure)
    
    fertility = Effect(
    name = 'Фертильность',
    id = 'fertility', 
    increment = -1,
    type = 'illness',
    description = 'Увеличивает шанс забеременеть. Увеличивает возбуждение.')
    allEffects.append(fertility)
    randomEffects.append(fertility)
    
    fertilityCure = Effect(
    name = 'Бесплодие',
    id = 'fertilityCure', 
    increment = 0,
    type = 'illness',
    description = 'Уменьшает шанс забеременеть. Снижает желание.')
    allEffects.append(fertilityCure)
    randomEffects.append(fertilityCure)
    
    love = Effect(
    name = 'Приворот',
    id = 'love', 
    increment = -0.6,
    type = 'illness',
    description = 'Вызывает чувство влюблённости и желания')
    allEffects.append(love)
    
    loveCure = Effect(
    name = 'Отворот',
    id = 'loveCure', 
    increment = -0.6,
    type = 'illness',
    description = 'Уменьшает влюблённость и желание')
    allEffects.append(loveCure)
    randomEffects.append(loveCure)
    
    bleeding = Effect(
    name = 'Кровотечение',
    id = 'bleeding', 
    increment = -3,
    type = 'illness',
    description = 'Медленно убивает персонажа.')
    allEffects.append(bleeding)
    randomEffects.append(bleeding)
    
    bleedingCure = Effect(
    name = 'Густокровие',
    id = 'bleedingCure', 
    increment = -3,
    type = 'illness',
    description = 'Сгущает кровь, останавливает кровотечение')
    allEffects.append(bleedingCure)
    
    spellBreaker = Effect(
    name = 'Чаролом',
    id = 'spellBreaker', 
    increment = -50,
    type = 'illness',
    description = 'Убирает все эффекты с существа')
    allEffects.append(spellBreaker)
    
    spellBreakerCure = Effect(
    name = 'Чароболь',
    id = 'spellBreakerCure', 
    increment = -25,
    type = 'illness',
    description = 'Усиливает все эффекты на существе')
    allEffects.append(spellBreakerCure)
    
    regeneration = Effect(
    name = 'Регенерация',
    id = 'regeneration', 
    increment = -2,
    type = 'illness',
    description = 'Медленно восстанавливает здоровье')
    allEffects.append(regeneration)
    
    regenerationCure = Effect(
    name = 'Увядание',
    id = 'regenerationCure', 
    increment = -2,
    type = 'illness',
    description = 'Медленно уменьшает здоровье, вплоть до летального исхода.')
    allEffects.append(regenerationCure)
    randomEffects.append(regenerationCure)
    
    godWill = Effect(
    name = 'Непреклонность',
    id = 'godWill', 
    increment = -10,
    type = 'illness',
    description = 'Увеличивает силу воли и притупляет чувства. Делает оргазм почти недостижимым.')
    allEffects.append(godWill)
    
    godWillCure = Effect(
    name = 'Безволие',
    id = 'godWillCure', 
    increment = -10,
    type = 'illness',
    description = 'Уменьшает силу воли и обостряет чувства. Делает оргазм легче.')
    allEffects.append(godWillCure)
    randomEffects.append(godWillCure)
    
    etheral = Effect(
    name = 'Бесплотность',
    id = 'etheral', 
    increment = -20,
    type = 'illness',
    description = 'Делает существо невидимым и неосязаемым.')
    allEffects.append(etheral)
    
    etheralCure = Effect(
    name = 'Проявление',
    id = 'etheralCure', 
    increment = -25,
    type = 'illness',
    description = 'Снимает эффект бесплотности. Позволяет призракам временно обрести вещественность.')
    allEffects.append(etheralCure)
    
    boost = Effect(
    name = 'Ускорение',
    id = 'boost', 
    increment = -20,
    type = 'illness',
    description = 'Ускоряет существо, субъективно замедляя для него время.')
    allEffects.append(boost)
    
    boostCure = Effect(
    name = 'Замедление',
    id = 'boostCure', 
    increment = -4,
    type = 'illness',
    description = 'Сильное замедление как восприятия, так и двигательной активности. Вплоть до паралича.')
    allEffects.append(boostCure)
    randomEffects.append(boostCure)
    
    concentration = Effect(
    name = 'Концентрация',
    id = 'concentration', 
    increment = -10,
    type = 'illness',
    description = 'Увеличивает концентрацию, обеспечивая глубокое слияние с Изнанкой.')
    allEffects.append(concentration)
    
    concentrationCure = Effect(
    name = 'Рассеянность',
    id = 'concentrationCure', 
    increment = -4,
    type = 'illness',
    description = 'Ослабляет концентрацию и расслабляет.')
    allEffects.append(concentrationCure)
    
    poison = Effect(
    name = 'Яд',
    id = 'poison', 
    increment = -11,
    type = 'illness',
    description = 'Стремительно уменьшает жизни.')
    allEffects.append(poison)
    randomEffects.append(poison)
    
    poisonCure = Effect(
    name = 'Антидот',
    id = 'poisonCure', 
    increment = -25,
    type = 'illness',
    description = 'Лечит яд и даёт иммунитет на время действия.')
    allEffects.append(poisonCure)
    
    impotence = Effect(
    name = 'Импотенция',
    id = 'impotence', 
    increment = 1,
    type = 'illness',
    description = 'Снижает желание мужчин. Не имеет задокументированного эффекта на женщинах')
    allEffects.append(impotence)
    randomEffects.append(impotence)
    
    impotenceCure = Effect(
    name = 'Лошадиная сила',
    id = 'impotenceCure',
    increment = -10,
    type = 'illness',
    description = 'Увеличивает мужскую силу. В высоких концентрациях оказывает на женщин странный эффект')
    allEffects.append(impotenceCure)
    
    faith = Effect(
    name = 'Вера в силу',
    id = 'faith', 
    increment = 0,
    type = 'illness',
    description = 'Вера крестьян в вашу силу. Увеличивает общее количество маны и скорость её регенерации.')
    allEffects.append(faith)
    
    faithCure = Effect(
    name = 'Неверие',
    id = 'faithCure',
    increment = 0,
    type = 'illness',
    description = 'Неверие крестьян в вас. Антипод веры.')
    allEffects.append(faithCure)