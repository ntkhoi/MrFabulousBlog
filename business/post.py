from BlogModel.post import Post as  DBPost
from datetime import datetime
from lib.exceptions import InvalidFieldError, AccessDeniedError, UserNotFoundError, PostNotFoundError
from lib.utils import is_id_valid, get_slug_from_string


class Post(object):
    @classmethod
    def get_posts_pagination(cls, page=1, per_page=10):
        """
        Get many post at a time, order by post time
        :param page: page index begin at 1
        :param per_page:
        :return:
        """
        if not is_id_valid(page):
            page = 1

        if int(per_page) <= 0 or int(per_page) >= 50:
            per_page = 10

        pagination = DBPost.pagination_get(page=page, per_page=per_page, order_by="time desc")
        return pagination

    @classmethod
    def get_post(cls,post_id):
        if not is_id_valid(post_id):
            raise InvalidFieldError("Post is invalid ", ["post_id"])
        post = DBPost.get_by_id(post_id)
        return  post

    @classmethod
    def add_post(cls, user_id, title, content, feature_image=None, tags=None, categories=None, draft=False):

            # not need to check author existent

            # if title is empty, use curent date as title
            if len(title) == 0:
                time = datetime.now()
                title = time.strftime("%A %d %B %Y")

            if not content:
                raise InvalidFieldError("Post's content could not be empty", ["content"])

            if not categories:
                categories = ""
                # categories = [default.DEFAULT_CATEGORY]

            args = {
                "user_id": user_id,
                "title": title,
                "content": content,
                "feature_image": feature_image,
                "tags": tags,
                "categories": categories,
                "draft": draft
            }

            post = DBPost(**args)
            try:
                post.save()
                return post
            except:
                raise
    # @classmethod
    # def get_post(cls, post_id):
    #     if not is_id_valid(post_id):
    #         raise InvalidFieldError("Post id is invalid", ["post_id"])
    #     post = DBPost.get_by_id(post_id)
    #
    #     # if post:
    #     #     comments = post.comments.all()
    #     #
    #     #     post.comments = comments
    #     return post


