from flask import *
from datetime import datetime
from flask_assets import Bundle, Environment
from flask_bootstrap import Bootstrap



app = Flask(__name__)
Bootstrap(app)
assets = Environment(app)

js = Bundle('jquery.min.js', 'browser.min.js', 'breakpoints.min.js','util.js','main.js'
            , output='gen/all.js')
assets.register('all_js', js)
css = Bundle('noscript.css', 'main.css',output='gen/all.css')
assets.register('all_css', css)

@app.route('/')
def index():
    return render_template('layouts.html')

@app.route('/About')
def about():
    return render_template('About.html')

@app.route('/navbar')
def menubar():
    return render_template('navbar.html')

@app.route('/Sms', methods=['GET', 'POST'])
def sms():
    if request.method == 'POST':
        request.form['name','number']
        return 'SUCCESS!!!'
    return render_template('Sms.html', title= 'Sms')



if __name__ == '__main__':
    app.run(debug=True)
