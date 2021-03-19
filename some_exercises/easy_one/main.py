from flask import Flask
import db_session
from users import User
from jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('B:/programming/yandex_luceym/flask_learning/flask/some_exercises/easy_one/db/base.db')
    db_sess = db_session.create_session()
    for user in db_sess.query(User).filter(User.age < 18):
        print(f"{user} {user.age} years")


if __name__ == '__main__':
    main()