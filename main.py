from scrape import get_text


if __name__ == "__main__":
    URL = "https://www.wsj.com/articles/transcript-daly-says-fed-policy-is-better-positioned-to-address-higher-inflation-11639781077"
    print(get_text(URL))
