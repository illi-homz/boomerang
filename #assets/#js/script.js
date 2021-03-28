'use strict';

@@include('@@webRoot/#assets/#js/lib/webp.js');
@@include('@@webRoot/#assets/#js/lib/jquery.min.js');
@@include('@@webRoot/#assets/#js/lib/slick.min.js');
@@include('@@webRoot/#assets/#js/lib/validator.js');
@@include('@@webRoot/#assets/#js/lib/maskedinput.min.js');

@@include('@@webRoot/#assets/components/air-datepicker/air-datepicker.js');


const gz = {
    goToBlock(target, isMobile=false, event=undefined)
    {
        if (event) event.preventDefault();
        if (isMobile) this.header.toggleMenu()

        $('html,body').animate({
        scrollTop: typeof(target) === 'string'
            ? $(target).offset().top
            : $(target.hash).offset().top
        });
    },
    changeLang(lang)
    {
        $('._lang-item').removeClass('active')
        $('._lang-item-'+lang).addClass('active')
    }
}

@@include('@@webRoot/#assets/components/select/select.js')
@@include('@@webRoot/#assets/components/header/header.js');
@@include('@@webRoot/#assets/components/services/services.js');


gz.init = function() {
    $("._input-phone").mask("+7(999)999-99-99");
}

$(document).ready(() => {
    gz.init()
})
