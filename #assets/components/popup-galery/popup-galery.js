gz.popupGalery = {
    $slider: null,
    initSlider(id)
    {
        if (!gz.popupGalery.$slider)
        {
            gz.popupGalery.$slider = $('._popup-galery__slider').slick({
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
        else {gz.popupGalery.$slider.slick('slickGoTo', id)}
    },
}
