import scrapy


class workanaSpider(scrapy.Spider):
    name = "workana"
    #comeca na page 2 pq a page 1 é só jobs e daria problema no next page, será corrigido
    start_urls = [
        'https://www.workana.com/jobs?page=2',
    ]

    def parse(self, response):
        for project in response.css('div.project-item'):

            # as skills ficam dentro desse label-expander, pega-o como string e trata a string para separar o nome das skills
            labelExpander = project.css('div.skills label-expander').get()
            skills = []
            if labelExpander is not None:
                start = 0
                hasNext = labelExpander.find("anchorText", start) > 0
                while hasNext:
                    skill = labelExpander[labelExpander.find("anchorText", start) + 10 + 3 :labelExpander.find("anchorLink", start) - 3]
                    skills.append(skill)
                    start =  labelExpander.find("anchorLink", start) + 10
                    hasNext = labelExpander.find("anchorText", start) > 0

            yield {
                'titulo': project.css('h2.project-title span::text').get(),
                'valor': project.css('span.values::text').get(),
                #'test': project.css('div.skills label-expander').getall(),
                'skills': skills,
            }

        # pega o ativo na paginacao, a pagina atual, e depois soma-se 1 ao numero da pagina, para ir pra proxima    
        next_page = ""
        next_page = response.css('ul.pagination li.active a::attr(href)').get()
        nextPageNumber = int(next_page[next_page.find("=") + 1:]) + 1
        next_page = next_page[0: next_page.find("=") + 1] + str(nextPageNumber)

        # condicao de parada 51 pq a pagina 51 dá erro, será corrigido (quando dá o erro o programa para)
        if nextPageNumber < 52:
            yield response.follow(next_page, callback=self.parse)
    
    