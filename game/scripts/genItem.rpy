init -1 python:
    allItems = []
    
    defaultPotion = Potion(
    mult = 0, 
    mainEffect = {}, 
    subEffects = {}
    )
    defaultPotion.name = 'Пуcтая бутылка'
    defaultPotion.id = 'defaultPotion'
    defaultPotion.durability = 1
    defaultPotion.picto = "images/items/defaultPotion.png"
    defaultPotion.type = 'hidden'
    # allItems.append(defaultPotion)
    currPotion = defaultPotion
    
    spiritus = Ingredient(
    effects = {intoxication:90, hunger:60}
    )
    spiritus.name = 'Чистый спирт'
    spiritus.id = 'spiritus'
    spiritus.durability = 1
    spiritus.picto = "images/items/spiritus.png"
    spiritus.type = 'food'
    allItems.append(spiritus)
    
    vodka = Ingredient(
    effects = {intoxication:40, hunger:30}
    )
    vodka.name = 'Водка'
    vodka.id = 'vodka'
    vodka.durability = 1
    vodka.picto = "images/items/vodka.png"
    vodka.type = 'food'
    allItems.append(vodka)
    
    wine = Ingredient(
    effects = {intoxication:20, hunger:10}
    )
    wine.name = 'Винишко'
    wine.id = 'wine'
    wine.durability = 1
    wine.picto = "images/items/wine.png"
    wine.type = 'food'
    allItems.append(wine)
    
    beer = Ingredient(
    effects = {intoxication:5, hunger:10}
    )
    beer.name = 'Пиво'
    beer.id = 'beer'
    beer.durability = 1
    beer.picto = "images/items/beer.png"
    beer.type = 'food'
    allItems.append(beer)
    
    water = Ingredient(
    effects = {intoxication:0.1, hunger:10}
    )
    water.name = 'Вода'
    water.id = 'beer'
    water.durability = 1
    water.picto = "images/items/water.png"
    water.type = 'food'
    allItems.append(water)
    
    meatChicken = Ingredient(
    effects = {hungerCure:10}
    )
    meatChicken.name = 'Куриное мясо'
    meatChicken.id = 'meatChicken'
    meatChicken.durability = 1
    meatChicken.picto = "images/items/meatChicken.png"
    meatChicken.type = 'food'
    # allItems.append(meatChicken)
    
    meatChickenCooked = Ingredient(
    effects = {hungerCure:40}
    )
    meatChickenCooked.name = 'Жаренная курица'
    meatChickenCooked.id = 'meatChickenCooked'
    meatChickenCooked.durability = 1
    meatChickenCooked.picto = "images/items/meatChickenCooked.png"
    meatChickenCooked.type = 'food'
    allItems.append(meatChickenCooked)
    
    wood = Ingredient(
    effects = {noEffect:0}
    )
    wood.name = 'Дрова'
    wood.id = 'wood'
    wood.durability = 1
    wood.picto = "images/items/wood.png"
    wood.type = 'catalizator'
    # allItems.append(wood)
    
    boots = Item(
        durability = 100,
        name = 'Подбитые металлом сапоги',
        id = 'boots',
        picto = "images/items/boots.png",
        type = 'clothing'
    )
    allItems.append(boots)
    
    furArmor = Item(
        durability = 100,
        name = 'Меховая одежда',
        id = 'furArmor',
        picto = "images/items/furArmor.png",
        type = 'clothing'
    )
    allItems.append(furArmor)
    
    specBottle = Item(
        durability = 100,
        name = 'Странная бутыль',
        id = 'specBottle',
        picto = "images/items/specBottle.png",
        type = 'tool'
    )
    allItems.append(specBottle)
    
    dildo = Item(
        durability = 100,
        name = 'Самотык',
        id = 'dildo',
        picto = "images/items/dildo.png",
        type = 'tool'
    )
    allItems.append(dildo)
    
    plane = Item(
        durability = 100,
        name = 'Рубанок',
        id = 'plane',
        picto = "images/items/plane.png",
        type = 'tool'
    )
    allItems.append(plane)
    
    stick = Item(
        durability = 100,
        name = 'Черенок',
        id = 'stick',
        picto = "images/items/stick.png",
        type = 'tool'
    )
    allItems.append(stick)
    
    tentacle = Item(
        durability = 100,
        name = 'Щупальце',
        id = 'tentacle',
        picto = "images/items/tentacle.png",
        type = 'tool'
    )
    allItems.append(tentacle)
    
    marion = Item(
        durability = 100,
        name = 'Корень Мариона',
        id = 'marion',
        picto = "images/items/marion.png",
        type = 'tool'
    )
    allItems.append(marion)
    
    horseJizz = Item(
        durability = 100,
        name = 'Конская сперма',
        id = 'horseJizz',
        picto = "images/items/horseJizz.png",
        type = 'tool'
    )
    allItems.append(horseJizz)
    
    broom = Item(
        durability = 100,
        name = 'Метла',
        id = 'broom',
        picto = "images/items/broom.png",
        type = 'tool'
    )
    allItems.append(broom)