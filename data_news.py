from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def valor_internacional(theme):

        options = Options()
        options.headless = True

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

        if theme == 'economy':

            url = 'https://valorinternational.globo.com/economy/'

        elif theme == 'tech':
             
            url = 'https://valorinternational.globo.com/business/'

        driver.get(url)

        all_news = driver.find_element("xpath", '/html') 

        html_not = all_news.get_attribute('outerHTML')

        driver.quit()

        soup = BeautifulSoup(html_not, 'html.parser')

        news_boxes = soup.find_all('div', class_ = "feed-post-body-title gui-color-primary gui-color-hover")

        df_news = pd.DataFrame(columns=['headline', 'subhead', 'link', 'title', 'journal'], index=[0, 1, 2, 3, 4, 5])

        for i, news in enumerate(news_boxes):

            subhead = '-'
            headline = news.find("h2", class_ = "feed-post-link gui-color-primary gui-color-hover").a.text
            link =  news.find("h2", class_ = "feed-post-link gui-color-primary gui-color-hover").a['href']

            df_news.loc[i, 'subhead'] = subhead
            df_news.loc[i, 'headline'] = headline
            df_news.loc[i, 'link'] = link
            df_news.loc[i, 'title'] = theme
            df_news.loc[i, 'journal'] = 'valor_internacional'

            if i == 5:

                break

        return df_news


def china_daily(theme):

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if theme == "economy":

        url = 'https://www.chinadaily.com.cn/business/economy'

    elif theme == 'tech':

        url = 'https://www.chinadaily.com.cn/business/tech'

    driver.get(url)

    all_news = driver.find_element("xpath", '/html')  

    html_not = all_news.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    news_boxes = soup.find_all("div", class_ = 'mb10 tw3_01_2') 

    df_news = pd.DataFrame(columns=['headline', 'subhead', 'link', 'title', 'journal'], index=[0, 1, 2, 3, 4, 5])

    for i, news in enumerate(news_boxes):

        subhead = '-'
        headline = news.find("h4").text
        link =  news.find("h4").a['href']

        df_news.loc[i, 'subhead'] = subhead
        df_news.loc[i, 'headline'] = headline
        df_news.loc[i, 'link'] = link
        df_news.loc[i, 'title'] = theme
        df_news.loc[i, 'journal'] = 'china_daily'

        if i == 5:

            break

    return df_news

def ft(theme):

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if theme == "economy":

        url = 'https://www.ft.com/markets'

    elif theme == 'tech':

        url = 'https://www.ft.com/technology'

    elif theme == 'deep_dive':

        url = 'https://www.ft.com/deep-dive'

    driver.get(url)

    all_news = driver.find_element("xpath", '/html')  

    html_not = all_news.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    df_news = pd.DataFrame(columns=['headline', 'subhead', 'link', 'title', 'journal'], index=[0, 1, 2, 3, 4, 5])

    if theme != "deep_dive":

        main_news = soup.find("div", attrs={'class':"o-teaser o-teaser--article o-teaser--top-story o-teaser--landscape o-teaser--has-image js-teaser"}) 

        try:
            
            subhead = main_news.find("div", attrs={'class':"o-teaser__meta"}).a.text

        except:

            subhead = "-"

        headline = main_news.find("div", attrs={'class':'o-teaser__heading'}).a.text
        link = main_news.find("div", attrs={'class':'o-teaser__heading'}).a['href']
        
        df_news.loc[0, 'subhead'] = subhead
        df_news.loc[0, 'headline'] = headline
        df_news.loc[0, 'link'] = "https://www.ft.com" + link
        df_news.loc[0, 'title'] = theme
        df_news.loc[0, 'journal'] = 'ft'

        i = 0

        general_news = (soup.find("div", attrs={'data-trackable':"top-stories-column-one"})).find_all("div", class_ = 'o-teaser__content')

        for _, news in enumerate(general_news):

            i = i + 1

            try:

                subhead = news.find("div", attrs={'class':"o-teaser__meta"}).a.text

            except:

                subhead = '-'

            headline = news.find("div", attrs={'class':'o-teaser__heading'}).a.text
            link = news.find("div", attrs={'class':'o-teaser__heading'}).a['href']

            df_news.loc[i, 'subhead'] = subhead
            df_news.loc[i, 'headline'] = headline
            df_news.loc[i, 'link'] = "https://www.ft.com" + link
            df_news.loc[i, 'title'] = theme
            df_news.loc[i, 'journal'] = 'ft'

            if i == 3:

                break

        opnion_news = soup.find("div", attrs={'data-trackable':'opinion-and-analysis'}).find_all("div", class_ = 'o-teaser__content')

        for _, news in enumerate(opnion_news):

            i = i + 1

            try:

                subhead = news.find("div", attrs={'class':"o-teaser__meta"}).a.text

            except:

                subhead = '-'

            headline = news.find("div", attrs={'class':'o-teaser__heading'}).a.text
            link = news.find("div", attrs={'class':'o-teaser__heading'}).a['href']

            df_news.loc[i, 'subhead'] = subhead
            df_news.loc[i, 'headline'] = headline
            df_news.loc[i, 'link'] = "https://www.ft.com" + link
            df_news.loc[i, 'title'] = theme
            df_news.loc[i, 'journal'] = 'ft'

            if i == 5:

                break

        return df_news
    
    else:

        editorial = soup.find_all("li", attrs={'class': 'o-teaser-collection__item o-grid-row'}) 

        i = 0

        for _, news in enumerate(editorial):

            if news.find("div", attrs={'class':"o-ads__outer"}) == None: #pulando linhas de anúncios

                subhead = news.find("div", attrs={'class':"o-teaser__meta"}).a.text
                headline = news.find("div", attrs={'class':'o-teaser__heading'}).a.text
                link = news.find("div", attrs={'class':'o-teaser__heading'}).a['href']

                df_news.loc[i, 'subhead'] = subhead
                df_news.loc[i, 'headline'] = headline
                df_news.loc[i, 'link'] = "https://www.ft.com" + link
                df_news.loc[i, 'title'] = theme
                df_news.loc[i, 'journal'] = 'ft'

                if i == 5:

                    break

                i = i + 1
        
        return df_news

def cnbc(theme):

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if theme == "economy":

        url = 'https://www.cnbc.com/business/'

    elif theme == 'tech':

        url = 'https://www.cnbc.com/technology/'

    driver.get(url)

    all_news = driver.find_element("xpath", '/html')  

    html_not = all_news.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    news_boxes = soup.find_all('div', class_='Card-titleContainer') 

    df_news = pd.DataFrame(columns=['headline', 'subhead', 'link', 'title', 'journal'], index=[0, 1, 2, 3, 4, 5])

    for i, news in enumerate(news_boxes):

        subhead = '-'
        headline = news.find("a").text
        link =  news.find("a")['href']

        df_news.loc[i, 'subhead'] = subhead
        df_news.loc[i, 'headline'] = headline
        df_news.loc[i, 'link'] = link
        df_news.loc[i, 'title'] = theme
        df_news.loc[i, 'journal'] = 'cnbc'

        if i == 5:

            break

    return df_news

def fortune(theme):

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if theme == "economy":

        url = 'https://fortune.com/section/finance/'

    elif theme == 'tech':

        url = 'https://fortune.com/section/tech/'

    elif theme == 'ai':

        url = 'https://fortune.com/tag/artificial-intelligence/'

    driver.get(url)

    all_news = driver.find_element("xpath", '/html')  

    html_not = all_news.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    news_boxes = soup.find_all('div', attrs={"data-cy" : "article-card-wrapper"}) 

    df_news = pd.DataFrame(columns=['headline', 'subhead', 'link', 'title', 'journal'], index=[0, 1, 2, 3, 4, 5])

    for i, news in enumerate(news_boxes):

        subhead = news.find("div", class_ = 'card-wrapper').a.text
        headline = news.find("h2", class_ = 'sc-3358ecfd-0 ktXRqS card-title').a.get_text(strip=True)
        link = news.find("h2", class_ = 'sc-3358ecfd-0 ktXRqS card-title').a['href']

        df_news.loc[i, 'subhead'] = subhead
        df_news.loc[i, 'headline'] = headline
        df_news.loc[i, 'link'] = link
        df_news.loc[i, 'title'] = theme
        df_news.loc[i, 'journal'] = 'fortune'

        if i == 5:

            break

    return df_news


def cnn(theme):

    options = Options()
    options.headless = True

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)

    if theme == "economy":

        url = 'https://edition.cnn.com/business'

    elif theme == 'tech':

        url = 'https://edition.cnn.com/business/tech'

    driver.get(url)

    all_news = driver.find_element("xpath", '/html')  

    html_not = all_news.get_attribute('outerHTML')
 
    driver.quit()

    soup = BeautifulSoup(html_not, 'html.parser')

    news_boxes = soup.find_all('div', attrs={'data-component-name':"card"}) 

    df_news = pd.DataFrame(columns=['headline', 'subhead', 'link', 'title', 'journal'], index=[0, 1, 2, 3, 4, 5, 6, 7, 8])

    for i, news in enumerate(news_boxes):

        subhead = "-"
        headline = news.find('span', class_ = 'container__headline-text').text
        link = news.find('a')['href']
    
        df_news.loc[i, 'subhead'] = subhead
        df_news.loc[i, 'headline'] = headline
        df_news.loc[i, 'link'] = "https://edition.cnn.com" + link
        df_news.loc[i, 'title'] = theme
        df_news.loc[i, 'journal'] = 'cnn'

        if i == 8:

            break

    if theme == "economy":

        df_news = df_news.drop(index=[3, 4, 5])

    elif theme == 'tech':

        df_news = df_news.drop(index=[0, 1, 2])

    df_news = df_news.reset_index(drop=True)

    return df_news



def scraping_news():

    #usa

    cnn_e = cnn('economy')
    cnn_t = cnn('tech')
    cnbc_e = cnbc('economy')
    cnbc_t = cnbc('tech')
    f_e = fortune('economy')
    f_t = fortune('tech')
    f_ia = fortune('ai')

    #world
    cd_e = china_daily('economy')
    cd_t = china_daily('tech')
    vi_e = valor_internacional('economy')
    vi_t = valor_internacional('tech')
    ft_e = ft('economy')
    ft_t = ft('tech')
    ft_dd = ft('deep_dive') 

    news = pd.concat([cnn_e, cnn_t, cnbc_e, cnbc_t, f_e, f_t, f_ia, cd_e, cd_t, vi_e, vi_t, ft_e, ft_t, ft_dd], ignore_index=True)

    print(news)

    news.to_csv("news.csv", index = False)

if __name__ == "__main__":
    
    scraping_news()







