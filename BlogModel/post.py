from base import db , ModelMethod
from datetime import datetime

class Post(db.Model , ModelMethod):
    __tableName__ = 'post'
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(512))
    content = db.Column(db.Text())
    feature_image = db.Column(db.String(512))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    time = db.Column(db.DateTime())
    tags = db.Column(db.String(128))
    categories = db.Column(db.String(128))
    draft = db.Column(db.Boolean(), default=False)

    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __init__(self, user_id, title, content, feature_image=None, post_date=None, tags=None, categories=(),
                 draft=False):
        self.title = title
        self.content = content
        self.user_id = user_id
        if feature_image:
            self.feature_image = feature_image
        if post_date is None:
            self.time = datetime.now()
        else:
            self.time = post_date

        if tags:
            self.tags = tags
        if categories:
            self.categories = ",".join("`%s`" % cat for cat in categories)

        self.draft = draft
