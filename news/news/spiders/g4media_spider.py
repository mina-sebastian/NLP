import scrapy


class G4MediaSpider(scrapy.Spider):
    name = "g4media"
    allowed_domains = ["g4media.ro"]
    start_urls = ["https://www.g4media.ro/"]

    def parse(self, response):
        # Select each article block by its class
        articles = response.css("div.post-review")

        for article in articles:
            url = article.css("h3.post-title a::attr(href)").get()
            if url:
                yield response.follow(url, callback=self.parse_article)

        # Pagination handling if needed (e.g., if crawling beyond homepage)
        next_page = response.css("a.next.page-numbers::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response):
        title = response.css("h1.entry-title::text").get()
        date = response.css("ul.post-medatada li.entry-date::text").get()
        paragraphs = response.css("div.entry-content p::text").getall()
        content = " ".join(p.strip() for p in paragraphs if p.strip())

        yield {
            "url": response.url,
            "title": title.strip() if title else "",
            "date": date.strip() if date else "",
            "content": content,
        }
