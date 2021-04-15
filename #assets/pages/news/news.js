gz.news = {
    page: 1,
    async getNews()
    {
        const news = await fetch(`/api/get-news?page=${this.page}`)
            .then((response) => {
                return response.json();
            })

        this.page++


        const template = news.reduce((acc, n) => {
            const date = new Intl
                .DateTimeFormat('ru-RU', {day:'2-digit',month:'long'})
                .format(new Date(n.date))

            return acc += this.newTemplate
                .replace( /{{id}}/ig, n.id )
                .replace( /{{title}}/ig, n.title )
                .replace( /{{desc}}/ig, n.desc )
                .replace( /{{date}}/ig, date )
                .replace( /{{url}}/ig, n.img )
        }, '')

        document
            .querySelector('._news__wrapper')
            .insertAdjacentHTML('beforeend',template)
    },
    newTemplate: `
        <div class="news__item g-news">
            <div class="g-news__item-title">
                <a href="/news/{{id}}">{{title}}</a>
            </div>
            <div class="g-news__item-desc">{{desc}}</div>
            <div class="g-news__item-df-jcsb">
                <div class="news__item-date">{{date}}</div>
                <a href="/news/{{id}}" class="g-news__item-detail">Подробнее</a>
            </div>
            <div class="g-news__item-img">
                <a href="/news/{{id}}">
                    <img src="{{url}}" alt="img">
                </a>
            </div>
        </div>
    `
}
