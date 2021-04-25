gz.documents = {
    showPopup(item)
    {
        this.initSlider(item)
    },
    initSlider(item)
    {
        let $imgsList = $(`._documents ._documents__item`)

        const id = $imgsList.index(item)

        $imgsList = $imgsList.clone().attr('onclick', null)

        const $slider = $('._popup-slider__slider')
        if (!$slider.html()) $slider.html($imgsList)

        this.openPopup('._popup-slider__slider', id)
    },
    openPopup(slider, id)
    {
        gz.popup.open('_popup-slider', gz.popupSlider.initSlider, [slider, id])
    }
}
