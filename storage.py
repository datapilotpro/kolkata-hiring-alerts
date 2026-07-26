import json
import os

FILE_NAME = "sent_links.json"


def load_sent_links():
    """Load previously sent links."""
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_sent_links(links):
    """Save all sent links."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(links, f, indent=4)


def is_duplicate(link):
    """Check whether link already exists."""
    sent = load_sent_links()
    return link in sent


def add_link(link):
    """Save a new link."""
    sent = load_sent_links()

    if link not in sent:
        sent.append(link)
        save_sent_links(sent)
