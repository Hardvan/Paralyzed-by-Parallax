from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/moonlight')
def moonlight():

    return render_template('moonlight.html')


@app.route('/mountain')
def mountain():

    return render_template('mountain.html')


if __name__ == "__main__":
    app.run(debug=True)
