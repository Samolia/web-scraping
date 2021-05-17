from application import scraping_by_preview, create_articles_list


if __name__ == '__main__':
    keywords = {'Python', 'Разработка веб-сайтов', 'Компьютерное зрение', 'Программирование'}
    url = 'https://habr.com/ru/all/'
    create_articles_list('articles/articles_to_read.txt', scraping_by_preview(url, keywords))
