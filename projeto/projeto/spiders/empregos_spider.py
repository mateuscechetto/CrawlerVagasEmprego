import scrapy


class empregosSpider(scrapy.Spider):
    name = "empregos"
    start_urls = [
        ##'https://www.trabalhabrasil.com.br/?q=tecnologia',
        'https://www.vagas.com.br/vagas-de-?a%5B%5D=24',
        'https://www.geekhunter.com.br/vagas',
        'https://www.vagasfloripa.com.br/job-category/informatica-ti-telecomunicacoes/',
        ##'https://www.empregos.com.br/vagas#v=VQAAAB%2BLCAAAAAAABAAzMbfKzEvLL8pNLMlMTtQtydRN1c3MK0ktykstObTcEyx1eCFITj%2FEUyFVwRMqZ21qZlVgeGi5obWpuVVQak5qWWJecmYiRBgAYCSEVVUAAAA%3D&k=emXlzKUd9kqTtsTRLxTKHg%3D%3D'
    ]

    def parse(self, response):
        #encontrar o sinal de '$' e localizar o elemento pai
        for job in response.xpath("//text()[contains(translate(.,'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'DESENVOLVEDOR')]/ancestor::*[position() = 5]"):
            maiorString = ""
            for filho in job.xpath(".//child::text()"):
                if len(maiorString) <= len(filho.get()):
                    maiorString = filho.get()
            yield {
                #primeiro uso de um header (h1,h2 etc) como o titulo da vaga
                'nome da vaga': job.xpath(".//text()[contains(translate(.,'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),'DESENVOLVEDOR')]").get(),
                #elemento com o $ como o salario
                'salario': job.xpath(".//text()[contains(.,'$')]").get(),
                #filho de maior tamanho
                'descrição': maiorString,
                'local': job.xpath(".//text()[contains(.,'SP') or contains(., 'São Paulo') or contains(.,'Sao Paulo') or contains(.,'Santa Catarina')]").get(),
                'pagina': response.request.url
            }