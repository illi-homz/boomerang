gz.header = {
    changeLang(btn, lang)
    {
        $('._lang-item').removeClass('header__lang-item--active')
        $(btn).addClass('header__lang-item--active')
        setCookie('locale', lang)
        window.location.reload(false)
    },
    toggleMenu()
    {
        $('._header__nav').toggleClass('header__nav--visible')
        $('._burger').toggleClass('burger--close')
        $('._header__topline').toggleClass('header__topline--shadow')

        $('body').toggleClass('lock')
    }
}
