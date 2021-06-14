gz.newsDetail = {
    init()
    {
        this.sliderInit()
    },
    sliderInit()
    {
        $('._news-detail__slider').slick({
            lazyLoad: 'ondemand',
            mobileFirst: true,
            infinite: false,
            dots: false,
            arrows: false,
            vertical: true,
            slidesToShow: 3,
            slidesToScroll: 3,
            adaptiveHeight: true,
            responsive: [
                {
                    breakpoint: 768,
                    settings: {
                        vertical: false,
                        slidesToShow: 3,
                        slidesToScroll: 1,
                        infinite: true,
                        arrows: true,
                        dots: true,
                    }
                },
                {
                    breakpoint: 1024,
                    settings: {
                        vertical: false,
                        slidesToShow: 4,
                        slidesToScroll: 1,
                        infinite: true,
                        arrows: true,
                        dots: true,
                    }
                },
            ]
        })
    }
}
