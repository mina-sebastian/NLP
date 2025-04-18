import scrapy
from urllib.parse import urljoin


class Digi24Spider(scrapy.Spider):
    name = "digi24"
    allowed_domains = ["digi24.ro"]
    start_urls = [
        "https://www.digi24.ro/stiri/politica",
        "https://www.digi24.ro/stiri/economie",
        "https://www.digi24.ro/stiri/externe",
        "https://www.digi24.ro/stiri/sci-tech",
        "https://www.digi24.ro/stiri/actualitate",
    ]

    def parse(self, response):
        # Extract article URLs from <article> tags
        for article in response.css("article"):
            relative_url = article.css("a::attr(href)").get()
            if relative_url:
                full_url = urljoin(response.url, relative_url)
                
                if "/stiri/" in full_url:
                    yield response.follow(full_url, callback=self.parse_article)

    def parse_article(self, response):
        title = response.css("h1::text").get()
        date = response.css("div.article-date span::text").get()
        paragraphs = response.css("div.article-body p::text").getall()
        content = " ".join([p.strip() for p in paragraphs if p.strip()])

        if title and content:
            yield {
                "url": response.url,
                "title": title.strip(),
                "date": date.strip() if date else None,
                "content": content,
            }
