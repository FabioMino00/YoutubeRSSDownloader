import feedparser

FEEDS = {
    'breakingitaly': 'https://www.youtube.com/feeds/videos.xml?channel_id=UC4V3oCikXeSqYQr0hBMARwg'
}


feed = feedparser.parse(FEEDS['breakingitaly'])

if feed.status == 200:
    for entry in feed.entries:
        url = entry.link

        if 'shorts' in entry.link:
            print("Shorts detected")
        else:
            print(entry.title)
            print(entry.link)
else:
    print("Failed to get RSS feed. Status code:", feed.status)