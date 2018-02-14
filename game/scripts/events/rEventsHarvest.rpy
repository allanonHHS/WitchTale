label event_loc_harvestingForest_0_1:
    show expression 'images/events/forest/1.png' as tempPic
    player.say '{color=#fff782}Раздвинув кустики, я потянулась к особо крупному соцветию нужных мне растений. Но, к сожалению, не удержала равновесия и упала лицом прямо на острые колючки! Чёрт, как же больно то!'
    python:
        player.incPrana(-5)
    $ move(curloc)
    
label event_loc_harvestingForest_0_2:
    show expression 'images/events/forest/2.png' as tempPic
    player.say '{color=#fff782}Увлёкшись сбором растений, я не заметила в кустиках змею и она меня укусила! ЧЁрТ ЧЁРТ ЧЁРТ! Надо скорее принять противоядие!'
    python:
        player.applyEffects({poison:25})
    $ move(curloc)
    
label event_loc_harvestingForest_0_3:
    show expression 'images/events/forest/3.png' as tempPic
    player.say '{color=#fff782}Собирая ингредиенты возле трухлявого пенька, я сильно рассадила руку о торчащую щепку! Рукав робы начал моментально пропитываться кровью. Надо скорее остановить кровь!'
    python:
        player.applyEffects({bleeding:25})
    $ move(curloc)
    
label event_loc_harvestingForest_0_4:
    show expression 'images/events/forest/4.png' as tempPic
    player.say '{color=#fff782}Забравшись глубоко в лес, в поисках ингредиентов, я чуть не попалась волчьей стае на глаза. Затаившись в кустах, я просидела несколько часов, стараясь не дышать и молясь, чтобы ветер не подул мне в спину.'
    $ advancetime(1)
    $ move(curloc)
    
label event_loc_harvestingForest_0_5:
    show expression 'images/events/forest/5.png' as tempPic
    player.say '{color=#fff782}Неожиданно мне на спину прыгнул дикокрыс. Робу он, конечно, порвать не смог, но оставил мне на память несколько царапин на спине.'
    $ player.incPrana(-5)
    $ move(curloc)
    
label event_loc_harvestingForest_0_6:
    show expression 'images/events/forest/6.png' as tempPic
    player.say '{color=#fff782}Неудачно наклонившись, я подвернула ногу. Мне пришлось снять сапоги и массировать её около часа, прежде чем я снова смогла пойти дальше.'
    $ changetime(60)
    $ move(curloc)
    
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################

label event_loc_harvestingHills_0_1:
    show expression 'images/events/hills/1.png' as tempPic
    player.say '{color=#fff782}Я оступилась и съехала с горки, пребольно подвернув при этом ногу. Надо быть осторожней. Я, всё таки, не горная коза, и, если сломаю себе ногу, останусь тут навсегда.\nЯ потратила кучу времени, массируя опухающее колена и ожидая, пока уляжется боль.'
    python:
        player.incPrana(-10)
    $ advancetime(1)
    $ move(curloc)
    
label event_loc_harvestingHills_0_2:
    show expression 'images/events/hills/2.png' as tempPic
    player.say '{color=#fff782}Увлёкшись собирательством, я не заметила как совсем недалеко от меня затрещали ветки и послышался волчий вой. Благо волки были сыты, и тоже не обратили на меня внимания. Но, чтобы не рисковать, я на карачках начала уползать подальше от стаи. Всё закончилось благополучно, за исключением потери кучи времени на отступление.'
    $ advancetime(1)
    $ move(curloc)
    
###########################################################################################################################
###########################################################################################################################
###########################################################################################################################

label event_loc_harvestinghotSprings_0_1:
    show expression 'images/events/hotSprings/1.png' as tempPic
    player.say '{color=#fff782}Наклонившись к большому соцветию споровых сумок я не заметила притаившийся среди них ядобрызг, который выпустил облачко яда от моего дыхания. Я чувствую себя слегка опьянённой.'
    $ player.applyEffects({intoxication:25})
    $ move(curloc)
    
label event_loc_harvestinghotSprings_0_2:
    show expression 'images/events/hotSprings/2.png' as tempPic
    player.say '{color=#fff782}Потянувшись за очередной травкой, я неловко расставила ноги над расщелиной. Внезапно обжёгший меня столбик пара стал мне напоминанием о том, что стоит быть аккуратнее.'
    $ player.incPrana(-5)
    $ move(curloc)
    
label event_loc_harvestinghotSprings_0_3:
    show expression 'images/events/hotSprings/3.png' as tempPic
    player.say '{color=#fff782}Увлёкшись собирательством, я не услышала предательское постукивание хитиновых лапок приближающегося гигантского паука. Заметила я его только тогда, когда с тихим щелчком его задние лапы распрямились и он взмыл в воздух.'
    menu:
        'Попытаться увернуться':
            if rand(1,3) == 1:
                show expression 'images/events/hotSprings/3_1.png' as tempPic
                player.say '{color=#fff782}Мне не удалось увернуться, и я почувствовала, как ядовитые жвалы процарапали мою кожу, впрыскивая яд. Сделав своё дело, паук удалился, ожидая пока я достаточно ослабею и упаду. Необходимо срочно принять противоядие!'
                $ player.applyEffects({poison:50})
            else:
                player.say '{color=#fff782}Мне удалось увернуться, и, пролетевший мимо паук, покатился вниз по склону, ломая свои лапки.'
    $ move(curloc)

