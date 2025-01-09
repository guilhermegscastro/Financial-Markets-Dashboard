from data_news import scraping_news
import time

while True:

    def atualizar_rotinas():

        scraping_news()

    atualizar_rotinas()

    time.sleep(86400)