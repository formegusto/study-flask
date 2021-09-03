import pymongo

MONGO_HOST = "localhost"
MONGO_CONN = pymongo.MongoClient("mongodb://{}".format(MONGO_HOST))


def conn_mongodb():
    try:
        MONGO_CONN.admin.command("ismaster")
        blog_ab = MONGO_CONN.blog_session_db.blog_db
    except:
        MONGO_NEW_CONN = pymongo.MongoClient("mongodb://{}".format(MONGO_HOST))
        blog_ab = MONGO_NEW_CONN.blog_session_db.blog_db

    return blog_ab
