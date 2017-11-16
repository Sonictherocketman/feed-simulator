# RSS and JSON Feed Simulator

*A small flask app that generates and serves pseudo-random RSS and JSON Feeds for testing purposes.*


## About this Project

Writing code that needs to parse and store the contents of remote RSS and JSON feeds can be tricky. Testing against real feeds can be slow and uncontrolled, and testing against static fixtures might not catch bugs when feeds are updated (or updated incorrectly).

This simple Flask app generates RSS and JSON feeds that can be relied upon to update when told and remain static otherwise, and since it's locally, it's easy to write tests against.


## Installation and Running

Installation is super easy, and running it is even more so.


```bash
$ git clone https://github.com/Sonictherocketman/feed-simulator
$ cd feed-simulator
$ pip install -r requirements.txt
$ ./start_server
```


## Contributions Welcome

I'm still looking to add a number of features like:

- Tests and Test Coverage.
- Support for `HEAD` requests.
- Purposely malformed feeds.
- Feeds with repeated, unreliable GUID/ID elements.
- Routes that return incorrect headers.
    - Feed was updated but `HEAD` headers say it wasn't.
    - Feed was NOT updated but `HEAD` headers say it was.
- RSS 1.0 and 0.9 support
- Atom support

If you find something you'd like to add, fork the project and submit a PR!


## Documentation

This app has a number of different URL routes and params it supports.


### Routes

- `/rss/<feed_id>`: Generates an RSS 2.0 feed with the given ID.

#### Sample Request

```
$ http :5000/jsonfeed/testing?random=1&clear=1

<rss>
    <channel>
        <title>testing</title>
        <link>https://rssfeed.org/testing</link>
        <description>A testing feed with id: testing</description>
        <item>
            <title>Test item: 9c2753f3653149b8a03d09c9cf5cb610</title>
            <description>Lorem ipsum.</description>
            <pubDate>2017-11-16T19:30:36.448431</pubDate>
            <guid>9c2753f3653149b8a03d09c9cf5cb610</guid>
        </item>
    </channel>
</rss>
```


- `/jsonfeed/<feed_id>`: Generates a JSON Feed with the given ID.

#### Sample Request

```
$ http :5000/jsonfeed/testing?random=1&clear=1

{
    "version": "https://jsonfeed.org/version/1",
    "title": "testing",
    "description": "A testing feed with id: testing",
    "home_page_url": "https://jsonfeed.org/",
    "feed_url": "https://jsonfeed.org/testing",
    "author": {
        "name": "A cool person."
    },
    "items": [
        {
            "id": "https://jsonfeed.org/2017/05/17/6010abc366254a7690ca1dc6e0538e62",
            "content_html": "<p>Lorem ipsum.</p>",
            "title": "Test item: 6010abc366254a7690ca1dc6e0538e62",
            "content": "Lorem ipsum.",
            "url": "https://jsonfeed.org/2017/05/17/6010abc366254a7690ca1dc6e0538e62",
            "date_published": "2017-11-16T19:28:30.961458"
        }
    ]
}
```


### Params

Both routes accept the same parameters:

- `new`: Adds a new feed item to the cached feed.
- `random`: Randomly adds a new item to the feed.
- `clear`: Clears the cached feed and creates a new one.

**Note:** Parameters must contain a value. `random=1` not just `random`
