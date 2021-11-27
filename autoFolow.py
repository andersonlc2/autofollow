#!python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
from timeout import Timeout


class AutoFollow:
    """
        Cria um objetivo que simula uma navegação automática no instagram
    """
    def __init__(self, page):
        """Método construtor"""
        self.driver = webdriver.Firefox()
        self.user = "dotsystemgo"
        self.passw = "Alc250489"
        self.page = page
        self.followlist = ""
        self.follows = 0
        self.c = 1

    def openpg(self):
        """Abre o navegador"""
        sleep(2)
        self.driver.get("https://www.instagram.com")
        self.login()

    def login(self):
        """Faz o login"""
        sleep(random.randint(5, 10))
        user = self.driver.find_element(By.NAME, "username")
        user.send_keys(self.user)
        sleep(random.randint(3, 12))
        passw = self.driver.find_element(By.NAME, "password")
        passw.send_keys(self.passw)
        sleep(random.randint(3, 23))
        passw.send_keys(Keys.ENTER)
        sleep(5)
        actve = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/div/div/section/div/button")
        actve.click()
        self.enterpage()

    def enterpage(self):
        """Navega até a página escolhida"""
        print("\nExecutando...\n\n")
        self.driver.get("https://www.instagram.com/" + self.page)
        self.numfollow()

    def numfollow(self):
        """Pega a informação da quantidade de seguidores e clica neles"""
        sleep(random.randint(3, 11))
        following = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        aux0 = following.find_element(By.TAG_NAME, "span").text
        if "," in aux0:
            aux1 = aux0.replace(",", ".")
        else:
            aux1 = aux0

        if 'milhões' in aux1:
            self.follows = int(float(aux1.strip('milhões')))*1000000
        elif 'mil' in aux1:
            self.follows = int(float(aux1.strip('mil')))*1000
        else:
            self.follows = int(aux1)
        following.click()
        self.createlist()

    def createlist(self):
        """Cria uma lista com cada seguidor"""
        sleep(3)
        f = self.driver.find_element(By.TAG_NAME, "body")
        sleep(3)
        for t in range(0, 5):
            sleep(1)
            f.send_keys(Keys.TAB)
        for i in range(1, 100):
            sleep(1.5)
            f.send_keys(Keys.END)
        sleep(random.randint(3, 11))
        listfolDiv = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[2]/ul/div")
        self.followlist = listfolDiv.find_elements(By.CSS_SELECTOR, "li > div > div > button")
        self.follow()

    def follow(self):
        """Segue cada um da lista"""
        for l in self.followlist:
            if l.text == "Seguir":
                l.click()
                sleep(2)
                if l.text == "Seguir":
                    break
                self.cont()
        self.createlog()

    def cont(self):
        """Faz a contagem de seguidores em tempo real"""
        texto = f"Following +{self.c}"
        print('\b' * len(texto), end='', flush=True)
        print(texto, end='')
        self.c = self.c + 1

    def createlog(self):
        """Gera um arquivo txt que salva os resultados e fecha o navegador"""
        fileTotal = open('following.txt', 'a')
        with fileTotal as f:
            f.write(f"{datetime.datetime.now()}\nTotal following: {self.c-1}\n\n")
        fileTotal.close()
        sleep(10)
        self.driver.quit()


if __name__ == '__main__':
    while True:
        Timeout(15).start()
        AutoFollow('prefeiturasenadorcanedo').openpg()
