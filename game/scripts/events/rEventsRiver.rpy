label event_loc_river_0_1:
    $ s1 = getChar('female','young')
    $ s2 = getChar('male','young')
    show expression 'images/events/river/r1.png' as tempPic
    player.say '{color=#fff782}Прогуливаясь по реке, я заметила развлекающуюся парочку вдалеке. Интересно, стоит ли мне подходить поближе?'
    menu:
        'Подойти':
            if player.getCorr() < 10:
                player.say '{color=#fff782}Я считаю, что подглядывать за такими вещами не очень правильно. Я лучше пойду дальше.'
            else:
                $ player.incCorr(1)
                $ player.incLust(5)
                show expression 'images/events/river/r1_1.png' as tempPic
                player.say '{color=#fff782}Я подошла поближе. [s1.fname] и [s2.fname] перешли от активной прелюдии к активному сексу. Его член глубоко погружался в киску женщины, так что та не могла сдержать стонов.'
                s2.say 'Единый, ка же хорошо! Никогда не думала, что делать это в речке будет так классно!'
                s1.say 'Ну вот, а ты ещё сомневалась! Жар твоей щели и холод воды нехерово так заводят!'
                s2.say 'О-о-о! Какой ты пошлый, [s1.fname]!'
                player.say '{color=#fff782}Я чувствую растущее возбуждение, наблюдая за парочкой. Мне тоже захотелось ощутить горячий член внутри свой намокающей щёлки.'
                menu:
                    'Подрочить' if player.getCorr() > 20:
                        $ player.incLust(30)
                        $ changetime(20)
                        show expression 'images/events/river/r1_2.png' as tempPic
                        player.say '{color=#fff782}Сбросив с себя одежду и устроившись на камне неподалёку, я дотронулась до своего клитора, вздрогнув от приятных ощущений разлившихся по телу.'
                        show expression 'images/events/river/r1_1.png' as tempPic
                        s1.say 'Да, дорогой не останавливайся! Ты так глубоко входишь!'
                        s2.say 'По-моему твоя пещерка стала гораздо уже! Я с трудом сдерживаюсь!'
                        s1.say 'Это от воды. Ах! Она такая холодная! Ох! Да! От неё у меня всё сжимается внутри!'
                        show expression 'images/events/river/r1_2.png' as tempPic
                        player.say '{color=#fff782}Я с трудом различала доносившиеся до меня слова, но и их хватало, чтобы взвинтить мои ощущения до предела. С киски закапала влага, смешиваясь с ручной водой и уносясь вниз по течению. Пальцы лихорадочно терзали набухщий бугорок клитора. По телу пробегали приятные волны, предвещающие оргазм.'
                        show expression 'images/events/river/r1_1.png' as tempPic
                        s1.say 'Да-а-а-а!!!!'
                        player.say '{color=#fff782}Над рекой разнёсся крик полный экстаза, и кончающая девушка затряслась в руках своего любовника. Понимая, что ещё секунда, и они меня могут заметить, я с сожалением убрала руки от своей промежности и поспешила уйти.'
                    'Подойти к ним' if player.getCorr() > 45 and getPar(slaves,'loy') > 30:
                        show expression 'images/events/river/r1_2.png' as tempPic
                        player.say '{color=#fff782}Раздевшись и немного поласкав себя, я набралась смелости, чтобы подойти к совокупляющейся парочке.'
                        show expression 'images/events/river/r1_3.png' as tempPic
                        player.say '{color=#fff782}Мне не пришлось долго убеждать мужчину, что шесть дырок лучше, чем три, и вскоре я очутилась перед ним на коленях, страстно облизывая небольшой член.'
                        show expression 'images/events/river/r1_4.png' as tempPic
                        player.say '{color=#fff782}Напротив меня сидела [s1.fname] и старалась не отставать от моего стремительно двигающегося языка. Наши губы регулярно соприкасались на нежной коже разделяющего нас пениса.'
                        s1.say 'Где ты этому научилась? - на секунду оторвавшись от облизывания головки, спрсила меня девушка.'
                        player.say 'Книжек много читала! [s2.fname], мне кажется, или ты уже достаточно твёрд, чтобы удовлетворить нас обеих?'
                        show expression 'images/events/river/r1_5.png' as tempPic
                        player.say '{color=#fff782}[s2.fname] поставил нас в интересную позицию, снова войдя в свою любовницу и приткнув свой нос между моими ягодицами. Его язык оказался достаточно длинен, чтобы доставать до моей щелки, чем он и не преминул воспользоваться.'
                        player.say '{color=#fff782}Не знаю, как он не сбивался с ритма, но его длинющий язык двигался внутри моей киски совершенно в другом темпе, чем его член в щёлке любвницы снизу. Мне стращно захотелось оказаться снизу, о чём я не замедлила попросить.'
                        player.say '[s2.fname], я тоже хочу как [s1.fname], я тоже хочу твой член!'
                        show expression 'images/events/river/r1_6.png' as tempPic
                        player.say '{color=#fff782}[s1.fname] обиженно застонала, когда мокрый от выделений член выскользнул из её влагалища и погрузился в моё.'
                        player.say 'Да-а-а!'
                        player.say '{color=#fff782}Небольшой, но крепкий и горячий член легко вошёл в мою возбуждённую киску, приятно массируя трепещущие стенки влагалища. [s2.fname] умело пользовался своим хером, вводя его под разными углами и задевая какие то места во влагалище, от которых у меня начинали дрожать ноги и из горла рвались нечленораздельные крики.'
                        player.say '{color=#fff782}Движения моего тела сверху видимо возбуждали селянку не менее крепкого члена внутри. Её рука не спеша опустилась к набухшему от прилива крови клитору и принялась играть с ним. Чем активней я выражала своё удовольствие, тем шире становились её зрачки и тем активнее двигались пальцы в промежности.'
                        s1.say 'Любимый, я кончаю! Войди в меня!'
                        show expression 'images/events/river/r1_7.png' as tempPic
                        player.say '{color=#fff782}Мужчина не замедлил исполнить просьбу кончающей женщины и, резко вынув из меня свой член, ввёл его в сокращающуюся в оргазме киску. Будучи слишком возбуждённой, я уселась на лицо женщины и принялась тереться своей промежностью о её нос и губы.'
                        show expression 'images/events/river/r1_8.png' as tempPic
                        player.say '{color=#fff782}Громкие стоны внизу и оросившее мою спину горячее семя заставило мою киску неистово сокращаться и заливать лицо девушки смазкой. Я с трудом удержалась на коленях, неистово кончая от переполняющих меня ощущений и страсти. [s1.fname] пыталась выбраться из под меня, активно вертя головой, но её нос, постоянно задевающий клитор, просто не давал мне взять в себя в руки и перестать оргазмировать.'
                        $ s1.incLoy(30)
                        $ s2.incLoy(30)
                        player.say '{color=#fff782}Наконец, немного отходнув и помывшись, мы пошли каждый по своим делам. Мои отношения с этой парочкой стали крепче!'
                        python:
                            player.incCorr(5)
                            player.setLust(0)
                    'Уйти':
                        player.say 'Я лучше пойду, а то совсем заведусь и наделю глупостей.'
        'Не обращать внимания':
            pass
    $ move(curloc)
    
label event_loc_river_0_2:
    if hour not in [19,20,21]:
        $ skipEvent()
    show expression 'images/events/river/r2.png' as tempPic
    player.say '{color=#fff782}Прогуливаясь по реке, я машинально посмотрела в сторону заходящего солнца, и обмерла от изумления и раскрывшейся мне красоты. Огненно красный шар солнца медленно опускался за высокие деревья леса, и последним своим отсветом освещал белые горы в красноватые оттенки.'
    $ move(curloc)
    
label event_loc_river_0_3:
    $ s1 = getChar('female','young')
    $ player.incCorr(1)
    show expression 'images/events/river/r3.png' as tempPic
    player.say '{color=#fff782}С берега я заметила молодую женщину. [s1.fname] мощными гребками пересекала реку, эротично извиваясь в прохладной воде и предоставив лучам солнца ласкать свою обнажённую кожу.'
    player.say '{color=#fff782}"И не боится ведь, что мужики нагрянут... Так ведь и до греха дойти может..." - подумалось мне, пока я наблюдала за купающейся девушкой прислонившись к упавшему дереву.'
    $ move(curloc)
    
label event_loc_river_0_4:
    $ s1 = getChar('female','young')
    $ s2 = getChar('female','young')
    $ s3 = getChar('female','young')
    show expression 'images/events/river/r4.png' as tempPic
    player.say '{color=#fff782}"Девки в озере купались, хер берёзовый нашли..." - вспомнились мне слова из песни, когда я наблюдала за тремя селянками, притащившим к реке деревянный хер - "У плотника что ли заказывали?"'
    menu:
        'Уйти по тихому':
            player.say '{color=#fff782}Ну и нехай развлекаются. Как будто у меня других дел нет.'
        'Смотреть' if player.getCorr() > 10:
            $ player.incCorr(1)
            $ player.incLust(15)
            show expression 'images/events/river/r4_1.png' as tempPic
            s3.say 'Ну вы там что, девочки, собираетесь уже на жатву или нет? Сколько играться то с этим хером можно то? - спросила [s3.fname], стоя по пояс в воде и поглаживая себя по блестящим ягодицам.'
            show expression 'images/events/river/r4_2.png' as tempPic
            s2.say 'Ага, сама уже наигралась, а теперь всех торопишь, сейчас, [s1.fname] закончит и моя очередь попробовать это новое творение Франса! - глаза женщины жадно пожирали блестящий от вагинальных соков деревянный член, который ритмично скрывался в щелке её подружки.'
            s1.say 'Ах, ах, ох, кажется я сейчас обкончаюсь, девчонки! - Бёдра женщины ходили ходуном, вынуждая раскрасневшуюся щель погружаться всё глубже на деревянный член, издавая при этом влажные звуки.'
            show expression 'images/events/river/r4_3.png' as tempPic
            s1.say 'О-о-о, да-а-а! Кончаю!!! - [s1.fname] затряслась, её живот начало сводить ритмичным спазмом, и на и без того мокрый деревянный член выплеснулась очередная порция жидкости.'
            show expression 'images/events/river/r4_2.png' as tempPic
            s2.say 'Да ты никак обоссалась от радости, подруга? Слезай, моя очередь, только сейчас, сполосну его в речке.'
            show expression 'images/events/river/r4_1.png' as tempPic
            s3.say 'Ох, что-то вы меня распалили, давайте я по быстрому попрыгаю, и пойду на сенокос, а вы тут хоть до вечера развлекайтесь!'
            show expression 'images/events/river/r4.png' as tempPic
            player.say '{color=#fff782}Женщины начали ругаться за право обладания этим сомнительным артефактом деревенского мастерства, а я, насмотревшись на это представление, в слегка возбуждённом состоянии отправилась дальше.'
            $ changetime(30)
    $ move(curloc)
    
label event_loc_river_0_5:
    if trigger[25] == 0:
        $ trigger[25] = 1
        $ river_0_5 = getChar('female','young')
        show expression 'images/events/river/r5.png' as tempPic
        player.say '{color=#fff782}Я заметила [river_0_5.fname], которая голышом загорала на берегу реки. Не желая нарушать её уединения, я расположилась поодаль, стянув сапоги и дав ноющим ногам отдохнуть, под приятным ветерком с реки. К сожалению, вскоре я услышала мужские голоса, и мне пришлось уйти, чтобы никто не подумал, якобы я подглядываю.'
    elif trigger[25] == 1:
        $ s1 = getChar('male')
        $ s2 = getChar('male')
        $ trigger[25] = 2
        show river as tempPic
        s1.say '[s2.fname], как думаешь, [river_0_5.fname] сегодня снова загорает?'
        s2.say 'А хрен её знает! Пошли посмотрим на эту задницу Единого!'
        show expression 'images/events/river/r5_1.png' as tempPic
        player.say '{color=#fff782}[river_0_5], то ли не замечая, то ли не предавая значения подглядывающим гостям, продолжала запекать свою белоснежную задницу на полуденном солнце.'
        s1.say '[river_0_5], покажи свою щёлку получше! - закричал один из селянинов, быстро сунув руку в штаны, и начав там недвусмысленные движения.'
        river_0_5.say 'Пошли в задницу, половые голодранцы! На жён своих смотрите! - нехотя, [river_0_5] начала собираться, под раздосадованный вой обломавшихся мужчин.'
        show river as tempPic
        s2.say 'Ну кто тебя за язык тянул, [s1]? Какого хера ты вечно свой хавальник раскрываешь, когда надо молчать, а?'
        player.say '{color=#fff782}Я поспешно покинула своё укрытие, оставив переругивающихся селян позади.'
    elif trigger[25] == 2:
        $ s1 = getChar('male')
        $ s2 = getChar('male')
        show expression 'images/events/river/r5_2.png' as tempPic
        player.say '{color=#fff782}Я снова встретила [river_0_5], которая сидела на берегу, отмачивая свои ножки и задницу в тёплой, прибрежной водичке. Моё укрытие чуть выше по течению, было укромным и незаметным. Вскоре послышались голоса селян, идущих за водой.'
        s1.say 'О, [river_0_5], и тут ты! Говорят ты за так даёшь посмотреть на свою щёлку? Покажешь нам, а? - [s1] радостно пнул локтём в бок своего друга.'
        s2.say 'Ага, покажешь нам?'
        river_0_5.say 'Отрыжка Предвечного, да как же вы мне все надоели! - [river_0_5] начала громко ругаться и поносить на чём свет стоит двоих бедолаг.'
        menu:
            'Уйти':
                player.say '{color=#fff782}Видя, что ничего нового не произойдёт, я осторожно собралась и ушла. Но было бы у меня под рукой подходящее зелье, чтобы заставить её желать этих мужланов...'
            'Вылить в воду зелье фертильности' if player.hasElexir(fertility):
                $ trigger[25] = 3
                $ player.removeElexir(fertility)
                $ player.incCorr(1)
                player.say '{color=#fff782}Я осторожно вылила в воду зелье, стараясь, чтобы оно попало в поток, который омывал девушку, и стала ждать. Вскоре эликсир подействовал, видимо пробравшись сквозь слизистую влагалища. Щёки селянки покраснели, и тон разговора сменился.'
                river_0_5.say 'Мальчики, значит вы хотите посмотреть на меня, ну чтож, я поменяла решение. Что-то мне пошалить захотелось...'
                show expression 'images/events/river/r5_3.png' as tempPic
                'С этими словами, [river_0_5] встала на колени, и призывно оттопырила свой зад, показывая киску с набухшими и алыми, от прилившей крови, губами. В ответ она услышала вздох восхищения. Удивительно, но мужчины совершенно не стесняясь друг друга, сунули руки в свои портки принялись теребить своё хозяйство, не убирая взгляда от белоснежной задницы селянки. Решив, что дело сделано, Вальда отправилась по своим делам.'
    else:
        $ s1 = getChar('male')
        show river as tempPic
        player.say '{color=#fff782}Неподалёку, я услышала громкие стоны, перепутать которые ни с чем было нельзя.'
        menu:
            'Посмотреть' if player.getCorr() > 10:
                $ player.incLust(25)
                play movie "images/events/river/r5_4.webm" loop
                show movie with dissolve
                player.say '{color=#fff782}Довольно быстро я нашла источник звуков. [river_0_5], с затуманенным взглядом, сидела на селянине и своей киской дразнила его торчащий в небеса член. Её половые губы плавно двигались вдоль ствола, оставляя на нём блестящие подтёки влаги. Клитор постоянно находился в соприкосновении с грубой кожей холопского хера, и иногда по телу девушки пробегала волна удовольствия.'
                player.say 'Неужели это моё зелье до сих пор действует? - промелькнуло у меня в голове, но я быстро отбросила эту мысль. Похоже, что эликсир просто спустил тетиву желания, и теперь девушка, распробовав все прелести внимания и секса, на полную катушку наслаждалась жизнью.'
                s1.say 'Единый, [river_0_5], я уже хочу войти в тебя! Хватит издеваться надо мной!'
                river_0_5.say '[s1], но это же так приятно! К чему торопиться, у нас ещё полно времени, пока мой папаша заметит моё отсутствие. Ох... Просто наслаждайся, пока самая красивая девушка деревни объезжает твоего конька-горбунка.'
                player.say '{color=#fff782}Насчёт самой красивой я не уверена, но вот в том, что по разврату ты не последняя - это точно!'
                s1.say 'Ну пожалуйста! Ты такая мягкая... А этот запах, он просто сводит с ума! Дай мне в тебя войти, в конце концов, женщина!'
                river_0_5.say 'Ох, вы все одинаковые внутри, но такие разные снаружи! Ладно!'
                play movie "images/events/river/r5_5.webm" loop
                '[river_0_5] быстро повернулась задницей к мужчине, и сразу же вогнала мокрый от своих же соков ствол в свою вагину.'
                river_0_5.say 'О Единый, [s1], как же хорошо то! Твой хер буквально целует меня глубоко внутри!'
                '[s1] мог только рычать в ответ от удовольствия. Его бёдра инстинктивно двигались, помогая вбивать свой член всё глубже в щель девушки. Округу наполнили ещё более громкие стоны и хрипы, чем вы слышали до этого. Киска селянки громко хлюпала, принимая в себя "конька-горбунка". Вальда ощутила, как по её телу прокатилась волна возбуждения, а между ног приятно увлажнилось.'
                river_0_5.say 'Да, да! Засунь его поглубже! Ещё! Не останавливайся! О Единый-Всемилостивый, я кончаю!'
                hide movie with dissolve
                stop movie
                show expression 'images/events/river/r5_6.png' as tempPic
                '[s1] хрипло зарычал, и засадил свой небольшой член как можно глубже в жадное влагалище селянки. Вы увидели знакомую пульсацию, и из щёлки девушки начала вытекать белая жидкость. Сама [river_0_5] откинулась назад, на сильные руки односельчанина и тихо подрагивала в послеоргазменном состоянии. Её руки бессознательно теребили клитор, выжимая из маленького бугорка последние капли удовольствия.'
                river_0_5.say 'Ты.... Ты... Ты был бесподобен! У меня ещё ни с кем так не было!'
                player.say '{color=#fff782}Трудно в это поверить, учитывая что я тут не каждый день, а вот ты... - подумала я, и начала собираться.'
            'Уйти':
                pass
    $ changetime(30)
    $ move(curloc)
    
label event_loc_river_0_6:
    $ s1 = getChar('male','young')
    show expression 'images/events/river/r6.png' as tempPic
    player.say '{color=#fff782}На пристани, я увидела селянина, с умиротворением глядевшего в воду.'
    menu:
        'Уйти по тихому':
            player.say '{color=#fff782}Ну тупит он в воду и тупит. Мне то какое дело?'
        'Сесть рядом':
            $ s1.incLoy(10)
            $ player.applyEffects({concentration:80})
            $ changetime(60)
            show expression 'images/events/river/r6_1.png' as tempPic
            player.say '{color=#fff782}Я присела рядом с мужчиной и тоже начала наблюдать за рекой. Медленно, все мои проблемы отходили на второй план и ощущала, что глубже раскрываюсь перед Той стороной. Мы так и сидели в течение часа, ни говоря друг другу ни слова. Каждый думал и мечтал о чём то своём.'
        'Столкнуть его в воду':
            $ s1.incLoy(-50)
            show expression 'images/events/river/r6_2.png' as tempPic
            player.say '{color=#fff782}С хохотом я столкнула селянина в реку, и стала наблюдать, как тот выплывает.'
            s1.say 'Какого же хера ты делаешь, чертовка? Чем я тебе помешал то?'
            player.say 'Так я о тебе забочусь! День такой солнечный, а ты сидишь на самом солнцепёке без движения, вот я и подумала, что тебя удар хватил! А теперь вижу, всё в порядке, но ты поплавай ещё, охладись немного!'
            s1.say 'Ну я тебя сейчас, рыжая! Только доплыву!'
            player.say 'Ага, как же! Бывай, пловец! - я поднялась, и спешно ушла от раздражённого мужчины.'
    $ move(curloc)