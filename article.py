import newspaper


def get_text(page_source: str) -> str:
    article = newspaper.Article(url="")
    article.set_html(page_source)
    article.parse()
    return article.text
