__author__ = 'bluzky'
from flask import abort, render_template, request, redirect, url_for
from business.post import Post
# from business.post import Post

# import default

PER_PAGE = 10

def get_latest_post(page):
    try:
        pagination = Post.get_posts_pagination(page=page, per_page=PER_PAGE)
        return render_template("index.html", pagination=pagination)
    except Exception as e:
        abort(404)

def show_single_post(post_id):
    try:
        post = Post.get_post(post_id)
        if post:
            return render_template("single_post.html" , post=post)
        else:
            abort(404)
    except Exception as e:
        abort(404)


def add_post():
    try:
        args = {
            "user_id": 1,
            "title": request.form["title"] or None,
            "content": request.form["content"] or None,
            "categories": request.form.getlist("categories") or None,
            "tags":  None,
            "feature_image":   None,
        }
        post = Post.add_post(**args)

        return redirect(url_for('post', post_id=post.id))
    except Exception as e :
        abort(400)

#
# #----------------------------------------------------------------------------------#
# #----------------------------------------------------------------------------------#
# #--------------------------Private Method-------------------------------------------#
# #----------------------------------------------------------------------------------#
# #----------------------------------------------------------------------------------#
#
# def __get_posts_pagination(cls, page=1, per_page=10):
#     """
#     Get many post at a time, order by post time
#     :param page: page index begin at 1
#     :param per_page:
#     :return:
#     """
#     if not is_id_valid(page):
#         page = 1
#
#     if int(per_page) <= 0 or int(per_page) >= 50:
#         per_page = 10
#
#     pagination = DBPost.pagination_get(page=page, per_page=per_page, order_by="time desc")
#     return pagination
