'use strict';

// global components
@@include('@@webRoot/#assets/#js/lib/webp.js');
@@include('@@webRoot/#assets/#js/lib/jquery.min.js');
@@include('@@webRoot/#assets/#js/lib/slick.min.js');


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

// components
@@include('@@webRoot/#assets/#js/lib/popup.js');
@@include('@@webRoot/#assets/components/popup-galery/popup-galery.js');
@@include('@@webRoot/#assets/components/header/header.js');
@@include('@@webRoot/#assets/components/index/index-services/index-services.js');
@@include('@@webRoot/#assets/components/index/index-news/index-news.js');
@@include('@@webRoot/#assets/components/about/about-arsenal/about-arsenal.js');
@@include('@@webRoot/#assets/components/about/about-clients/about-clients.js');
@@include('@@webRoot/#assets/components/about/about-galery/about-galery.js');

// pages
@@include('@@webRoot/#assets/pages/news/news.js');
@@include('@@webRoot/#assets/pages/news-detail/news-detail.js');


gz.init = function() {
    // $("._input-phone").mask("+7(999)999-99-99");

    gz.indexServices.init()
    gz.indexNews.init()
    gz.aboutArsenal.init()
    gz.aboutClients.init()
    gz.popup.init()
    gz.newsDetail.init()
}

$(document).ready(() => {
    gz.init()
})
