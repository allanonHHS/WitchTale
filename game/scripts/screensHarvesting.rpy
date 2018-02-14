screen harvesting:
    python:
        tab_cols = 5
        tab_rows = 1 + int(player.getSkill('harvesting')/20)
    
    hbox:
        key "game_menu" action Function(move, curloc)
        textbutton 'Назад (Esc)' action [Function(move, curloc)]
        # textbutton 'Собрать всё видимое' action [Function(harvestAll),Show('harvesting')]
        
    vbox xalign 0.99 yalign 0.0:
        $ currtime = gettime('day')
        # text '[currtime]' style style.param
        if minute < 10:
            $ temtime = '%s:0%s' % (hour, minute)
        else:
            $ temtime = '%s:%s' % (hour, minute)
        text '[currtime] [temtime]' style style.description xalign 0.99
        
    fixed xpos 0.3 ypos 0.15 xmaximum 550:
        frame:
            grid tab_cols tab_rows:
                xfill True
                spacing 10
                for x in range(0, tab_cols*tab_rows):
                    # $ selection = selectionArr[x]
                    $ item = itemSelection[x]
                    if selectionArr[x] <= 5:
                        if x not in addedItem:
                            # $ visibleItem.append(x)
                            imagebutton:
                                    idle im.MatrixColor(im.FactorScale(item.picto,0.5), im.matrix.opacity(0.9))
                                    hover im.MatrixColor(im.FactorScale(item.picto,0.5), im.matrix.opacity(1.0))
                                    action getHarvestAction(x, item, 'easy')
                        else:
                            null
                    elif selectionArr[x] <= 9:
                        if x not in visibleItem:
                            imagebutton:
                                idle im.MatrixColor('images/mine_yellow.png', im.matrix.opacity(0.9))
                                hover im.MatrixColor('images/mine_yellow.png', im.matrix.opacity(1.0))
                                action selectAction(x, 5)
                        else:
                            if x not in addedItem:
                                imagebutton:
                                        idle im.MatrixColor(im.FactorScale(item.picto,0.5), im.matrix.opacity(0.9))
                                        hover im.MatrixColor(im.FactorScale(item.picto,0.5), im.matrix.opacity(1.0))
                                        action getHarvestAction(x, item, 'medium')
                            else:
                                null
                    else:
                        if x not in visibleItem:
                            imagebutton:
                                idle im.MatrixColor('images/mine_red.png', im.matrix.opacity(0.9))
                                hover im.MatrixColor('images/mine_red.png', im.matrix.opacity(1.0))
                                action selectAction(x, 15)
                        else:
                            if x not in addedItem:
                                imagebutton:
                                        idle im.MatrixColor(im.FactorScale(item.picto,0.5), im.matrix.opacity(0.9))
                                        hover im.MatrixColor(im.FactorScale(item.picto,0.5), im.matrix.opacity(1.0))
                                        action getHarvestAction(x, item, 'hard')
                            else:
                                null

screen harvestingFail:
    tag harvestingResult
    zorder 1
    modal False
    frame xpos 0.5 ypos 0.05 xanchor 0.5 yanchor 0.5:
        vbox:
            text('Я испортила ингредиент, пытаясь добыть его.')
            if showIncSkill == 1:
                $ temp = player.getSkill('harvesting')
                text('Но я учла свою ошибку и увеличила навык собирательства до [temp]!')
    # Тут пауза!
            # with pause(5)
    # on "show" action Hide("brewingFail")
                
screen harvestingSuccess(item):
    tag harvestingResult
    zorder 1
    modal False
    frame xpos 0.5 ypos 0.05 xanchor 0.5 yanchor 0.5:
        vbox:
            $ temp = item.name
            text('Я добыла ингредиент [temp]!')

label harvestingFail:
    $ showIncSkill = 0
    show screen harvesting
    if rand(0, player.getSkill('harvesting')) < 5:
        $ temp = player.getSkill('harvesting')
        $ player.incSkill('harvesting')
        $ showIncSkill = 1
    show screen harvestingFail
    if len(addedItem) == (1 + int(player.getSkill('harvesting')/20))*5:
        $ move(curloc)
    pause 2.0
    hide screen harvestingFail
    call screen harvesting
    
label harvestingSuccess:
    show screen harvesting
    show screen harvestingSuccess(harvested)
    if len(addedItem) == (1 + int(player.getSkill('harvesting')/20))*5:
        $ move(curloc)
    pause 2.0
    hide screen harvestingSuccess
    call screen harvesting
    
label initHarvest:
    $ clrscr()
    $ visibleItem = []
    $ addedItem  = []
    $ selectionArr = []
    $ itemSelection = []
    $ preRandom = []
    $ harvested = ''
    if curloc == 'loc_forest':
        show forest
    elif curloc == 'loc_hills':
        show hills
    elif curloc == 'loc_hotSprings':
        show hotSprings
    python:
        global selectionArr, curloc
        for x in range(0,100):
            selectionArr.append(rand(0,10))
            if curloc == 'loc_forest':
                itemSelection.append(choice(ingForest))
            elif curloc == 'loc_hills':
                itemSelection.append(choice(ingHills))
            elif curloc == 'loc_hotSprings':
                itemSelection.append(choice(ingHot))
            preRandom.append(rand(0,40))
    call screen harvesting
    
init python:
    def getHarvestAction(x, item, difficulty):
        global preRandom
        if difficulty == 'easy':
            if player.getSkill('harvesting') < preRandom[x]:
                return [Function(changetime,10), AddToSet(addedItem, x), Jump('harvestingFail')]
            else:
                return [Function(changetime,10), Function(player.addItemAmount, item, 1), AddToSet(addedItem, x), SetVariable('harvested', item), Jump('harvestingSuccess')]
                
        elif difficulty == 'medium':
            if player.getSkill('harvesting') < preRandom[x] + 20:
                return [Function(changetime,10), AddToSet(addedItem, x), Jump('harvestingFail')]
            else:
                return [Function(changetime,10), Function(player.addItemAmount, item, 5), AddToSet(addedItem, x), SetVariable('harvested', item), Jump('harvestingSuccess')]
                
        elif difficulty == 'hard':
            if player.getSkill('harvesting') < preRandom[x] + 50:
                return [Function(changetime,10), AddToSet(addedItem, x), Jump('harvestingFail')]
            else:
                return [Function(changetime,10), Function(player.addItemAmount, item, 15), AddToSet(addedItem, x), SetVariable('harvested', item), Jump('harvestingSuccess')]
                
    def selectAction(x, chance):
        global visibleItem
        if rand(1,100) > chance:
            return [AddToSet(visibleItem, x), Show('harvesting')]
        else:
            if curloc == 'loc_forest':
                return [AddToSet(visibleItem, x), Function(tryEvent, 'loc_harvestingForest')]
            elif curloc == 'loc_hills':
                return [AddToSet(visibleItem, x), Function(tryEvent, 'loc_harvestingHills')]
            elif curloc == 'loc_hotSprings':
                return [AddToSet(visibleItem, x), Function(tryEvent, 'loc_harvestinghotSprings')]
                
        
    def harvestAll():
        global visibleItem, addedItem, itemSelection
        tab_cols = 5
        tab_rows = 1 + int(player.getSkill('harvesting')/20)
        for x in range(0, tab_cols*tab_rows):
            if x in visibleItem and x not in addedItem:
                player.addItemAmount(itemSelection[x], 1)
                addedItem.append(x)