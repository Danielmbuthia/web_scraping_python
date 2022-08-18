from bs4 import BeautifulSoup

import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web = response.text

soup = BeautifulSoup(yc_web, 'html.parser')
articles = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get('href')
    article_links.append(link)

articles_points = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

highest_point = max(articles_points)
highest_point_index = articles_points.index(highest_point)

highest_voted_article = [article_texts[highest_point_index], article_links[highest_point_index], highest_point]
print(article_texts)
print(article_links)
print(articles_points)
print(highest_point)
print(highest_point_index)
print(highest_voted_article)
