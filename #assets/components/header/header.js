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
    },
    toggleTheme()
    {
        // console.log('sdss');
        const rootAttr = document.documentElement.getAttribute('theme')
        console.log('rootAttr', rootAttr);

        const isLight = rootAttr === 'light'


        if (isLight) {
            document.documentElement.setAttribute('theme', 'dark')
            $('._theme-switcher').removeClass('light')
            $('._header__ul').removeClass('light')
            localStorage.setItem('theme', 'dark')
        } else {
            document.documentElement.setAttribute('theme', 'light')
            $('._theme-switcher').addClass('light')
            $('._header__ul').addClass('light')
            localStorage.setItem('theme', 'light')
        }
    }
}
