from article import get_text
from scrape import get_page_source

if __name__ == "__main__":
    URL = "https://www.wsj.com/articles/transcript-daly-says-fed-policy-is-better-positioned-to-address-higher-inflation-11639781077"
    page_source = get_page_source(URL)
    print(get_text(page_source))
