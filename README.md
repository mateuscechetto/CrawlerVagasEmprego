# Crawler Vagas Emprego
Crawler para buscar as vagas de emprego em tecnologia desenvolvido para a disciplina INE5454

## Get Started
### Dependências
[Scrapy](https://docs.scrapy.org/en/latest/intro/install.html#intro-install)
```
pip install Scrapy
```

### Como usar
* Clone o projeto
```
git clone https://github.com/mateuscechetto/CrawlerVagasEmprego.git
```
* Entre com o terminal (CMD) na pasta projeto
* Execute o crawler de empregos para atualizar o empregos.json
```
scrapy crawl empregos -O empregos.json
```
