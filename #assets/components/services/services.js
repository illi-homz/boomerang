gz.services = {
    init()
    {
        this.sliderInit()
        this.moveNavs()
    },
    sliderInit()
    {
        $('._services__slider').slick({
            lazyLoad: 'ondemand',
            mobileFirst: true,
            infinite: true,
            dots: true,
            arrows: true,
            slidesToScroll: 1
        })
            .on('afterChange', () => this.changeSlideData())

        this.changeSlideData()
    },
    moveNavs()
    {
        const $nav = $('._services__nav')

        $nav.append($('._services__slider .slick-prev'))
        $nav.append($('._services__slider .slick-dots'))
        $nav.append($('._services__slider .slick-next'))
    },
    changeSlideData()
    {
        const $slide = $('.services .slick-slide.slick-active')
        const title = $slide.data('title')
        const linkTitle = $slide.data('link')
        const url = $slide.data('url')

        $('._services__slider-title').html(title)
        $('._services__to-article')
            .html(linkTitle)
            .attr('href', url)

    }
}
