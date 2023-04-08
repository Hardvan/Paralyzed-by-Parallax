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


@app.route('/jungle')
def jungle():

    return render_template('jungle.html')


@app.route('/serenescroller')
def serenescroller():

    return render_template('serenescroller.html')


@app.route('/futurecard')
def futurecard():

    return render_template('futurecard.html')


@app.route('/superslider')
def superslider():

    return render_template('superslider.html')


if __name__ == "__main__":
    app.run(debug=True)
