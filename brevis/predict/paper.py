from newspaper import Article
import newspaper


def trending():
	trending_terms=newspaper.hot()
	trending_urls=newspaper.popular_urls()[:10]
	return trending_terms,trending_urls


def get_text(url):
	article=Article(url, keep_article_html=True)
	article.download()
	article.parse()
	original=article.article_html
	text = article.text
	return original,text
