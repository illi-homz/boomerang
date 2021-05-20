gz.linksList = {
    init()
    {
        const link = $('._links-list li.active')
        if (link.length)
        {
            const linkOffset = link[0].offsetLeft - 16
            $('._links-list').scrollLeft(linkOffset);
        }
    }
}