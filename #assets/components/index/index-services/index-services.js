gz.indexServices = {
    init()
    {
        this.sliderInit()
        this.moveNavs()
    },
    sliderInit()
    {
        $('._index-services__slider').slick({
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
        const $nav = $('._index-services__nav')

        $nav.append($('._index-services__slider .slick-prev'))
        $nav.append($('._index-services__slider .slick-dots'))
        $nav.append($('._index-services__slider .slick-next'))
    },
    changeSlideData()
    {
        const $slide = $('.index-services .slick-slide.slick-active')
        const title = $slide.data('title')
        // const linkTitle = $slide.data('link')
        const url = $slide.data('url')

        $('._index-services__slider-title').html(title)
        $('._index-services__to-article')
            // .html(linkTitle)
            .attr('href', url)

    }
}
