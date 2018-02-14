label getRequest:
    python:
        if waitRequest == None:
            changetime(60)
            # currRequest = copy.copy(intoxicationR3)
            currRequest = copy.copy(choice(allRequests))
            currRequest.char = getChar(currRequest.sex)
            if currRequest.patient == True:
                if currRequest.align == 'bad' and currRequest.char.getEnemy(currRequest.patientSex) != False:
                    currRequest.patient = currRequest.char.getEnemy(currRequest.patientSex)
                elif currRequest.align == 'good' and currRequest.char.getFriend(currRequest.patientSex) != False:
                    currRequest.patient = currRequest.char.getFriend(currRequest.patientSex)
                else:
                    currRequest.patient = getChar(currRequest.patientSex)
        clrscr()
    call screen requestScreen
    
screen requestScreen:
    zorder 1
    modal True
    if currRequest.char.getSex() == 'male':
        add 'images/events/request/main.png'
    else:
        add 'images/events/request/mainFemale.png'
    add 'images/bg.png'
    # fixed xpos 0.75 ypos 0.5:
        # add 'images/picto/GG/n5.png'
    fixed xpos 0.01 ypos 0.01:
        vbox:
            add currRequest.char.picto
            $ name = currRequest.char.name
            if currRequest.char.getSex() == 'female':
                $ sex = 'женщина'
            else:
                $ sex = 'мужчина'
            text ('[name], [sex]') style style.my_text
            $ age = currRequest.char.age
            text ('Возраст [age]') style style.my_text
            $ alignText = getAlignment(currRequest.char)
            text ('[alignText]') style style.my_text
            # if development > 0:
                # text ('[align]') style style.my_text
            $ loy = int(currRequest.char.getLoy())
            text ('Лояльность [loy]') style style.my_text
            
    fixed xpos 0.2 ypos 0.01 xmaximum 800:
        vbox:
            $ description = currRequest.description
            text('[name]' + '[description]')

            if currRequest.patient != False:
                null height 10
                $ name = currRequest.patient.name
                $ alignText = getAlignment(currRequest.patient).lower()
                text('Эта просьба затрагивает ещё одного человека: [name], он/она [alignText]')
            null height 10
            if currRequest.empathyTry == False:
                text('Я не пробовала задействовать эмпатию.')
            elif currRequest.empathy == False and currRequest.empathyTry == True:
                text('Я дотронулась до руки, но в этой мешанине чувств и образов не смогла выявить точный diagnosis.')
            else:
                $ effect = getAntiEffect(currRequest.effect.keys()[0]).name
                $ strength = currRequest.effect.values()[0]
                text('Дотронувшись до руки и пробравшись сквозь мешанину образов, чувств и желаний, я поняла, что необходимо просителю. Это Зелье:[effect] с силой [strength]')
                
            
            
    fixed xpos 0.71 ypos 0.5:
        vbox:
            textbutton _('Эмпатия') xminimum 200 action [
                SetField(currRequest,'empathyTry', True), 
                SensitiveIf(currRequest.empathyTry == False),
                If(player.skills.get('empathy') + empathyAdj > rand(0,100), true = SetField(currRequest,'empathy', True), false = Function(player.incSkill, 'empathy'))
                ]
            textbutton _('Дать зелье') xminimum 200 xmaximum 200 action Show('givePotion')
            textbutton _('Дать совет') xminimum 200 action Jump('goodAdvice')
            textbutton _('Оскорбить') xminimum 200 action Jump('badAdvice')
            textbutton _('Отказать') xminimum 200 action Jump('rejectRequest')
            textbutton _('Обождать') xminimum 200 xmaximum 200 action Jump('waitRequest')
        
        
screen givePotion:
    zorder 2
    modal True
    add 'images/bg.png'
    $ adj = ui.adjustment()
    textbutton _('Назад') action Hide('givePotion')
    python:
        tab_i = inv_show_list('elixir')
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
                        action [Function(givePotion, x)]
                for i in range(int(tab_n)):
                    vbox:
                        null
        bar adjustment adj style "vscrollbar"
    use showItem

init python:
    import math
    def givePotion(item):
        global currRequest, strengthAdj
        player.removeItem(item)
        for x in currRequest.effect:
            for y in item.effects:
                clrscr()
                if checkAntiEffect(x, y) == True:
                    if math.fabs(item.effects.get(y) - currRequest.effect.get(x)) > strengthAdj:
                        if item.effects.get(y) - currRequest.effect.get(x) > strengthAdj:
                            renpy.jump ('failTooStrong')
                        else:
                            renpy.jump ('failTooWeak')
                    else:
                        renpy.jump ('successRequest')
                else:
                    renpy.jump ('failRequest')
                
label successRequest:
    python:
        currRequest.char.incLoy(20)
        player.applyEffects({faith:1})
        if currRequest.patient != False:
            if currRequest.align == 'bad':
                currRequest.patient.incLoy(-10)
            elif currRequest.align == 'good':
                currRequest.patient.incLoy(10)
        waitRequest = None
    show expression 'images/events/request/reward.png' as tempPic
    if currRequest.patient == False:
        if currRequest.char.getSex() == 'male':
            player.say '{i}Селянин выпивает содержимое и его лицо украшается улыбкой. Очевидно, что зелье подействовало и подействовало так, как нужно!'
        else:
            player.say '{i}Селянка выпивает содержимое и её лицо украшается улыбкой. Очевидно, что зелье подействовало и подействовало так, как нужно!'
    else:
        if currRequest.char.getSex() == 'male':
            player.say 'Ээй! А награда?'
            currRequest.char.say 'Дык, я же ещё не испытал то, что ты дала! О какой награде может идти речь?'
            player.say 'Просто поверь. То, что я дала тебе поможет. Если нет, вернёшься и спалишь мой дом, но слово своё я держу.'
            currRequest.char.say 'Ладно, верю. Чего ты хочешь?'
        else:
            player.say 'Ээй! А награда?'
            currRequest.char.say 'Дык, милочка, я же ещё не испытала то, что ты дала! О какой награде может идти речь?'
            player.say 'Просто поверь. То, что я дала тебе поможет. Если нет, вернёшься с мужем и спалишь мой дом, но слово своё я держу.'
            currRequest.char.say 'Ладно, верю. Чего ты хочешь?'
    menu:
        'Настало время потребовать награду!'
        'Просить денег':
            if trigger[0] == 0:
                player.say 'Я дала тебе не самое дешёвое зелье, мне необходимо как-то компенсировать его стоимость.'
                currRequest.char.say 'К-к-комлекировать чё? Не надо меня комплексировать! Сделала хорошо, отпусти подобру поздорову! Век тебе благодарен буду!'
                player.say '100 срубо за лечение и можешь идти дальше пахать поле, пасти овец или чем ты там занимаешься.'
                currRequest.char.say 'Чего??? Да я столько за год не зарабатываю! Вот, на, держи десятку, и я разнесу добрую весть о том, как ты мне помогла!'
                player.say 'Чёрт с тобой, давай.'
                show expression 'images/events/request/gold.png' as tempPic
                player.say '{i}Вот ведь беднота... И как мне выживать на эти копейки?'
                player.say '{i}Я получила 10 срубо и клятвенные заверения в верности. Логика подсказывает мне, что не стоит им особо доверять. Таких как я предают при первой возможности...'
                $ trigger[0] = 1
            else:
                player.say '10 срубо.'
                currRequest.char.say 'Дорого, госпожа...'
                if currRequest.char.getSex() == 'male':
                    player.say '10 срубо, иначе хрен отсохнет.'
                else:
                    player.say '10 срубо, иначе у мужа хрен отсохнет.'
                show expression 'images/events/request/gold.png' as tempPic
                if currRequest.char.getSex() == 'male':
                    player.say '{i}Моментально заткнувшийся холоп безропотно отдаёт кровные.'
                else:
                    player.say '{i}Моментально замолчавшая селянка безропотно отдаёт кровные.'
            python:
                player.incMoney(10)
                currRequest.char.incLoy(20)
        'Просить продукты':
            python:
                for x in range(0,2):
                    if rand(1,3) == 1:
                        player.addItem(meatChickenCooked)
                    player.addItem(meatChickenCooked)
                currRequest.char.incLoy(20)
            if trigger[1] == 0:
                player.say 'Я дала тебе не самое дешёвое зелье, и прошу услугу взамен. Ты должен приносить мне еду 3 раза в день в течении недели.'
                currRequest.char.say 'Ведунья! Помилуй! Детки по лавкам голодные сидят, баронские люди лютуют. Церковь десятину берёт, откуда я тебе столько еды достану?'
                player.say 'Ну ладно, 3 дня приноси еду...'
                currRequest.char.say 'Госпожа. Да я рад был бы тебя всю жизнь кормить за сердце твоё доброе! Но нету у меня лишней еды, нетути! Могу свой обед отдать...'
                player.say 'Чёрт с тобой, давай.'
                player.say '{i}Вот ведь беднота... Даже пожрать у них нечего...'
                player.say '{i}Я получила несколько кусков курятины. С голоду не помру, но положение безрадостное.'
                $ trigger[1] = 1
            else:
                player.say 'Давай что есть пожрать и до свидания.'
                currRequest.char.say 'Конечно, вот.'
                player.say '{i}[currRequest.char.lname] выкладывает курятину из своей котомки.'

        'Помощь в сборе ингредиентов' if currRequest.char.lname in ['Охотник', 'Охотница', 'Лесник']:
            player.say 'Я потратилась на тебя и мне нужны кое какие ингредиенты... Ты [currRequest.char.lname], наверняка у тебя завалялось несколько перьев орла, или волчьи глаза?'
            currRequest.char.say 'Ну обычно я такое выкидываю, но для тебя могу принести разный хлам из дома.'
            if currRequest.char.getSex() == 'male':
                player.say '{i}[currRequest.char.lname] быстро сбегал в свою избушку и принёс мне немного полезных компонентов.'
            else:
                player.say '{i}[currRequest.char.lname] быстро сбегала в свою избушку и принесла мне немного полезных компонентов.'
            python:
                for x in range(5,20):
                    player.addItem(choice(ingHunter))
        'Помощь в сборе ингредиентов' if currRequest.char.lname != 'Охотник' and currRequest.char.getSex() == 'male':
            player.say '{i}[currRequest.char.lname] предложил мне было денег, но я отказалась. Есть один ингридиент, который мне проблематично добыть без чужой помощи. Будь [currRequest.char.fname] охотником, всё было бы проще. Ну а что можно взять с простого мужика? Правильно, только это.'
            jump requestSperm
    $ move(curloc)
    
label failRequest:
    $ player.applyEffects({faith:-1})
    show expression 'images/events/request/main.png' as tempPic
    $ currRequest.char.incLoy(-10)
    if currRequest.patient == False:
        if currRequest.char.getSex() == 'male':
            player.say '{i}[currRequest.char.fname] употребляет то, что я ему предложила, но не получает ожидаемого исцеления.'
            currRequest.char.say 'Чёртова ведьма! Если со мной что-то случится, мои друзья сразу донесут Святому Официуму! Побойся!'
            player.say 'Побоюсь, побоюсь. Дуй давай, пока ноги не отсохли!'
            player.say '{i}[currRequest.char.lname] плюёт мне под ноги, обещая рассказать друзьям, как я его обманула! Ну буду надеяться, что врагов у него побольше, чем друзей. Его недругам явно понравится эта шуточка!'
        else:
            player.say '{i}[currRequest.char.fname] употребляет то, что я ей предложила, но не получает ожидаемого исцеления.'
            currRequest.char.say 'Чёртова ведьма! Если со мной что-то случится, прокляну тебя, твоего отца и твою мать!'
            player.say 'Пфф. Моей родне твои проклятья уже не грозят, а вот об меня ты зубки пообломаешь! Благодари, что не померла на месте, а теперь иди!'
            player.say '{i}[currRequest.char.lname] плюёт мне под ноги, обещая рассказать друзьям, как я её обманула! Ну буду надеяться, что врагов у неё побольше, чем друзей. Её недругам явно понравится эта шуточка!'
    else:
        python:
            if currRequest.align == 'bad':
                currRequest.patient.incLoy(5)
            elif currRequest.align == 'good':
                currRequest.patient.incLoy(-10)
        player.say '{i}В тот момент я всё таки дала просителю не то, что он хотел. Конечно, об этом я узнала только через пару дней, но что сделано, то изменить нельзя. Можно только попробовать исправить.'
    python:
        waitRequest = None
        move(curloc)
        
    
label failTooStrong:
    $ currRequest.char.incLoy(-5)
    if currRequest.patient == False:
        if currRequest.char.getSex() == 'male':
            show expression 'images/events/request/main.png' as tempPic
            player.say '{i}[currRequest.char.name] выпивает то, что вы ему предложили, и лицо его разглаживается, правда спустя мгновение начинает хмуриться снова. Похоже, что я не угадала с силой!'
            currRequest.char.say 'Ну вот мля. Не понос, так золотуха! Ну его на хер, пойду дедовскими способами лечиться! А ты, ведьма, будь ты проклята, сука!'
            player.say 'Поосторожней с такими словами... Они могут и вернуться, [currRequest.char.fname]!'
            player.say '{i}[currRequest.char.fname] бурчит что-то через плечо, разворачивается и уходит в направлении ближайшего трактира. Платы от него вы не дождётесь. Как и компенсации за ингредиенты.'
        else:
            player.say '{i}[currRequest.char.name] выпивает то, что вы ей предложили, и простое лицо разглаживается, правда спустя мгновение начинает хмуриться снова. Похоже, что я не угадала с силой!'
            currRequest.char.say 'Ну вот мля. Не понос, так золотуха! Даже я умею суп мешать, а ты три травки нормально сварить не можешь! Будь ты проклята, сука!'
            player.say 'Поосторожней с такими словами... Они могут и вернуться, [currRequest.char.fname]!'
            player.say '{i}[currRequest.char.fname] бурчит что-то через плечо, разворачивается и уходит домой. Платы от неё вы не дождётесь. Как и компенсации за ингредиенты.'
    else:
        python:
            if currRequest.align == 'bad':
                currRequest.patient.incLoy(-15)
            elif currRequest.align == 'good':
                currRequest.patient.incLoy(-5)
        player.say '{i}В тот момент я всё таки дала просителю не то, что он хотел. Конечно, об этом я узнала только через пару дней, но что сделано, то изменить нельзя. Можно только попробовать исправить.'
    python:
        waitRequest = None
        move(curloc)
        
label failTooWeak:
    $ currRequest.char.incLoy(5)
    if currRequest.patient == False:
        if currRequest.char.getSex() == 'male':
            show expression 'images/events/request/main.png' as tempPic
            player.say '{i}[currRequest.char.name] выпивает то, что вы ему предложили, и лицо его разглаживается, правда спустя мгновение начинает хмуриться снова. Похоже, что я не угадала с силой!'
            currRequest.char.say 'Ну оно вроде подействовало, но вроде как не до конца... Слышь, ну его на хер я думаю, вот тебе за труды, а я пойду себе, дедовскими способами полечусь.'
            player.say '{i}[currRequest.char.fname] разворачивается и уходит в направлении ближайшего трактира. Он оставляет мне пару монет компенсации. Ну хоть что-то... Хотя я не уверена, что пара монет окупит ингредиенты, что я извела на этого холопа.'
        else:
            show expression 'images/events/request/mainFemale.png' as tempPic
            player.say '{i}[currRequest.char.name] выпивает то, что вы ей предложили, и простое лицо разглаживается, правда спустя мгновение начинает хмуриться снова. Похоже, что я не угадала с силой!'
            currRequest.char.say 'Ну оно вроде подействовало, но вроде как не до конца... Милочка, отчего же оно так то?'
            player.say 'Ну не смогла точно рассчитать силу. Вас тут много ходит, а зелья я одна готовлю...'
            player.say '{i}[currRequest.char.fname]  разворачивается и расстроенно уходит домой. Она оставляет мне пару монет компенсации. Ну хоть что-то... Хотя я не уверена, что пара монет окупит ингредиенты, что я извела на этого простушку.'
    else:
        python:
            if currRequest.align == 'bad':
                currRequest.patient.incLoy(-5)
            elif currRequest.align == 'good':
                currRequest.patient.incLoy(5)
        if currRequest.char.getSex() == 'male':
            player.say '{i} [currRequest.char.fname] поблагодарил меня и даже дал пару монет в задаток.'
        else:
            player.say '{i} [currRequest.char.fname] поблагодарила меня и даже дала пару монет в задаток.'
        player.say '{i}В тот момент я всё таки дала просителю не то, что он хотел. Конечно, об этом я узнала только через пару дней, но что сделано, то изменить нельзя. Можно только попробовать исправить.'
    python:
        waitRequest = None
        player.incMoney(rand(2,3))
        move(curloc)
        
label goodAdvice:
    $ currRequest.char.incLoy(10)
    if currRequest.char.getSex() == 'male':
        show expression 'images/events/request/main.png' as tempPic
    else:
        show expression 'images/events/request/mainFemale.png' as tempPic
    player.say '[currRequest.adviceG]'
    currRequest.char.say 'Э-э-х. Ну я попробую, конечно, но хрен его знает. Спасибо...'
    player.say 'Спасибо на хлеб не положишь, знаешь ли.'
    currRequest.char.say 'А?'
    player.say '{i}Я доступна объяснила просителю, что даже за советы надо платить. К сожалению денег он мне не дал, но перекусить предложил.' 
    python:
        waitRequest = None
        player.addItem(meatChickenCooked)
        move(curloc)
        
label badAdvice:
    $ currRequest.char.incLoy(-5)
    if currRequest.char.getSex() == 'male':
        show expression 'images/events/request/scoldMale.png' as tempPic
    else:
        show expression 'images/events/request/scoldFemale.png' as tempPic
    player.say '[currRequest.adviceB]'
    currRequest.char.say 'Думаешь поможет? Э-э-э! Да ты никак смеёшься надо мной, чертовка?'
    if currRequest.char.getSex() == 'male':
        player.say 'Давай иди и исполняй! Ведь ты за этим приходил, смерд?'
    else:
        player.say 'Давай иди и исполняй! Ведь ты за этим приходила, раба?'
    currRequest.char.say 'Ну, сука, ты у нас ещё попляшешь с пеньковой тётушкой... Дай только до Чёрных добраться...'
    python:
        waitRequest = None
        move(curloc)
        
label rejectRequest:
    $ currRequest.char.incLoy(-2)
    if currRequest.char.getSex() == 'male':
        show expression 'images/events/request/main.png' as tempPic
    else:
        show expression 'images/events/request/mainFemale.png' as tempPic
    player.say 'Я не могу тебе помочь.'
    if currRequest.char.getSex() == 'male':
        currRequest.char.say 'Что? Да я сюда час пёрся за помощью! Хоть совет дай!'
    else:
        currRequest.char.say 'Что? Да я сюда час пёрлась за помощью! Хоть совет дай!'
    player.say 'Я не хочу. Уходи.'
    currRequest.char.say 'Тьфу, ведьма!'
    python:
        waitRequest = None
        move(curloc)
        
label waitRequest:
    if currRequest.char.getSex() == 'male':
        show expression 'images/events/request/main.png' as tempPic
    else:
        show expression 'images/events/request/mainFemale.png' as tempPic
    player.say '{i}Я попросила подождать, пока я приготовлю нужное зелье. Мне дали пару часов.'
    $ waitRequest = {currRequest:mtime}
    $ move(curloc)
    
label requestSperm:
    $ s1 = currRequest.char
    show expression 'images/events/request/sperm.png' as tempPic
    if trigger[8] == 0:
        $ trigger[8] = 1
        player.say 'Тут такое дело. В общем мне от тебя не нужны деньги. Оставь свои срубо. Мне нужна порция твоего эякулята.'
        currRequest.char.say 'Чё? Нет у меня никакого юкулята!'
        player.say 'Спермы, дурак! Сперма твоя мне нужна!'
        currRequest.char.say 'А. Это... Ну ладно. Чё, прям здесь что ли?'
        player.say 'Зайди ко мне в дом, там у кровати плошка стоит. Вот в неё и спусти.'
        currRequest.char.say 'Понятно. Ты это, помочь не хочешь? А то как-то не Писанию, самому то...'
        player.say 'А ко мне приходить, это по Писанию? Иди давай! Дело простое, запутаться не должен!'
    else:
        player.say 'Письку в руки, дуй в дом, плошка на столе. Через 15 минут она должна быть заполнена спермой, иди, не мешкай, у меня ещё куча дел!'
    label requestSpermMenu:
    show expression 'images/events/request/wait.png' as tempPic
    menu:
        '[currRequest.char.fname] ушёл и пропал в вашем доме. Его нет уже 10 минут.'
        'Пойти проверить':
            if trigger[33] == 1:
                menu:
                    'Подсматривать из дома':
                        $ trigger[9] = 0
                    'Подсматривать из окна':
                        $ trigger[9] = 1
                    'Посмотреть поближе':
                        $ trigger[9] = 2
                    'Подсматривать из окна и ласкать себя':
                        $ trigger[9] = 3
                    'Подсматривать из дома и ласкать себя':
                        $ trigger[9] = 4
            if trigger[9] == 0:
                $ trigger[9] = 1
                python:
                    if player.getCorr() < 20:
                        player.incCorr(1)
                player.say 'И чего он там так долго делает то???'
                show expression 'images/events/request/mast1.png' as tempPic
                player.say '{i}Я зашла в дом и слегка оторопела от увиденного. [currRequest.char.fname] вольготно расположился на моей кровати и теребил свой торчащий в потолок член. Похоже, что дело приближалось к развязке.'
                currRequest.char.say 'Да-а-а, сучка! Получи стрелу в колено!'
                show expression 'images/events/request/mast2.png' as tempPic
                player.say '{i}Его хер изверг из себя струю спермы, заляпывая вокруг всё, кроме плошки. Я поспешно ретировалась, страшно взбешённая произошедшим.'
                show expression 'images/events/request/scoldMale.png' as tempPic
                currRequest.char.say 'Я закончил! - радостно выпалил [currRequest.char.lname].'
                player.say 'Ты мне всю кровать залил своим семенем! Как я теперь оттирать его буду?'
                currRequest.char.say 'Ну я это, собрал в плошку... Как ты и просила...'
                player.say 'Я просила сразу кончать туда, а не расписывать мне обиталище белыми красками! Хрен с тобой, иди, пока я не сделала что-то страшное!'
                $ player.incLust(5)
            elif trigger[9] == 1:
                $ trigger[9] = 2
                python:
                    if player.getCorr() < 20:
                        player.incCorr(3)
                $ player.incLust(10)
                show expression 'images/events/request/mast3.png' as tempPic
                player.say '{i}На этот раз я решила не рисковать чистотой своей робы и решила посмотреть через окно. Как ни странно, зрелище меня впечатлило ничуть не меньше. Я даже прикрыла рот от нервного трепета. Всё это казалось таким неправильным, но таким... Волнующим!'
                show expression 'images/events/request/mast4.png' as tempPic
                player.say '{i}Мужчина не спеша подрачивал свой член. Вскоре на кончике появилась белая капля, и [currRequest.char.lname] ловко подхватил плошку, спустив туда своё семя. Меня слегка потряхивало от возбуждения.'
            elif trigger[9] == 2:
                $ trigger[9] = 3
                python:
                    if player.getCorr() < 20:
                        player.incCorr(5)
                $ player.incLust(15)
                show expression 'images/events/request/mast5.png' as tempPic
                player.say '{i}Меня так заворожили движения руки и крепкий, налитый кровью член, что в этот раз я решила рассмотреть его ещё ближе. Когда [currRequest.char.lname] скрылся в моём доме, я аккуратно подобралась к окну так, что набухший хер оказался почти прямо перед моим носом. Меня аж затрясло от возбуждения и руки потянулись к влагалищу, как когда то в другой жизни...'
                player.say '{i}К сожалению, не успела я как следует насладиться зрелищем, как [currRequest.char.fname] шумно кончил, наплескав добрую половину плошки.'
            elif trigger[9] == 3:
                $ trigger[9] = 4
                python:
                    if player.getCorr() < 20:
                        player.incCorr(5)
                # $ player.setCorr(max(player.getCorr() + 5, 20))
                $ player.incLust(30)
                show expression 'images/events/request/mast5.png' as tempPic
                player.say '{i}Как и в прошлый раз, я начала подглядывать за холопом, сидя прямо под окном. Его член мерно двигался, и я ощущала растущую теплоту и возбуждение внизу живота. Мне тоже захотелось оказаться рядом с ним и ласкать этот твёрдый хер. Но я сдерживалась. Хотя и не до такой степени, чтобы не пойти на лёгкое безумство.'
                show expression 'images/events/request/mast6.png' as tempPic
                player.say '{i}Аккуратно переместившись, чтобы видеть все достоинства открывающегося передо мной вида, я сбросила робу и начала поглаживать свою насквозь промокшую киску. Пальчики уверенно нащупали бугорок клитора и принялись теребить его.'
                player.say '{i}Не отрывая взгляда от качающегося члена в окне, я запустила пальцы в свою жаждущую щель и, стараясь попадать в ритм мужчины, начала вгонять в себя свёрнутые винтом пальчики. Я пожирала глазами пульсирующий орган, мечтая о том, как он будет входить меня. К сожалению моего самообладания не хватило на то, чтобы броситься в объятья холопа, но хватило, чтобы не кончить одновременно с извергнувшейся из головки спермой.'
                player.say '{i}Быстро одевшись, я поправила робу и глубоко вздохнула, пытаясь унять дрожь в голосе. Надеюсь, что в следующий раз я буду способна на большее!'
            else:
                $ trigger[33] = 1
                $ player.setLust(0)
                python:
                    if player.getCorr() < 20:
                        player.incCorr(5)
                show expression 'images/events/request/mast7.png' as tempPic
                player.say '{i}И в очередной раз я не смогла удержаться от того, чтобы посмотреть на удовлетворяющего себя холопа. Неужели я становлюсь настолько распущенной, что столь вульгарные вещи доставляют мне удовольствие? Сама не понимаю как так произошло, но я снова оказалась в своём доме, наслаждаясь видом торчащего за углом члена.'
                player.say '{i}Моя рука уверенно нащупала намокшие от возбуждения губы, и с тихим стоном я провела пальцами между ними. Кончики пальцев уверенно нащупали сладкий бугорочек и по телу пробежала лёгкая дрожь наслаждения. Я то ускоряла, то замедляла движения, разглядывая мускулистое тело мужчины. Чувство страха быть замеченной и острое наслаждение от игривых пальчиков поставило меня на грань оргазма, готового прорваться в любой миг.'
                player.say 'А-а-ах!'
                currRequest.char.say 'Кто здеся?'
                show expression 'images/events/request/mast8.png' as tempPic
                player.say '{i}Я отпрянула к стене, не прекращая ласкать себя. Резкий страх ударил по нервам, ноги затряслись и меня накрыл оргазм. Матка неистово сокращалась, глаза начали закатываться, а влагалище упруго сжало терзающие его пальцы. По полу тихо забарабанили падающие с киски капли смазки. Я едва сдержалась, чтобы не закричать от удовольствия.'
                currRequest.char.say 'Наверное показалось... Ладно, надо заканчивать скорее, а то ещё в жабу превратит и буду квакать на болотах.'
                player.say '{i}Всё ещё вздрагивая от каждого прикосновения к своему телу, я быстро оделась и выскочила из дома.'
                
                
        'Пойти помочь' if player.getCorr() >= 20:
            $ s1.incLoy(50)
            if trigger[34] == 1:
                menu:
                    'Показать себя':
                        $ trigger[10] = 0
                    'Показать киску':
                        $ trigger[10] = 1
                    'Мастурбировать перед ним':
                        $ trigger[10] = 2
                    'Мастурбировать':
                        $ trigger[10] = 3
                    'Показать задницу':
                        $ trigger[10] = 4
            if trigger[10] == 0:
                python:
                    trigger[10] = 1
                    player.incLust(20)
                    if player.getCorr() < 50:
                        player.incCorr(5)
                player.say 'Да сколько можно возиться! Пойду, помогу ему. А то небось от страха хрен в яйцах спрятался.'
                show expression 'images/events/request/help1.png' as tempPic
                player.say '{i}Скинув с себя робу, я вошла в дом, чтобы замотивировать крестьянина видом своего обнажённого тела. Как и прочие, тот лежал на моей кровати яростно надрачивая распухший хрен.'
                currRequest.char.say 'Ты это, чего это?'
                player.say 'Да вот решила слегка помочь тебе, а то ты слишком долго возишься.'
                currRequest.char.say 'А, это, то есть... Мы счас или ты мне?'
                player.say 'Нет, ты смотришь и заканчиваешь максимально быстро, уяснил? Давай, двигай ручёнками, гоп гоп гоп!'
                show expression 'images/events/request/help2.png' as tempPic
                player.say '{i}Холоп радостно ускорился, пожирая моё обнажённое тело глазами, а я прикусила палец и закрыла киску рукой, сгорая одновременно и от стыда, и от возбуждения. Ладошка, лежащая на промежности мгновенно намокла от истекающих и из меня соков.'
                currRequest.char.say 'Я сейчас это...'
                player.say 'Давай давай! Прям в плошку! И чтобы ни капли мимо!'
                player.say '{i}Холоп схватил ёмкость и громким хрипом начал извергаться в неё. От этого зрелища и одуряющего запаха спермы мои ноги слегка затряслись, а киска слегка приоткрылась, жаждя получить немного пахучей жидкости.'
                show expression 'images/events/request/spermAfter.png' as tempPic
                player.say '{i}Крестьянин ушёл, а я всё смотрела в плошку, от которой тянуло каким-то первобытным запахом, от которого теплело внизу живота.'
            elif trigger[10] == 1:
                python:
                    trigger[10] = 2
                    player.incLust(20)
                    if player.getCorr() < 50:
                        player.incCorr(5)
                    player.incDirty(1)
                player.say 'Какие они все неторопливые, когда нужно быть побыстрее! На своей жёнужке наверняка в 2 минуты укладывается, включая полторы на раздевание!'
                show expression 'images/events/request/help3.png' as tempPic
                player.say '{i}Уже привычно я избавилась от одежды и вошла в дом к мужчине. Тот, как и все до него, лежал широко раздвинув ноги, пытаясь добыть нужную мне жидкость.'
                currRequest.char.say 'Ты это, чё это ты а?'
                player.say 'Да вот устала ждать, пока ты мне надоешь порцию. Решила помочь. Но только смотреть, руками не трогать, ясно?'
                currRequest.char.say 'Дык это мы завсегда, ага!'
                show expression 'images/events/request/help4.png' as tempPic
                player.say '{i}Я вошла и уселась перед ним на сундучок, широко раздвинув ноги и предоставляя шикарный вид на своё обнажённое тело. Глаза мужчины вперились в мою промежность, а рука заходила вверх и вниз как безумная.'
                currRequest.char.say 'Ахереть!'
                player.say 'Ты это, быстрее давай. А то я что-то продрогла сидеть так перед тобой.'
                player.say '{i}Меня действительно потряхивало. Только, боюсь, это было скорее от возбуждения и осознания неправильности того, что я делаю, нежели от холода.'
                show expression 'images/events/request/help5.png' as tempPic
                player.say '{i}Неожиданно для меня тело мужчины напряглось ещё сильнее, он слегка задрожал, и с его члена вырвалась белая струя, приземляясь мне на грудь и ноги.'
                player.say 'Ну что ты за мудак то за такой!'
                currRequest.char.say 'Ну ты такая! Такая! В общем как-то увлёкся... - извиняющимся тоном сообщил холоп.'
                player.say 'Козёл! Греби давай отсюда!'
                show expression 'images/events/request/spermAfter.png' as tempPic
                player.say '{i}Я собрала в ёмкость сперму со своей груди и живота, а потом ещё некоторое время сидела, вспоминая как густые, горячие капли стекали по моему дрожащему от возбуждения телу.'
            elif trigger[10] == 2:
                python:
                    trigger[10] = 3
                    player.incLust(20)
                    if player.getCorr() < 50:
                        player.incCorr(5)
                    player.incDirty(1)
                player.say 'Почему-то я даже не удивлена тому, что они так задерживаются. Похоже, что попросту начали ждать, пока я приду. С другой стороны это довольно занятно, так что почему бы и не придти, в самом деле?'
                show expression 'images/events/request/help3.png' as tempPic
                player.say 'Я так понимаю, что ты меня ждёшь? - игриво спросила я, заходя в комнату.'
                currRequest.char.say 'Ну надо же, не соврали! - лицо холопа на кровати растянулось в щербатой усмешке.'
                player.say 'Ну тогда правила ты знаешь. Смотреть можно и даже нужно, а трогать нельзя. Понятно?'
                currRequest.char.say 'Чтож тут непонятного!'
                show expression 'images/events/request/help6.png' as tempPic
                player.say '{i}Я присела к нему на кровать, положив ладошку на свою мгновенно промокшую киску.'
                player.say 'Ну что застопорился, продолжай!'
                player.say '{i}Мужчина радостно угукнул и заработал рукой. На этот раз я решила не отставать и тоже активно задвигала пальчиками. Это было так здорово, сидеть рядом и мастурбировать, глядя друг на друга! Я никогда не испытывала подобных чувств и такого возбуждения.'
                player.say '{i}Комната наполнилась похотливыми шлепками и хлюпаньем. Я постанывала, периодически подбадривая холопа, но надеялась, что он продержится подольше, дав мне получше запечатлеть в памяти эту картину.'
                currRequest.char.say 'Ща кончу!'
                show expression 'images/events/request/help7.png' as tempPic
                player.say 'Давай! - и я пошире раздвинула ноги, ускоряя свои движения. Мне уже не раз приходилось наблюдать, как кончает мужчина, но, каждый раз, это зрелище вызывало у меня непередаваемые ощущения. Его член затрясся, и начал обрызгивать моё тело ароматной спермой. Мне не хватило буквально чуть - чуть, чтобы не начать кончать вместе с ним, но всё равно матка приятно заныла, когда кожа ощутила горячее и влажное касание семени.'
                player.say 'Молодчина, теперь иди!'
                show expression 'images/events/request/spermAfter.png' as tempPic
                player.say '{i}Я собрала в ёмкость сперму со своего живота и ног, а потом ещё некоторое время сидела, вспоминая холоп заливал моё тело пахучим семенем.'
            elif trigger[10] == 3:
                python:
                    trigger[10] = 4
                    player.setLust(0)
                    if player.getCorr() < 50:
                        player.incCorr(5)
                show expression 'images/events/request/help8.png' as tempPic
                player.say '{i}Я яростно мастурбировала на крыльце своего дома, слыша, как внутри удовлетворяет себя очередной крестьянин.'
                player.say 'Разве так должна выглядеть ведьма? Почему я стала настолько похотлива? Почему это происходит со мной? Или это из за связи с Изнанкой? Не знаю... Но так хочется снова оказаться рядом! К чёрту! В конце концов, это моя жизнь и я вольна делать то, что захочу!'
                show expression 'images/events/request/help9.png' as tempPic
                player.say 'Заткнись и продолжай!'
                player.say '{i}Я бесцеремонно вошла в дом и забралась на кровать. Рука привычно очутилась между ног, а вторая начала пощипывать сосок. На этот раз холоп попался толковый и, без лишних слов, продолжил наяривать свой член.'
                player.say '{i}Я рассматривала этот перевитый венами член и ласкала себя. Мне было комфортно и уютно, так что я полностью отдалась наслаждению. Пальчики угодливо ныряли в похотливую дырочку и смазывали соками выпирающий клитор. Я едва удерживалась от того, чтобы запихнуть этот член в себя.'
                player.say 'Давай же, кончай!'
                show expression 'images/events/request/help10.png' as tempPic
                player.say '{i}Мои пальцы двигались по клитору так быстро, что просто размазались в воздухе. Холоп застонал, и струя ударила мне прямо в лицо. Одурев от мужского запаха, я немедленно начала кончать, содрогаясь всем телом и громко постанывая. Вид кончающей рядом женщины вынуждал крестьянина не останавливаться и струйки семени продолжали орошать моё лицо и грудь.'
                show expression 'images/events/request/help7.png' as tempPic
                player.say 'Молодчина. Теперь одевайся и уходи.'
                player.say '{i}Я сидела перед всё ещё истекающим семенем членом, пытаясь придти в себя после оргазма. Мне ещё предстояло собрать с себя нужное мне вещество и заняться прочими делами.'
            else:
                python:
                    player.incLust(10)
                    if player.getCorr() < 50:
                        player.incCorr(5)
                    trigger[34] = 1
                show expression 'images/events/request/help3.png' as tempPic
                player.say '{i}Раздевшись, я вошла к мужчине, но обнаружила его на этот раз не у кровати, а у стены.'
                player.say 'Развлекаешься? Помощь требуется?'
                currRequest.char.say 'Как бы это, не откажусь конечно!'
                show expression 'images/events/request/help11.png' as tempPic
                player.say '{i}Я обратила внимание на размеры сегодняшнего холопа.'
                player.say 'Нехреновый ты себе хрен отрастил! Ладно, сейчас я повернусь к двери передом, а к тебе задом и, немного наклонюсь. Плошку в руки, и чтобы ни капли не пропало. И да, если этот член приблизиться ко мне ближе, чем на 10 сантиметров, пользоваться ты им будешь только для похода в туалет. Уяснил?'
                show expression 'images/events/request/help12.png' as tempPic
                currRequest.char.say 'А как же! - мужчина радостно закивал и уставился на мой зад.'
                player.say '{i}Я слегка раздвинула ягодицы, чтобы открылся как можно более соблазнительный вид, и срамное чавкание за спиной резко ускорилось. Вскоре я услышала надсадный хрип и довольный холоп протянул мне наполненную спермой ёмкость.'
                
        'Выдоить его' if player.getCorr() >= 50:
            $ s1.incLoy(100)
            if player.getLust() < 50:
                player.say '{color=#fff782}Я не чувствую особого желания, вступать в более близкие контакты, чем необходимо.'
                jump requestSpermMenu
            if trigger[35] == 1:
                menu:
                    'Подрочить ему':
                        $ trigger[32] = 0
                    'Поработать ножками':
                        $ trigger[32] = 1
                    'Отсосать':
                        $ trigger[32] = 2
                    'Отдаться':
                        $ trigger[32] = 3
                    'Трахнуть':
                        $ trigger[32] = 4
            $ s1 = currRequest.char
            if trigger[32] == 0:
                $ trigger[32] = 1
                $ player.incCorr(5)
                $ player.incLust(20)
                $ changetime(60)
                $ player.addItem(semen)
                $ player.addItem(semen)
                $ player.addItem(semen)
                show expression 'images/events/request/hand0.png' as tempPic
                player.say '{color=#fff782}Повинуясь наитию, я решила помочь селянину, и выдоить его самолично. Наверняка получится побольше на выходе, хоть и придётся постараться самой. Не теряя времени, я вошла в свою хижину.'
                show expression 'images/events/request/hand1.png' as tempPic
                player.say '{color=#fff782}[currRequest.char] стоял у окошка, и вдумчиво теребил свой член. Глядя на эту деревенскую простоту, на моём лице проскользнула улыбка.'
                player.say 'Эй, деревенщина, ты что-то долго копаешься, помощь требуется? - задорно окликнула я мужика.'
                s1.say 'А, что? - он обернулся, глядя на меня, но не переставая дрочить, - А, ну это... Как бы не откажусь!'
                show expression 'images/events/request/hand2.png' as tempPic
                player.say 'Ещё бы ты отказался! - шуточно возмутилась я, становясь на колени за мужиком и беря в руку его агрегат, - Ну ка, покажи, что ты так долго прятал от жёнушки!'
                player.say '{color=#fff782}Ощутив в руке приятную твёрдость, я начала неспешно водить ладошкой по члену, медленно оголяя пунцовую головку.'
                player.say '{color=#fff782}Нравится, развратник?'
                s1.say 'Ох и нежные у вас ручки, госпожа ведьма! - выдохнул счастливый селянин.'
                player.say 'Травница я, а не ведьма, дурак!'
                s1.say 'О-о-о, как скажете, только не останавливайтесь! - бёдра селянина пришли в движения, отвечая моим ласкам, - А то моя жена за весь день коров надоит, косой намашется, руки - как деревяшки, право слово!'
                player.say '{color=#fff782}Видя, что селянин готов кончить, я замедлила движения, лишь изредка подёргивая напрягшийся член, чтобы удержать его на краю.'
                s1.say 'О боже, кажется я сейчас...'
                player.say 'Даже и не думай! - прикрикнула я на мужчину, - Держись!'
                show expression 'images/events/request/hand3.png' as tempPic
                player.say '{color=#fff782}Насколько я уже знала, чем дольше мужчину я меньше, чем больше даст он в конце. Поэтому я игралась с его членом на протяжении целого часа, держа его на грани оргазма, пока он, наконец не разрядился нереальным количеством семени, которое я едва смогла собрать.'
            elif trigger[32] == 1:
                $ trigger[32] = 2
                $ player.incCorr(5)
                $ player.incLust(20)
                $ changetime(60)
                show expression 'images/events/request/hand0.png' as tempPic
                player.say '{color=#fff782}Вспоминая количество семени, которое в прошлый раз выдал мне крестьянин, я не сдержалась и вновь решила заняться добычей полезного ингредиента поплотнее. Войдя в свою хижину, я увидела, как [s1] сидит на полу и наяривает свой стручок перед плошкой.'
                show expression 'images/events/request/hand4.png' as tempPic
                player.say 'Ты не против, если я присоединюсь? - скидывая одежду спросила я, и, не дожидаясь разрешения, уселась позади холопа, прижимаясь своими грудями к загорелой спине крестьянина.'
                s1.say 'Ох! - только и смог вымолвить мужчина, когда моя рука нежно обхватила ствол его члена, и крепко сжала.'
                player.say 'Надеялся небось, что я зайду, а? - моя рука не спеша двигалась вдоль его хера.'
                s1.say 'Ну... Мне говорили, да, что иногда заходите, но я и не надеялся!'
                player.say 'Да? И что же обо мне ещё говорили? - плюнув на ладонь, я круговыми движениями начала гладить его головку. Мужчина отреагировал тихим стоном, а член начал слегка дрожать в моей руке.'
                s1.say 'Ну, говорили что вы красивая. Что позволяете смотреть, пока мы это. Но что сами не брезгуете помочь, такого не припомню! - мужчина замялся на мгновение, - А вы можете меня ножкой потрогать?'
                player.say 'Так я и так вроде тебя трогаю! - удивилась я, и для пущей уверенности, провела обнажённой ступнёй по его бедру.'
                s1.say 'Да нет, там. - И [s1] многозначительно показал на свой член.'
                show expression 'images/events/request/foot1.png' as tempPic
                player.say 'А ты не так прост, а? - приподняла я бровь, и, сев напротив селянина, положила пальчики своей ноги на основание его члена. Моя вторая нога начала массировать напрягшуюся от возбуждения мошонку.'
                s1.say 'Нет, не совсем так. Положи на хер всю ступню, - смущаясь попросил крестьянин.'
                show expression 'images/events/request/foot2.png' as tempPic
                player.say '{color=#fff782}Уже напрягаясь, я выполнила его указания, попытавшись попутно поласкать его. Крестьянин одобрительно закивал, и начал тереться о мою ногу, вызывая щекотливые ощущения.'
                player.say 'И долго мы этим планируем заниматься? - не останавливая движения спросила я. Мне начало откровенно нравится ощущать кожей его твёрдый, пульсирующий член.'
                show expression 'images/events/request/foot3.png' as tempPic
                player.say '{color=#fff782}Не говоря ни слова, [s1] встал, и пока я соображала, что, собственно происходит, его член начал извергать на меня потоки спермы, забрызгивая меня с ног до головы. Я просто лежала и ошарашенно смотрела, как пульсирующий меж моих ног член выплёскивал всё новые и новые струи.'
                s1.say 'Я что-то сделал неправильно? - видя моё выражение лица, спросил задрожавший от страха холоп.'
                show expression 'images/events/request/angry1.png' as tempPic
                player.say 'Неправильно? Неправильно? Да ты обкончал меня всю, как последнюю шлюху, хотя должен был спустить в эту плошку! Ты... Ты!!! - от переполнявшего меня возмущения, я просто потеряла дар речи.'
                s1.say 'П-п-п-простите! - заикающийся крестьянин примирительно поднял руки, и начал пятиться от меня.'
                player.say 'Пошёл нахуй отсюда! И чтобы я тебя больше не видела, понял? - в ярости я топнула ножкой и требовательно указала крестьянину на дверь.'
            elif trigger[32] == 2:
                $ trigger[32] = 3
                $ player.incCorr(10)
                $ player.incLust(-200)
                $ changetime(60)
                show expression 'images/events/request/blow1.png' as tempPic
                player.say 'Ну и чего ты тут завис в одиночестве? Чего не выполняем свои обязанности? - спросила я, поглядывая на вяло висящую письку селянина.'
                s1.say 'Это. Не получается что-то, всегда как кол стоял, а сейчас ни в какую! Ну честное слово! - расстроенно сообщил мужик.'
                player.say 'Хм. А если так? - спросила я, сбрасывая с себя робу.'
                show expression 'images/events/request/blow2.png' as tempPic
                player.say '{color=#fff782}Удивлённые от резкого поворота событий, глаза мужика расширились, а брови взлетели к середине лба. Взглядом он начал пожирать моё молодое тело, а его член спустя считанные секунды налился силой.'
                player.say 'Нравится? - развратно покачала я бёдрами, разглядывая вздрагивающий в такт сердцебиению член.'
                s1.say 'Ага! - видимо от такого зрелища, у мужика слегка упал и без того не выдающийся интеллект. На его лице застыло глупое, удивлённое выражение. Не факт, что он вспомнит как за член то держаться.'
                show expression 'images/events/request/blow3.png' as tempPic
                player.say 'Ну иди сюда, горемычный! - проворковала я, и нежно ухватила стоящий колом член за головку.'
                s1.say 'О-о-о! - словарный запас у парня явно не прибавился.'
                player.say '{color=#fff782}Я чувствовать пальчиками нежную кожу с выпуклыми венами, и не могла насытиться этими ощущениями. Я чувствовала, как внутри меня разгорается пожар сладострастия. Мне невыносимо захотелось посмотреть на этот ствол поближе.'
                show expression 'images/events/request/blow4.png' as tempPic
                player.say '{color=#fff782}Я опустилась на колени, и настойчиво трепещущий в моих руках член оказался прямо перед глазами. От него пахло резким, мускусным запахом и потом. Но мне нравилось. Я не смогла противиться желанию и лизнула его.'
                s1.say 'Ох! - крестьянин глупел на глазах. Но мне было глубоко плевать на его мозги. В моих руках находилась гораздо более занимательная часть.'
                player.say '{color=#fff782}Я лизнула член во второй раз, на вкус он был приятен и солоноват. Я прильнула к стволу губами и начала страстно посасывать, водя вдоль губами. Я облизывала язычком каждую венку и каждую морщинку. Мне хотелось большего.'
                show expression 'images/events/request/blow5.png' as tempPic
                player.say '{color=#fff782}Обхватив головку губами, я жадно запихала её в рот, плотно зажав пальцами основание члена, задеревеневшего от прилившей крови. Меж моих ног продолжал бушевать влажный пожар, и я засунула в свою киску два пальца, не переставая посасывать подрагивающий на языке орган.'
                show expression 'images/events/request/blow6.png' as tempPic
                s1.say 'А... О! - холоп положил свою лапищу мне на голову, вцепившись своими пальцами в мои волосы и стал сам двигать бёдрами, вгоняя член всё глубже.'
                player.say '{color=#fff782}Но мне было всё равно. Я плавала в розовом океане наслаждения, запах страсти туманил мне мозг, а непослушные пальцы терзали упругую плоть моего влагалища. По телу разливалась сладкая дрожь. Я с радостью отдалась на волю нехитрых движений члена в моём рту, не забывая посасывать и лобызать его по мере сил.'
                show expression 'images/events/request/blow7.png' as tempPic
                player.say '{color=#fff782}В тот момент, когда с громким рычанием мужик начал заливать мою глотку семенем, моё тело мгновенно отозвалось оргазмом. Закрыв глаза, я послушно глотала вливающуюся в меня жидкость, сотрясаясь в это время в собственном наслаждении. Лишь когда сперма начала выплескиваться из моего переполненного рта, я поняла, что наделала.'
                show expression 'images/events/request/anger2.png' as tempPic
                player.say 'Да какого, сука, хера, опять то? - фурией вскочила я на ноги, оттолкнув опешившего мужика, - Ты должен был кончить в плошку, чтобы я могла потом использовать твою сперму!'
                s1.say 'А вы разве её не пьёте всё равно? Ну там для молодости что-ли?'
                player.say 'Ты дебил? Дебил? - яростно уставилась я на недоумевающего селянина. В ответ тот лишь пожал плечами, очевидно не понимая медицинского термина.'
                player.say 'Дебил... - вздохнула уже спокойнее, - Вали отсюда подобру - поздорову.'
            elif trigger[32] == 3:
                $ trigger[32] = 4
                $ player.incCorr(10)
                $ player.incLust(-200)
                $ player.addItem(semen)
                $ player.addItem(semen)
                $ player.addItem(semen)
                $ changetime(30)
                show expression 'images/events/request/sex1.png' as tempPic
                player.say '{color=#fff782}Не долго думая, я просто скинула робу и во всём своём обнажённом великолепии подошла к мастурбирующему холопу, положив свои руки ему на плечи. Аккуратно переступив, я завела торчащий член себе между ножек, так, что он начал приятно тыкаться в мои губки.'
                s1.say 'Ох. Я как бы это. Это, можно, да? - заикаясь спросил мужик, слегка удивлённый моей непринуждённостью.'
                player.say 'Просто заткнись, хорошо? - я была слишком сильно возбуждена, чтобы терпеть его глупые высказывания.'
                player.say '{color=#fff782}Мои бёдра пришли в движение, губки заскользили по торчащему между ног стволу, покрывая его блестящей влагой. С губ сорвался тихий стон, когда головка члена задела клитор. Но я хотела большего.'
                show expression 'images/events/request/sex2.png' as tempPic
                player.say 'Подержи это, хорошо? - попросила я холопа, понимая ногу. Мужик охотно согнул руку, давая мне возможность расположиться по удобнее. Моя попка ходила вперёд и назад всё с большей амплитудой и блестящая головка члена иногда настойчиво застревала у входа во влагалище.'
                show expression 'images/events/request/sex3.png' as tempPic
                player.say '{color=#fff782}Наконец, я встала на цыпочки, и всем своим весом, наделась на торчащий между ног хер, позволяя головке войти в мою пещерку. Тело задрожало от наслаждения, когда стенки влагалища расступились перед входящей в него плотью. Мои ногти зацарапали по загорелой спине селянина, оставляя за собой белые полосы. [s1] зарычал в ответ, поднимая меня выше.'
                player.say '{color=#fff782}Мы начали двигаться в унисон. Он держал мою ногу, а я вцепилась в его шею. Член мерно скользил во мне, вызывая мурашки на спине. Из громко чавкающей вагины, по висящей в воздухе правой ноге покатилась густая капля. Я закусила губу, стараясь не закричать от наслаждения. Моя правая ножка настойчиво искала опору, поднимаясь всё выше.'
                show expression 'images/events/request/sex4.png' as tempPic
                player.say '{color=#fff782}[s1] дал опору для моей второй ноги, и заведя свои лапищи под попку, начал подбрасывать меня на своём члене. От каждого движения тот проникал всё глубже, до самого конца и упираясь в матку. Каждый толчок отзывался в теле маленькой вспышкой наслаждения. Влагалище плотно обхватывало сладко терзающий его орган.'
                player.say 'Да, вот так, да! - я уже не могла сдерживаться, и выкрикивала бессмысленные слова в ответ на животные рыки мужчины.'
                player.say 'Ар-р-р-р! - привыкшие к грубой работе руки без труда подбрасывали моё тело в воздух, и позволяли ему со всего маха падать вниз, прямо на торчащий вертикально член. Наши мускулы дрожали от напряжения яростного соития, из влагалища вырывались мелкие капли, размазываясь и блестя на волосатом животе крестьянина. Я чувствовала, что мой оргазм близок.'
                show expression 'images/events/request/sex5.png' as tempPic
                player.say '{color=#fff782}Я в очередной раз рухнула на полностью заполнивший меня член, и ощутила, как в матку бьют горячие струи семени. Будучи на грани, моё тело немедленно отозвалось ответным оргазмом. Напрягаясь, ноги вытянулись в струнку, влагалище бешено запульсировало, вынуждая меня сотрясаться в мелких конвульсиях. Спустя несколько секунд, начавший опадать член выскользнул из влагалища, и [s1] опустил меня прямо рядом с плошкой.'
                show expression 'images/events/request/sex6.png' as tempPic
                player.say '{color=#fff782}Я продолжала кончать, стоя на коленях перед плошкой, наполнявшейся выплёскиваемой из моего влагалища спермой.'
                s1.say 'Я всё правильно сделал? - участливо поинтересовался заботливый селянин.'
                player.say 'Бля-я-ядь, да! - вырвалось из меня, когда тело скрутила очередная конвульсия оргазма, а в миску упал большой сгусток семени.'
                s1.say 'Ну я пойду тогда? - мужик прижал к себе свою одежду.'
                player.say 'Ох... Иди... - меня начало отпускать, и кинув мимолётный взгляд на плескавшуюся подо мной сперму, я удивилась её количеству.'
            else:
                $ trigger[35] = 1
                $ player.incCorr(10)
                $ player.incLust(30)
                $ s1.incLoy(-100)
                show expression 'images/events/request/blow2.png' as tempPic
                player.say 'Ну как ты тут, [s1]? - окликнула я мужика, заходя в свою хату.'
                s1.say 'Ой! Я скоро закончу! - напугался селянин, и попытался прикрыть свой торчащий срам.'
                player.say 'Я тут подумала, может тебе помощь какая требуется? - лизнув палец, я ухватила себя за сосок, ощущая сладкое напряжение внизу живота.'
                s1.say 'Нет, нет! Я сам, всё сам! - стушевался [s1] и попытался продолжить.'
                player.say 'Ну уж нет! Я не готова доверить столько ответственный процесс, такому дилетанту как ты! На колени! - прикрикнула я на мужика.'
                show expression 'images/events/request/fuck1.png' as tempPic
                s1.say 'Нет, нет, пожалуйста, у меня семья, дети! Мужики, которые у вас побывали, они словно потеряли душу, на жён не смотрят, только о вас мечтают, пожалуйста! - но я была непреклонна. Уперев ему колено в шею, и резким движением повалив селянина на пол, я уселась сверху.'
                show expression 'images/events/request/fuck2.png' as tempPic
                player.say '{color=#fff782}Ухватив селянина за всё ещё напряжённый член, я направила его к влажному входу в свою вагину. Резко опустив бёдра, моё тело с наслаждением ощутило, как упругая плоть полностью заполнила меня.'
                player.say 'Ну что, плохо что ли? - я отвесила холопу пощёчину. Тот лишь жалобно захныкал, от чего мне стало как то противно. Очевидно, что он был труслив и боялся меня. Но начав, остановиться было сложно, поэтому я продолжила скакать на парне, ничуть не заботясь о чего состоянии, и отдавшись своим ощущениям.'
                show expression 'images/events/request/fuck3.png' as tempPic
                player.say '{color=#fff782}Наклонившись поближе, и отвернув от себя жалобное лицо селянина, я продолжала его трахать. Моя киска с удовольствием поглощала его член дюйм за дюймом, а потом выпускала назад. Клитор постоянно задевали кучерявые волосы лобка, от чего по телу пробегали здоровенные мурашки удовольствия.'
                player.say 'Хороший мальчик! Вот так вот, не спеши! - утешала я плачущую подо мной дылду, - Дай тётеньке своё семя!'
                s1.say 'Я теперь про-о-о-оклят! - завывал [s1], - Я теперь никого не полюблю-у-у-у-у!'
                player.say '{color=#fff782}В очередной раз плюнув на стенания придурка, я ускорилась, и обнаружила, что член во мне активно пульсирует, изливая своё содержимое внутрь. На миг я остановилась.'
                player.say 'Серьёзно? Уже? - с нескрываемым расстройством посмотрела я на парня, - У тебя что ли не было никого до меня?'
                s1.say 'У-у-у-у! - слёзы страха прочертили две дорожки на его лице.'
                player.say 'Подожди, я сейчас! - предупредила я парня, слезая с его члена, и подставляя под свою киску миску для семени.'
                show expression 'images/events/request/fuck4.png' as tempPic
                player.say '{color=#fff782}[s1] не преминул воспользоваться возможностью, и, схватив свои вещи умотал, сверкая своей голой задницей и оглашая окрестности горестным воем.'
                player.say 'Мда, не тот нонче мужик пошёл. Не тот, -  вздохнула я, огорчаясь скоропостижному исчезновению не самого плохого хера в моей жизни.'
        'Дождаться':
            show expression 'images/events/request/sperm.png' as tempPic
            player.say '{i}Я терпеливо дожидалась мужчину, пока он наполнял плошку у кровати. Наконец он вышел слегка вспотевший и измотанный и с гордой улыбкой протянул мне результаты своих трудов неправедных.'
            currRequest.char.say 'Вот! - {i}Он гордо протянул мне миску на дне которой плескалось немного белой жидкости.'
            player.say 'Мог бы и там оставить. Иди.'
            show expression 'images/events/request/spermAfter.png' as tempPic
            player.say '{i}Крестьянин ушёл, а я всё смотрела в плошку, от которой тянуло каким-то первобытным запахом, от которого теплело внизу живота.'
    python:
        for x in range(1,3):
            player.addItem(semen)
        player.incLust(5)
        changetime(30)
        move(curloc)
        