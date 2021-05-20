'use strict';

// global components
@@include('@@webRoot/#assets/#js/lib/webp.js');
@@include('@@webRoot/#assets/#js/lib/jquery.min.js');
@@include('@@webRoot/#assets/#js/lib/slick.min.js');
@@include('@@webRoot/#assets/#js/lib/cookies.js');
@@include('@@webRoot/#assets/#js/lib/lazyload.js');


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
}

// components
@@include('@@webRoot/#assets/#js/lib/select.js');
@@include('@@webRoot/#assets/#js/lib/popup.js');
@@include('@@webRoot/#assets/components/popup-slider/popup-slider.js');
@@include('@@webRoot/#assets/components/header/header.js');
@@include('@@webRoot/#assets/components/index/index-services/index-services.js');
@@include('@@webRoot/#assets/components/index/index-news/index-news.js');
@@include('@@webRoot/#assets/components/about/about-arsenal/about-arsenal.js');
@@include('@@webRoot/#assets/components/about/about-clients/about-clients.js');
@@include('@@webRoot/#assets/components/about/about-galery/about-galery.js');
@@include('@@webRoot/#assets/components/links-list/links-list.js');

// pages
@@include('@@webRoot/#assets/pages/news/news.js');
@@include('@@webRoot/#assets/pages/news-detail/news-detail.js');
@@include('@@webRoot/#assets/pages/services-detail/services-detail.js');
@@include('@@webRoot/#assets/pages/articles/articles.js');
@@include('@@webRoot/#assets/pages/contacts/contacts.js');
@@include('@@webRoot/#assets/pages/documents/documents.js');


gz.init = function() {
    // $("._input-phone").mask("+7(999)999-99-99");

    gz.indexServices.init()
    gz.indexNews.init()
    gz.aboutArsenal.init()
    gz.aboutClients.init()
    gz.popup.init()
    gz.newsDetail.init()
    gz.servicesDetail.init()
    gz.contacts.init()
    gz.linksList.init()
    initLazyLoading()
}

$(document).ready(() => {
    gz.init()
})
