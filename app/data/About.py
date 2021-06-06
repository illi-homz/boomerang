from django.conf import settings
static = settings.STATIC_URL
from .Global import data as global_data

data = {
    'RU': {
        **global_data['RU'],
        'title': 'О нас',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'О нас', 'url': '#'}
        ],

        'linksList': [
            {'title': 'История', 'url': '/about?tab=history', 'tab': 'history'},
            {'title': 'Наш арсенал', 'url': '/about?tab=arsenal', 'tab': 'arsenal'},
            {'title': 'Наши клиенты', 'url': '/about?tab=clients', 'tab': 'clients'},
            {'title': 'Отзывы', 'url': '/about?tab=feedbacks', 'tab': 'feedbacks'},
            {'title': 'Вакансии', 'url': '/about?tab=vacancies', 'tab': 'vacancies'},
            {'title': 'Галерея', 'url': '/about?tab=galery', 'tab': 'galery'},
        ],

        'historys': [
            'Руководящий состав группы охранных предприятий «Бумеранг» имеет большой опыт организации эффективной охраны предприятий различного профиля. На предприятии имеется резерв для оперативной замены и усиления постов охраны. Работа охранников на объектах контролируется круглосуточно. С 17-00 до 9-00 работает оперативный дежурный, которому каждый час докладывается оперативная обстановка на всех объектах. Также, в ночное время осуществляются проверки несения службы сотрудниками отдела внутреннего контроля.',
            'Соучредителями ЧОО «МОП Центр» выступают охранные организации, расположенные в каждом субъекте Российской Федерации в Центральном, Приволжском, Северо-Западном, Южном и Северо-Кавказском федеральных округах, а также ряд охранных организаций в Дальне-Восточном и Сибирском федеральных округах; Объединение охранных организаций в рамках проекта «МОП Центр» направлено на координацию защиты интересов клиентов, работающих в нескольких субъектах Российской Федерации.'
        ],

        'historyPhotos': [
            static + 'img/about/historys/photo_1',
            static + 'img/about/historys/photo_2',
            static + 'img/about/historys/photo_3',
        ],

        'servicesTitle': 'Группа охранных предприятий «Бумеранг» предоставляет следующие услуги:',

        'services': [
            'Вооруженная охрана и невооруженная охрана персонала и материальных ценностей заказчика;',
            'Сопровождение грузов по территории Российской Федерации;',
            'Консультирование и подготовка рекомендаций по вопросам охраны и защиты от противоправных действий;',
            'Пультовая охрана с выездом группы быстрого реагирования на место происшествия;',
            'Проектирование и монтаж видеонаблюдения, охранно-пожарной сигнализации.'
        ],

        'targetsTitle': 'В частном охранном предприятии Бумеранг с целью повышения качества работы сотрудников создан отдел внутреннего контроля со следующими задачами:',

        'targets': [
            'Контроль за соблюдением выполнения должностных инструкций по охране объектов;',
            'Сбор информации о нарушениях и преобразованием их в статистические данные;',
            'Анализ нарушений;',
            'Предоставление собранной информации о нарушениях и преобразовании их в статистические данные.'
        ],

        'trainingTitle': 'В своей кадровой политике группа охранных предприятий «Бумеранг» опирается на подготовленные кадры:',

        'trainingText': 'Готовит квалифицированных сотрудников охраны в рамках своего предприятия, сотрудники предприятия направляются на учебу в центры подготовки частных охранников, с сотрудниками предприятия постоянно проводятся инструкторские занятия по правомерности применения специальных средств самозащиты и оружия, а также по изучению должностных инструкций и применению полученных знаний в своей практической работе. Значительная часть охранников имеет стаж работы более пяти лет только в составе ЧОП Бумеранг. Получившие опыт работы в Вооруженных силах, МВД и других силовых структурах.',

        'trainingImg': 'img/shield-big.svg',

        'anyInfo': [
            'В августе 2013 года ГПБ "Бумеранг" стала соучредителем в межрегиональном охранном предприятии «Центр».',
            'Группа охранных предприятий «Бумеранг» тесно сотрудничает с РУВД всех районов города, с сотрудниками отдела лицензионно-разрешительной работы ГУВД и РУВД.',
            'В настоящее время в охранном предприятии работает 750 человек. На вооружении состоит 52 (пятьдесят две) единицы огнестрельного оружия (пистолеты ИЖ-71, DOG-1, карабины «Сайга-410К», ружья ИЖ-81, «Сайга- 12К», карабины ПКСК).'
        ],

        'weapons': [
            {
                'title': 'ДОГ-1',
                'type': 'Револьвер гладкоствольный',
                'characteristics': [
                    ['Калибр', '12,5 мм'],
                    ['Вместимость патронов в барабан', '5 шт.'],
                    ['Длина патронника', '35 мм'],
                    ['Длина ствола', '90 мм'],
                    ['Масса с неснаряженным барабаном', '1 кг'],
                    ['Габаритные размеры (Д / Ш / В)', '212 / 46 / 157 мм'],
                ],
                'texts': [
                    'Точность стрельбы револьвера проверена по прямоугольной мишени 700х500мм на дистанции 5м патронами 12,5х35 и соответствует техническим условиям.',
                    'Револьвер пригоден для стрельбы только патронами завоской снарядки в районах с холодным и умеренным климатом при температуре окружающей среды от минус 50o до плюс 50oС.'
                ],
                'img': static + 'img/about/arsenal/weapon_1'
            },
            {
                'title': 'САЙГА-20С',
                'type': 'Карабин гладкоствольный самозарядный',
                'characteristics': [
                    ['Калибр', '20 мм'],
                    ['Вместимость магазина', '5 (2) шт.'],
                    ['Масса карабина (без магазина, принадлежностей, чехла с ремнем)', '3,2 кг'],
                    ['Габаритные размеры (Д / Ш / В)', '1050 / 70 / 190 мм'],
                    ['Длина ствола', '570 мм'],
                    ['Кучность стрельбы дробью №5 на дистанции 35м по мишени диаметром 750мм со стволом с дульным сужением 0,9мм', '60%'],
                    ['Кучность стрельбы дробью №5 на дистанции 35м по мишени диаметром 750мм со стволом без дульного сужения', '40%'],
                ],
                'texts': [
                    'Параметры по точности и кучности стрельбы пулевыми патронами не устанавливаются ввиду большого (до 10 и более раз) отличия по поперечнику рассеивания пуль патронов различных фирм-изготовителей.',
                    'Наилучшие результаты по кучности обеспечивают пулевые патроны "Federal" (США) и "Hubertus" (Германия).',
                    'Кучность стрельбы дробовым снарядом - процентное отношение пробоин в наиболее пораженной зоне контрольной мишени к общему количеству дробин в снаряде патрона.',
                    'Из карабина производится не более трех выстрелов, и если один из них дал указанную выше кучность, карабин считается удовлетворяющим требованиям на кучность стрельбы.',
                ],
                'img': static + 'img/about/arsenal/weapon_2'
            },
            {
                'title': 'САЙГА-410К',
                'type': 'Карабин охотничий гладкоствольный самозарядный',
                'characteristics': [
                    ['Калибр', '0,410 дюймов'],
                    ['Вместимость магазина', '2, 4 шт.'],
                    ['Масса карабина с магазином (без принадлежностей, чехла с ремнем)', '3,1 кг'],
                    ['Габаритные размеры (Д / Ш / В)', '910 / 97 / 195 мм'],
                    ['Длина ствола', '404 мм'],
                    ['Кучность стрельбы дробью №6 с насадкой №3 на дистанции 25м по мишени диаметром 540мм', '40%'],
                ],
                'texts': [
                    'Параметры по точности и кучности стрельбы пулевыми патронами не устанавливаются ввиду большого (до 10 и более раз) отличия по поперечнику рассеивания пуль патронов различных фирм-изготовителей.',
                    'Наилучшие результаты по кучности обеспечивают пулевые патроны "Federal" и "Remington" (США).',
                    'Кучность стрельбы дробовым снарядом - процентное отношение пробоин в наиболее пораженной зоне контрольной мишени к общему количеству дробин в снаряде патрона.',
                    'Из карабина производится не более трех выстрелов, и если один из них дал указанную выше кучность, карабин считается удовлетворяющим требованиям на кучность стрельбы.',
                ],
                'img': static + 'img/about/arsenal/weapon_3'
            },
            {
                'title': 'САЙГА-410К',
                'type': 'Карабин короткоствольный',
                'characteristics': [
                    ['Калибр', '0,410 дюймов'],
                    ['Вместимость магазина', '4 шт.'],
                    ['Масса карабина с магазином (без принадлежностей, чехла с ремнем)', '3,3 кг'],
                    ['Габаритные размеры (Д / Ш / В)', '840 / 97 / 182 мм'],
                    ['Длина ствола', '182 мм'],
                    ['Кучность стрельбы дробью №6 с насадкой №3 на дистанции 25м по мишени диаметром 540мм', '40%'],
                ],
                'texts': [
                    'Параметры по точности и кучности стрельбы пулевыми патронами не устанавливаются ввиду большого (до 10 и более раз) отличия по поперечнику рассеивания пуль патронов различных фирм-изготовителей.',
                    'Наилучшие результаты по кучности обеспечивают пулевые патроны "Federal" и "Remington" (США).',
                    'Кучность стрельбы дробовым снарядом - процентное отношение пробоин в наиболее пораженной зоне контрольной мишени к общему количеству дробин в снаряде патрона.',
                    'Из карабина производится не более трех выстрелов, и если один из них дал указанную выше кучность, карабин считается удовлетворяющим требованиям на кучность стрельбы.',
                ],
                'img': static + 'img/about/arsenal/weapon_4'
            },
            {
                'title': 'ПКСК',
                'type': 'Портативный короткоствольный служебный карабин',
                'characteristics': [
                    ['Калибр', '9 мм'],
                    ['Вместимость магазина', '10 шт.'],
                    ['Масса без патронов', '1,6 кг'],
                    ['Габаритные размеры (Д / Ш)', '540 / 54 мм'],
                    ['Длина ствола', '120 мм'],
                ],
                'texts': [
                    '9-мм портативный короткоствольный служебный карабин конструкции Драгунова является индивидуальным оружием и предназначен для ведения стрельбы на дальности до 50м.',
                    'Наиболее целесообразно вести стрельбу на дальности до 25м, так как в этих пределах сохраняются достаточный запас убойного действия пули и характеристики рассеивания, обеспечивающие надежное поражение характерных целей.',
                    'Для стрельбы из карабина применяются 9-мм (пистолетные) патроны 9х17К "Курц".',
                ],
                'img': static + 'img/about/arsenal/weapon_5'
            },
            {
                'title': 'РСА',
                'type': 'Револьвер',
                'characteristics': [
                    ['Калибр', '9 мм'],
                    ['Количество патронов в барабане', '6 шт.'],
                    ['Масса без патронов', '0,84 кг'],
                    ['Масса снаряженной обоймы', '0,065 кг'],
                    ['Габаритные размеры (Д / Ш / В)', '215 / 40 / 150 мм'],
                    ['Длина ствола', '75 мм'],
                    ['Начальная скорость полета пули', '275 м/с'],
                    ['Ресурс, выстрелов', 'не менее 3000'],
                    ['Кучность стрельбы на дальности 25 м с руки с упора R100', 'не более 12 см'],
                    ['Прицельная дальность стрельбы', '50 м'],
                ],
                'texts': [
                    '9-мм револьвер служебной конструкции Стечкина и Авраамова предназначен для проведения охранных мероприятий по защите жизни, здоровья и собственности людей. Может эксплуатироваться',
                    'в различных климатических условиях в пределах интервала температур окружающей среды от +50 <sup>о</sup>С до -50 <sup>о</sup>С.',
                    'Для стрельбы из револьвера применяются патроны 9х17К ("КУРЦ").',
                ],
                'img': static + 'img/about/arsenal/weapon_6'
            },
            {
                'title': 'ИЖ-71',
                'type': 'Пистолет',
                'characteristics': [
                    ['Калибр', '9 мм'],
                    ['Вместимость магазина', '8 шт.'],
                    ['Масса без патронов', '0,77 кг'],
                    ['Габаритные размеры (Д / Ш / В)', '161 / 30,5* / 126,7 мм'],
                    ['Длина ствола', '93,5 мм'],
                ],
                'texts': [
                    'Примечание: ширина пистолета с ортопедической рукояткой равна 34 мм.',
                ],
                'img': static + 'img/about/arsenal/weapon_7'
            },
        ],

        'vacancies': {
            'desc': 'В связи с расширением компании примем на работу охранников с опытом и без опыта работы. Проводим обучение и обеспечиваем лицензией новых сотрудников охранного предприятия.',
            'items': [
                # {
                #     'title': 'Требования',
                #     'items': [
                #         'Опыт работы',
                #         'Наличие лицензии (Обязательно)',
                #         'Без вредных привычек'
                #     ]
                # },
                {
                    'title': 'Условия работы',
                    'items': [
                        'Различные графики работы',
                        'Объекты в разных частях города',
                        'З/П 1700 рублей смена'
                    ]
                },
            ],
        },
    },
    'EN': {
        **global_data['EN'],
        'title': 'About us',

        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'About us', 'url': '#'}
        ],

        'linksList': [
            {'title': 'History', 'url': '/about?tab=history', 'tab': 'history'},
            {'title': 'Our Arsenal', 'url': '/about?tab=arsenal', 'tab': 'arsenal'},
            {'title': 'Сlients', 'url': '/about?tab=clients', 'tab': 'clients'},
            {'title': 'Reviews', 'url': '/about?tab=feedbacks', 'tab': 'feedbacks'},
            {'title': 'Vacancies', 'url': '/about?tab=vacancies', 'tab': 'vacancies'},
            {'title': 'Gallery', 'url': '/about?tab=galery', 'tab': 'galery'},
        ],

        'historys': [
            'The management of the group of security companies "Boomerang" has extensive experience in organizing effective security for facilities of various profiles. The enterprise has a reserve for prompt replacement and strengthening of security posts. The work of security guards at the facilities is monitored around the clock. From 17-00 to 9-00 an operational duty officer works, to whom the operational situation at all objects is reported every hour. Also, at night, inspections of service by employees of the internal control department are carried out.',
            'The co-founders of the MOP Center private limited liability company are security organizations located in each constituent entity of the Russian Federation in the Central, Volga, North-West, South and North-Caucasian Federal Districts, as well as a number of security organizations in the Far-Eastern and Siberian Federal Districts; The association of security organizations within the framework of the MOP Center project is aimed at coordinating the protection of the interests of clients working in several constituent entities of the Russian Federation.'
        ],

        'historyPhotos': [
            static + 'img/about/historys/photo_1',
            static + 'img/about/historys/photo_2',
            static + 'img/about/historys/photo_3',
        ],

        'servicesTitle': 'The group of security companies "Boomerang" provides the following services:',

        'services': [
            'Armed and unarmed security of personnel and material assets of the customer;',
            'Escorting cargo on the territory of the Russian Federation;',
            'Consulting and preparation of recommendations on issues of protection and protection against unlawful actions;',
            'Monitored security system with the departure of a rapid response team to the scene;',
            'Design and installation of video surveillance, security and fire alarms.'
        ],

        'targetsTitle': 'In the private security company Boomerang, in order to improve the quality of employees\' work, an internal control department has been created with the following tasks:',

        'targets': [
            'Control over the implementation of job descriptions for the protection of facilities;',
            'Collecting information about violations and converting them into statistical data;',
            'Analysis of violations;',
            'Providing collected information on violations and converting them into statistical data.'
        ],

        'trainingTitle': 'In its personnel policy, the group of security companies "Boomerang" relies on trained personnel:',

        'trainingText': 'Prepares qualified security personnel within the framework of his enterprise. Employees of the company are sent to training centers for private security guards. With the employees of the enterprise, instructors are constantly held on the legality of the use of special self-defense equipment and weapons, as well as on the study of job descriptions and the application of the knowledge gained in their work. A significant part of the security guards have more than five years of experience in the Boomerang private security company and experience in the Armed Forces, the Ministry of Internal Affairs and other law enforcement agencies.',

        'trainingImg': 'img/shield-big.svg',

        'anyInfo': [
            'In August 2013 GPB "Boomerang" became a co-founder in the interregional security company «Center».',
            'The group of security companies "Boomerang" closely cooperates with the all district police departments of the city, with the employees of the department of licensing and permitting work of district police department and the main police department.',
            'The security company currently employs 750 people. It is armed with 52 (fifty two) firearms (IZH-71, DOG-1 pistols, Saiga-410K carbines, IZH-81, Saiga-12K rifles, PSS carbines).'
        ],

        'weapons': [
            {
                'title': 'DOG-1',
                'type': 'Smooth-bore revolver',
                'characteristics': [
                    ['Caliber', '12,5 mm'],
                    ['Capacity of cartridges in the cylinder', '5 cart.'],
                    ['Chamber length', '35 mm'],
                    ['Barrel length', '90 mm'],
                    ['Mass with empty cylinder', '1 kg'],
                    ['Overall dimensions (L / W / H)', '212 / 46 / 157 mm'],
                ],
                'texts': [
                    'The firing accuracy of the revolver was tested against a 700x500mm rectangular target at a distance of 5 m with 12.5x35 cartridges and meets the technical specifications.',
                    'The revolver is suitable for firing only original ammunition in areas with cold and temperate climates at ambient temperatures from - 50 to + 50 degrees С.'
                ],
                'img': static + 'img/about/arsenal/weapon_1'
            },
            {
                'title': 'Saiga-20С',
                'type': 'Self-loading smooth-bore carbine',
                'characteristics': [
                    ['Caliber', '20 mm'],
                    ['Magazine capacity', '5 (2) cart.'],
                    ['Weight of the carbine (without magazine, accessories, case with belt)', '3,2 kg'],
                    ['Overall dimensions (L / W / H)', '1050 / 70 / 190 mm'],
                    ['Barrel length', '570 mm'],
                    ['Accuracy of shooting with shot number 5 at a distance of 35 m at a target with a diameter of 750 mm with a barrel with a muzzle restriction of 0.9 mm', '60%'],
                    ['Accuracy of shooting with shot number 5 at a distance of 35m at a target with a diameter of 750mm with a barrel without muzzle restriction', '40%'],
                ],
                'texts': [
                    'Parameters for the accuracy of firing ammunition are not set due to the large (up to 10 or more times) difference in the diameter of the dispersion of bullets from different manufacturers.',
                    'Federal (USA) and Hubertus (Germany) bullet cartridges provide the best results in terms of accuracy.',
                    'Accuracy of shooting with a shot projectile - the percentage of holes in the most affected area of the control target to the total number of pellets in the cartridge\'s projectile.',
                    'The rifle fires no more than three shots, and if one of them gives the above accuracy, the rifle is considered to meet the accuracy requirements.',
                ],
                'img': static + 'img/about/arsenal/weapon_2'
            },
            {
                'title': 'Saiga-410К',
                'type': 'Self-loading smooth-bore hunting carbine',
                'characteristics': [
                    ['Caliber', '0,410 inches'],
                    ['Magazine capacity', '2, 4 cart.'],
                    ['Weight of the carabiner with magazine (without accessories, case with belt)', '3,1 kg'],
                    ['Overall dimensions (L / W / H)', '910 / 97 / 195 mm'],
                    ['Barrel length', '404 mm'],
                    ['Accuracy of shooting with shot No. 6 with nozzle No. 3 at a distance of 25m at a target with a diameter of 540mm', '40%'],
                ],
                'texts': [
                    'Parameters for the accuracy of firing ammunition are not set due to the large (up to 10 or more times) difference in the diameter of the dispersion of bullets from different manufacturers.',
                    'Federal and Remington bullet cartridges (USA) provide the best results in accuracy.',
                    'Accuracy of shooting with a shot projectile - the percentage of holes in the most affected area of the control target to the total number of pellets in the cartridge\'s projectile.',
                    'The rifle fires no more than three shots, and if one of them gives the above accuracy, the rifle is considered to meet the accuracy requirements.',
                ],
                'img': static + 'img/about/arsenal/weapon_3'
            },
            {
                'title': 'Saiga-410К',
                'type': 'Short-barreled carbine',
                'characteristics': [
                    ['Caliber', '0,410 inches'],
                    ['Magazine capacity', '4 cart.'],
                    ['Weight of the carabiner with magazine (without accessories, case with belt)', '3,3 kg'],
                    ['Overall dimensions (L / W / H)', '840 / 97 / 182 mm'],
                    ['Barrel length', '182 mm'],
                    ['Accuracy of shooting with shot No. 6 with nozzle No. 3 at a distance of 25m at a target with a diameter of 540mm', '40%'],
                ],
                'texts': [
                    'Federal and Remington bullet cartridges (USA) provide the best results in accuracy.',
                    'Accuracy of shooting with a shot projectile - the percentage of holes in the most affected area of the control target to the total number of pellets in the cartridge\'s projectile.',
                    'The rifle fires no more than three shots, and if one of them gives the above accuracy, the rifle is considered to meet the accuracy requirements.',
                    'Federal and Remington bullet cartridges (USA) provide the best results in accuracy.',
                ],
                'img': static + 'img/about/arsenal/weapon_4'
            },
            {
                'title': 'PSSC',
                'type': 'Portable short-barreled service carbine',
                'characteristics': [
                    ['Caliber', '9 mm'],
                    ['Magazine capacity', '10 cart.'],
                    ['Weight without cartridges', '1,6 kg'],
                    ['Overall dimensions (L / W)', '540 / 54 mm'],
                    ['Barrel length', '120 mm'],
                ],
                'texts': [
                    '9-mm portable short-barreled service carbine designed by Dragunov is an individual weapon and is intended for firing at a distance of up to 50 m.',
                    'It is most advisable to fire at a distance of up to 25m. Within these limits, the lethal effect of the bullet and the dispersion characteristics are preserved, ensuring reliable destruction of targets.',
                    '9-mm (pistol) cartridges 9x17K "Kurz" are used for firing a carbine.',
                ],
                'img': static + 'img/about/arsenal/weapon_5'
            },
            {
                'title': 'RSA',
                'type': 'Revolver',
                'characteristics': [
                    ['Caliber', '9 mm'],
                    ['The number of cartridges in the cylinder', '6 cart.'],
                    ['Weight without cartridges', '0,84 kg'],
                    ['Mass of the equipped magazine', '0,065 kg'],
                    ['Overall dimensions (L / W / H)', '215 / 40 / 150 mm'],
                    ['Barrel length', '75 mm'],
                    ['Muzzle velocity', '275 m/s'],
                    ['Amount of shots', 'not less than 3000'],
                    ['Accuracy of shooting at a distance of 25 m from the hand from the support R100', 'no more than 12 cm'],
                    ['Sighting range', '50 m'],
                ],
                'texts': [
                    'The 9-mm revolver designed by Stechkin and Avraamov is intended for carrying out security measures to protect the life, health and property of people. It can be operated in various climatic conditions within the range of ambient temperatures from +50 to -50 degrees C.',
                    '9x17K cartridges ("KURTS") are used for firing a revolver.',
                ],
                'img': static + 'img/about/arsenal/weapon_6'
            },
            {
                'title': 'IZH-71',
                'type': 'Pistol',
                'characteristics': [
                    ['Caliber', '9 mm'],
                    ['Magazine capacity', '8 cart.'],
                    ['Weight without cartridges', '0,77 kg'],
                    ['Overall dimensions (L / W / H)', '161 / 30,5* / 126,7 mm'],
                    ['Barrel length', '93,5 mm'],
                ],
                'texts': [
                    'Note: Handgun prosthetic grip width is 34 mm.',
                ],
                'img': static + 'img/about/arsenal/weapon_7'
            },
        ],

        'vacancies': {
            # 'desc': 'Due to the expansion of the company, we will employ security guards.',
            'desc': 'In connection with the expansion of the company, we will hire security guards with and without work experience. We provide training and licenses for new employees of the security company.',
            'items': [
                # {
                #     'title': 'Requirements',
                #     'items': [
                #         'Work experience',
                #         'Availability of a license (Required)',
                #         'Without bad habbits'
                #     ]
                # },
                {
                    'title': 'Working conditions',
                    'items': [
                        'Various work schedules',
                        'Facilities in different parts of the city',
                        'Salary 1700 rubles shift'
                    ]
                },
            ],
        },
    },
}
