import requests
from bs4 import BeautifulSoup
import re


def scraping_by_preview(url, keywords):
    article_info = []
    keywords_pattern = '|'.join(keywords)
    response = requests.get(url)
    if not response.ok:
        raise ValueError('response is not valid')
    soup = BeautifulSoup(response.text, features='html.parser')
    for article in soup.find_all('article'):
        hubs = {hub.text for hub in article.find_all('a', class_='hub-link')}
        date = article.find('span', class_='post__time').text
        post_title = article.find('h2', class_='post__title').text.strip()
        href = article.find('h2', class_='post__title').find('a').attrs.get('href')
        text_preview = article.find('div', class_='post__text').text
        # для поиска по всей статье
        response = requests.get(href)
        if not response.ok:
            raise ValueError('response is not valid')
        full_soup = BeautifulSoup(response.text, features='html.parser')
        full_post = full_soup.find('div', class_='post__body_full').text.strip()

        if re.search(keywords_pattern, post_title, flags=re.I) or \
                re.search(keywords_pattern, text_preview, flags=re.I) or \
                re.search(keywords_pattern, full_post, flags=re.I) or \
                hubs & keywords:
            result = f'Дата: {date}\nЗаголовок: {post_title}\nСсылка: {href}\n'
            article_info.append(result)
            print(result)
    return article_info
