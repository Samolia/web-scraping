def create_articles_list(file_name, articles_info):
    with open(file_name, 'w', encoding='utf-8') as file:
        for article in articles_info:
            file.write(f'{article}\n')
    return 'Статьи для прочтения добавлены в файл'
