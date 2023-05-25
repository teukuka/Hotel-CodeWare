

from crawler import Crawler

webCrawler = Crawler()

login = "mateus.Jorel@hotmail.com"
senha = "P@ssw0rd123"
webCrawler.cadastro(login, senha)

login = "teukuka.silva@hotmail.com"
senha = "mateus4444mateus"
webCrawler.login(login, senha)


webCrawler.reserva()
