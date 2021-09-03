from flask_login import UserMixin
from db_model.mysql import conn_mysql


class User(UserMixin):
    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id
        self.user_email = user_email
        self.blog_id = blog_id

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get(user_id):
        mysql_db = conn_mysql()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * " +\
            "FROM user_info " +\
            "WHERE USER_ID='{}'".format(
                user_id
            )
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            db_cursor.close()
            return None
        print("Login:{}".format(user))
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        db_cursor.close()
        return user

    @staticmethod
    def find(user_email):
        mysql_db = conn_mysql()
        db_cursor = mysql_db.cursor()
        sql = "SELECT * " +\
            "FROM user_info " +\
            "WHERE USER_EMAIL='{}'".format(
                user_email
            )
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        if not user:
            db_cursor.close()
            return None
        print("Find:{}".format(user))
        user = User(user_id=[0], user_email=user[1], blog_id=user[2])
        db_cursor.close()
        return user

    @staticmethod
    def create(user_email, blog_id):
        user = User.find(user_email)
        if user == None:
            mysql_db = conn_mysql()
            db_cursor = mysql_db.cursor()
            sql = "INSERT INTO user_info " +\
                "(USER_EMAIL, BLOG_ID) " +\
                "VALUES ('{}', '{}')".format(
                    user_email,
                    blog_id
                )

            db_cursor.execute(sql)
            mysql_db.commit()
            return User.find(user_email)
        else:
            return user
