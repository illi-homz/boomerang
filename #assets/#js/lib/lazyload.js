function initLazyLoading()
{
    let lazyImages = Array.from(document.querySelectorAll('img[data-src],source[data-srcset]'));
    const loadMapBlock = document.querySelector('._load-map');
    const windowHeight = document.documentElement.clientHeight;

    const lazyImagesPositions = [];
    if (lazyImages.length > 0) {
        lazyImages.forEach(img => {
            if (img.dataset.src || img.dataset.srcset) {
                lazyImagesPositions.push(img.getBoundingClientRect().top + pageYOffset);
                lazyScrollCheck();
            }
        });
    }

    document.addEventListener('scroll', lazyScroll);

    function lazyScroll() {
        if (document.querySelectorAll('img[data-src],source[data-srcset]').length > 0) lazyScrollCheck()
        else {document.removeEventListener('scroll', lazyScroll)}
    };


    function lazyScrollCheck() {
        let imgIndex = lazyImagesPositions.findIndex(el => pageYOffset > el - windowHeight)
        if (imgIndex >= 0) {
            if (lazyImages[imgIndex].dataset.src) {
                lazyImages[imgIndex].src = lazyImages[imgIndex].dataset.src
                lazyImages[imgIndex].removeAttribute('data-src')
            } else if (lazyImages[imgIndex].dataset.srcset) {
                lazyImages[imgIndex].srcset = lazyImages[imgIndex].dataset.srcset
                lazyImages[imgIndex].removeAttribute('data-srcset')
            }
            delete lazyImagesPositions[imgIndex]
        }
    };
}
