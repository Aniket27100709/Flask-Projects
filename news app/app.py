from flask import Flask,render_template
import requests

app=Flask(__name__)

@app.route('/')
def index():
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=006e5e034a0140918161a291946d9e60"
    r=requests.get(url).json()
    case={
        'articles':r['articles']
    }
    return render_template("index.html",case=case)

if __name__=='__main__':
    app.run(debug=True)