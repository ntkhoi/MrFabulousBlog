__author__ = 'bluzky'

class InvalidFieldError(Exception):
    def __init__(self, msg, error_fields = []):
        self.error_fields = error_fields
        super(InvalidFieldError, self).__init__(msg)

class DuplicatedError(Exception):
    def __init__(self, error_field, value):
        self.error_field = error_field
        self.error_value = value
        msg = "{0} with value {1} has ben used".format(error_field, value)
        super(DuplicatedError, self).__init__(msg)

class UserNotFoundError(Exception):
    def __init__(self, msg=None, name=None, email=None):

        if name:
            msg = "User %s does not exist" % name
            self.username = name
        elif email:
            msg = "User with email %s does not exist" % email
            self.email = email
        elif msg is None:
            msg = "User does not exist"

        super(UserNotFoundError, self).__init__(msg)

class UserNotActivatedError(Exception):
    def __init__(self, email):
        self.user_email = email
        super(UserNotActivatedError, self).__init__("User has not been activated")

class PostNotFoundError(Exception):
    def __init__(self, msg = None, post_id=None):
        if post_id:
            self.post_id = post_id
            msg = "Post with id = %d does not exist"
        elif msg is None:
            msg = "Post does not exist"

        super(PostNotFoundError,self).__init__(msg)

class CommentNotFoundError(Exception):
    def __init__(self, msg = None, comment_id=None):
        if comment_id:
            self.comment_id = comment_id
            msg = "Comment with id = %d does not exist"
        elif msg is None:
            msg = "Comment does not exist"

        super(CommentNotFoundError,self).__init__(msg)

class AccessDeniedError(Exception):
    def __init__(self, msg):
        super(AccessDeniedError,self).__init__(msg)

class InvalidActionError(Exception):
    def __init__(self, msg):
        super(InvalidActionError,self).__init__(msg)