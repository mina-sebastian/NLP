import logging
import scrapy
import html
import json

class G4MediaSpider(scrapy.Spider):
    name = "g4media"
    allowed_domains = ["g4media.ro"]
    start_urls = ["https://www.g4media.ro/articole"]

    already_scraped_urls = [article['url'] for article in json.load(open("articles_g4media.json", "r", encoding="utf-8"))] if json.load(open("articles_g4media.json", "r", encoding="utf-8")) else []
    print(f"Already scraped URLs: {len(already_scraped_urls)}")

    def parse(self, response):
        # Select each article block by its class
        articles = response.css("div.post-review")

        for article in articles:
            url = article.css("h3.post-title a::attr(href)").get()
            if url and url not in self.already_scraped_urls:
                yield response.follow(url, callback=self.parse_article)

        next_page = response.css("div.navigation span a::text").re_first(r"»")
        if next_page:
            # Select the href of the span that contains » 
            next_link = response.css("div.navigation span a:contains('»')::attr(href)").get()
            if next_link:
                yield response.follow(next_link, callback=self.parse)

    
    def parse_article(self, response):
        title = response.css("h1.post-title::text").get()
        date = response.css("span.post-date::text").get()
        author = response.css("span[itemprop='author'] span[itemprop='name']::text").get()

        paragraphs = response.css("div.entry-content p").xpath("string()").getall()
        content = " ".join(html.unescape(p.strip()) for p in paragraphs if p.strip())

        
        paragraphs = response.css("div.post-content p").xpath("string()").getall()
        content = " ".join(html.unescape(p.strip()) for p in paragraphs if p.strip())

        yield {
            "url": response.url,
            "title": title.strip() if title else "",
            "date": date.strip() if date else "",
            "author": author.strip() if author else "",
            "content": content,
        }

