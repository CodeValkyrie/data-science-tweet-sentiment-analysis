# I think we may need database software to help the data storage and extract which is efficient.
# If neccessary, please download the mongodb from the offical website: https://www.mongodb.com/
import json
import pymongo


# Code from https://www.thetopsites.net/article/53409156.shtml
# Generates a generator for the data given in the file to stream the data.
def stream_read_json(filename):
    start_pos = 0
    with open(filename, 'r') as f:
        while True:
            try:
                obj = json.load(f)
                yield obj
                return
            except json.JSONDecodeError as e:
                f.seek(start_pos)
                json_str = f.read(e.pos)
                obj = json.loads(json_str)
                start_pos += e.pos
                yield obj


### import the json file to the mongoDB ###
# Making a Connection with MongoClient
collection = None
try:
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    # get a database
    db = client['assign1']
    # create and the the collection
    collection = db['tweet']

except Exception as e:
    print(e)

# insert the data to the MongoDB
for item in stream_read_json('test.json'):
    tweet_dict = item
    data = collection.insert_one(tweet_dict)

# structure in mongodb 
# with the command in console
# use assign1
# db.tweet.find().pretty()
# this is one of the tweet data
'''
{
        "_id" : ObjectId("5f5e1717cf0a898c272632e4"),
        "created_at" : "Fri Aug 12 10:04:53 +0000 2016",
        "id" : NumberLong("764039948567576576"),
        "id_str" : "764039948567576576",
        "text" : "@mike4193496 @realDonaldTrump I TOTALLY CONCUR!! This Election is just CRA CRA n Corruption in our Gov is Mind Blowing!! Trump= Last Hope!!!",
        "source" : "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "truncated" : false,
        "in_reply_to_status_id" : NumberLong("764001459671150595"),
        "in_reply_to_status_id_str" : "764001459671150595",
        "in_reply_to_user_id" : NumberLong("4852163069"),
        "in_reply_to_user_id_str" : "4852163069",
        "in_reply_to_screen_name" : "mike4193496",
        "user" : {
                "id" : 1507953240,
                "id_str" : "1507953240",
                "name" : "Kim Wasson",
                "screen_name" : "kimseacret3",
                "location" : "Maryland, USA",
                "url" : "http://www.seacretdirect.com/kimwasson",
                "description" : "I Love Life, Design Beautiful Florals for all Occasions & LOVE my Bride's. I Share Seacret Skin Care w those of us who desire to look Younger,am a Grandmother 2",
                "protected" : false,
                "verified" : false,
                "followers_count" : 244,
                "friends_count" : 271,
                "listed_count" : 4,
                "favourites_count" : 9426,
                "statuses_count" : 277,
                "created_at" : "Wed Jun 12 01:12:18 +0000 2013",
                "utc_offset" : null,
                "time_zone" : null,
                "geo_enabled" : true,
                "lang" : "en",
                "contributors_enabled" : false,
                "is_translator" : false,
                "profile_background_color" : "C0DEED",
                "profile_background_image_url" : "http://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_image_url_https" : "https://abs.twimg.com/images/themes/theme1/bg.png",
                "profile_background_tile" : false,
                "profile_link_color" : "0084B4",
                "profile_sidebar_border_color" : "C0DEED",
                "profile_sidebar_fill_color" : "DDEEF6",
                "profile_text_color" : "333333",
                "profile_use_background_image" : true,
                "profile_image_url" : "http://pbs.twimg.com/profile_images/344513261566755204/793e4f7fc2661c7493d5c896f979a308_normal.jpeg",
                "profile_image_url_https" : "https://pbs.twimg.com/profile_images/344513261566755204/793e4f7fc2661c7493d5c896f979a308_normal.jpeg",
                "profile_banner_url" : "https://pbs.twimg.com/profile_banners/1507953240/1459276810",
                "default_profile" : true,
                "default_profile_image" : false,
                "following" : null,
                "follow_request_sent" : null,
                "notifications" : null
        },
        "geo" : null,
        "coordinates" : null,
        "place" : {
                "id" : "faef11a3eaa8abdb",
                "url" : "https://api.twitter.com/1.1/geo/id/faef11a3eaa8abdb.json",
                "place_type" : "city",
                "name" : "Chesapeake Beach",
                "full_name" : "Chesapeake Beach, MD",
                "country_code" : "US",
                "country" : "United States",
                "bounding_box" : {
                        "type" : "Polygon",
                        "coordinates" : [
                                [
                                        [
                                                -76.5803,
                                                38.644972
                                        ],
                                        [
                                                -76.5803,
                                                38.721348
                                        ],
                                        [
                                                -76.526929,
                                                38.721348
                                        ],
                                        [
                                                -76.526929,
                                                38.644972
                                        ]
                                ]
                        ]
                },
                "attributes" : {

                }
        },
        "contributors" : null,
        "is_quote_status" : false,
        "retweet_count" : 0,
        "favorite_count" : 0,
        "entities" : {
                "hashtags" : [ ],
                "urls" : [ ],
                "user_mentions" : [
                        {
                                "screen_name" : "mike4193496",
                                "name" : "Mike",
                                "id" : NumberLong("4852163069"),
                                "id_str" : "4852163069",
                                "indices" : [
                                        0,
                                        12
                                ]
                        },
                        {
                                "screen_name" : "realDonaldTrump",
                                "name" : "Donald J. Trump",
                                "id" : 25073877,
                                "id_str" : "25073877",
                                "indices" : [
                                        13,
                                        29
                                ]
                        }
                ],
                "symbols" : [ ]
        },
        "favorited" : false,
        "retweeted" : false,
        "filter_level" : "low",
        "lang" : "en",
        "timestamp_ms" : "1470996293571"
}

'''