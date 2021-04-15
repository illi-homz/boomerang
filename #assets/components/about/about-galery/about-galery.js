gz.aboutGalery = {
    showPopup(item)
    {
        this.initSlider(item)
    },
    initSlider(item)
    {
        let $imgsList = $('._about-galery ._about-galery__img')

        const id = $imgsList.index(item)

        $imgsList = $imgsList.clone().attr('onclick', null)

        const $slider = $('._popup-galery__slider')
        if (!$slider.html()) $slider.html($imgsList)

        gz.popup.open('_popup-galery', gz.popupGalery.initSlider, [id])
    },
    items: 5,
    showItems: 6,
    showMoreItems()
    {
        this.items += this.showItems
        $(`._about-galery ._about-galery__img`).css('display', 'flex')
        $(`._about-galery ._about-galery__img:nth-child(n + ${this.items})`)
            .css('display', 'none')

        let itemCounter = 0
        const $items = $(`._about-galery ._about-galery__img`)

        $items.each((i, el) => {
            if (el.style.display === 'flex') itemCounter++
        })

        if (itemCounter >= $items.length)
            $('._about-galery__show-more').css('display', 'none')
    }
}
