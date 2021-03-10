from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<strong>Миссия Колонизация Марса</strong>'


@app.route('/index')
def ind():
    return '<strong>И на Марсе будут яблони цвести!</strong>'


@app.route('/promotion')
def prom():
    return '''
	<strong>Человечество вырастает из детства.!</strong></br>
	<strong>Человечеству мала одна планета.</strong></br>
	<strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong></br>
	<strong>И начнем с Марса!</strong></br>
	<strong>Присоединяйся!</strong>
	'''


@app.route('/image_mars')
def mars():
    return '''<title>Привет, Марс!</title>
	<h1>Жди нас, Марс!</h1></br>
	<img src="{url_for('static', filename='img/mars.png')}"</br>
	<p>Вот она какая, красная планета.</p>
	'''


@app.route('/promotion_image')
def prom_image():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
	<title>Колонизация</title>
	<link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
</head>
<body>
	<h1>Жди нас, Марс!</h1>
	<img src="{url_for('static', filename='img/mars.png')}">
	<div class="bg-secondary">
	<h3 class='grey'>Человечество вырастает из детства.</h3>
	</div>
	<div class="bg-success">
	<h3 class='green'>Человечеству мала одна планета.</h3>
	</div>
	<div class="bg-secondary">
	<h3 class='grey'>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
	</div>
	<div class="bg-warning">
	<h3 class='yellow'>И начнем с Марса!</h3>
	</div>
	<div class="bg-danger">
	<h3 class='red'>Присоединяйся!</h3>
	</div>



	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
</body>
</html>'''


@app.route('/choice/<planet>')
def choice(planet):
    return f'''
	<title>Варианты выбора</title>
	<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
	<h1>Мое предложение: {planet}</h1>
	<h3>Эта планета близка к земле;</h3
	<div class="alert alert-success">
		<h5>На ней много необходимых ресурсов;</h5>
	</div>
	<div class="alert alert-secondary">
		<h5>На ней есть вода и атмосфера;</h5>
	</div>
	<div class="alert alert-warning">
		<h5>На ней есть небольшое магнитное поле</h5>
	</div>
	<div class="alert alert-danger">
		<h5>Наконец, она просто красива!</h5>
	</div>
	'''


@app.route('/astronaut_selection')
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
						  	<div class='text-center'>
                            	<h2>Анкета претендента</h2>
								<h5>На участие в миссии</h5>
							</div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" aria-describedby="Surname" placeholder="Введите фамилию">
                                    <input type="text" class="form-control" placeholder="Введите имя">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
