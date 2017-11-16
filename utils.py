from collections import OrderedDict
from datetime import datetime
import uuid

from loremipsum import get_sentence
from lxml.builder import E


# JSON Feed Utils.


def get_default_jsonfeed(feed_id):
    return OrderedDict([
      ("version", "https://jsonfeed.org/version/1"),
      ("title", feed_id),
      ("description", "A testing feed with id: %s" % feed_id),
      ("home_page_url", "https://jsonfeed.org/"),
      ("feed_url", "https://jsonfeed.org/%s" % feed_id),
      ("author", {
        "name": "A cool person."
      }),
      ("items", [])
    ])

def get_new_jsonfeed_item():
    id = uuid.uuid4().hex
    date = datetime.utcnow()
    content = get_sentence(1)

    return {
      "id": "https://jsonfeed.org/2017/05/17/{}".format(id),
      "url": "https://jsonfeed.org/2017/05/17/{}".format(id),
      "title": "Test item: {}".format(id),
      "content_html": "<p>{}</p>".format(content),
      "content": "{}".format(content),
      "date_published": date.isoformat()
    }


# RSS Feed Utils.


def get_default_rssfeed(feed_id):
    return (
        E.rss(
            E.channel(
                E.title(feed_id),
                E.link("https://rssfeed.org/%s" % feed_id),
                E.description("A testing feed with id: %s" % feed_id),
            )
        )


    )

def get_new_rssfeed_item():
    id = uuid.uuid4().hex
    date = datetime.utcnow()
    content = get_sentence(1)

    return (
        E.item(
            E.title("Test item: {}".format(id)),
            E.description(content),
            E.pubDate(date.isoformat()),
            E.guid(id),
        )
    )
