gz.contacts = {
    init()
    {
        try {
            ymaps.ready(this.initYamap)
        } catch (e)
        {
            console.log('no ymaps');
        }
    },
    initYamap()
    {
        let myMap = new ymaps.Map('yamap', {
            center: [56.310931, 44.056161], // Дзауджикау
            zoom: 16
        })

        myMap.geoObjects.add(new ymaps.Placemark([56.310931, 44.056161], {
            balloonContentHeader: 'ООО Бумаранг',
            balloonContentBody: '<a href="tel:+7 (831) 28-28-911">+7 (831) 28-28-911</a><br/>'
        }, {
            preset: 'islands#governmentCircleIcon',
            iconColor: '#2B303C'
        }))
    }
}
