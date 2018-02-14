init python:
    ingForest = []
    ingHills = []
    ingHot = []
    ingHunter = []
    
    whiteRot = Ingredient(
    effects = {intoxicationCure:5, godWillCure:20, poison:50}
    )
    whiteRot.name = 'Белая гниль'
    whiteRot.id = 'whiteRot'
    whiteRot.durability = 1
    whiteRot.picto = "images/items/whiteRot.png"
    whiteRot.type = 'ingredient'
    allItems.append(whiteRot)
    ingForest.append(whiteRot)

    mushroom = Ingredient(
    effects = {diareaCure:5, concentration:5, poisonCure:15}
    )
    mushroom.name = 'Белый гриб'
    mushroom.id = 'mushroom'
    mushroom.durability = 1
    mushroom.picto = "images/items/mushroom.png"
    mushroom.type = 'ingredient'
    allItems.append(mushroom)
    ingForest.append(mushroom)

    vagExtract = Ingredient(
    effects = {fertility:10, love:10, regenerationCure:5, concentrationCure:5}
    )
    vagExtract.name = 'Вагинальный экстракт'
    vagExtract.id = 'vagExtract'
    vagExtract.durability = 1
    vagExtract.picto = "images/items/vagExtract.png"
    vagExtract.type = 'ingredient'
    allItems.append(vagExtract)

    heatherFruit = Ingredient(
    effects = {etheral:5, poison:5}
    )
    heatherFruit.name = 'Вересковый плод'
    heatherFruit.id = 'heatherFruit'
    heatherFruit.durability = 1
    heatherFruit.picto = "images/items/heatherFruit.png"
    heatherFruit.type = 'ingredient'
    allItems.append(heatherFruit)
    ingHot.append(heatherFruit)

    wolfEye = Ingredient(
    effects = {fertilityCure:20, boost:10, boostCure:2, impotenceCure:5}
    )
    wolfEye.name = 'Волчий глаз'
    wolfEye.id = 'wolfEye'
    wolfEye.durability = 1
    wolfEye.picto = "images/items/wolfEye.png"
    wolfEye.type = 'ingredient'
    allItems.append(wolfEye)
    ingHunter.append(wolfEye)
    
    blueGrape = Ingredient(
    effects = {diarea:5, godWillCure:5, impotence:15}
    )
    blueGrape.name = 'Голубой виноград'
    blueGrape.id = 'blueGrape'
    blueGrape.durability = 1
    blueGrape.picto = "images/items/blueGrape.png"
    blueGrape.type = 'ingredient'
    allItems.append(blueGrape)
    ingForest.append(blueGrape)
    
    smokeResin = Ingredient(
    effects = {spellBreakerCure:20, regenerationCure:5}
    )
    smokeResin.name = 'Дымящаяся смола'
    smokeResin.id = 'smokeResin'
    smokeResin.durability = 1
    smokeResin.picto = "images/items/smokeResin.png"
    smokeResin.type = 'ingredient'
    allItems.append(smokeResin)
    ingHot.append(smokeResin)

    greenMoss = Ingredient(
    effects = {intoxicationCure:5, concentration:5, poisonCure:10}
    )
    greenMoss.name = 'Зелёный мох'
    greenMoss.id = 'greenMoss'
    greenMoss.durability = 1
    greenMoss.picto = "images/items/greenMoss.png"
    greenMoss.type = 'ingredient'
    allItems.append(greenMoss)
    ingHills.append(greenMoss)

    godAsh = Ingredient(
    effects = {bleedingCure:20, poisonCure:20}
    )
    godAsh.name = 'Зола бога'
    godAsh.id = 'godAsh'
    godAsh.durability = 1
    godAsh.picto = "images/items/godAsh.png"
    godAsh.type = 'ingredient'
    allItems.append(godAsh)
    ingHot.append(godAsh)

    rootAcacia = Ingredient(
    effects = {regeneration:15, poison:5, impotence:5}
    )
    rootAcacia.name = 'Корень акации'
    rootAcacia.id = 'rootAcacia'
    rootAcacia.durability = 1
    rootAcacia.picto = "images/items/rootAcacia.png"
    rootAcacia.type = 'ingredient'
    allItems.append(rootAcacia)
    ingHot.append(rootAcacia)

    rootRafflesia = Ingredient(
    effects = {diarea:15, etheralCure:5}
    )
    rootRafflesia.name = 'Корень раффлезии'
    rootRafflesia.id = 'rootRafflesia'
    rootRafflesia.durability = 1
    rootRafflesia.picto = "images/items/rootRafflesia.png"
    rootRafflesia.type = 'ingredient'
    allItems.append(rootRafflesia)
    ingForest.append(rootRafflesia)

    rootKennel = Ingredient(
    effects = {diareaCure:20, bleeding:5, concentrationCure:15}
    )
    rootKennel.name = 'Корень собачайника'
    rootKennel.id = 'rootKennel'
    rootKennel.durability = 1
    rootKennel.picto = "images/items/rootKennel.png"
    rootKennel.type = 'ingredient'
    allItems.append(rootKennel)
    ingHills.append(rootKennel)

    redVine = Ingredient(
    effects = {bleedingCure:15, regeneration:5}
    )
    redVine.name = 'Красная лоза'
    redVine.id = 'redVine'
    redVine.durability = 1
    redVine.picto = "images/items/redVine.png"
    redVine.type = 'ingredient'
    allItems.append(redVine)
    ingHot.append(redVine)

    bloodSlug = Ingredient(
    effects = {regenerationCure:20, etheralCure:10, poison:5}
    )
    bloodSlug.name = 'Кровь слизняка'
    bloodSlug.id = 'bloodSlug'
    bloodSlug.durability = 1
    bloodSlug.picto = "images/items/bloodSlug.png"
    bloodSlug.type = 'ingredient'
    allItems.append(bloodSlug)
    ingForest.append(bloodSlug)
    

    wingBlueMessenger = Ingredient(
    effects = {love:10, godWillCure:10}
    )
    wingBlueMessenger.name = 'Крыло голубого вестника'
    wingBlueMessenger.id = 'wingBlueMessenger'
    wingBlueMessenger.durability = 1
    wingBlueMessenger.picto = "images/items/wingBlueMessenger.png"
    wingBlueMessenger.type = 'ingredient'
    allItems.append(wingBlueMessenger)
    ingHills.append(wingBlueMessenger)

    wingNightMoth = Ingredient(
    effects = {etheralCure:20, boostCure:5, poison:5}
    )
    wingNightMoth.name = 'Крыло ночного мотылька'
    wingNightMoth.id = 'wingNightMoth'
    wingNightMoth.durability = 1
    wingNightMoth.picto = "images/items/wingNightMoth.png"
    wingNightMoth.type = 'ingredient'
    allItems.append(wingNightMoth)
    ingForest.append(wingNightMoth)

    wingTizania = Ingredient(
    effects = {intoxicationCure:10, spellBreaker:2, poisonCure:5}
    )
    wingTizania.name = 'Крыло тизании'
    wingTizania.id = 'wingTizania'
    wingTizania.durability = 1
    wingTizania.picto = "images/items/wingTizania.png"
    wingTizania.type = 'ingredient'
    allItems.append(wingTizania)
    ingHot.append(wingTizania)

    iceMountFlower = Ingredient(
    effects = {bleeding:10, etheral:5}
    )
    iceMountFlower.name = 'Ледяной горноцвет'
    iceMountFlower.id = 'iceMountFlower'
    iceMountFlower.durability = 1
    iceMountFlower.picto = "images/items/iceMountFlower.png"
    iceMountFlower.type = 'ingredient'
    allItems.append(iceMountFlower)
    ingHills.append(iceMountFlower)

    purpleMultiFlower = Ingredient(
    effects = {diareaCure:5, regenerationCure:15, poison:5}
    )
    purpleMultiFlower.name = 'Лиловый многоцвет'
    purpleMultiFlower.id = 'purpleMultiFlower'
    purpleMultiFlower.durability = 1
    purpleMultiFlower.picto = "images/items/purpleMultiFlower.png"
    purpleMultiFlower.type = 'ingredient'
    allItems.append(purpleMultiFlower)
    ingForest.append(purpleMultiFlower)

    shimmeringBell = Ingredient(
    effects = {bleeding:20, etheral:10, poison:15}
    )
    shimmeringBell.name = 'Мерцающий колокольчик'
    shimmeringBell.id = 'shimmeringBell'
    shimmeringBell.durability = 1
    shimmeringBell.picto = "images/items/shimmeringBell.png"
    shimmeringBell.type = 'ingredient'
    allItems.append(shimmeringBell)
    ingHills.append(shimmeringBell)

    amanita = Ingredient(
    effects = {intoxication:80, poison:20}
    )
    amanita.name = 'Мухомор'
    amanita.id = 'amanita'
    amanita.durability = 1
    amanita.picto = "images/items/amanita.png"
    amanita.type = 'ingredient'
    allItems.append(amanita)
    ingForest.append(amanita)

    dandelion = Ingredient(
    effects = {fertility:5, impotenceCure:1}
    )
    dandelion.name = 'Надуванчик'
    dandelion.id = 'dandelion'
    dandelion.durability = 1
    dandelion.picto = "images/items/dandelion.png"
    dandelion.type = 'ingredient'
    allItems.append(dandelion)
    ingForest.append(dandelion)

    featherStork = Ingredient(
    effects = {fertility:15, bleeding:5, boost:10}
    )
    featherStork.name = 'Перья аиста'
    featherStork.id = 'featherStork'
    featherStork.durability = 1
    featherStork.picto = "images/items/featherStork.png"
    featherStork.type = 'ingredient'
    allItems.append(featherStork)
    ingHunter.append(featherStork)

    featherCrow = Ingredient(
    effects = {fertilityCure:15}
    )
    featherCrow.name = 'Перья ворона'
    featherCrow.id = 'featherCrow'
    featherCrow.durability = 1
    featherCrow.picto = "images/items/featherCrow.png"
    featherCrow.type = 'ingredient'
    allItems.append(featherCrow)
    ingHunter.append(featherCrow)
    
    featherEagle = Ingredient(
    effects = {regenerationCure:5, godWill:15, boost:10}
    )
    featherEagle.name = 'Перья орла'
    featherEagle.id = 'featherEagle'
    featherEagle.durability = 1
    featherEagle.picto = "images/items/featherEagle.png"
    featherEagle.type = 'ingredient'
    allItems.append(featherEagle)
    ingHunter.append(featherEagle)

    CockEar = Ingredient(
    effects = {bleeding:5, boostCure:15}
    )
    CockEar.name = 'Петушиные ушки'
    CockEar.id = 'CockEar'
    CockEar.durability = 1
    CockEar.picto = "images/items/CockEar.png"
    CockEar.type = 'ingredient'
    allItems.append(CockEar)
    ingForest.append(CockEar)

    rowan = Ingredient(
    effects = {diareaCure:10, regeneration:5, boost:5}
    )
    rowan.name = 'Рябина'
    rowan.id = 'rowan'
    rowan.durability = 1
    rowan.picto = "images/items/rowan.png"
    rowan.type = 'ingredient'
    allItems.append(rowan)
    ingForest.append(rowan)

    seedsBlackTop = Ingredient(
    effects = {loveCure:15, godWill:20, concentration:10}
    )
    seedsBlackTop.name = 'Семена чернотопника'
    seedsBlackTop.id = 'seedsBlackTop'
    seedsBlackTop.durability = 1
    seedsBlackTop.picto = "images/items/seedsBlackTop.png"
    seedsBlackTop.type = 'ingredient'
    allItems.append(seedsBlackTop)
    ingHot.append(seedsBlackTop)

    heartDemon = Ingredient(
    effects = {intoxication:70, spellBreaker:50, regeneration:55, boost:50, impotenceCure:50}
    )
    heartDemon.name = 'Сердце демона'
    heartDemon.id = 'heartDemon'
    heartDemon.durability = 1
    heartDemon.picto = "images/items/heartDemon.png"
    heartDemon.type = 'ingredient'
    allItems.append(heartDemon)

    heartHuman = Ingredient(
    effects = {intoxication:10, spellBreaker:10, regeneration:25, boost:15, impotenceCure:25}
    )
    heartHuman.name = 'Сердце человека'
    heartHuman.id = 'heartHuman'
    heartHuman.durability = 1
    heartHuman.picto = "images/items/heartHuman.png"
    heartHuman.type = 'ingredient'
    allItems.append(heartHuman)

    silverFish = Ingredient(
    effects = {fertilityCure:5, loveCure:15, regeneration:15, poisonCure:15}
    )
    silverFish.name = 'Серебрянная рыбка'
    silverFish.id = 'silverFish'
    silverFish.durability = 1
    silverFish.picto = "images/items/silverFish.png"
    silverFish.type = 'ingredient'
    allItems.append(silverFish)
    ingHunter.append(silverFish)

    bluePollen = Ingredient(
    effects = {etheral:20}
    )
    bluePollen.name = 'Синяя пыльца'
    bluePollen.id = 'bluePollen'
    bluePollen.durability = 1
    bluePollen.picto = "images/items/bluePollen.png"
    bluePollen.type = 'ingredient'
    allItems.append(bluePollen)
    ingHills.append(bluePollen)

    iceTooth = Ingredient(
    effects = {spellBreaker:15, etheralCure:15, boostCure:20}
    )
    iceTooth.name = 'Снежный зуб'
    iceTooth.id = 'iceTooth'
    iceTooth.durability = 1
    iceTooth.picto = "images/items/iceTooth.png"
    iceTooth.type = 'ingredient'
    allItems.append(iceTooth)
    ingHills.append(iceTooth)

    honeyComb = Ingredient(
    effects = {diarea:10, bleedingCure:10}
    )
    honeyComb.name = 'Соты'
    honeyComb.id = 'honeyComb'
    honeyComb.durability = 1
    honeyComb.picto = "images/items/honeyComb.png"
    honeyComb.type = 'ingredient'
    allItems.append(honeyComb)
    ingForest.append(honeyComb)

    flowerThistle = Ingredient(
    effects = {loveCure:10, boostCure:10, poison:10}
    )
    flowerThistle.name = 'Соцветие чертополоха'
    flowerThistle.id = 'flowerThistle'
    flowerThistle.durability = 1
    flowerThistle.picto = "images/items/flowerThistle.png"
    flowerThistle.type = 'ingredient'
    allItems.append(flowerThistle)
    ingForest.append(flowerThistle)

    semen = Ingredient(
    effects = {fertility:10, loveCure:5, godWill:5}
    )
    semen.name = 'Сперма'
    semen.id = 'semen'
    semen.durability = 1
    semen.picto = "images/items/semen.png"
    semen.type = 'ingredient'
    allItems.append(semen)

    ginacia = Ingredient(
    effects = {intoxication:5, bleeding:15, poison:5}
    )
    ginacia.name = 'Споровая сумка гинации'
    ginacia.id = 'ginacia'
    ginacia.durability = 1
    ginacia.picto = "images/items/ginacia.png"
    ginacia.type = 'ingredient'
    allItems.append(ginacia)
    ingHot.append(ginacia)

    flowerFaslin = Ingredient(
    effects = {love:5, spellBreakerCure:5}
    )
    flowerFaslin.name = 'Цветок фаслины'
    flowerFaslin.id = 'flowerFaslin'
    flowerFaslin.durability = 1
    flowerFaslin.picto = "images/items/flowerFaslin.png"
    flowerFaslin.type = 'ingredient'
    allItems.append(flowerFaslin)
    ingForest.append(flowerFaslin)

    flowerLichen = Ingredient(
    effects = {fertilityCure:10, regeneration:10}
    )
    flowerLichen.name = 'Цветы лишайника'
    flowerLichen.id = 'flowerLichen'
    flowerLichen.durability = 1
    flowerLichen.picto = "images/items/flowerLichen.png"
    flowerLichen.type = 'ingredient'
    allItems.append(flowerLichen)
    ingHills.append(flowerLichen)

    blackloe = Ingredient(
    effects = {bleedingCure:10, poison:10}
    )
    blackloe.name = 'Чёрлоэ'
    blackloe.id = 'blackloe'
    blackloe.durability = 1
    blackloe.picto = "images/items/blackloe.png"
    blackloe.type = 'ingredient'
    allItems.append(blackloe)
    ingHot.append(blackloe)

    scaleLatimeria = Ingredient(
    effects = {intoxicationCure:15, godWillCure:5}
    )
    scaleLatimeria.name = 'Чешуя латимерии'
    scaleLatimeria.id = 'scaleLatimeria'
    scaleLatimeria.durability = 1
    scaleLatimeria.picto = "images/items/scaleLatimeria.png"
    scaleLatimeria.type = 'ingredient'
    allItems.append(scaleLatimeria)
    ingHunter.append(scaleLatimeria)

    ectoplasm = Ingredient(
    effects = {loveCure:20, spellBreaker:5, etheral:50}
    )
    ectoplasm.name = 'Эктоплазма'
    ectoplasm.id = 'ectoplasm'
    ectoplasm.durability = 1
    ectoplasm.picto = "images/items/ectoplasm.png"
    ectoplasm.type = 'ingredient'
    allItems.append(ectoplasm)

    poisonMultiFlower = Ingredient(
    effects = {spellBreakerCure:10, poison:40, poisonCure:5}
    )
    poisonMultiFlower.name = 'Ядовитый многоцвет'
    poisonMultiFlower.id = 'poisonMultiFlower'
    poisonMultiFlower.durability = 1
    poisonMultiFlower.picto = "images/items/poisonMultiFlower.png"
    poisonMultiFlower.type = 'ingredient'
    allItems.append(poisonMultiFlower)
    ingForest.append(poisonMultiFlower)

    eggCaper = Ingredient(
    effects = {love:15, godWill:10}
    )
    eggCaper.name = 'Яйцо глухаря'
    eggCaper.id = 'eggCaper'
    eggCaper.durability = 1
    eggCaper.picto = "images/items/eggCaper.png"
    eggCaper.type = 'ingredient'
    allItems.append(eggCaper)
    ingForest.append(eggCaper)