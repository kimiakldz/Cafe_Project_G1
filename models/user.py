from core.manager import db, login_manager
# from flask_login import UserMixin
from flask_security import UserMixin, RoleMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


user_roles = db.Table('user_roles',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                      )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    address = db.Column(db.String)
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=user_roles,
                            backref=db.backref('users', lazy='dynamic'))
    #
    # def has_role(self, role):
    #     # db is your database session.
    #     query = db.query(Role).filter(Role.title == role).first()
    #     if query:
    #         if query.title in self.roles:
    #             return True
    #     return False


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)





