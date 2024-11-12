from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/callback')
def callback():
    # Handle the callback logic here
    return 'Callback received!'

if __name__ == '__main__':
    app.run(debug=True)
