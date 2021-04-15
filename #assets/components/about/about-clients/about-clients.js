gz.aboutClients = {
    init()
    {
        this.sliderInit()
    },
    sliderInit()
    {
        const clientsLength = $('._about-clients__item').length

        $('._about-clients__slider').slick({
            lazyLoad: 'ondemand',
            mobileFirst: true,
            infinite: false,
            dots: false,
            arrows: false,
            vertical: true,
            slidesToShow: clientsLength,
            slidesToScroll: clientsLength,
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
                        slidesToScroll: 3,
                        infinite: true,
                        arrows: true,
                        dots: true,
                    }
                },
            ]
        })
    },

    showDetail(item)
    {
        const url = item.dataset.img
        $('._popup-img__img').attr('src', url + '.png')
        $('._popup-img__img-source').attr('srcset', url + '.webp')
    },

    items: 4,
    showItems: 5,
    showMoreItems()
    {
        this.items += this.showItems
        $(`._about-clients__item`).css('display', 'flex')
        $(`._about-clients__item:nth-child(n + ${this.items})`)
            .css('display', 'none')

        let itemCounter = 0
        const $items = $(`._about-clients__item`)

        $items.each((i, el) => {
            if (el.style.display === 'flex') itemCounter++
        })

        if (itemCounter >= $items.length)
            $('._about-clients__show-more').css('display', 'none')
    }
}
