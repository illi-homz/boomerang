gz.aboutArsenal = {
    init()
    {
        this.sliderInit()
    },
    sliderInit()
    {
        const arsenalLength = $('._about-arsenal__item').length

        $('._about-arsenal__slider').slick({
            lazyLoad: 'ondemand',
            mobileFirst: true,
            infinite: false,
            // adaptiveHeight: true,
            dots: false,
            arrows: false,
            vertical: true,
            slidesToShow: arsenalLength,
            slidesToScroll: arsenalLength,
            responsive: [
                {
                    breakpoint: 768,
                    settings: {
                        vertical: false,
                        slidesToShow: 2,
                        slidesToScroll: 1,
                        infinite: true,
                        arrows: true,
                    }
                },
            ]
        })
    },

    toggleDetails(el)
    {
        const $item = $(el).parents('._about-arsenal__item')
        // $item.find('._about-arsenal__item-data').toggleClass('active')
        console.log($item.find('._about-arsenal__item-characteristic'));
        $item.find('.about-arsenal__item-characteristic:nth-child(n + 5)').slideToggle(200)
        $(el).toggleClass('active')
    },

    items: 3,
    showItems: 4,
    showMoreItems()
    {
        this.items += this.showItems
        $(`._about-arsenal__item`).css('display', 'block')
        $(`._about-arsenal__item:nth-child(n + ${this.items})`)
            .css('display', 'none')

        let itemCounter = 0
        const $items = $(`._about-arsenal__item`)

        $items.each((i, el) => {
            if (el.style.display === 'block') itemCounter++
        })

        if (itemCounter >= $items.length)
            $('._about-arsenal__show-more').css('display', 'none')
    }
}
