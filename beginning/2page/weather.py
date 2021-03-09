from flask import Flask
import ws

app = Flask(__name__)

@app.route('/')
def index():
	with open('D:/flask/beginning/2page/design.html', 'r', encoding='utf-8') as html_stream:
		html = html_stream.read()
		weather = ws.get_weather()
		for replace in weather:
			html = html.replace(f'{{ {replace} }}', str(weather[replace]))



if __name__ == '__main__':
	app.run(port=80, host='127.0.0.1', debug=True, load_dotenv=True)