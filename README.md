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

If you find something you'd like to add, fork the project and submit a PR!
