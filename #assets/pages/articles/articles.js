gz.articles =
{
    init()
    {},
    filterArticlesByCategory(v)
    {
        this.dataValue = v
        const articles = $('._articles__item')
        articles.removeClass('show')
        if (v === '') {articles.removeClass('hide')}
        else
        {
            articles.filter(`._articles__item[data-value="${v}"]`).removeClass('hide')
            articles.filter(`._articles__item:not([data-value="${v}"])`).addClass('hide')
        }
    },
}
