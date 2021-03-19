from flask import Flask
import db_session
from users import User
from jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('B:/programming/yandex_luceym/flask_learning/flask/some_exercises/easy_one/db/base.db')
    user = Jobs()
    user.team_leader = 1
    user.job = 'deployment of residential modules 1 and 2'
    user.work_size = 15
    user.collaborators = '2, 3'
    user.start_date = datetime.datetime.now()
    user.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


if __name__ == '__main__':
    main()