import requests
from bs4 import BeautifulSoup
import re


def count_topic_wiki_occurences(topic, section=None):
    """
    Fetches Wikipedia article for given topic and returns number of occurences of the topic word in the article text.

    topic: the topic for the article
    section: (optional) query a given section
    """

    BASE_URL = (
        "https://en.wikipedia.org/w/api.php?action=parse&prop=text&format=json&page="
    )

    url = BASE_URL + topic
    if section is not None:
        url = url + f"&section={section}"

    # Fetch HTML and convert to lower case
    res = requests.get(url)
    if res.status_code != 200:
        print(f"Got status code {res.status_code} upon request. Quitting...")
        return

    article_text = res.json()["parse"]["text"]["*"].lower()
    topic = topic.lower()

    # Parse HTML
    soup = BeautifulSoup(article_text, "html.parser")

    # Find all text fields that include topic
    hit_list = soup.find_all(text=lambda text: text and topic in text)

    # Merge text fields
    hit_string = " ".join(hit_list)

    # Find all exact matches for topic in text
    hits = len(re.findall(r"\b" + topic + r"\b", hit_string))

    return hits


# print(count_topic_wiki_occurences("Vipps"))
