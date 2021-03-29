gz.services = {
    init()
    {
        this.sliderInit()
        this.moveNavs()
    },
    sliderInit()
    {
        $('._services__slider').slick({
            mobileFirst: true,
            infinite: true,
            dots: true,
            arrows: true,
            slidesToScroll: 1
        });
    },
    moveNavs()
    {
        const $nav = $('._services__nav')

        $nav.append($('._services__slider .slick-prev'))
        $nav.append($('._services__slider .slick-dots'))
        $nav.append($('._services__slider .slick-next'))
    }
}
