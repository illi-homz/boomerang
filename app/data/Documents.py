from django.conf import settings
static = settings.STATIC_URL

data = {
    'RU': {
        'title': 'Документы',

        'breadCrumbs': [
            {'title': 'Главная', 'url': '/'},
            {'title': 'Документы', 'url': '#'}
        ],

        'mainLicenses': 'Лицензии на осуществление охранной деятельности',
        'techLicenses': 'Лицензия на осуществление деятельности по монтажу, техническому обслуживанию и ремонту средств обеспечения пожарной безопасности зданий и сооружений',
    },
    'EN': {
        'title': 'Documents',

        'breadCrumbs': [
            {'title': 'Main', 'url': '/'},
            {'title': 'Documents', 'url': '#'}
        ],

        'mainLicenses': 'Licenses to carry out security activities',
        'techLicenses': 'License to carry out activities for the installation, maintenance and repair of fire safety equipment for buildings and structures',
    }
}
