import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["www.darty.com"]
    start_urls = ["https://www.darty.com/nav/achat/telephonie/telephone_mobile_seul/iphoneex/index.html#dartyclic=X_tele-obje-conn_ipho"]
    # Ajouter un User-Agent personnalisé
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    def parse(self, response):
        phones = response.xpath('//section[@class="product_list_content"]') 
        for phone in phones:
            desc = phone.xpath('./div[@class="prd-family"]/a/span/text()').get()
            prix = phone.xpath('./div[@class="product-price__price price"]/text()').get()

            yield {
                'Nom': desc,
                'prix': prix
            }

        #suivante = response.xpath('//li[@class="next"]/a/@href').get()
        #if suivante is not None:
            #lien = response.urljoin(suivante)
            #yield scrapy.Request(lien)
