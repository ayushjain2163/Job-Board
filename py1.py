from flask import Flask, redirect,url_for

app=Flask(__name__)
@app.route("/")
def hello():
    return "hello world"

@app.route("/temp")
def temp():
    return "study hard"

@app.route("/welcome/<string:track>")  #url binding
def welcome(track):
    return f"Hello people welcome to {track} bootcamp"

@app.route("/hc/<string:option>")
def hc(option):
    if option=="CAD":
        return redirect(url_for('welcome',track=option))
    else :
        return redirect(url_for('temp'))  # here in url_for we use function not the routes

if __name__=="__main__":
    app.run(debug=True) 