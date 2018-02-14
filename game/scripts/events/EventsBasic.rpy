init:
    image centeredText = ParameterizedText(xalign=0.5, yalign=0.5, style = 'bigRed')
    
label brewTutorial:
    $ clrscr()
    show expression 'images/events/basic/brew1.png' as tempPic
    player.say 'Так, надо припомнить, как меня учили варить. В первую очередь, мне надо выбрать, что именно я буду использовать в качестве спиртовой основы для своего зелья.'
    show expression 'images/events/basic/brew2.png' as tempPic
    player.say 'После выбора основы, можно открыть один из многих ящичков моего алхимического стола, и посмотреть конкретные ингредиенты под каждый эффект. Ну пусть в этот раз будет регенерация! Очень полезный эффект, позволяющий быстрее заживлять раны на теле.'
    show expression 'images/events/basic/brew3.png' as tempPic
    player.say 'После этого у меня мне остаётся выбрать любой ингредиент из небольшой кучки. Все они будут обладать нужным мне эффектом. Ну пусть будет красная лоза.'
    show expression 'images/events/basic/brew4.png' as tempPic
    player.say 'Чтобы случайно не сварить из красной лозы зелье с эффектом густокровия, мне надо правильно направить потоки маны и сконцентрироваться на нужном эффекте.'
    show expression 'images/events/basic/brew5.png' as tempPic
    player.say 'Несмотря на то, что я могла продолжать добавлять ингредиенты, я могу сразу перейти на дестиляцию. Второй эффект красной лозы - густокровие, всё ещё присутствует как побочный эффект в моём зелье. Чтобы убрать его, нужно добавить ещё один ингредиент с противоположным эффектом.'
    show expression 'images/events/basic/brew6.png' as tempPic
    player.say 'Например мерцающий колокольчик, у которого есть эффект кровотечения, который является антиподом густокровия.'
    show expression 'images/events/basic/brew7.png' as tempPic
    player.say 'Всё, после того, как мы избавились от густокровия, можно забирать получившееся зелье!'
    $ move(curloc)
    
label sleep:
    $ clrscr()
    python:
        global hour, ptime, last_sleeped
        
        player.incEnergy(1000)
        advancetime(1)
        player.reset()
        
        renpy.jump('loc_dreams')
        
label loc_dreams:
    $ clrscr()
    if player.hasItem(furArmor.name) and player.hasItem(boots.name) and trigger[40] == 0:
        jump koven1
        
    if player.hasItem(horseJizz.name) and player.hasItem(marion.name) and player.hasItem(stick.name) and trigger[40] == 1:
        jump koven1_1
        
    if hour in range(6,23):
        show expression 'images/events/basic/dreamDay.png' as tempPic
    else:
        if player.getLust() > 80:
            show expression 'images/events/basic/dreamNaked.png' as tempPic
        else:
            show expression 'images/events/basic/dreamNight.png' as tempPic
    if player.hasEffect(intoxication):
        player.say '{color=#fff782}Я провалилась в пьяный сон полный кошмаров. На утро я проснулась со страшным сушняком и голодом.'
    else:
        player.say '{color=#fff782}В это раз мне ничего не снилось и, провалившись в ласковые объятия сна, я отлично выспалась.'
    $ move(curloc)
    
label death:
    $ clrscr()
    if hour in range(6,23):
        show expression 'images/events/basic/deathDay.png' as tempPic
    else:
        show expression 'images/events/basic/deathNight.png' as tempPic
    $ clrscr()
    show black
    player.say '{color=#fff782}В тот день я умерла. Умерла по настоящему, но не насовсем. Я долго блуждала в темноте, пытаясь понять где я нахожусь, пока не услышала чей то голос.'
    show centeredText 'ПОСЛУЖИ ЕЩЁ!' at truecenter
    with dissolve
    pause 5
    hide centeredText
    with dissolve
    player.say '{color=#fff782}Какая то сила потащила меня, коверкая мою душу и выдирая из неё крохи энергии, чтобы залить их в безжизненное тело. Я очнулась. Всё нестерпимо болело и я ощущала пустоту внутри. Словно что-то, что делало меня самой собой вдруг безвозвратно ушло.'
    python:
        player.incPrana(25)
        for x in player.skills:
            player.skills[x] = player.skills[x] - rand(10,30)
            player.skills[x] = max(0,player.skills[x])
        move(curloc)
        
label meditation:
    $ clrscr()
    if hour in range(6,23):
        show expression 'images/events/river/meditationD.png' as tempPic
    else:
        show expression 'images/events/river/meditationN.png' as tempPic

    menu:
        'Одежда сковывает и отвлекает во время медитации. С другой стороны вид моего обнажённого тела будет привлекать не нужные взгляды.'
        'Раздеться и медитировать' if player.getCorr() > 20:
            if hour in range(6,23) and rand(1,3) >= 2:
                show expression 'images/events/river/medCatched.png' as tempPic
                player.say '{color=#fff782}Только я разделась и начала входить в транс, как услышала с другого берега радостные крики и улюлюкание. Местная детвора живописно восхищалась моими формами! Мне ничего не оставалось, как прикрыться рукой и начать быстро одеваться.'
            else:
                if hour in range(6,23):
                    show expression 'images/events/river/medNakedD.png' as tempPic
                else:
                    show expression 'images/events/river/medNakedN.png' as tempPic
                player.say '{color=#fff782}Скинув с себя одежду, я медленно вхожу в транс. В меня буквально врывается Изнанка, наполняя душу силой. Спустя час я чувствую себя отдохнувшей и сконцентрированной.'
                python:
                    player.applyEffects({concentration:80})
                    player.incEnergy(120)
                    changetime(rand(50,70))
        'Медитировать в одежде':
            if hour in range(6,23):
                show expression 'images/events/river/medClothedD.png' as tempPic
            else:
                show expression 'images/events/river/medClothedN.png' as tempPic
            if rand(1,2) == 1:
                player.say '{color=#fff782}Я медленно вхожу в транс и замираю от холодного прикосновения Изнанки. Моя связь с потусторонним растёт. Открыв глаза, я вижу что прошло около часа.'
                python:
                    player.applyEffects({concentration:50})
                    player.incEnergy(120)
                    changetime(rand(50,70))
            else:
                player.say '{color=#fff782}Целый час я сидела, пытаясь сконцентрироваться и расширить канал с Изнанкой, но у меня ничего не получилось.'
                $ changetime(60)
    $ move(curloc)

label unconscious:
    $ clrscr()
    if hour in range(6,23):
        show expression 'images/events/basic/deathDay.png' as tempPic
    else:
        show expression 'images/events/basic/deathNight.png' as tempPic
    player.say '{color=#fff782}Я потеряла сознание от усталости. Слишком измотала сама себя. От долгого лежания на земле, я немного простыла, что не самым лучшим образом сказалось на моём здоровье.'
    python:
        player.incPrana(-5)
        changetime(120)
        player.incEnergy(100)
        move(curloc)
        
label drunk:
    $ clrscr()
    if hour in range(6,23):
        show expression 'images/events/basic/deathDay.png' as tempPic
    else:
        show expression 'images/events/basic/deathNight.png' as tempPic
    player.say '{color=#fff782}Я опьянела настолько, что уснула прямо на земле. Сон на холодной траве не очень хорошо сказался на моём здоровье.'
    python:
        player.incPrana(-5)
        changetime(120)
        player.incEnergy(100)
        move(curloc)
        
label hotSpringsNoBoots:
    $ clrscr()
    show expression 'images/events/basic/hotSpringsNoBoots.png' as tempPic
    player.say '{color=#fff782}Чёрт! Здесь очень-очень жарко! Земля прямо пышет пламенем! Мне нужна какая-нибудь защита для ног! Нужно навестить кузнеца, может быть он что-то придумает.'
    $ move(curloc)
        
label hotSpringsBoots:
    $ clrscr()
    show expression 'images/events/basic/hotSpringsBoots.png' as tempPic
    player.say '{color=#fff782}Здесь очень жарко! Я надеваю свои подбитые металлом сапоги и снимаю робу. Обнажённое тело поможет охладиться, а сапоги неплохо защитят ноги.'
    $ move(curloc)
    
label hillsNoFur:
    $ clrscr()
    show hills
    player.say 'Во имя Пожирателя! Да как же тут холодно то! Тут невозможно находится без тёплой одежды! Надо скорее возвращаться и заглянуть в местную лавку! \nХмм, а это что?'
    python:
        hillsNoFur_item = choice(ingHills)
        player.addItem(hillsNoFur_item)
    'Вальда нашла [hillsNoFur_item.name]'
    $ changetime(60)
    $ move(curloc)
    
label horsePower:
    $ clrscr()
    show cellar as tempPic
    player.say 'Хмм. У меня появилось зелье лошадиной силы... Я слышала, что оно может оказывать странный эффект на женщин, но все упоминания как то обходят опсиание этого эффекта стороной. Просто пишут, что не стоит его употреблять. А как я могу советовать какие то зелья не испробовав их самой?'
    menu:
        'Попробовать зелье':
            show expression 'images/events/basic/horsePower_1.png' as tempPic
            $ player.removeElexir(impotenceCure)
            $ player.incLust(-100)
            $ trigger[26] = 1
            'Вальда опрокинула бутылочку Лошадиной силы, и замерла в ожидании ощущений. Первое ощущение было - сблевать всё на пол, ибо вкус оказался отвратительнейший. Но волевым усилием молодая колдунья подавила его.'
            player.say 'Единый... Такое чувство, словно меня выворачивают наизнанку там, внизу... Чёрт, как больно то!'
            'Вальда сунула руку себе под робу, пытаясь ощупать то, что может так невыносимо болеть. На её лице немедленно отразился испуг. Желая проверить свои догадки, она немедленно скинула робу, чтобы рассмотреть себя получше.'
            show expression 'images/events/basic/horsePower_2.png' as tempPic
            player.say 'Мать моя женщина... Да что же это такое то?'
            'В том месте, где должна была находится небольшая и аккуратная вагина, торчал неслабых таких размеров хер. Он вздрагивал в такт сердцебиению и налившаяся, покрасневшая головка буквально молила о том, чтобы её поласкали.'
            player.say 'Я не могу... Так хочется... Надо его убрать! Так, сейчас я сварю зелье... Нет. Я не смогу сварить даже куриный суп в таком состоянии. Надо... О Предвечный, как же хорошо!'
            show expression 'images/events/basic/horsePower_3.png' as tempPic
            player.say '{color=#fff782}Я случайно дотронулась до головки, в том месте, где она присоединялась к стволу, и задрожала от пронзивших меня чувств. Моё тело вздрогнуло и приятная волна разлилась от кончика члена до грудей, заставив ягодицы задрожать от удовольствия. Не в силах противостоять желанию, я сделала это снова и снова. Я начала поглаживать головку двумя пальчиками, наслаждаясь переполнявшими меня чувствами. Мой указательный пальчик массировал уздечку, а большой трогал саму толстую часть. Член словно задеревенел, и, несмотря на то, что я перестала отчётливо ощущать свои прикосновения, непрекращающиеся волны удовольствия не давали мне остановиться. От каждого прикосновения внутри меня что-то сжималось, и я поняла, что у меня наступает мой первый, мужской оргазм.'
            show expression 'images/events/basic/horsePower_4.png' as tempPic
            'Тело Вальды изогнулось в удовольствии, и пульсирующий член начал выдавать струю за струёй, покрывающие ведьмочку с головы до ног.'
            player.say 'Да! О, как же хорошо! Никогда такого не испытывала! Да!'
            player.say '{color=#fff782}Я оттянула кожу с головки подальше, чтобы видеть эту красоту меж моих ног, и вздрогнула в последний раз, когда окончательный спазм плюнул мне в лицо горячей спермой.\nОтстрелявшись, член стал опадать. Он становился всё меньше и меньше, пока не исчез совсем.'
            show expression 'images/events/basic/horsePower_5.png' as tempPic
            player.say '{color=#fff782}Я лежала, смотря в каменный потолок, вновь и вновь вспоминая пережитые мгновения.'
            player.say 'Так вот, что мужики чувствуют, когда кончают... Неудивительно, что они такие озабоченные.'
        'Оставить пробу на время':
            player.say 'Да, сейчас нет времени, всё потом.'
            $ move('loc_home')
    $ move(curloc)
            
label no_money:
    $ clrscr()
    show expression "images/locations/shop.png" as tempPic
    $ s1 = aaron
    s1.say 'Не, не, деточка. Сначала деньги покажи! - Аарон решительно убрал мою руку с ящика, в котором лежали различные травки.'
    player.say 'Может быть в долг? - заискивающе спросила я.'
    s1.say 'Ты в долг лечишь? Я думаю что нет, иначе бы по миру пошла с протянутой рукой. Вот и мне надо всех кормить, так что будь добра, иди подобру - поздорову!'
    player.say 'А как же присказка, что "Покупатель всегда прав?"'
    s1.say 'Покупатель без денег? Не смеши меня! Вон из моей лавки!'
    $ move('loc_village')
    
label heromancy:
    $ clrscr()
    show expression 'images/events/basic/heroStart.png' as tempPic
    if trigger[27] == 0:
        $ trigger[27] = 1
        player.say '{color=#fff782}Я решила слегка потренироваться в навыке эмпатии, внушив селянам, что я, якобы, могу читать судьбы по линиям на руках. Конечно, ничего читать в этом узоре я не могу, да и не встречала ни в одной книжке, что это вообще возможно. В любом случае, что-то узнать я смогу, если получится увидеть ауру человека. Авось и пара монеток перепадёт за "предсказание".'
    menu:
        '{color=#fff782}Я встала у таверны, и изредка покрикивая, что готова предсказать судьбу по руке, стала ждать.'
        'Ждать клиента':
            jump heromancyDo
        'Заняться внушением' if player.getMana() >= 50:
            $ changetime(60)
            $ player.incMana(-50)
            call screen infusionChars
        'Закончить с предсказаниями':
            $ move(curloc)

label heromancyDo:
    python:
        s1 = getChar()
        changetime(30)
    if player.getMana() < 10:
        player.say '{color=#fff782}Я почти потеряла связь с Изнанкой. Я не смогу воспользоваться эмпатией. Мне надо отдохнуть и помедитировать.'
        $ move(curloc)
    if lt() != 1:
        player.say '{color=#fff782}Сомневаюсь, что найду хоть одного клиента ночью.'
        $ move(curloc)
    if rand(1,2) == 1 or development == 1:
        $ player.incMana(-15)
        if s1.getSex() == 'male':
            show expression 'images/events/basic/heroMale.png' as tempPic
            s1.say 'Ну, рыжая, погадай ка мне, да расскажи, что меня ждёт, - спросил [s1], протягивая мне руку, которую я аккуратно взяла, пытаясь рассмотреть его мысли.'
        else:
            show expression 'images/events/basic/heroFemale.png' as tempPic
            s1.say 'Ну, рыжая, погадай ка мне, да расскажи, что меня ждёт, - спросила [s1], протягивая мне руку, которую я аккуратно взяла, пытаясь рассмотреть её мысли..'
        if player.getSkill('empathy') < rand(0,100):
            $ s1.incLoy(-1)
            $ player.incSkill('empathy')
            $ temp = player.getSkill('empathy')
            player.say '{color=#fff782}У меня ничего не вышло... Поэтому я просто наплела с три короба что-то про дальнюю дорогу и казённый дом. Доверия мои слова не вызвали, поэтому никакой награды за свою предсказание я не получила. Ну кроме того, что мой навык слегка увеличился до [temp].'
        else:
            $ player.incMoney(rand(1,5))
            $ s1.incLoy(10)
            if s1.getSex() == 'male':
                player.say '{color=#fff782}Коснувшись грубой руки селянина, я открыла себя Изнанке, и поток его эмоций, мыслей и желаний полностью захватил моё сознание!'
                if player.getSkill('empathy') > rand(0,200) or development == 1:
                    $ player.applyEffects({faith:1})
                    $ tryEvent('loc_heromancyMale')
                label herMaleJump:
                player.say '{color=#fff782}Основываясь на новой информации, я без проблем смогла обмануть доверчивого мужчину, выдав желаемое им за действительное. Он даже радостно расстался с парой срубо из своего кошелька.'
            else:
                player.say '{color=#fff782}Коснувшись небольшой руки женщины, я открыла себя Изнанке, и поток её эмоций, мыслей и желаний полностью захватил моё сознание!'
                if player.getSkill('empathy') > rand(0,200) or development == 1:
                    $ player.applyEffects({faith:1})
                    $ tryEvent('loc_heromancyFemale')
                label herFemaleJump:
                player.say '{color=#fff782}Основываясь на новой информации, я без проблем смогла обмануть доверчивую крестьянку, нагородив ей с три короба. Она даже радостно рассталась с парой срубо из своего кошелька.'
            
    else:
        python:
            changetime(30)
        player.say '{color=#fff782}Я прождала хоть кого-нибудь целых пол часа, но никто так не заинтересовался моими услугами. Не уверена, стоит ли ждать ещё.'
    jump heromancy
    
label infusionDo:
    $ s1 = showChar
    if s1.getSex() == 'male':
        show expression 'images/events/basic/heroMale.png' as tempPic
    else:
        show expression 'images/events/basic/heroFemale.png' as tempPic
    menu:
        'Наконец, я увидела того, кого хотела, и, настойчиво предлагая свои услуги гадалки, вцепилась ему в руку.\n
        Раскрыв себя Изнанке, я установила прочный контакт с сознанием пациента и приготовилась влить ему одно из воспоминаний.'
        'Воспоминание храбрости':
            $ s1.setSkill('will', s1.getSkill('will') + infusionMod)
            if s1.getSex() == 'male':
                show expression 'images/events/basic/memory1.png' as tempPic
                'Я внушила крестьянину, что он однажды, служа в войсках местного барона, смог одним ударом победить внезапно напавшего на него волка.\n
                Я почувствовала, что он стал немного храбрее.'
            else:
                show expression 'images/events/basic/memory2.png' as tempPic
                'Я внушила селянке, что однажды, когда на её ферму напала стая волков, она одела отцовские доспехи и в одиночку отбила нападение.\n
                Я ощутила, что она стала немного храбрее.'
        'Воспоминание трусости':
            $ s1.setSkill('will', s1.getSkill('will') - infusionMod)
            if s1.getSex() == 'male':
                show expression 'images/events/basic/memory3.png' as tempPic
                'Я внушила крестьянину, что до смерти пугают собаки, волки, даже безобидные лисы.\n
                Я почувствовала, что он стал немного трусливее.'
            else:
                play movie 'images/events/basic/memory4.webm' loop
                show movie with dissolve
                'Я внушила селянке, что на неё напал обезумевший без самки пёс-овцепас, когда она возвращалась с полей. Его здоровенный, таранящий её киску красный член, она не сможет забыть ещё долго, что вынудит её постоянно опасаться за свою честь.\n
                 Я почувствовала, что селянка стала немного трусливее.'
                stop movie
                hide movie
        'Воспоминание здоровья':
            $ s1.setSkill('health', s1.getSkill('health') + infusionMod)
            if s1.getSex() == 'male':
                show expression 'images/events/basic/memory5.png' as tempPic
                'Я внушила крестьянину, что он смог подебить какого то страшного лесного монстра голыми руками!\n
                Тело следует за разумом, и крестьянин волей-неволей станет сильнее.'
            else:
                show expression 'images/events/basic/memory6.png' as tempPic
                'Я внушила селянке, что она любит бегать по утрам. Прям как проснётся, сразу бежит, то к соседке, то на поле. Вообще, передвигаться бегом - её любимое занятие.\n
                Крестьянка определённо станет здоровее после этого.'
        'Воспоминание недуга':
            $ s1.setSkill('health', s1.getSkill('health') - infusionMod)
            if s1.getSex() == 'male':
                show expression 'images/events/basic/memory7.png' as tempPic
                'Я внушила крестьянину, что он в детстве на спор спрыгнул с высого утёса в воду и сильно поломался.\n
                Тело следует за разумом, и крестьянин будет страдать от выдуманных недугов.'
            else:
                show expression 'images/events/basic/memory8.png' as tempPic
                'Я внушила селянке, что у неё злобный отец. И однажды, когда слишком сильно подвела глаза углём, для похода на сельскую вечеринку, он избил её так, что она неделю не могла встать с кровати.\n
                Тело следует за разумом, и крестьянка будет страдать от выдуманных недугов.'
        'Воспоминание развратности' if player.getCorr() > s1.getCorr():
            $ s1.incCorr(infusionMod)
            if s1.getSex() == 'male':
                show expression 'images/events/basic/memory9.png' as tempPic
                'Я внушила крестьянину, что он в детстве любил подглядывать за своей матерью, когда она переодевалась. И даже сейчас, попрошествию стольких лет, он до сих пор не испытывает за это угрызения совести.\n
                Я почувствовала, что он стал немного развратнее.'
            else:
                $ temp = rand(1,2)
                if temp == 1:
                    show expression 'images/events/basic/memory10.png' as tempPic
                    'Я внушила селянке, что однажды она бесстыдно обнажённой вышла из своей комнаты, и, помахивая трусиками перед отцовским армейским другом, спросила куда делось её новое платье.\n
                    Я почувствовала, что крестьянка стала немного развратнее.'
                elif temp == 2:
                    play movie 'images/events/basic/memory10_1.webm' loop
                    show movie with dissolve
                    'Я внушила селянке, что однажды она согласилась переспать не только со своим парнем, но и с его другом одновременно. Сладкие воспоминания об этом опыте до сих пор заставляют её мгновенно увлажняться внизу.\n
                    Я почувствовала, что крестьянка стала немного развратнее.'
                    stop movie
                    hide movie
        'Воспоминание святости':
            $ s1.incCorr(-infusionMod)
            if s1.getSex() == 'male':
                show expression 'images/events/basic/memory11.png' as tempPic
                'Я внушила крестьянину, что он любит посещать местную церковь Единого ухаживать за страждущими и больными.\n
                Я почувствовала, что он стал менее развратен.'
            else:
                show expression 'images/events/basic/memory11.png' as tempPic
                'Я внушила селянке, что она любит посещать местную церковь Единого ухаживать за страждущими и больными.\n
                Я почувствовала, что она стала менее развратна.'
    $ move(curloc)