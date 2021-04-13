gz.header = {
    changeLang(lang)
    {
        $('._lang-item').removeClass('header__lang-item--active')
        $('._lang-item-'+lang).addClass('header__lang-item--active')
    },
    toggleMenu()
    {
        $('._header__nav').toggleClass('header__nav--visible')
        $('._burger').toggleClass('burger--close')
        $('._header__topline').toggleClass('header__topline--shadow')

        $('body').toggleClass('lock')
    }
}
