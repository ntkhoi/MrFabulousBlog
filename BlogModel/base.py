from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()

class ModelMethod(object):

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.detele(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_one(cls, filter_dict):
        return cls.query.filter_by(**filter_dict).first()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def get(cls, filter_dict=None, per_page=20, start=0, order_by=None):
        if filter_dict:
            if order_by:
                return cls.query.filter_by(**filter_dict).order_by(text(order_by)).offset(start).limit(per_page).all()
            else:
                return cls.query.filter_by(**filter_dict).offset(start).limit(per_page).all()

        else:
            if order_by:
                return cls.query.order_by(text(order_by)).offset(start).limit(per_page).all()
            else:
                return cls.query.offset(start).limit(per_page).all()

    @classmethod
    def search(cls, search_dict, per_page=20, start=0, order_by=None):
        search_str = ""
        for k, v in search_dict.items():
            search_str += " {0} LIKE '%{1}%' or".format(k, v)
        if search_str:
            search_str = search_str[:len(search_str) - 2]
        if order_by:
            return cls.query.filter(text(search_str)).order_by(text(order_by)).offset(start).limit(per_page).all()
        else:
            return cls.query.filter(text(search_str)).offset(start).limit(per_page).all()

    @classmethod
    def pagination_get(cls, filter_dict=None, page=1, per_page=10, order_by=None):
        if filter_dict:
            if order_by:
                return cls.query.filter_by(**filter_dict).order_by(text(order_by)).paginate(page=page,
                                                                                            per_page=per_page,
                                                                                            error_out=False)
            else:
                return cls.query.filter_by(**filter_dict).paginate(page=page, per_page=per_page, error_out=False)

        else:
            if order_by:
                return cls.query.order_by(text(order_by)).paginate(page=page, per_page=per_page, error_out=False)
            else:
                return cls.query.paginate(page=page, per_page=per_page, error_out=False)

    @classmethod
    def pagination_search(cls, search_dict, page=1, per_page=10, order_by=None):
        search_str = ""
        for k, v in search_dict.items():
            search_str += " {0} LIKE '%{1}%' or".format(k, v)
        if search_str:
            search_str = search_str[:len(search_str) - 2]
        if order_by:
            return cls.query.filter(text(search_str)).order_by(text(order_by)).paginate(page=page, per_page=per_page,
                                                                                        error_out=False)
        else:
            return cls.query.filter(text(search_str)).paginate(page=page, per_page=per_page, error_out=False)

    