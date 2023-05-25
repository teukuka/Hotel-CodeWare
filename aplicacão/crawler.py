import shutil
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Crawler:

    def __init__(self) -> None:
        profile = webdriver.FirefoxProfile()
        profile.set_preference("javascript.enabled", True)
        self.driver = webdriver.Firefox(profile)
        self.url_home = "https://www.booking.com/index.pt-br.html?label=gen173bo-1DCAEoggI46AdILVgDaCCIAQGYAS24ARnIAQ_YAQPoAQH4AQOIAgGYAgKoAgO4ApWXu6MGwAIB0gIkM2M5N2MwNmQtNTI3NS00MzNhLWE3N2YtMjg4NTRmYjFkNjE52AIE4AIB&sid=4e4851bfd1460b2bcbdede62e9a2014e&lang_changed=1&sb_price_type=total&"
        

    def cadastro(self, login, senha):

        self.driver.get(self.url_home)

        botao_cadastro = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/header/nav[1]/div[2]/a[2]")
        botao_cadastro.click()

        form_email = self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(login)

        botao_continuar = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/button/span')
        botao_continuar.click()

        sleep(5)

        form_senha = self.driver.find_element(By.XPATH, '//*[@id="new_password"]').send_keys(senha)
        form_confirmar_senha = self.driver.find_element(By.XPATH, '//*[@id="confirmed_password"]').send_keys(senha)

        botao_criar_conta = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/button')
        botao_criar_conta.click()

        sleep(5)

    def login(self, login, senha):

        
        self.driver.get(self.url_home)

        botao_login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/header/nav[1]/div[2]/div/a/span')
        botao_login.click()

        form_email = self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(login)
        botao_continuar = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[3]/button/span')
        botao_continuar.click()

        sleep(5)

        form_senha = self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
        botao_login = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/form/div[2]/button')
        botao_login.click()


    def reserva(self):

        self.driver.get(self.url_home)
        
        form_destino = self.driver.find_element(By.XPATH, '//*[@id=":Ra9:"]').send_keys('Belo Horizonte')
        form_checkin = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div/button[1]')
        form_checkin.click()
        sleep(2)

        botao_data_checkin = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/div/div[1]/table/tbody/tr[5]/td[4]/span')
        botao_data_checkin.click()
        sleep(2)

        botao_checkout = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[1]/button[2]')
        botao_checkout.click()
        sleep(2)

        botao_data_ckeckout = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/nav/div[2]/div/div[1]/div/div[2]/table/tbody/tr[2]/td[2]/span')
        botao_data_ckeckout.click()
        sleep(2)

        botao_pesquisar = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/form/div[1]/div[4]/button/span')
        botao_pesquisar.click()
