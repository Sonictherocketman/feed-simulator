import json, random, os

from flask import Flask, request, Response
import lxml

import utils


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cache = os.environ.get('cache', os.path.join(BASE_DIR, 'cache'))
app = Flask(__name__)

if not os.path.exists(cache):
    os.mkdir(cache)


def _should_add_item(request):
    if request.args.get('random', False):
        new = True if random.random() > 0.5 else False
    else:
        new = request.args.get('new', False)
    return new


@app.route("/")
def home():
    return "Hello World!"


@app.route('/rss/<feed_id>')
def rss(feed_id):
    path = '{}.xml'.format(os.path.join(cache, feed_id))
    clear = request.args.get('clear', False)
    if not clear:
        try:
            with open(path, 'r') as f:
                # Get the feed from the cache or make new.
                feed = lxml.etree.parse(f)
        except (FileNotFoundError):
            feed = utils.get_default_rssfeed(feed_id)
    else:
        feed = utils.get_default_rssfeed(feed_id)

    if _should_add_item(request):
        new_item = utils.get_new_rssfeed_item()
        feed.xpath('/rss/channel')[0].insert(0, new_item)

    data = lxml.etree.tostring(feed)
    with open(path, 'wb+') as f:
        f.seek(0)
        f.write(data)

    return Response(data, mimetype='application/xml')


@app.route('/jsonfeed/<feed_id>')
def jsonfeed(feed_id):
    path = '{}.json'.format(os.path.join(cache, feed_id))
    clear = request.args.get('clear', False)
    if not clear:
        try:
            with open(path, 'r') as f:
                # Get the feed from the cache or make new.
                feed = json.load(f)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            feed = utils.get_default_jsonfeed(feed_id)
    else:
        feed = utils.get_default_jsonfeed(feed_id)

    if _should_add_item(request):
        new_item = utils.get_new_jsonfeed_item()
        feed['items'].insert(0, new_item)

    with open(path, 'w+') as f:
        f.seek(0)
        json.dump(feed, f, sort_keys=True)

    return Response(json.dumps(feed, indent=2), mimetype='application/json')
