import sys
import requests
from tabulate import tabulate
from util import Article, TopViews


# Personal header information removed. See Pageview API at https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews
headers = {
    "User-Agent": "",
    "From": ""
}


def main():
    choice = get_user_selection()
    if choice == "1":
        article = get_article_info()
        data = get_pageviews(article)
        print(tabulate_pageviews(data))
    else:
        topviews = get_topview_info()
        data = get_topviews(topviews)
        print(tabulate_topviews(data, topviews))


def get_user_selection():
    while True:
        choice = input("Please select:\n(1) Monthly pageviews counts by article\n(2) Most viewed articles in a specific month\n").strip()
        if choice not in ["1", "2"]:
            print("Please select (1) or (2): ")
            continue
        return choice


def get_article_info():
    url = input("What is the English language wikipedia article URL?\n").strip()
    while True:
        try:
            year = input("What is the desired year (YYYY)? ").strip()
            int(year)
            break
        except:
            print("Please input a valid year")
            continue

    url = snip_url(url)
    return Article(url, year)


def snip_url(url):
    # Get article name from Wikipedia URL
    article_name = url.split("/")[-1]
    return article_name


def get_pageviews(article):
    # Pass URL and year into Wikipedia API, parse JSON response
    endpoint = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/{article.url}/monthly/{article.year}010100/{article.year}123100"
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()

    sys.exit(f"Error: {response.status_code}")


def tabulate_pageviews(data):
    # Store pageviews data from JSON in a list of lists and tabulate it

    table = []
    for item in data["items"]:
        table.append([item["timestamp"][:4], item["timestamp"][4:6], item["views"]])
    return tabulate(table, headers=["Year", "Month", "Pageviews"], tablefmt="grid")


def get_topview_info():
    year = input("Input desired year (YYYY): ").strip()
    month = input("Input desired month (MM): ").strip()
    while True:
        try:
            numarticles = int(input("Input desired number of articles, up to 1000: ").strip())
            if numarticles < 1:
                print("Please input a number of articles greater than zero")
                continue
            break
        except:
            print("Please input a valid number of articles")
            continue
    return TopViews(month, year, numarticles)


def get_topviews(top_views):
    # Pass user-defined year and month into API, parse JSON response
    endpoint = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/top/en.wikisource/all-access/{top_views.year}/{top_views.month}/all-days"
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()

    sys.exit(f"Error: {response.status_code}")


def tabulate_topviews(data, top_views):
    # Store topviews data from JSON in a list of lists and tabulate it

    table = []
    for article in data["items"][0]["articles"]:
        # stop appending data once the number of articles reaches the user defined limit
        if len(table) == top_views.numarticles:
            break
        table.append([article["rank"], article["article"], article["views"]])
    return tabulate(table, headers=["Rank", "Article", "Pageviews"], tablefmt="grid")


if __name__ == "__main__":
    main()
