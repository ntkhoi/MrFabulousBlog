from base import db, ModelMethod

class User(db.Model , ModelMethod):
    __tableName__ = 'user'
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120 ) , unique=True)
    password = db.Column(db.String(80))
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    avatar = db.Column(db.String(512), default="")
    brief = db.Column(db.String(1024), default="")
    role = db.Column(db.String(20), default="editor")
    activated = db.Column(db.Boolean, default=False)

    # activation_id is used for activating account and reset password
    activation_id = db.Column(db.String(64))

    posts = db.relationship('Post', backref=db.backref('author', lazy='select'), lazy='dynamic')
    comments = db.relationship('Comment', backref=db.backref('user', lazy='select'), lazy='dynamic')

    @property
    def ful_name(self):
        return "%s %s" % (self.first_name , self.last_name)

    def __init__(self, email, password, first_name, last_name, avatar=None, brief=None, role=None):
        # self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        if avatar:
            self.avatar = avatar
        if brief:
            self.brief = brief

        if role:
            self.role = role

    def is_authenticated(self):
        if self.id:
            return True
        else:
            return False

    def is_active(self):
        return self.activated

    def is_anonymous(self):
        if self.id:
            return False
        else:
            return True

    def get_id(self):
        return unicode(self.id)  # python 2

    def public_info(self):
        user_info = {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role,
        }
        return user_info

    def __repr__(self):
        return "User: %s %s" % (self.first_name, self.last_name)
