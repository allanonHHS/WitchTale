##############################################################################
# кастомные скрины
##############################################################################
init python:
    import string
    myItem = 0
    mySet = []
    voteDecision = False
    last_inventory = 'all'
    def inv_show_list(type) :
        global myItem
        if not type in ['all','food','elixir']:
            type = 'all'
        list = []
        showed = []
        for x in player.inventory:
            if type == 'all' and not x.id in showed:
                list += [x]
                showed += [x.id]
            elif type == 'food' and not x.id in showed and x.type == 'food':
                list += [x]
                showed += [x.id]
            elif type == 'elixir' and x.type == 'food' and 'Зелье' in x.name:
                list += [x]
        if len(list) > 0 :
            if not myItem in list :
                myItem = list[0]
        else :
            myItem = 0        
        return list
        
    def inv_show_sell() :
        global aaronAssortiment, myItem
        list = []
        showed = []
        for x in aaronAssortiment:
            if not x.id in showed:
                list += [x]
                showed += [x.id]
        if len(list) > 0 :
            if not myItem in list :
                myItem = list[0]
        else :
            myItem = 0        
        return list
        
    def inv_action (item):
        if item.type in ['ingredient','food']:
            return [Function(player.applyEffects, item.effects), Function(player.FremoveItem, item)] 
            # return [Function(player.removeItem, item)]
        if item.id == 'tentacle' and trigger[41] == 11 and curloc == 'loc_village':
            return [Jump('koven1tent2')]
        return [NullAction()]
        
    def buy_action (item):
        if player.money >= 5:
            return [Function(player.addItem, item), Function(player.incMoney, -5), RemoveFromSet(aaronAssortiment, item)] 
        else:
            return [Jump('no_money')]

    def sell_action (item):
        global soldItems
        counter = 0
        for x in soldItems:
            if x.getEffect() == item.getEffect():
                counter += 1
        if counter < 10:
            return [Function(player.removeItem, item), Function(player.incMoney, int(item.getEffectStrength()/4)), AddToSet(soldItems, item)]
        else:
            return [Jump('no_more')]
            
    def getSellable(sellable):
        tempArr = []
        for x in player.inventory:
            for y in sellable:
                if y in x.name:
                    tempArr.append(x)
        return tempArr

        
##############################################################################
# Основной скрин статистики
##############################################################################
screen hoverStats:
    fixed xpos 0.22 ypos 0.001:
        vbox spacing 1:
            $ temp = int(player.getEnergy())
            text 'Энергия - [temp]' style style.effects 
            $ temp = int(player.getPrana())
            text 'Прана - [temp]' style style.effects 
            $ temp = int(player.getMana())
            text 'Мана - [temp]' style style.effects
            $ temp = int(player.getLust())
            text 'Возбуждение - [temp]' style style.effects
    vbox xalign 0.01 yalign 0.15:
        for effect in player.effects:
            text '[effect.name] : [effect.strength]' style style.effects
    
screen stats_screen:
    # tag interface
    # add 'images/overlay.png'
    # use locationChars
            
    fixed xpos 0.01 ypos 0.01:
        imagebutton:
            idle 'blankShowStats.png'
            hover 'blankShowStats.png'
            hovered [Show('hoverStats'), Hide('locationChars')]
            unhovered [Hide('hoverStats'), Show('locationChars')]
            action NullAction()
            
    fixed xpos 0.01 ypos 0.01:
        vbox xmaximum config.screen_width/2:
            
            $ temp = int(player.getEnergy())
            # if temp > 200:
                # text _('Ваша энергия: [temp]') style style.param
            # else:
                # text _('Ваша энергия: [temp]') style style.paramwarning
            bar value temp range 1000 xmaximum 300  style style.energyBar 
            bar value player.getPrana() range 100 xmaximum 300 style style.healthBar
            bar value player.getMana() range player.getMaxMana() xmaximum 300 style style.manaBar
            bar value player.getLust() range player.getMaxlust() xmaximum 300 style style.lustBar
            null height 10
            
            if player.isSperm() > 0:
                $ temp = player.printSperm()
                text _('В сперме [temp]') style style.paramwarning

            # Buttons
            hbox style style.myBox:
                if player.getSperm('лицо') == True:
                    imagebutton auto 'images/actions/face_%s.png' action Jump('cleanFace')
                if player.getSperm('рот') == True:
                    imagebutton auto 'images/actions/mouth_%s.png' action Jump('cleanMouth')
                if player.getSperm('грудь') == True:
                    imagebutton auto 'images/actions/body_%s.png' action Jump('cleanBody')
                if player.getSperm('руки') == True:
                    imagebutton auto 'images/actions/hands_%s.png' action Jump('cleanHands')
                if player.getSperm('ноги') == True:
                    imagebutton auto 'images/actions/feet_%s.png' action Jump('cleanFeet')
                if player.getSperm('вагина') == True:
                    imagebutton auto 'images/actions/pussy_%s.png' action Jump('cleanPussy')
                if player.getSperm('анус') == True:
                    imagebutton auto 'images/actions/ass_%s.png' action Jump('cleanAss')
                    
    vbox xalign 0.5:
        $ temp = getPar(slaves,'loy')
        # if temp > stat_loy:
            # text 'Лояльность жителей: [temp]' style style.paramgreen
        # elif temp < stat_loy:
            # text 'Лояльность жителей: [temp]' style style.paramwarning
        # else :
            # text 'Лояльность жителей: [temp]' style style.param
        # python:
            # stat_loy = temp
        text 'Лояльность жителей: [temp]' style style.description
        if player.countItem(meatChickenCooked.name) < 10:
            $ temp = player.countItem(meatChickenCooked.name)
            if player.countItem(meatChickenCooked.name) == 0:
                text 'У меня нет еды!' style style.normalRed
            else:
                text 'Осталось еды: [temp]' style style.description
        $ pranaWarn = ''
        if player.getPrana() < 80:
            $ pranaWarn = 'Мне нехорошо'
        if player.getPrana() < 50:
            $ pranaWarn = 'Мне плохо!'
        if player.getPrana() < 20:
            $ pranaWarn = 'Я УМИРАЮ!!!'
        text '[pranaWarn]' style style.normalRed
        
        

    vbox xalign 0.99 yalign 0.0:
        $ currtime = gettime('day')
        # text '[currtime]' style style.param
        if minute < 10:
            $ temtime = '%s:0%s' % (hour, minute)
        else:
            $ temtime = '%s:%s' % (hour, minute)
        text '[currtime] [temtime]' style style.description xalign 0.99
        null height 10
        # text '{u}Промотать:{/u}' style style.param xalign 0.99
        grid 2 1:
            xalign 0.99
            imagebutton auto 'images/actions/wait15_%s.png' action [Function(waiting,15)]
            imagebutton auto 'images/actions/wait60_%s.png' action [Function(waiting,60)]
        key "K_SPACE" action Function(waiting,15)
        # text '{u}Посмотреть:{/u}' style style.param xalign 0.99
        grid 2 1:         
            xalign 0.99
            imagebutton auto 'images/actions/journal_%s.png' action [Function(clrscr), Show('charInfo')]
            imagebutton auto 'images/actions/inventory_%s.png' action [Function(clrscr), Show('inventory_unit')]


        # text '{u}Действия:{/u}' style style.param xalign 0.99
        $counter = 0
        for lab, act, req in loc_btn :
            if req:
                $counter += 1
                if lab[:3] != '{i}':
                    textbutton lab + ' (' + str(counter) + ')':
                        xalign 0.99
                        action act
                        style "navigation_button" text_style "navigation_button_text"
                    key "K_" + str(counter) action act
                else:
                    textbutton lab  + ' (' + str(counter) + ')':
                        xalign 0.99
                        action act
                        style "navigation_button" text_style "action_button_text"
                    key "K_" + str(counter) action act
    
    fixed :
        vbox:
            yalign 0.99
            for tmp_text in loc_txt :
                text '[tmp_text]' :
                    style style.description 


                    
screen inventory_unit:
    zorder 1
    modal True
    fixed :
        add 'images/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action Function(move, curloc)
            textbutton _('Назад') action Function(move, curloc)
            textbutton _('Всё') action [SetVariable('last_inventory','all'), Function(clrscr),Show('inventory_unit')]
            textbutton _('Еда') action [SetVariable('last_inventory','food'), Function(clrscr), Show('inventory_unit')]
            textbutton _('Зелья') action [SetVariable('last_inventory','elixir'), Function(clrscr), Show('inventory_unit')]
    frame xalign 1.0 ypos 0.01:
        text('[player.money] срубо')
    $ adj = ui.adjustment()
    python:
        tab_i = inv_show_list(last_inventory)
        tab_cols = 13.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        # tab_rows = 30
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        # area (250, 75, 925, 660)
        area (250, 90, 1120, 680)
        # add 'bg2.png' xpos -10 ypos -10
        frame xminimum 1140 xpos -10 yminimum 695 ypos -10:
            null
        viewport:
            yadjustment adj
            mousewheel True
            draggable True
            grid tab_cols tab_rows:   
                xfill True
                spacing 5
                for x in tab_i:
                    # $ x.picto = 'images/noimage.gif'
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(0.7))
                        # idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))
                        hovered [SetVariable('myItem', x)]
                        action inv_action (x)
                for i in range(int(tab_n)):
                    vbox:
                        null
                    # add im.FactorScale('images/noimage.gif',0.4)
        # bar adjustment adj style "vscrollbar"
    use showItem

# менюшка с описанием предмета слева
screen showItem:
    zorder 1
    vbox xpos 0.01 ypos 0.1:
        if myItem != 0:
            add myItem.picto
            null height 10
            text '[myItem.name]' style style.my_text
            $ temp = player.countItems(myItem.name)
            text _('Количество [temp]') style style.my_text
            if myItem.type in ['ingredient','food']:
                for effect in myItem.effects:
                    $ tempStr = myItem.effects.get(effect)
                    text '[effect.name] : [tempStr]' style style.my_text

            if player.hasItem(myItem.name):
                textbutton _('Выбросить') action [Hide ('showItem'), Function(player.FremoveItem, myItem)]
                
screen showPeople:
    zorder 1
    modal True
    fixed :
        add 'images/bg.png'
    $ adj = ui.adjustment()
    python:
        tab_i = slaves
        tab_cols = 7.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (250, 90, 1120, 660)
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:   
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.9), im.matrix.opacity(0.9))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.9), im.matrix.opacity(1.0))
                        hovered [SetVariable('showChar', x), Show('charInfoLeft')]
                        # hovered [SetVariable('showChar', x), Show('charInfoLeft')]
                        action NullAction()
                for i in range(int(tab_n)):
                    vbox:
                        null
        bar adjustment adj style "vscrollbar"

    # use showPeople
    
screen charInfoLeft:
    zorder 1
    modal False
    vbox xpos 0.26 ypos 0.15:
        add showChar.picto
        frame:
            has vbox
            xmaximum 700
            text (showChar.name)
            $age = showChar.age
            text ('Возраст [age]')
            $ desc = showChar.reaction
            if development == 1:
                $ temp = showChar.getSkill('health')
                text('health [temp]')
                $ temp = showChar.getSkill('will')
                text('will [temp]')
                $ temp = showChar.getCorr()
                text('corr [temp]')
            text ('[desc]')
            if development == 1:
                text(showChar.location)
            
screen journal:
    add 'images/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action Function(move, curloc)
            textbutton _('Назад (Esc)') action Function(move, curloc)
            textbutton _('Персонаж') action Show('charInfo')
            textbutton _('Эффекты') action Show('effects')
            
screen effects:
    use journal
    tag journal
    $ adj = ui.adjustment()
    python:
        tab_i = allEffects
        tab_cols = 1.0
        tab_rows = len(allEffects)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (50, 90, 1350, 660)
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:   
                xfill True
                spacing 10
                for x in tab_i:
                    frame ymaximum 35:
                        text('[x.name]: ')
                        text('[x.description]') xalign 1.0
                # for i in range(int(tab_n)):
                    # vbox:
                        # null
        # bar adjustment adj style "vscrollbar"
        
screen locationChars:
    $ adj = ui.adjustment()
    python:
        tempArr = []
        for x in slaves:
            if x.location == curloc:
                tempArr.append(x)
        tab_i = tempArr
        tab_i.sort(key=lambda x: x.lname)
        tab_cols = 4.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    fixed xpos 0.01 ypos 0.14:
        hbox:
            textbutton _('Манить') action [SensitiveIf(player.getMana() >= 70 and len(tab_i) > 0 and player.getSkill('empathy') >= 50), Show('allChars')]
    side "c r":
        area (15, 145, 350, 350)
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.5), im.matrix.opacity(0.9))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.5), im.matrix.opacity(1.0))
                        hovered [SetVariable('showChar', x), Show('charInfoLeft')]
                        unhovered [Hide('charInfoLeft')]
                        # hovered [SetVariable('showChar', x), Show('charInfoLeft')]
                        action Jump('interactionMain')
                for i in range(int(tab_n)):
                    vbox:
                        null
        # bar adjustment adj style "vscrollbar"
    side "c r":
        # area (5, 480, 364, 310)
        area (15, 495, 300, 300)
        viewport:
            yadjustment adj
            mousewheel True
            has vbox
            for effect in player.effects:
                text '[effect.name] : [effect.strength]' style style.effects
        
screen charInfo:
    use journal
    tag journal
    $ temp = min(int(player.getCorr()/20), 4) + 1
    add  im.FactorScale('images/picto/GG/pn%d.png' % temp,0.9) xpos 0.0 ypos 1.0 yanchor 1.0
    fixed xpos 0.25 ypos 0.1:
        vbox:
            text ('[player.name]')
            null height 10
            $temp1 = player.getCorr()
            text ('Развращённость: [temp1] из 100')
            $temp1 = player.getLust()
            $temp2 = player.getMaxlust()
            text ('Возбуждение: [temp1] из [temp2]')
            $temp1 = min(100,player.getSkill('alchemy'))
            text ('Зельеварение: [temp1] из 100')
            $temp1 = min(100,player.getSkill('harvesting'))
            text ('Собирательство: [temp1] из 100')
            $temp1 = min(100,player.getSkill('empathy'))
            text ('Эмпатия: [temp1] из 100')
            null height 20
            text ('Активные эффекты и болезни:')
            null height 10
            for effect in player.effects:
                text '[effect.name] : [effect.strength]'
                
            
    fixed xpos 0.5 ypos 0.1:
        vbox:
            xmaximum 700
            text ('Журнал:')
            null height 10
            
            if trigger[13] == 1:
                text ('Продолжать искать плотника...')
            if trigger[13] == 2:
                text ('Ещё раз найти этого чёртового плотника!')
            if trigger[13] == 10:
                text ('ЗАВЕРШЕНО: Кузнец получил приворотное зелье. Хотя, возможно стоило рассказать ему о плотнике?')
            if trigger[13] == 3 and trigger[15] == 0:
                text ('Поговорить с кузнецом.')
            if trigger[15] == 1 and trigger[13] == 3:
                text ('Принести кузнецу приворотное зелье, или рассказать ему о плотнике.')
            if trigger[13] == 4:
                text ('Накопить побольше жизней и маны и провести ритуал с кузнецом.')
            if trigger[13] == 11:
                text ('ЗАВЕРШЕНО: Кузнец теперь моя безвольная игрушка.')
            if trigger[13] == 12:
                text ('ЗАВЕРШЕНО: Кузнец благодарен мне по гроб жизни за свой новый инструмент.')

            if trigger[29] == 1:
                text ('Поговорить с Конрадом.')
            if trigger[29] == 3:
                text ('Принести шлюхе зелье бесплодия.')
            if trigger[29] == 4:
                text ('ЗАВЕРШЕНО: Шлюха каждую неделю будет получать от меня зелье бесплодия в обмен на... На разное.')
                
            if trigger[2] == 1 and trigger[3] == 0:
                text ('Поговорить с пьяницей у таверны.')
            if trigger[4] == 1 and trigger[6] == 0 and trigger[7] == 0:
                text ('ЗАВЕРШЕНО: Я отсосала "скривну" у пьянчуги. Фе-е-е. Даже вспоминать противно!')
            if trigger[6] == 1:
                text ('ЗАВЕРШЕНО: Я дала пьянице приворотное зелье, и он сделал для меня скидку.')
            if trigger[7] == 1:
                text ('ЗАВЕРШЕНО: Я дала пьянице зелье безволия, и теперь он продаёт мне алкоголь по себестоимости.')
                
            if trigger[20] == 2:
                text ('Навестить Аарона ещё раз.')
            if trigger[20] == 3:
                text ('ЗАВЕРШЕНО: Аарон имеет право раз в неделю делать со мной всё, что угодно.')
            if trigger[20] == 4:
                text ('Мне необходимо принести элексир фертильности Аарону.')
            if trigger[20] == 5:
                text ('Навестить Аарона ещё раз.')
            if trigger[20] == 6:
                text ('Принести Аарону зелье бесплодия, или сварить для себя эликсир Лошадиной силы.')
            if trigger[20] == 7:
                text ('ЗАВЕРШЕНО: У Аарона теперь фригидная жена, зато у меня у меня есть меховой костюм.')
            if trigger[20] == 8:
                text ('ЗАВЕРШЕНО: Жена Аарона теперь будет иногда заглядывать ко мне (Не в версии 0.2)')

            
screen aaronSellScreen:
    zorder 1
    modal True
    fixed :
        add 'images/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action Function(move, curloc)
            textbutton _('Назад') action Function(move, curloc)
    frame xalign 1.0 ypos 0.01:
        text(' Всё стоит по 5 срубо. У вас осталось [player.money] срубо.')
    $ adj = ui.adjustment()
    python:
        tab_i = inv_show_sell()
        tab_cols = 13.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        # area (250, 75, 925, 660)
        area (250, 90, 1120, 660)
        
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:   
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(0.7))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))
                        hovered [SetVariable('myItem', x)]
                        action buy_action (x)
                for i in range(int(tab_n)):
                    vbox:
                        null
        bar adjustment adj style "vscrollbar"
    use showItem
    
screen paramShow:
    for i in range(0, len(globalArr)):
        frame xpos 0.0 ypos 0.75 - i*0.05:
            $ name = globalArr[i].name
            $ change = globalChange[i]
            text ('[name]: Лояльность изменилась на [change]')
            # style 'navigation_button_text'
    timer 2.0 action Hide("paramShow")
    
screen allChars:
    zorder 1
    modal True
    fixed :
        add 'images/lure.png'
    frame xalign 0.51 ypos 0.01:
        text('Я напрягла свои ментальные силы, чтобы заставить придти ко мне того, кого захочу. Причём он будет думать, что пришёл по собственной воле. Хоть это трудоёмкий и сложный процесс, но он всегда даёт положительный результат.')
    $ adj = ui.adjustment()
    python:
        tab_i = slaves
        tab_i.sort(key=lambda x: x.lname)
        tab_cols = 9.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (250, 90, 1120, 660)
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.7), im.matrix.opacity(0.9))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.7), im.matrix.opacity(1.0))
                        hovered [SetVariable('showChar', x), Show('charInfoLure')]
                        unhovered [Hide('charInfoLure')]
                        # hovered [SetVariable('showChar', x), Show('charInfoLeft')]
                        action [Function(player.incMana, -70), Jump('interactionMain')]
                for i in range(int(tab_n)):
                    vbox:
                        null
        # bar adjustment adj style "vscrollbar"

screen charInfoLure:
    zorder 1
    modal False
    vbox xpos 0.0 ypos 0.09:
        add showChar.picto
        frame:
            has vbox
            xmaximum 250
            text (showChar.name)
            $age = showChar.age
            text ('Возраст [age]')
            $ desc = showChar.reaction
            text ('[desc]')
            if development == 1:
                text(showChar.location)
                
screen infusionChars:
    zorder 1
    modal True
    fixed :
        add 'images/events/basic/heroStart.png'
    frame xalign 0.51 ypos 0.01:
        text('Я стояла и высматривала того, кого хочу изменить, влив в него различные воспоминания или фантазии.')
    $ adj = ui.adjustment()
    python:
        tempArr = []
        for x in slaves:
            if '"' not in x.lname:
                tempArr.append(x)
        tab_i = tempArr
        tab_i.sort(key=lambda x: x.lname)
        tab_cols = 9.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        area (250, 90, 1120, 660)
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.7), im.matrix.opacity(0.9))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.7), im.matrix.opacity(1.0))
                        hovered [SetVariable('showChar', x), Show('charInfoLure')]
                        unhovered [Hide('charInfoLure')]
                        # hovered [SetVariable('showChar', x), Show('charInfoLeft')]
                        action [Jump('infusionDo')]
                for i in range(int(tab_n)):
                    vbox:
                        null
                        
screen sellScreen:
    zorder 1
    modal True
    fixed :
        add 'images/bg.png'
    fixed xpos 0.01 ypos 0.01:
        hbox :
            key "game_menu" action Function(move, curloc)
            textbutton _('Назад') action Function(move, curloc)
    frame xalign 1.0 ypos 0.01:
        vbox:
            text('Разбойники скупают зелья опьянения, лошадиной силы, густокровия, регенерации и запора.')
            text('У меня есть [player.money] срубо.')
    $ adj = ui.adjustment()
    python:
        tab_i = getSellable(['Лошадиной','Регенера','Запор','Густокро','Опьянение'])
        tab_cols = 13.0
        tab_rows = round(float(len(tab_i))/float(tab_cols) +0.45)
        tab_n = (tab_rows*tab_cols) - len(tab_i)
    side "c r":
        # area (250, 75, 925, 660)
        area (250, 90, 1120, 660)
        viewport:
            yadjustment adj
            mousewheel True
            grid tab_cols tab_rows:   
                xfill True
                spacing 10
                for x in tab_i:
                    imagebutton:
                        idle im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(0.7))
                        hover im.MatrixColor(im.FactorScale(x.picto,0.4), im.matrix.opacity(1.0))
                        hovered [SetVariable('myItem', x)]
                        action sell_action (x)
                for i in range(int(tab_n)):
                    vbox:
                        null
        bar adjustment adj style "vscrollbar"
    use showSellItem
    
screen showSellItem:
    zorder 1
    vbox xpos 0.01 ypos 0.1:
        if myItem != 0:
            add myItem.picto
            null height 10
            text '[myItem.name]' style style.my_text
            $ temp = str(int(myItem.getEffectStrength()/4))
            text _('Цена [temp]') style style.my_text
            if myItem.type in ['ingredient','food']:
                for effect in myItem.effects:
                    $ tempStr = myItem.effects.get(effect)
                    text '[effect.name] : [tempStr]' style style.my_text
                    
screen authors:
    add 'images/authors.png'
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Назад") action Return()
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Сохранить игру") action ShowMenu("save")
        textbutton _("Загрузить игру") action ShowMenu("load")
        # textbutton _("Главное меню") action MainMenu()
        # textbutton _("Справка") action Help()
        textbutton _("Поддержать") action ShowMenu("support")
        textbutton _("Выход") action Quit()
    tag menu
    fixed xpos 0.5 ypos 0.1:
        vbox:
            text('Создатели:')
            text(' Allanon - текст, код, сюжет')
            text(' irvin.zamora - код')
            text(' Meganom - текст, сюжет')
            text('')
            text('Отдельное спасибо за участие:')
            text(' iverysexyman')
            text(' Andrei7373')
            text(' olegan')
            text(' Daooda')
            text(' DeGross')
            text(' dodo13')
            text(' Крабе')
            text(' Rupo')
            text(' Шлюханы')
            
screen support:
    add 'images/support.png'
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Назад") action Return()
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Сохранить игру") action ShowMenu("save")
        textbutton _("Загрузить игру") action ShowMenu("load")
        # textbutton _("Главное меню") action MainMenu()
        textbutton _("Авторы") action ShowMenu("authors")
        textbutton _("Выход") action Quit()
    tag menu
    frame style "gm_root" xpos 0.4 ypos 0.1 xmaximum 800 ymaximum 300:
        vbox:
            text('Тут вы можете поддержать проект, если захотите: {a=https://www.patreon.com/allanon}Patreon{/a}')
            null height 10
            text('Правда, хочу отметить, что это не даст вам каких-то бонусов, в виде возможности поиграть в новые билды раньше, чем другие, зато вы простимулируете меня выпускать новые версии чаще.\nБез вашей поддержки, я не брошу проект, и буду работать как раньше. Медленно и со вкусом. С ней же я буду возвращаться к мысли, что кто-то ждёт мою игру чаще. Возможно, это поможет.')
            null height 10
            text('Сказать спасибо или выразить свои пожелания можно {a=https://albedo.pw/thread-1406.html}тут{/a} и {a=http://nigredo.fludilka.su/viewtopic.php?id=245}тут{/a}.')
            null height 10
            text('Приятной игры!')