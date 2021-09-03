import pymysql

MYSQL_HOST = "localhost"
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user="root",
    passwd="root",
    database="blog_db",
    charset="utf8"
)


def conn_mysql():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)

    return MYSQL_CONN
