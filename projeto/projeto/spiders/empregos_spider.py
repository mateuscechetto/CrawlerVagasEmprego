import scrapy


class empregosSpider(scrapy.Spider):
    name = "empregos"
    start_urls = [
        'https://www.trabalhabrasil.com.br/?q=tecnologia',
        'https://www.empregos.com.br/vagas#v=VQAAAB%2BLCAAAAAAABAAzMbfKzEvLL8pNLMlMTtQtydRN1c3MK0ktykstObTcEyx1eCFITj%2FEUyFVwRMqZ21qZlVgeGi5obWpuVVQak5qWWJecmYiRBgAYCSEVVUAAAA%3D&k=emXlzKUd9kqTtsTRLxTKHg%3D%3D'
    ]

    def parse(self, response):
        #encontrar o sinal de '$' e localizar o elemento pai
        for job in response.xpath("//*[text()[contains(.,'$')]]/.."): 
            yield {
                #primeiro uso de um header (h1,h2 etc) como o titulo da vaga
                'nome da vaga': job.css("h1::text,h2::text,h3::text,h4::text,h5::text")[0].get(),
                #elemento com o $ como o salario
                'salario': job.xpath("//text()[contains(.,'$')]").get()
            }