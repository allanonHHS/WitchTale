init -20 python:
    import copy, codecs, sys, time
    from random import choice
    from operator import itemgetter, attrgetter, methodcaller

    reload(sys)  
    sys.setdefaultencoding('utf8')
    
    ###################################################################
    # Класс частей тела
    ###################################################################

    class BodyPart():
        def __init__(self, name, visibility = False, sperm = False, size = 0, maxSize = 0, minSize = 0):
            self.name = name
            self.visibility = visibility
            self.sperm = sperm
            self.size = size
            self.minSize = minSize
            self.maxSize = maxSize

        def normalize(self):
            self.size = max(self.minSize, min(self.size, self.maxSize))

    # Общий класс тела с частями, общими для всех
    class Body(object):
        def __init__(self, height = 140, bodyparts = None):
            self.parts = {}
            self.parts['ноги'] = BodyPart('ноги', True)
            self.parts['лицо'] = BodyPart('лицо', True)
            self.parts['грудь'] = BodyPart('грудь', True, minSize = 0, maxSize = 10)
            self.parts['анус'] = BodyPart('анус', minSize = 0, maxSize = 10)
            self.parts['рот'] = BodyPart('рот')
            self.parts['руки'] = BodyPart('руки', True)
            self.height = height

            # Копируем и перезаписываем части тела, если надо
            if bodyparts:
                self.parts.update(bodyparts)

        @classmethod
        def random(cls):
            body = cls(height = rand(140, 170))
            body.parts['анус'].size = randf(0, 1)
            return body

        def normalize(self):
            for _,v in self.parts.iteritems():
                v.normalize()

        def sex(self):
            return 'U wot m8'

        def partsWithSperm(self):
            return [v for k,v in self.parts.iteritems() if v.sperm]


    # Мужское тело
    class MaleBody(Body):
        def __init__(self, height, bodyparts = None, anusSize = 0, penisSize = 0):
            super(MaleBody, self).__init__(height, bodyparts)
            self.parts['пенис'] = BodyPart('пенис', minSize = 0, maxSize = 30, size = penisSize) #
            self.parts['анус'].size = anusSize

        @classmethod
        def random(cls):
            body = super(MaleBody, cls).random()
            body.parts['пенис'].size = randf(10, 15)
            return body

        def sex(self):
            return 'male'

    # Женское тело
    class FemaleBody(Body):
        def __init__(self, height, bodyparts = None, anusSize = 0, vaginaSize = 0, breastSize = 0):
            super(FemaleBody, self).__init__(height, bodyparts)
            self.parts['вагина'] = BodyPart('вагина', minSize = 0, maxSize = 10, size = vaginaSize)
            self.parts['анус'].size = anusSize
            self.parts['грудь'].size = breastSize

        @classmethod
        def random(cls):
            body = super(FemaleBody, cls).random()
            body.parts['вагина'].size = randf(0, 1)
            body.parts['грудь'].size = randf(0, 3)
            return body

        def sex(self):
            return 'female'

    # Фута
    class FutaBody(Body):
        def __init__(self, height, bodyparts = None, anusSize = 0, vaginaSize = 0, penisSize = 0, breastSize = 0):
            super(FutaBody, self).__init__(height, bodyparts)
            self.parts['вагина'] = BodyPart('вагина', minSize = 0, maxSize = 40, size = vaginaSize)
            self.parts['пенис'] = BodyPart('пенис', minSize = 0, maxSize = 30, size = penisSize)
            self.parts['анус'].size = anusSize
            self.parts['грудь'].size = breastSize

        @classmethod
        def random(cls):
            body = super(FutaBody, cls).random()
            body.parts['пенис'].size = randf(10, 15)
            body.parts['вагина'].size = randf(0, 1)
            body.parts['грудь'].size = randf(0, 3)
            return body

        def sex(self):
            return 'futa'

    # Параметры персонажа
    class Stats:
        def __init__(self, **stats):
            self.loyalty = stats['loyalty'] if 'loyalty' in stats else 0
            self.fun = stats['fun'] if 'fun' in stats else 0
            self.corr = stats['corr'] if 'corr' in stats else 0
            self.lust = stats['lust'] if 'lust' in stats else 0
            self.maxlust = stats['maxlust'] if 'maxlust' in stats else 0
            self.maxmana = stats['maxmana'] if 'maxmana' in stats else 0
            self.prana = stats['prana'] if 'prana' in stats else 0
            self.mana = stats['mana'] if 'mana' in stats else 0
            self.beauty = stats['beauty'] if 'beauty' in stats else 0
            self.energy = stats['energy'] if 'energy' in stats else 0
            self.dirty = stats['dirty'] if 'dirty' in stats else 0

        def normalize(self):
            self.loyalty = min(max(self.loyalty,-100),100)
            self.fun = min(max(self.fun,0),100)
            self.corr = min(max(self.corr,0),100)
            self.lust = min(max(self.lust,0),self.maxlust)
            self.maxlust = min(max(self.maxlust,0),200)
            self.maxmana = min(max(self.maxmana,0),200)
            self.prana = min(max(self.prana,0),100)
            self.mana = min(max(self.mana,0), self.maxmana)
            self.energy = min(max(self.energy,0),1000)
            self.beauty = min(max(self.beauty,0),200)
            self.dirty = min(max(self.dirty,0),30)

        @classmethod
        def random(cls):
            stats = cls()
            stats.loyalty = randf(0, 10)
            stats.fun = randf(10, 20)
            stats.corr = randf(0, 5)
            stats.lust = randf(0, 50)
            stats.will = randf(0, 100)
            stats.prana = randf(50, 100)
            stats.mana = randf(0, 100)
            stats.energy = randf(500, 1000)
            stats.beauty = randf(20, 90)
            stats.maxlust = 100
            stats.maxmana = 100
            return stats

    class Char(object):

        # Мужские имена
        maleNames = ['Абелард', 'Август', 'Агидиус', 'Адалард', 'Адалбречт', 'Адалвалф', 'Адалрик', 'Адалрикус', 'Адалстан', 'Адалуолф', 'Адалхард', 'Адальберт', 'Аддлер', 'Аделалф', 'Аделбречт', 'Аделмар', 'Аделрик', 'Аделхард', 'Аджид', 'Адлар', 'Адлер', 'Адольф', 'Алард', 'Аларикус', 'Альберт', 'Алмерик', 'Алоис', 'Алтман', 'Алфихар', 'Алфонс', 'Амалирикус', 'Амалрик', 'Амалрих', 'Анико', 'Анкэль', 'Ансгар', 'Анселл', 'Анселл', 'Анселм', 'Ансельм', 'Ансоберт', 'Апсэль', 'Арман', 'Армен', 'Армин', 'Арн', 'Арндт', 'Арне', 'Арнольд', 'Артур', 'Астор', 'Ахлф', 'Аццо', 'Бамбер', 'Баптист', 'Бартолд', 'Бартолемос', 'Бартоломос', 'Бенедикт', 'Берингар', 'Бернд', 'Берндт', 'Бернхард', 'Бертолд', 'Берхард', 'Болдер', 'Бонифац', 'Бруно', 'Брунс', 'Варин', 'Велтен', 'Вендэль', 'Вензеслос', 'Вензэль', 'Вернер', 'Вертэр', 'Виг', 'Виланд', 'Вилберт', 'Виллафрид', 'Вилли', 'Вилфрид', 'Вилфрит', 'Вилхелм', 'Вим', 'Винзенз', 'Винфрид', 'Витолд', 'Воинот', 'Волдемар', 'Волдо', 'Волдхар', 'Волдэри', 'Волкер', 'Волф', 'Волфганг', 'Вольфрам', 'Гайдин', 'Ганс', 'Гантер', 'Гантрам', 'Генрих', 'Георг', 'Герард', 'Герарт', 'Герберт', 'Годафрид', 'Гоззо', 'Гомерик', 'Горст', 'Готтард', 'Готтилф', 'Готтлиб', 'Готтлоб', 'Готтолд', 'Готтфрид', 'Готчолк', 'Гофрид', 'Гоц', 'Гэровалд', 'Гюнтер', 'Гюнтхер', 'Дачс', 'Дедерик', 'Дедрик', 'Дедрич', 'Детлеф', 'Джакоб', 'Джебберт', 'Джебхард', 'Джевехард', 'Джервалф', 'Джервас', 'Джерд', 'Джереон', 'Джерлак', 'Джернот', 'Джеррит', 'Джерт', 'Джерфрид', 'Джерхардт', 'Джерхолд', 'Джисилберт', 'Джисфрид', 'Джозеф', 'Джокем', 'Джокэн', 'Джорг', 'Джочим', 'Дидерик', 'Дидерич', 'Диди', 'Дидрич', 'Диерет', 'Дизэлм', 'Дирк', 'Дитлинд', 'Дитмар', 'Дитрич', 'Дитфрид', 'Еремиас', 'Ерс', 'Зэодор', 'Иво', 'Игнац', 'Изаак', 'Изидор', 'Ингваз', 'Индж', 'Исаак', 'Йохан', 'Карл', 'Карлманн', 'Карломан', 'Карстен', 'Каспар', 'Керт', 'Кипп', 'Кифер', 'Клеменс', 'Клос', 'Колман', 'Коломан', 'Конрад', 'Константин', 'Корбиниан', 'Корбл', 'Кристоф', 'Ксейвр', 'Куно', 'Кэйетан', 'Кэйсер', 'Лабберт', 'Ладвиг', 'Ламмерт', 'Лампречт', 'Ландеберт', 'Ландоберкт', 'Ланзо', 'Леберечт', 'Ленз', 'Леон', 'Леонхард', 'Леонхардт', 'Леопольд', 'Леудболд', 'Лиафвин', 'Лиутберт', 'Лоренц', 'Лотар', 'Лотэйр', 'Лудджер', 'Луитджер', 'Луитполд', 'Лукаш', 'Луц', 'Максимилиан', 'Манфред', 'Манфрид', 'Маркус', 'Мартин', 'Матис', 'Меинард', 'Меино', 'Меинрад', 'Меинхард', 'Менно', 'Мертен', 'Мориц', 'Никлос', 'Николаус', 'Николос', 'Одо', 'Олберик', 'Олберих', 'Олбрект', 'Олбречт', 'Олдман', 'Олдрик', 'Олдрис', 'Олдрич', 'Оллард', 'Оллдрич', 'Ортвин', 'Орэль', 'Отто', 'Оттокар', 'Панкрац', 'Парзифал', 'Парзифаль', 'Полди', 'Полдти', 'Рабан', 'Раджинманд', 'Радульф', 'Раймунд', 'Райнер', 'Райнхард', 'Райнхольд', 'Ральф', 'Рафаэль', 'Реджинар', 'Реджинманд', 'Реджинолд', 'Реджинхард', 'Рейн', 'Рето', 'Рикердт', 'Рикерт', 'Ричард', 'Ротджер', 'Руди', 'Рудиджер', 'Рудольф', 'Руперт', 'Руппрехт', 'Рэйнер', 'Саша', 'Северин', 'Сепп', 'Сеппэль', 'Сигард', 'Сигберт', 'Сигманд', 'Сигфрид', 'Сиджи', 'Сиджисвалд', 'Сиджисманд', 'Сик', 'Симен', 'Стефан', 'Стеффен', 'Танкред', 'Тджарк', 'Тедерик', 'Тилл', 'Тилло', 'Тиуоз', 'Трогот', 'Ув', 'Удо', 'Улбречт', 'Улрич', 'Уолахфрид', 'Уолтэр', 'Уотан', 'Уц', 'Уэнделл', 'Фалберт', 'Фалко', 'Фарамонд', 'Фастред', 'Фед', 'Фестер', 'Филипп', 'Фило', 'Флоренц', 'Франц', 'Фреддерк', 'Фредж', 'Фридеман', 'Фридрих', 'Фридхелм', 'Фридхолд', 'Фритц', 'Фундук', 'Хаган', 'Хайнц', 'Ханк', 'Харальд', 'Хардвин', 'Харман', 'Харманд', 'Хартвиг', 'Хартвин', 'Хартман', 'Хартмут', 'Хейден', 'Хейк', 'Хейко', 'Хейлгар', 'Хеймерик', 'Хеймо', 'Хейн', 'Хейнер', 'Хейно', 'Хелмудт', 'Хелмут', 'Хелмфрид', 'Хелфгот', 'Хелфрид', 'Хеннинг', 'Хенрик', 'Хериберт', 'Херман', 'Херрик', 'Хилберт', 'Хилдеберт', 'Хилдебранд', 'Хинрич', 'Хладвиг', 'Хлодовик', 'Храбан', 'Хрода', 'Хродалф', 'Хродвалф', 'Хродеберт', 'Хродланд', 'Хродрик', 'Хролф', 'Хугуберт', 'Хулдерик', 'Хунфрит', 'Хупперт', 'Хуппречт', 'Хэймирич', 'Хэймо', 'Чустаффус', 'Эб', 'Эберард', 'Эберарт', 'Эберт', 'Эберхард', 'Эбнер', 'Эверт', 'Эгджерт', 'Эгон', 'Эдзард', 'Эдсэль', 'Эдуард', 'Эилерт', 'Экберт', 'Экехард', 'Экхард', 'Экхардт', 'Элдрик', 'Элдрич', 'Эллдрич', 'Эмерик', 'Эмерис', 'Эмиль', 'Эммерик', 'Эморри', 'Энгэль', 'Энджелберт', 'Энн', 'Эрвин', 'Эрдман', 'Эрдмудт', 'Эрдмут', 'Эрих', 'Эрнст', 'Эрхард', 'Эуген', 'Эцэль', 'Юалд', 'Юрген']

        # Женские имена
        femaleNames = ['Агна', 'Агнезэ', 'Агнет', 'Адала', 'Адалинда', 'Адалуолфа', 'Адалхеид', 'Адалхеидис', 'Аделинд', 'Аделинда', 'Аделинде', 'Аделонда', 'Аделхайд', 'Аделхеит', 'Алеит', 'Алина', 'Алоисия', 'Альбертина', 'Амалазуинта', 'Амали', 'Амалия', 'Амелинда', 'Ангелика', 'Анели', 'Анина', 'Анналейса', 'Анналис', 'Анналиса', 'Аннели', 'Аннелин', 'Аннелис', 'Аннемари', 'Анселма', 'Атала', 'Барбел', 'Белинда', 'Бенедикта', 'Бертилда', 'Бинди', 'Бит', 'Брижит', 'Бриджит', 'Бруна', 'Бруннхилд', 'Брунхилд', 'Брунхилдт', 'Верена', 'Вибек', 'Вибк', 'Вигберг', 'Виктория', 'Вилда', 'Вилхелмайн', 'Вилхелмина', 'Волда', 'Врени', 'Габи', 'Габраяле', 'Гадрун', 'Ганда', 'Гандула', 'Геновефа', 'Герти', 'Гертрауд', 'Гертруд', 'Гертруда', 'Гертрудт', 'Гратия', 'Грет', 'Грета', 'Гретта', 'Гретэль', 'Гречен', 'Гретхен', 'Гризелда', 'Дагмар', 'Джат', 'Джата', 'Джатта', 'Джерд', 'Джерди', 'Джерлинд', 'Джиса', 'Джисела', 'Джит', 'Джитта', 'Джозефа', 'Джолента', 'Джулиане', 'Дитрича', 'Ерсэль', 'Зелда', 'Зензи', 'Зибилле', 'Зузанне', 'Ивонет', 'Ивон', 'Идан', 'Изолд', 'Илма', 'Илс', 'Илса', 'Имк', 'Имма', 'Индж', 'Инджеборг', 'Ирма', 'Ирмалинда', 'Ирмгард', 'Ирмтрод', 'Ирмтруд', 'Ирмхилд', 'Какили', 'Какилия', 'Карла', 'Карлин', 'Карлот', 'Каролайн', 'Катарина', 'Катрайн', 'Катрин', 'Кейтрин', 'Керстин', 'Киль', 'Киндж', 'Кирса', 'Клара', 'Кларамонд', 'Кларимондт', 'Класилда', 'Конрадайн', 'Кордула', 'Корина', 'Коринна', 'Кресзенз', 'Кресзентия', 'Кримхилд', 'Кристен', 'Кристиана', 'Куниберт', 'Куниганд', 'Кэйт', 'Кэйтарайн', 'Кэтрин', 'Латгард', 'Лени', 'Леона', 'Леонор', 'Лизелот', 'Лиис', 'Лили', 'Лило', 'Лис', 'Лиса', 'Лисбет', 'Лиселот', 'Лисл', 'Лисэль', 'Лора', 'Лоре', 'Лорелей', 'Лореляй', 'Лот', 'Луитгард', 'Лулу', 'Люизе', 'Майн', 'Малазинта', 'Малвайн', 'Маргарезэ', 'Маргарета', 'Маргарете', 'Маргрезэ', 'Мареик', 'Марил', 'Марлин', 'Марлис', 'Марте', 'Махтилдис', 'Меик', 'Мета', 'Мет', 'Мечтилд', 'Минна', 'Минни', 'Мирджам', 'Мици', 'Мод', 'Мэйдд', 'Надджа', 'Оделия', 'Одила', 'Одилия', 'Олк', 'Ортрун', 'Оттила', 'Оттилд', 'Оттили', 'Оттилия', 'Оттолайн', 'Райк', 'Раффаела', 'Ребекка', 'Реинхилд', 'Ренэйт', 'Роземари', 'Росвита', 'Рохесия', 'Руперта', 'Сабина', 'Саша', 'Сванхилд', 'Сванхилда', 'Свенджа', 'Селма', 'Сента', 'Сигилд', 'Сиглинд', 'Сиджи', 'Соммер', 'Сондж', 'Софи', 'Сюз', 'Табея', 'Татяна', 'Тересия', 'Тилл', 'Тэресия', 'Улрике', 'Уолберга', 'Уолтрод', 'Уши', 'Фелики', 'Франциска', 'Фреджа', 'Фрид', 'Фридерайк', 'Фрици', 'Фрок', 'Хадвиджис', 'Хайнрике', 'Ханн', 'Ханнелор', 'Хедвиг', 'Хеди', 'Хеилвиг', 'Хеилвидис', 'Хелене', 'Хелма', 'Хелмайн', 'Хельюидис', 'Хенрике', 'Хермайн', 'Хилд', 'Хилдегард', 'Хилдегэйрд', 'Хилтрод', 'Хилтруд', 'Хилтрьюд', 'Хильда', 'Хродохэйдис', 'Хулда', 'Шуонхилд', 'Элеонор', 'Элк', 'Элли', 'Элфи', 'Элфрид', 'Эльза', 'Эмили', 'Эмма', 'Эрма', 'Эрмелинда', 'Эрментрауд', 'Эрментрод', 'Эрментруд', 'Эрминтрьюд', 'Эрмтрауд', 'Эрмтруд', 'Эрна', 'Эрнста', 'Ют']

        # Фамилии
        # maleLastNames = {'Крестьянин':90, 'Охотник':10, 'Лесник':10}
        # femaleLastNames = {'Крестьянка':50, 'Селянка':50, 'Охотница':5}
        maleLastNames = {'Крестьянин':100, 'Селянин':50}
        femaleLastNames = {'Крестьянка':50, 'Селянка':50}
        def __init__(self, fname = '', lname = '', color = '#FFFFFF', age = 0, body = None, stats = None, picto = '', location = '', wear = None, inventory = None, money = 0, skills = None, friends = None, enemies = None):
            if body is None:
                body = Body()
            if stats is None:
                stats = Stats()
            if wear is None:
                wear = []
            if inventory is None:
                inventory = []
            if skills is None:
                skills = {}
            if friends is None:
                friends = []
            if enemies is None:
                enemies = []

            self.fname = fname
            self.lname = lname
            self.name = fname + ' ' + lname
            self.sex = body.sex()
            self.age = age
            self.body = body
            self.stats = stats
            self.color = color
            self.inventory = inventory
            self.wear = wear
            self.skills = skills
            self.effects = []
            self.picto = picto
            self.location = location
            self.money = money
            self.say = Character (self.fullName(), kind=adv, dynamic = False, color = self.color, show_side_image = Image(self.picto, xalign=0.01, yalign=0.99), window_left_padding = 170)
            config.side_image_tag = self.picto
            self.reaction = ''
            self.friends = friends
            self.enemies = enemies
        
        # Создание случайного персонажа с полом sex ('male', 'female' или 'futa') и картинкой picto
        @classmethod
        def random(cls, sex, picto):
            # выбор пола
            body = Body()
            if sex == 'female':
                body = FemaleBody.random()
            elif sex == 'futa':
                body = FutaBody.random()
            elif sex == 'male':
                body = MaleBody.random()

            stats = Stats.random()
            firstName = choice(cls.maleNames) if body.sex() == 'male' else choice(cls.femaleNames)
            lastName = choice(cls.lastNames)
            if body.sex() != 'male':
                lastName += 'а'

            color = '#FFFFFF'
            if body.sex() == 'female':
                color = '#FF85F1'
            elif body.sex() == 'male':
                color = '#269AFF'
            elif body.sex() == 'futa':
                color = '#FC3A3A'
            
            character = cls(firstName, lastName, color = color, age = rand(20, 60), body = body, stats = stats, picto = picto, inventory = [], wear = [])
            return character

        def normalize(self):
            self.body.normalize()
            self.stats.normalize()

        def fullName(self):
            return self.fname + ' ' + self.lname
            
###################################################################
# Incrementers
###################################################################
        def incMoney(self,amount):
            self.money += amount
            
        def getMoney(self):
            return self.money

# Изменение loyalty
        def incLoy(self,amount):
            global globalChange, globalArr
            
            self.stats.loyalty += amount
            for x in self.friends:
                x.stats.loyalty += amount/2
            for x in self.enemies:
                x.stats.loyalty -= amount/2
                
            if renpy.get_screen("paramShow") == None:
                globalChange = []
                globalArr = []
                
            globalChange.append(amount)
            globalArr.append(self)
               
            renpy.show_screen('paramShow')

            
# Изменение fun
        def incFun(self,amount):
            self.stats.fun += amount
# Изменение развратности
        def incCorr(self,amount):
            if self != player:
                self.stats.corr += amount
            else:
                self.stats.corr += amount
# Изменение lust
        def incLust(self,amount):
            self.stats.lust += amount
# Изменение prana
        def incPrana(self,amount):
            self.stats.prana += float(amount)
            
# Изменение mana
        def incMana(self,amount):
            if self.getMana() + amount >= 0:
                self.stats.mana += amount
            else:
                amount += self.getMana()
                self.stats.mana = 0
                self.incPrana(amount)
            
# Изменение beauty
        def incBeauty(self,amount):
            self.stats.beauty += amount
# Изменение energy
        def incEnergy(self,amount):
            self.stats.energy += amount
# Изменение dirty
        def incDirty(self,amount):
            self.stats.dirty += amount
            
        def incSkill(self,skill):
            if self.skills.has_key(skill):
                self.skills[skill] += 1
            
###################################################################
# Setters
###################################################################

# Измнение loyalty
        def setLoy(self,amount):
            self.stats.loyalty = float(amount)
# Измнение fun
        def setFun(self,amount):
            self.stats.fun = float(amount)
# Измнение развратности
        def setCorr(self,amount):
            self.stats.corr = float(amount)
# Измнение lust
        def setLust(self,amount):
            self.stats.lust = float(amount)
# Измнение prana
        def setPrana(self,amount):
            self.stats.prana = float(amount)
# Измнение mana
        def setMana(self,amount):
            self.stats.mana = float(amount)
# Измнение intelligence
        def setIntel(self,amount):
            self.stats.intelligence = float(amount)
# Измнение beauty
        def setBeauty(self,amount):
            self.stats.beauty = float(amount)
# Измнение energy
        def setEnergy(self,amount):
            self.stats.energy = float(amount)
# Измнение dirty
        def setDirty(self,amount):
            self.stats.dirty = int(amount)
            
# Измнение dirty
        def setMaxMana(self,amount):
            self.stats.maxmana = int(amount)
            
        def setSkill(self,skill,amount):
            if self.skills.has_key(skill):
                self.skills[skill] = amount
            
###################################################################
# Getters
###################################################################
        def getFriend(self,*args):
            tempArr = []
            for x in self.friends:
                if x.getSex() in args or args[0] == 'all':
                    tempArr.append(x)
            if len(tempArr) > 0:
                return choice(tempArr)
            return False
            
        def getEnemy(self,*args):
            tempArr = []
            for x in self.enemies:
                if x.getSex() in args or args[0] == 'all':
                    tempArr.append(x)
            if len(tempArr) > 0:
                return choice(tempArr)
            return False

# Получение loyalty
        def getLoy(self):
            return self.stats.loyalty
# Получение fun
        def getFun(self):
            if self.getLust() > 90:
                return self.stats.fun - 10
            else:
                return self.stats.fun
                
# Получение развратности
        def getCorr(self):
            if self.hasEffect(intoxication):
                return self.stats.corr + self.getEffect(intoxication).strength/2
            else:
                return self.stats.corr
            
# Получение lust
        def getLust(self):
            if self.hasEffect('love'):
                return min(100, self.stats.lust + self.getEffect('love').strength)
                
            elif self.hasEffect('loveCure'):
                return max(0, self.stats.lust - self.getEffect('loveCure').strength)
            else:
                return self.stats.lust
                
# Получение prana
        def getPrana(self):
            return round(self.stats.prana,1)
# Получение beauty
        def getBeauty(self):
            if self == player:
                beauty = float(self.stats.beauty - self.getDirty()*5)
            else:
                beauty = self.stats.beauty
            return beauty
# Получение energy
        def getEnergy(self):
            return round(self.stats.energy,1)
# Получение dirty
        def getDirty(self):
            return self.stats.dirty
            
        def getSex(self,*args):
            if len(args) == 0:
                return self.body.sex()
            else:
                if args[0] == 'mf':
                    if self.body.sex() == 'male':
                        return self.body.sex()
                    else:
                        return 'female'
                        
        def getMana(self):
            return round(self.stats.mana)
            
        def getMaxlust(self):
            if self.hasEffect('godWill'):
                return self.stats.maxlust + (self.getEffect('godWill').strength/2)
                
            elif self.hasEffect('godWillCure'):
                return self.stats.maxlust - (self.getEffect('godWillCure').strength/2)
            else:
                return self.stats.maxlust
                
        def getMaxMana(self):
                return self.stats.maxmana
                
        def getSkill(self,skill):
            if self.skills.has_key(skill):
                return self.skills[skill]
            return 0
            
###################################################################
# инвентарь
###################################################################

        # Добавление нескольких предметов в инвентарь
        def addItems(self,*args):
            flag = 0
            for x in args:
                for y in allItems:
                    if x == y.name:
                        temp = copy.copy(y)
                        self.inventory.append(temp)
                        flag += 1
            if flag == len(args):
                return True
            else:
                renpy.say('','ITEMS ARE NOT ADDED!')
                return False

        # Добавление одного предмета (можно использовать и addItems) просто на всякий пожарный.
        def addItem(self,item):
            temp = copy.copy(item)
            self.inventory.append(temp)
            
        def addItemAmount(self,item,amount):
            for x in range(0,amount):
                temp = copy.copy(item)
                self.inventory.append(temp)
            
        def FremoveItem(self,item):
            self.removeItem(item)
        
        # Удаление айтема
        def removeItem(self,item):
            if type(item) is str:
                for x in self.inventory:
                    if x.name == item:
                        self.inventory.remove(x)
                        return True
            else:
                if self.inventory.count(item) > 0:
                    self.inventory.remove(item)
                    return True
                if self.wear.count(item) > 0:
                    self.wear.remove(item)
                    return True
                for x in self.inventory:
                    if x.name == item.name:
                        self.inventory.remove(x)
                        return True
            return False
                
        # Удаление айтемов !!! Сносит ВСЕ с данным названием!!!
        def removeItems(self,*args):
            flag = 0
            for x in args:
                for y in self.inventory:
                    if x == y.name:
                        self.inventory.remove(y)
                        flag += 1
            for x in args:
                for y in self.wear:
                    if x == y.name:
                        self.wear.remove(y)
                        flag += 1
            if flag == len(args):
                return True
            else:
                return False

        # Проверка на наличие айтема
        def hasItem(self, name):
            for x in self.inventory:
                if name == x.name:
                    return True
            for x in self.wear:
                if name == x.name:
                    return True
            return False

        # Подсчёт айтемов
        def countItem(self, name):
            counter = 0
            for x in self.inventory:
                if name == x.name:
                    counter += 1
            return counter

        # Применение айтема
        def apply(self, name):
            for x in self.inventory:
                if x.name == name:
                    x.durability -= 1
                    self.checkDur()
                    return
                    
            for x in self.wear:
                if x.name == name:
                    x.durability -= 1
                    self.checkDur()
                    return
                    
        # Удаление всех использованных айтемов
        def checkDur(self):
            for x in self.inventory:
                if x.durability <= 0:
                    self.inventory.remove(x)
            for x in self.wear:
                if x.durability <= 0:
                    self.wear.remove(x)
                    
        def hasElexir(self, effect):
            for x in self.inventory:
                if x.type == 'food':
                    if effect.id in x.effects.keys()[0].id:
                        return True
            return False
            
        def getElexirMin(self, effect, strength):
            tempArr = []
            for x in self.inventory:
                if x.type == 'food':
                    if effect.id in x.effects.keys()[0].id and strength <= x.getEffectStrength():
                        tempArr.append(x)
            return tempArr

        def removeElexir(self, effect):
            for x in self.inventory:
                if x.type == 'food':
                    if effect.id in x.effects.keys()[0].id:
                        self.removeItem(x)
                        return True
            return False
            

#######################################################
# Применение эффектов
#######################################################
                    
        # Есть ли у чара эффект
        def hasEffect(self, effect):
            if isinstance(effect,Effect):
                for pEffect in self.effects:
                    if effect.id == pEffect.id:
                        return True
                return False
            else:
                for pEffect in self.effects:
                    if effect == pEffect.id:
                        return True
                return False
                
        # Получить эффект чара
        def getEffect(self, effect):
            if isinstance(effect,Effect):
                for pEffect in self.effects:
                    if effect.id == pEffect.id:
                        return pEffect
                return False
            else:
                for pEffect in self.effects:
                    if effect == pEffect.id:
                        return pEffect
                return False
        
        def getAntiEffect(self, effect):
            if effect.id[-4:] == 'Cure':
                for pEffect in self.effects:
                    if pEffect.id == effect.id[:-4]:
                        return pEffect
            else:
                for pEffect in self.effects:
                    if pEffect.id[:-4] == effect.id:
                        return pEffect
            return False

        def removeEffect(self, effect):
            if effect in self.effects:
                self.effects.remove(effect)
            else:
                if self.hasEffect(effect) != False:
                    self.effects.remove(self.getEffect(effect))
            
        def checkEffect(self,effect):
            if effect.strength <= 0:
                self.removeEffect(effect)
                return True
            return False
            
        # Применить эффект к чару (Передаётся словарь!)
        def applyEffects(self, effectsDict):
            for iEffect in effectsDict:
                if self.hasEffect(iEffect):
                    self.getEffect(iEffect).strength += effectsDict.get(iEffect)
                else:
                    tempAntiEffect = self.getAntiEffect(iEffect)
                    if tempAntiEffect != False:
                        tempAntiEffect.strength -= effectsDict.get(iEffect)
                        tempStrength = tempAntiEffect.strength
                        if self.checkEffect(tempAntiEffect):
                            tempEffect = copy.copy (iEffect)
                            tempEffect.strength = -tempStrength
                            self.effects.append(tempEffect)
                            self.checkEffect(tempEffect)
                    else:
                        tempEffect = copy.copy(iEffect)
                        tempEffect.strength = effectsDict.get(iEffect)
                        self.effects.append(tempEffect)
                    
#######################################################
# Прочее
#######################################################

        # Есть ли сперма вообще
        def isSperm(self):
            parts = self.body.partsWithSperm()
            for i in parts:
                if i.visibility:
                    return 2
            return 1 if len(parts) > 0 else 0

        # Если ли сперма на чём то из
        def getSperm(self,*args):
            partNames = [x.name for x in self.body.partsWithSperm()]
            for x in args:
                if x in partNames:
                    return True
            return False

        # Возвратить стрингу с перечислением заляпанных частей тела
        def printSperm(self):
            partNames = [x.name for x in self.body.partsWithSperm()]
            return ", ".join(partNames)

        # Заляпать спермой части тела
        def coverSperm(self, *args):
            for x in args:
                if x in self.body.parts:
                    self.body.parts[x].sperm = True

        # Помыться
        def cleanAll(self):
            self.stats.dirty = 0
            for _,x in self.body.parts.iteritems():
                x.sperm = False

        # Очистить часть тела
        def clean(self, *args):
            for x in args:
                if x in self.body.parts:
                    self.body.parts[x].sperm = False

        def buy(self, item, *args):
            if len(args) == 0:
                if self.money >= item.cost:
                    self.money -= item.cost
                    if self.hasItem(item.name) == True:
                        self.getItem(item.name).durability += item.durability
                    else :
                        temp = copy.copy(item)
                        self.inventory.append(temp)
            else :
                 if self.money >= item.cost:
                    self.money -= item.cost
                    temp = copy.copy(item)
                    self.inventory.append(temp)

        # Функция получения предмета по имени
        def getItem(self,id):
            for x in self.inventory:
                if x.id == id:
                    return x
            for x in self.wear:
                if x.id == id:
                    return x
            return False
            
        def getItems(self,id):
            tempArr = []
            for x in self.inventory:
                if x.id == id:
                    tempArr.append(x)
            return tempArr
            
        def sellItem(self,name):
            for x in self.inventory:
                if x.name == name:
                    self.money += x.cost
                    self.inventory.remove(x)
                    return True
            return False
            
        def sellItems(self,name):
            counter = 0
            while self.sellItem(name):
                counter += 1
            return counter

        def countItems(self,name):
            counter = 0
            for x in self.inventory:
                if x.name == name: #myItem.name:
                    counter += 1
            return counter
            
        # Сброс переменных
        def reset(self):
            self.normalize()

        def moveToLocation(self, loc, *args):
            """Перемещает персонажа в заданную локацию

            loc - объект класса Location, имя локации или None.
                  Если задан None - персонаж убирается с локации (на ночь)
            """
            global movedArray
            
            if loc is None:
                self.location = None
                return
                
            if isinstance(loc, basestring):
                loc = getLoc(loc)

            else:
                if not isinstance(loc, Location):
                    raise Exception('Argument for the moveToLocation method '
                                    'should be location name or location object')

            self.location = loc

        def getLocation(self):
            return self.location

        # def __repr__(self):
            # return ('<{} name: "{}", sex: "{}">'
                    # .format(self.__class__.__name__,
                            # self.name.encode('utf-8'),
                            # self.sex))
                            
        def __repr__(self):
            return (self.fname.encode('utf-8'))

# End class Char definition
    def getCharByName(name):
        global allChars
        tempArr = []
        for x in allChars:
            if name in x.fullName():
                tempArr.append(x)
        if len(tempArr) > 0:
            return choice(tempArr)
        return getChar()

    def getCharDesc(char):
        name = char.fname
        
        if char.getSkill('health') < 20 and char.getSkill('will') > 80 and '"' not in char.lname:
            char.lname = '"Самоубийца"'
            char.name = char.fname + ' ' + char.lname
        if char.getSkill('will') < 20 and char.getSkill('health') < 20 and '"' not in char.lname:
            char.lname = '"Ничтожество"'
            char.name = char.fname + ' ' + char.lname
            
        if char.getSex() == 'male':
            if char.age > 40 and char.getCorr() > 80 and '"' not in char.lname:
                char.lname = '"Старый развратник"'
                char.name = char.fname + ' ' + char.lname
            if char.age < 40 and char.getSkill('health') > 80 and char.getSkill('will') > 80 and '"' not in char.lname:
                char.lname = '"Охотник"'
                char.name = char.fname + ' ' + char.lname
            if char.getCorr() < 20 and char.getSkill('will') > 80 and '"' not in char.lname:
                char.lname = '"Святой"'
                char.name = char.fname + ' ' + char.lname
            if char.age < 40 and char.getSkill('will') > 80 and char.getCorr() > 80 and '"' not in char.lname:
                char.lname = '"Дырокол"'
                char.name = char.fname + ' ' + char.lname
            if char.age < 40 and char.getSkill('health') > 80 and char.getCorr() > 80 and char.getSkill('will') > 50 and '"' not in char.lname:
                char.lname = '"Первый парень на селе"'
                char.name = char.fname + ' ' + char.lname
                
                
            if char.getCorr() < 20:
                corr = 'пуританин'
            elif char.getCorr() < 50:
                corr = 'скромняга'
            elif char.getCorr() < 80:
                corr = 'обыватель'
            else:
                corr = 'развратник'
            
            if char.getSkill('health') < 20:
                health = 'болезненный'
            elif char.getSkill('health') < 50:
                health = 'хилый'
            elif char.getSkill('health') < 80:
                health = 'румяный'
            else:
                health = 'пышущий здоровьем'
            
            if char.getSkill('will') < 20:
                mana = 'труслив, как заяц'
            elif char.getSkill('will') < 50:
                mana = 'трусоват'
            elif char.getSkill('will') < 80:
                mana = 'не лишён мужества'
            else:
                mana = 'редкостный храбрец'
                
            if player.getSkill('empathy') > rand(1,200):
                if char.getLoy() < -50:
                    loy = 'ненавидит'
                elif char.getLoy() < 50:
                    loy = 'терпит'
                else:
                    loy = 'любит'
                char.reaction = name + ' - ' + health + ' ' + corr + '. Говорят, что он '+ mana +'. Меня он '+ loy +'.'
            else:
                char.reaction = name + ' - ' + health + ' ' + corr + '. Говорят, что он '+ mana +'. Я не знаю, как он ко мне относится.'
        else:
            if char.age < 40 and char.getSkill('health') > 80 and char.getSkill('will') > 80 and '"' not in char.lname:
                char.lname = '"Охотница"'
                char.name = char.fname + ' ' + char.lname
            if char.getCorr() < 20 and char.getSkill('will') > 80 and '"' not in char.lname:
                char.lname = '"Святая"'
                char.name = char.fname + ' ' + char.lname
            if char.age < 40 and char.getCorr() > 80 and char.getSkill('will') > 80 and '"' not in char.lname:
                char.lname = '"Блудница"'
                char.name = char.fname + ' ' + char.lname
            if char.age < 40 and char.getCorr() > 50 and char.getSkill('will') > 80 and '"' not in char.lname:
                char.lname = '"Гулящая"'
                char.name = char.fname + ' ' + char.lname
                
            if char.getCorr() < 20:
                corr = 'пуританка'
            elif char.getCorr() < 50:
                corr = 'скромница'
            elif char.getCorr() < 80:
                corr = 'фантазёрка'
            else:
                corr = 'давалка'
            
            if char.getSkill('health') < 20:
                health = 'болезненно-бледная'
            elif char.getSkill('health') < 50:
                health = 'тонкая, как тростинка'
            elif char.getSkill('health') < 80:
                health = 'румяная'
            else:
                health = 'пышущая здоровьем'
            
            if char.getSkill('will') < 20:
                mana = 'трусишка'
            elif char.getSkill('will') < 50:
                mana = 'трусовата'
            elif char.getSkill('will') < 80:
                mana = 'храбрая'
            else:
                mana = 'храбра до безумия'
            
            if player.getSkill('empathy') > rand(1,200):
                if char.getLoy() < -50:
                    loy = 'ненавидит'
                elif char.getLoy() < 50:
                    loy = 'терпит'
                else:
                    loy = 'любит'
                char.reaction = name + ' - ' + health + ' ' + corr + '. Говорят, что она '+ mana +'. Меня она '+ loy +'.'
            else:       
                char.reaction = name + ' - ' + health + ' ' + corr + '. Говорят, что она '+ mana +'. Я не знаю, как она ко мне относится'
