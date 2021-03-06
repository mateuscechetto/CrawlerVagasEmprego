import scrapy


class empregosSpider(scrapy.Spider):
    name = "empregos"
    start_urls = [
       'https://www.trabalhabrasil.com.br/?q=tecnologia',
        'https://www.vagas.com.br/vagas-de-?a%5B%5D=24',
        'https://www.geekhunter.com.br/vagas',
        'https://www.vagasfloripa.com.br/job-category/informatica-ti-telecomunicacoes/',
        'https://www.empregos.com.br/vagas#v=VQAAAB%2BLCAAAAAAABAAzMbfKzEvLL8pNLMlMTtQtydRN1c3MK0ktykstObTcEyx1eCFITj%2FEUyFVwRMqZ21qZlVgeGi5obWpuVVQak5qWWJecmYiRBgAYCSEVVUAAAA%3D&k=emXlzKUd9kqTtsTRLxTKHg%3D%3D',
        'https://landing.jobs/jobs?page=1&hd=false&t_co=false&t_st=false',
        'http://empregocerto.uol.com.br/vagas/informatica-ti.html',
        'https://oportunidades.targettrust.com.br/',
        'https://trampos.co/oportunidades/?ct[]=programacao&ct[]=ti',
        'https://hipsters.jobs/jobs/',
       'https://programathor.com.br/jobs',
        'https://www.catho.com.br/vagas/area-informatica-ti-engenharia-da-computacao/?page=3&area_id%5B0%5D=51'
    ] + [
        'https://www.vagas.com.br/vagas-de-tecnologia&page=%s' % page for page in range(2,35) 
    ] + [
        'https://www.geekhunter.com.br/vagas?page=%s' % page for page in range(2,73)
    ] + [
        'https://www.vagasfloripa.com.br/job-category/informatica-ti-telecomunicacoes/page/%s/' % page for page in range(2,8)
    ] + [
        'https://hipsters.jobs/jobs/?&p=%s' % page for page in range(2,60)
    ] + [
       'https://www.infojobs.com.br/vagas-de-tecnico-informatica-em-florianopolis,-sc.aspx?Page=%s' % page for page in range(1,4)
    ]

    #def __init__(self, *args, **kwargs): 
#
    #    super(empregosSpider, self).__init__(*args, **kwargs) 
#
    #    self.start_urls = [kwargs.get('start_url')] 
    #    #self.start_urls = kwargs.get('start_urls').split(',')



    def parse(self, response):
        #encontrar o sinal de '$' e localizar o elemento pai
        for job in response.xpath("//text()[contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'DESENVOLVEDOR') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ANALISTA') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'SUPORTE') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'TECNICO') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ESPECIALISTA') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'CONSULTOR') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'PROGRAMADOR') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ARQUITETO')]/ancestor::*[position() =4 ]"):
            maiorString = ""
            for filho in job.xpath(".//child::text()"):
                if len(maiorString) <= len(filho.get()):
                    maiorString = filho.get()
            yield {
                #primeiro uso de um header (h1,h2 etc) como o titulo da vaga
                'nome da vaga': job.xpath(".//text()[contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'DESENVOLVEDOR') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ANALISTA') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'SUPORTE') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'TECNICO') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ESPECIALISTA') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'CONSULTOR') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'PROGRAMADOR') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ARQUITETO')]").get(),
                #elemento com o $ como o salario
                'salario': job.xpath(".//text()[contains(.,'$')]").get(),
                #filho de maior tamanho
                'descrição': maiorString,
                'local': job.xpath(".//text()[contains(.,'-DF') or contains(.,'/DF ') or contains(text(),' DF ') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'DISTRITO FEDERAL') or contains(.,'-TO') or contains(.,'/TO ') or contains(text(),' TO ') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'TOCANTINS') or contains(.,'-SE') or contains(.,'/SE ') or contains(text(),'SE') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'SERGIPE') or contains(.,'-SC') or contains(.,'/SC ') or contains(text(),'SC') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'SANTA CATARINA') or contains(.,'-RR') or contains(.,'/RR ') or contains(text(),'RR') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'RORAIMA') or contains(.,'-RO') or contains(.,'/RO ') or contains(text(),'RO') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'RONDONIA') or contains(.,'-RS') or contains(.,'/RS ') or contains(text(),'RS') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'RIO GRANDE DO SUL') or contains(.,'-RN') or contains(.,'/RN ') or contains(text(),'RN') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'RIO GRANDE DO NORTE') or contains(.,'-RJ') or contains(.,'/RJ ') or contains(text(),'RJ') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'RIO DE JANEIRO') or contains(.,'-PI') or contains(.,'/PI ') or contains(text(),'PI') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'PIAUI') or contains(.,'-PE') or contains(.,'/PE') or contains(text(),'PE') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'PERNAMBUCO') or contains(.,'-PR') or contains(.,'/PR') or contains(text(),'PR') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'PARANA') or contains(.,'-PB') or contains(.,'/PB') or contains(text(),'PB') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'PARAIBA') or contains(.,'-PA') or contains(.,'/PA') or contains(text(),'PA') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁAAEEIOÁAAEEIO'),'PARÁ') or contains(.,'-MG') or contains(.,'/MG') or contains(text(),'MG') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'MINAS GERAIS') or contains(.,'-MS') or contains(.,'/MS') or contains(text(),'MS') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'MATO GROSSO DO SUL') orcontains(.,'-MT') or contains(.,'/MT') or contains(text(),'MT') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'MATO GROSSO') or contains(.,'-MA') or contains(.,'/MA') or contains(text(),'MA') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'MARANHAO') or contains(.,'-GO') or contains(.,'/GO') or contains(text(),'GO') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'GOAIS') or contains(.,'-ES') or contains(.,'/ES') or contains(text(),'ES') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ESPIRITO SANTO') or contains(.,'-CE') or contains(.,'/CE') or contains(text(),'CE') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'CEARA') or contains(.,'-BA') or contains(.,'/BA') or contains(text(),'BA') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'BAHIA') or contains(.,'-AM') or contains(.,'/AM') or contains(text(),'AM') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'AMAZONAS') or contains(.,'-AP') or contains(.,'/AP') or contains(text(),'AP') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'AMAPA') or contains(.,'-AL') or contains(.,'/AL') or contains(text(),'AL') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ALAGOAS') or contains(.,'-AC') or contains(.,'/AC') or contains(text(),'AC') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'ACRE') or contains(.,'-SP') or contains(.,'/SP') or contains(text(),'SP') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'SAO PAULO')]").get(),
                'home office/trabalho remoto': job.xpath(".//text()[contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'HOME-OFFICE') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'HOME OFFICE') or contains(translate(.,'abcdefghijklmnopqrstuvwxyzáâãéêíóÁÂÃÉÊÍÓ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZAAAEEIOAAAEEIO'),'REMOTO')]").get() is not None,
                'pagina': response.request.url
            }