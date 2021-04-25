gz.popupSlider = {
    $slider: null,
    initSlider(slider, id)
    {
        if (!gz.popupSlider.$slider)
        {
            gz.popupSlider.$slider = $(slider).slick({
                initialSlide: id,
                lazyLoad: 'ondemand',
                mobileFirst: true,
                infinite: false,
                dots: false,
                arrows: true,
                prevArrow: '<div class="slick-popup-prev"><div></div></div>',
                nextArrow: '<div class="slick-popup-next"><div></div></div>',
                slidesToShow: 1,
                slidesToScroll: 1
            })
        }
        else {gz.popupSlider.$slider.slick('slickGoTo', id)}
    },
}
