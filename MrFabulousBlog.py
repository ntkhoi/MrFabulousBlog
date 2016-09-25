from flask import Flask , render_template , request

from BlogModel import db
from config import app
from controler import post_controler
from lib import utils

user = {'nickname': 'Miguel'}  # fake user

# @app.route('/')
# def root():
#     return render_template('index.html', title = 'Home' )

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/index/<int:page>", methods=["GET", "POST"])
def homepage(page=1):
    return post_controler.get_latest_post(page=page)

@app.route("/post/<int:post_id>")
def post(post_id):
    return post_controler.show_single_post(post_id)


@app.route("/publish", methods=["GET", "POST"])
def add_post():
    if request.method == 'GET':
        return render_template("add_post.html")
    elif request.method == 'POST':
        a =  request.form['title']
        b = request.form['content']
        print a
        print b
        return post_controler.add_post()




@app.before_first_request
def initialize_database():
    db.create_all()


app.jinja_env.globals['has_readmore_tag'] = utils.has_readmore_tag
app.jinja_env.globals['get_short_content'] = utils.get_short_content

if __name__ == '__main__':
    db.init_app(app)
    app.run()
