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


@app.route('/hackedtext')
def hackedtext():

    return render_template('hackedtext.html')


@app.route('/liquid')
def liquid():

    return render_template('liquid.html')


@app.route('/magicalhover')
def magicalhover():

    return render_template('magicalhover.html')


@app.route('/gradientborder')
def gradientborder():

    return render_template('gradientborder.html')


@app.route('/tabbar')
def tabbar():

    return render_template('tabbar.html')


@app.route('/cards_slider')
def cards_slider():

    return render_template('cards_slider.html')


@app.route('/card_grid_hover')
def card_grid_hover():

    return render_template('card_grid_hover.html')


@app.route('/pill_buttons')
def pill_buttons():

    return render_template('pill_buttons.html')


@app.route('/tooltip')
def tooltip():

    return render_template('tooltip.html')



@app.route('/magical_text')
def magical_text():

    return render_template('magical_text.html')


if __name__ == "__main__":
    app.run(debug=True)
