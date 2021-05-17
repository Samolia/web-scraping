import requests
from bs4 import BeautifulSoup


def scraping_by_preview(url, keywords):
    article_info = []
    response = requests.get(url)
    if not response.ok:
        raise ValueError('response is not valid')
    soup = BeautifulSoup(response.text, features='html.parser')
    for article in soup.find_all('article'):
        hubs = {hub.text for hub in article.find_all('a', class_='hub-link')}
        if hubs & keywords:
            date = article.find('span', class_='post__time').text
            post_title = article.find('h2', class_='post__title').text.strip()
            href = article.find('h2', class_='post__title').find('a').attrs.get('href')
            result = f'Дата: {date}\nЗаголовок: {post_title}\nСсылка: {href}\n'
            article_info.append(result)
            print(result)
    return article_info
