import scrapy
from ..items import ProjetscrapyItem

class NomSpiderSpider(scrapy.Spider):
    name = 'nom_spider'
    allowed_domains = ['www.mobileshop.eu']
    start_urls = ['https://www.mobileshop.eu/fr/ios-os/']

    def parse(self, response):
        phones = response.xpath('//div[@class="product-module"]')
        for phone in phones :
            telephone= ProjetscrapyItem()
            telephone["nom"]=phone.xpath('.//div[@class="product-name"]/h5/a/text()').get()
            telephone["prix"] = phone.xpath('.//div[@class="price"]/div/text()').get()
            telephone["lien"]=response.urljoin(phone.xpath('.//div[@class="product-name"]/h5/a/@href').get())

            yield telephone

        next_page = response.xpath('//nav[@class="pager"]/div/div/a[contains(text(), "SUIVANT")]/@href').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url)