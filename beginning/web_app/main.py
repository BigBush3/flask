from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("D:/flask/beginning/web_app/db/blogs.db")
    user = User()
    user.name = "Пользователь 1"
    user.name = "Пользователь 2"
    user.name = "Пользователь 3"
    user.about = "биография пользователя 1"
    user.about = "биография пользователя 2"
    user.about = "биография пользователя 3"
    user.email = "email@email1.ru"
    user.email = "email@email2.ru"
    user.email = "email@email3.ru"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    news = News(title="Первая новость", content="Привет блог!", 
        user_id=1, is_private=False)
    db_sess.add(news)
    db_sess.commit()


if __name__ == '__main__':
    main()