init -1 python:
    allRequests = []
    
    impotenceR1 = Request(
    description = ' говорит, что его щекотун начал давать осечки. И вроде бы их немного, но становится всё больше. И все, главное, в самый неподходящий момент! Только новую бабёнку закадрит, только до кустов дело доходит, и тут раз, словно кирпич к херу привязали!',
    adviceG = 'Перестань нервничать, у тебя ещё всё в порядке. Не надо налегать на спиртное и отдыхай почаще. Вернётся и здоровье и сила в твой уд. И больше не докучай мне мелочами.',
    adviceB = 'А ты находясь с бабёнкой в постели прошепчи: "Змеюка-гремука! Вот тебе сладкая норука! Скорее туда прыгай, да башкою двигай!". Только громко шепчи, а то змеюка не услышит!',
    effect = {impotence:25},
    align = 'good',
    sex = 'male')
    allRequests.append(impotenceR1)
    
    impotenceR2 = Request(
    description = ' рассказывает про свои проблемы с женщинами. И вроде с одной получается, а с другой нет. С одной корешок силой налит, а с другой в дохлого червяка превращается. В общем за 20 минут я наслушалась столько сравнений пениса с различными овощами и зверьми, что мне начинает казаться, что периодическая импотенция - наименьшая из проблем этого мужчины.',
    adviceG = 'Могу помочь тебе только советом. Хватит прыгать от бабы к бабе, остепенись наконец! Найди ту, с которой твой сморчок словно ствол дуба, и наслаждайся жизнью. Ах да, ещё здоровое питание и прогулки на свежем воздухе.',
    adviceB = 'Возьми своего ваньку-встаньку, иди в лес и найди осиное гнездо. Засунь туда этот двадцать первый палец, и двигай внутри пока он не опухнет, словно рожа твоего папаши с похмелья. Если и это не излечит тебя от словоблудия, то я пас!',
    effect = {impotence:50},
    align = 'good',
    sex = 'male')
    allRequests.append(impotenceR2)
    
    impotenceR3 = Request(
    description = ' жалуется на то, что у него совсем не получается с женщинами. Мне не удаётся добиться от него, что именно не получается. Либо у него проблема с penis erectus, либо с деторождением.',
    adviceG = 'Могу тебе посоветовать получше питаться и пореже пытаться. Пореже пей, употребляй сметану и орехи, завари за воде настой одуванчика. Я больше ничем не могу тебе помочь.',
    adviceB = 'Ну раз не получается с девочками, попробуй с мальчиками. В глиномесном деле твоя висюлька и не потребуется! А там, глядишь, привыкнешь и только за мазью для задницы приходить будешь!',
    effect = {impotence:75},
    align = 'good',
    sex = 'male')
    allRequests.append(impotenceR3)
    
    poisonR1 = Request(
    description = ' просит у вас помощи в одном деликатном деле. Человеку страшно надоели вороватые соседи, которые так и норовят залезть в личный амбар, и желание наказать их стало невыносимым. Просьба заключается в предоставлении яда не летального действия.\n(По крайней мере вы именно так поняли красноречивое изречение: "Шоб гады блевали и срались денька два! Авось поумнеют!")',
    adviceG = 'Пойди, нарви ядовитого многоцвета, сделай настойку на спирту и влей её соседской корове в бадью. Самой корове ничего не будет, но её молоко станет ядовито для человека. После этого пара дней спокойствия тебе обеспечено.',
    adviceB = 'В общем идёшь в чёртовы озёра и ищешь самую большую споровую сумку гинации. Запоминай крепко! Засовываешь её себе в зад, и  рассказываешь о подвиге соседям. Не знаю насчёт "блевания", но от смеха они точно обосрутся. Иди.',
    effect = {poisonCure:25},
    patient = True,
    align = 'bad',
    sex = 'all')
    allRequests.append(poisonR1)
    
    diareaR1 = Request(
    description = ' просит у вас что нибудь от живота. На вопрос: "Что именно?", отвечает что раза 3 в день бегает по большому, но получается только помалу, да и жидковато. В общем очевидно, что нужно как-то замедлить частоту стула. Правда непонятно, насколько именно.',
    adviceG = 'Ты пей побольше водички, надави рябинового сока, да перемешай с мёдом. Принимай раз 5 в день, вскоре недуг твой должен пройти.',
    adviceB = 'Совет простой. Берёшь бутылку, суёшь в жопу. Как наполнится - меняешь. Следующий!',
    effect = {diarea:25},
    align = 'good',
    sex = 'all')
    allRequests.append(diareaR1)
    
    diareaCureR1 = Request(
    description = ' говорит, что в туалет уже 3 дня не может сходить. Тужится, тужится, а ничего кроме пуков не рождается. То ли у всё там слиплось от мёда, то ли банальный запор, не особо понятно. Но лечить надо.',
    adviceG = 'Возьми молока, добавь в него чистотела. Выдержи несколько часов и пей 3 раза в день. Если не поможет - придёшь.',
    adviceB = 'А как по твоему твоя жопа может рожать, если её никто не осеменял? Благо для того, чтобы родить говно, больших усилий не надо. Можно осемениться и с козлом. Так что козла за рога, ну и дальше понятно, я надеюсь.',
    effect = {diareaCure:25},
    align = 'good',
    sex = 'all')
    allRequests.append(diareaCureR1)
    
    intoxicationR3 = Request(
    description = ' рассказывает трагическую историю про то, что его сынишка перепил накануне свадьбы, и теперь вряд ли сможет принять участие в акте бракосочетания. Мне необходимо дать какое - нибудь отрезвляющее. Судя по описанию, парень просто в бессознательном состоянии.',
    adviceG = 'Не могу тебе сейчас ничего дать. Но рекомендую сделать промывание желудка и холодное ополаскивание. Так же можешь попробовать собрать несколько грибов белой гнили, тщательно счистить поверхность шляпки, и отварить её до появления жёлтого налёта. Это должно поставить его на ноги в течении нескольких минут.',
    adviceB = 'Вот ещё, пьянь отрезвлять! Волочите его так, хоть будет потом повод жену бить. Ведь он был без сознания, когда говорил "Да!".',
    effect = {intoxication:100},
    patient = True,
    patientSex = 'male',
    align = 'good',
    sex = 'all')
    allRequests.append(intoxicationR3)
    
    fertilityR1 = Request(
    description = ' просит у вас какое нибудь противозачаточное средство на один раз. Дословно: "Я тут с хахалем перепихнуться хочу, да боюсь как бы этот конь мне жеребёнка не заделал!"',
    adviceG = 'Возьми перо ворона, счисти оперение и поставь его на ночь вымачиваться в вине вместе с глазом серебряной рыбки. Перед тем как уединиться, выпей один стакан. Запомни, перед, а не после!',
    adviceB = 'Смажь своё отверстие цветочным мёдом, да садись на муравейник. Гарантирую, что после этого залететь ты не сможешь при всём желании!',
    effect = {fertility:25},
    align = 'good',
    sex = 'female')
    allRequests.append(fertilityR1)
    
    fertilityR2 = Request(
    description = ' жалуется на то, что её постоянно тошнит от любых запахов, и всё время хочется жрать. В процессе выяснения симптомов дама оговорилась, что пару недель назад изменяла мужу.',
    adviceG = 'Попроси у охотника волчий глаз, вырежи его зрачок. Потом положи в полночь зрачок в водку вместе с цветком лишайника. На утро пропитай ветошь в зелье и засунь себе в причинное место на 10 минут. Не пытайся работать в этот день, просто отдохни. И поторопись!',
    adviceB = 'Подожди ещё 8 месяцев и тошнота пройдёт. Правда прибавится головная боль от детского плача, но твоему мужу поди не привыкать воспитывать чужих детей!',
    effect = {fertility:50},
    align = 'good',
    sex = 'female')
    allRequests.append(fertilityR2)
    
    fertilityCureR4 = Request(
    description = ' жалуется, что никак не может завести детей. Сначала он думал, что проблема в жене, и даже начал похаживать к соседке, но это не привело ни к каким результатам. Разве что соседка рассказала о похождениях своим товаркам, и теперь мужчина настолько же популярен, насколько и стерилен.',
    adviceG = 'Я, конечно, могу тебе сварить зелье, что по силе сможет сделать фертильной даже задницу тролля, но ты подумай, нужно ли это тебе с такой то популярностью у деревенских баб? А так, не стесняйся преклонять колени перед здоровой бабой, её желание целительно.',
    adviceB = 'Практика показывает, что чем чаще мужик ходит налево, тем больше у него чужих детей. Причём не только в соседских домах. Иди, будут у твоей жены дети, не переживай!',
    effect = {fertilityCure:100},
    align = 'good',
    sex = 'male')
    allRequests.append(fertilityCureR4)
    
    loveCureR4 = Request(
    description = ' рассказывает о том, что влюбился до одури в дочку соседа, но она совершенно не отвечает взаимностью! Он и в трактир её приглашал и в стогу поваляться, ни в какую! В общем ему нужно приворотное зелье, да покрепче, чтобы не только в стогу поваляться, но и до свадебки действия хватило!',
    adviceG = 'Ты, вместо того, чтобы по трактирам да сеновалам приглашать, подарил бы ей цветочков, да показал, что ты рукастый мужик её отцу. Уж ему то наверняка не терпится сбагрить повзрослевшую дочь!',
    adviceB = 'А ты её подкарауль, да топориком по башке! И тёплая и сговорчивая, чего тебе ещё надо то с такими подкатами?',
    effect = {loveCure:100},
    patient = True,
    patientSex = 'female',
    align = 'bad',
    sex = 'male')
    allRequests.append(loveCureR4)
    
    loveCureR1 = Request(
    description = ' жалуется, что её муж со временем охладел к ней, да налево стал похаживать. Будучи юнцом и в зарослях носом покопаться любил, и в стогу посреди сенокоса поваляться был не дурак. А теперь раз в месяц тыкнет по полторы минуты, да отваливается храпеть!',
    adviceG = 'Ты себя в порядок приведи, заросли подбрей, да подмойся. Попробуй ещё его корешок языком облизать, очень уж мужики охочи до таких ласк!\nНет, я не шучу.\nДа, прямо в рот.',
    adviceB = 'Заплети из зарослей междуножных косу, да смажь её тестом. Опусти эту мотню в речку, да приговаривай: "Вот тебе волоса пахучие, прыгай, окунёк в пещеру вонючую!". Тут либо муж вернётся, либо на русале женишься. Иди и не докучай мне хернёй!',
    effect = {loveCure:25},
    patient = True,
    patientSex = 'male',
    align = 'good',
    sex = 'female')
    allRequests.append(loveCureR4)
    
    loveR1 = Request(
    description = ' говорит, что её задолбал мужнин приятель. Постоянно трапезничает дома, за задницу её щипает, предложения неприличные делает. Давеча вообще в погребе к стенке прижал, да сразу пальцы в щель засунул! Если бы не вырвалась, как пить дать, отдалась бы окаянному! Теперь женщина интересуется, нет ли какого средства, чтобы охладить его пыл?',
    adviceG = 'Ты вроде женщина, а мудрости в тебе ни на грош. Коли любит тебя муж, расскажи ему о приставаниях, и решится твоя проблема без твоего участия. Не променяет же он приятеля на родню?',
    adviceB = 'Да дай ты ему разочек с уговором, мол первый и последний раз! А может и не в последний. Да и не в первый точно! Ведь так только шлюх кадрят, а все вы, селянки, самые что ни на есть шлюхи!',
    effect = {love:25},
    patient = True,
    patientSex = 'male',
    align = 'bad',
    sex = 'female')
    allRequests.append(loveR1)
    
    bleedingR2 = Request(
    description = ' подбегает к вам и говорит, что у его жены случился выкидыш, и они никак не могут остановить кровотечение. Жена уже сильно ослабла, побледнела, но продолжает кровоточить. Нет ли возможности спаси её?',
    adviceG = 'Давай ей больше пить, желательно тёплого бульона. Так же возьми красную лозу и растолчи её в порошок. Этот порошок необходимо затолкать как можно ближе к месту кровотечения. Не забудь помыть перед этим руки! Иди, здоровья тебе и твоей жене.',
    adviceB = 'Небось бил шлюху за то, что от соседа понесла? Ну не печалься. Просто оставь её в покое, Единый даст, будет у тебя новая жена! Лучше прежней. Или хотя бы не настолько охочей до чужих ласк.',
    effect = {bleeding:50},
    patient = True,
    patientSex = 'female',
    align = 'good',
    sex = 'male')
    allRequests.append(bleedingR2)
    
    bleedingR1 = Request(
    description = ' хромая подходит к вам и говорит, что случайно проткнул ногу вилами. Дырка вроде небольшая, а кровь никак не унимается. Нет ли возможности помочь?',
    adviceG = 'Примотай пчелиные соты к ране. Воск забьёт повреждения, а мёд избавит от заражения. И постарайся в следущий раз перекидывать вилами сено, а не свои конечности.',
    adviceB = 'Палец послюнявь и заткни. Коли не сдохнешь, будет тебе наука как вилы держать, да чародейку по пустякам отвлекать!',
    effect = {bleeding:25},
    align = 'good',
    sex = 'male')
    allRequests.append(bleedingR1)
    
    regenerationCureR2 = Request(
    description = ' подходит к вам слегка пошатываясь. Вы сначала думаете, что человек поддатый, но его слова развеивают эту версию. Всё началось с простой простуды, потом добавилась слабость, кровотечение из  носа по утрам, потеря аппетита. Болезнь прогрессирует уже месяц и становится всё хуже.',
    adviceG = 'Каждый день заваривай корень акации. После закипания добавляй цветы лишайника. Пей эту смесь 3 раза в день, питайся получше и постарайся не вставать лишний раз с кровати.',
    adviceB = 'Тяжёлый случай. Перво-наперво позови местного попа и пошли его на хер. Потом пошли на хер детей и близких. Потом пошли на хер друзей и врагов. Это, конечно, тебе не поможет, но возможность послать кого то на хер тебе вряд ли ещё представится.',
    effect = {regenerationCure:50},
    align = 'good',
    sex = 'all')
    allRequests.append(regenerationCureR2)
    
    godWillR2 = Request(
    description = ' жалуется, что его жена совершенно не прислушивается к его приказам и словам. Давече отказала даже подать к борщу стопку водки! И это если не вспоминать про её крики, когда он возвращается с поля в компании друзей, чтобы распить кружку-другую крепкой наливки! В общем и целом ему нужно как-то усмирить норов жены.',
    adviceG = 'Возьми ножку белой гнили и вскипяти её в ведре с водой. Запомни, нужно не меньше 5 литров воды!\nПотом возьми кружку этого варева и выдави в неё кисть голубого винограда. Получится настой с приятным вкусом. Путь жена его пьёт хотя бы раз в день, это сломает её волю.',
    adviceB = 'Бей её почаще, бабы это уважают. Мебель дома ломай, это они уважают ещё сильнее. В наказание отдавай её потешиться своим дружкам, а как надоест - пусти по кругу в деревне. Если и после этого будет перечить - проверь под юбкой, возможно из вас двоих мужик в доме вовсе не ты.',
    effect = {godWill:50},
    patient = True,
    patientSex = 'female',
    align = 'bad',
    sex = 'male')
    allRequests.append(godWillR2)
    
    godWillCureR3 = Request(
    description = ' рассказывает про своего мужа - тряпку.\n"Сосед взял пилу и не возвращает - оправдывает его. К дочурке нашей по вечерам парни пристают - не гоняет их. Недавно даже у него на глазах с соседом заигрывать начала - даже слова не сказал. Что с ним сделать, чтобы он мужиком стал, а? Помоги, ведунья!"',
    adviceG = 'Есть хорошее средство. Возьми семена чернотопника, счисти шелуху, и зёрнам дай настояться в водке 4 дня. Потом отфильтруй раствор и добавь немного его спермы. Меня не волнует, как ты её достанешь, придумай что нибудь. У тебя для этого две руки и целый рот. Добавляй смесь в еду в течении месяца. Твой муж изменится.',
    adviceB = 'Попробуй трахнуться с соседом, пригласи его третьим. Или же пригласи не его, а дочку, пусть посмотрит как родня умеет веселиться! Вообще такой муж - золото! Все дороги перед тобой открыты, хочешь сама куртизанкой становись, хочешь - дочку продавай, фантастика!',
    effect = {godWillCure:75},
    patient = True,
    patientSex = 'male',
    align = 'good',
    sex = 'female')
    allRequests.append(godWillCureR3)
    
    boostR1 = Request(
    description = ' жалуется, что её любимый слишком шустрый. Нет, это хорошо, что он быстро может и крышу починить, и в драке ему равных нет. Но вот как дело доходит до постели - 15 секунд это не то время, которое бы она желала.',
    adviceG = 'Отвари петушиные ушки с соцветиями чертополоха. Пусть пьёт с утра. Работать он станет помедленнее, но и в постели его время улучшится.',
    adviceB = 'Ну с постелью дело можно порешать просто. Ты слишком узка для него, начни ходить с огурцом в щели. Потом смени его на кабачок. Когда дойдёшь до дыни, проверь время любимого! Уверена, что скорострел сможет продержаться секунд на 5 подольше!',
    effect = {boost:25},
    patient = True,
    patientSex = 'male',
    align = 'bad',
    sex = 'female')
    allRequests.append(boostR1)
    
    boostCureR2 = Request(
    description = ' ругается на своего сына. Что не скажешь, сначала тупит минут 5, потом только делать начинает. Попросишь лучину загасить, так он минут 10 может до неё идти. И сладу никакого с ним нет. Все давно поели, а он только к столу подходит. Все в поля ушли, а он ещё с постели не встал! Лодырь и бездырь растёт!',
    adviceG = 'Судя по всему ремень тут не поможет. Ну найди перья аиста, вымочи их в вине и добавляй настойку в питьё. То, что он станет нормальным не обещаю, но тупить должен поменьше.',
    adviceB = 'Дык весь в тебя сын то пошёл! Стоишь, тут бекаешь, мекаешь, толком непонятно ничего. Слишком медленный он видите ли! Да тут половине деревни вожжа под хвост попала, вертитесь возле меня, словно я пророк нового бога, а толку - чуть! А скорость нужна только в одном случае - при поносе. Вот как обсираться на ходу начнёт, так придёшь!',
    effect = {boostCure:50},
    align = 'good',
    sex = 'all')
    allRequests.append(boostCureR2)
    
    concentrationCureR1 = Request(
    description = ' жалуется, что отец стал с возрастом совсем рассеянным. То дверь запереть забудет, то корову покормить. Хотя пропустить рюмашку перед сном никогда не забывает! Есть ли что-то от рассеянности?',
    adviceG = 'Высуши шляпку белого гриба, перемешай с зелёным мхом и добавляй ему в пищу. Ясность рассудка вернётся.',
    adviceB = 'Возьми медовые соты и смажь ими свои веки так, чтобы они не закрывались. Так и за дедом уследишь, и про то, что не стоит ведьме глупостями докучать не забудешь!',
    effect = {concentrationCure:25},
    patient = True,
    patientSex = 'male',
    align = 'good',
    sex = 'all')
    allRequests.append(concentrationCureR1)
    
    etheralR1 = Request(
    description = ' подозревает, что жена ему изменяет с соседом, и так как он с детства был довольно большим и шумным, просит что-нибудь, что поможет стать ему незаметнее.',
    adviceG = 'Могу только посоветовать. Отправь жену за покупками, и скажи, что сам на рыбалку на целый день собираешься. Коли отпустит без проблем - насторожись и попробуй спрятаться под кроватью, авось тогда узнаешь, правы ли твои подозрения, али нет.',
    adviceB = 'Насри под кроватью большую кучу, коли любовник и есть - убежит от такого запаха сразу. А жена твоя и не заметит ничего, коль до сих пор с таким вонючкой в одном доме живёт!',
    effect = {etheralCure:25},
    patient = True,
    patientSex = 'male',
    align = 'good',
    sex = 'male')
    allRequests.append(etheralR1)