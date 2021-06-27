gz.indexNews = {
    init()
    {
        this.sliderInit()
    },
    sliderInit()
    {
        $('._index-news__slider').slick({
            // lazyLoad: 'ondemand',
            mobileFirst: true,
            infinite: false,
            dots: true,
            arrows: true,
            slidesToScroll: 1,  
            adaptiveHeight: true,
            responsive: [
                {
                    breakpoint: 768,
                    settings: {
                        adaptiveHeight: false,
                    }
            }]
        })
    },
}
