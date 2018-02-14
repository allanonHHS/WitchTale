label wash:
    $ clrscr()
    
    if hour >= 22 or hour < 5:
        jump washNight
    else:
        if rand(1,2) == 1:
            $ tryEvent('loc_swim')
        jump washDay

label washDay:
    $ clrscr()
    show expression 'images/events/river/washDay.png' as tempPic
    player.say '{color=#fff782}Я нашла укромный заливчик на реке и вымылась настолько быстро, насколько могла. Уж слишком много любопытных глаз ходит по округе в это время! Иногда мне казалось, что я слышу чьи-то голоса, но, к счастью, это была лишь игра воображения.'
    python:
        changetime(15)
        player.setDirty(0)
        move(curloc)
        
label washNight:
    $ clrscr()
    show expression 'images/events/river/washNight.png' as tempPic
    player.say '{color=#fff782}Я с удовольствием погрузилась в прохладные, ночные воды речушки. Высоко в небе сияла луна, лаская меня своим призрачным светом, а ноги покусывали мальки, очищая загрубевшую кожу.\nКак же я обожаю купаться по ночам, когда вокруг нет ни души и можно не боясь посвятить это время себе!'
    python:
        changetime(60)
        player.incEnergy(200)
        player.setDirty(0)
        move(curloc)
        
label fisher:
    $ clrscr()
    show expression 'images/events/river/fisherAsk.png' as tempPic
    player.say '{color=#fff782}Я подошла к рыбаку, который немедленно встал и уставился на меня так, словно никогда не видел женщины.'
    player.say 'Могу я купить у тебя немного рыбы?'
    oldman.say 'Можешь. 2 срубо и выбирай сколько влезет. И топай, пожалуйста потише, а то всю рыбу мне распугаешь!'
    menu:
        'Заплатить' if player.money >= 2:
            player.say '{color=#fff782}Я заплатила 2 монеты, и покопавшись в ведре с рыбой, выудила несколько экземпляров, которые мне подойдут.'
            python:
                rnd = rand(3,10)
                for x in range(0,rnd):
                    player.addItem(choice([silverFish,scaleLatimeria]))
        'Попробовать уговорить' if player.getCorr() >= 30:
            $ player.incLust(5)
            show expression 'images/events/river/fisher2.png' as tempPic
            if trigger[11] == 0:
                $ trigger[11] = 1
                player.say 'Я, как посмотрю тебе тут скучно и одиноко... Не согласишься ли разрешить порыться в твоём ведре, если я немного разбавлю этот вид красотой женского тела?'
                oldman.say 'Э-э-э? Чёт я не понял.'
            player.say 'Я тебе покажу сиськи, ты мне дашь порыться в ведре. Согласен?'
            oldman.say 'Это завсегда приятственно!'
            show expression 'images/events/river/fisher3.png' as tempPic
            player.say '{color=#fff782}Немного стесняясь, я разделась перед стариком, и убрала руки за спину, открывая шикарный вид на своё молодое тело.'
            if rand(1,3) == 1:
                show expression 'images/events/river/fisher4.png' as tempPic
                oldman.say 'Ахереть! Дай потрогаю!'
                player.say '{color=#fff782}Его руки потянулись ко мне в надежде ухватиться за грудь.'
                player.say 'Эй! Руки прочь! Уговор был только на посмотреть!'
                player.say '{color=#fff782}Рыбак понятливо кивнул и убрал руки за спину.'
            show expression 'images/events/river/fisher5.png' as tempPic
            oldman.say 'Ну, уважила старика! Выбирай что хочешь! - с улыбкой сказал старик, посозерцав мои прелести несколько минут.'
            python:
                rnd = rand(3,10)
                for x in range(0,rnd):
                    player.addItem(choice([silverFish,scaleLatimeria]))
        'Отойти':
            player.say 'Наверное, я куплю в другой раз...'
            oldman.say 'Тьфу, ходють тут всякие!'
    $ move(curloc)