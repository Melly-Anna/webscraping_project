import scrapy
from scrapy_splash import SplashRequest
from ..items import ProjetscrapyItem

class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["ldlc.com","localhost"]
    start_urls = ["https://www.ldlc.com/telephonie/telephonie-portable/mobile-smartphone/c4416/"]

# Utilise SplashRequest pour charger les pages avec JavaScript
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, callback=self.parse, args={'wait': 5})

    def parse(self, response):
        phones = response.xpath('//li[@class="pdt-item"]') 

        #pour debuger
        print(f"Nombre de produits trouvés : {len(phones)}") 
        for phone in phones:
            telephone= ProjetscrapyItem()
            telephone["nom"] = phone.xpath('./div[@class="dsp-cell-right"]/div[@class="pdt-info"]/div[@class="pdt-desc"]/h3[@class="title-3"]/a/text()').get()
            telephone["prix"] = phone.xpath('./div[@class="dsp-cell-right"]/div[@class="basket"]/div/div[@class="price"]/text()').get()
            telephone["lien"] = response.urljoin(phone.xpath('./div[@class="dsp-cell-right"]/div[@class="pdt-info"]/div[@class="pdt-desc"]/h3[@class="title-3"]/a/@href').get())

            yield telephone

        #suivre les liens des pages suivantes
        next_page = response.xpath('//li[@class="next"]/a/@href').get() 
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield SplashRequest(next_page_url, callback=self.parse, args={'wait': 5})



