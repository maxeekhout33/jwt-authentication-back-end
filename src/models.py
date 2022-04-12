from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(280), unique=False, nullable=False)
    name = db.Column(db.String(100))
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
            # do not serialize the password, its a security breach
        }

    @classmethod
    def create(cls, name, email, password):
        instance = cls(
            name=name,
            email=email,
            password=password
        )
        if isinstance(instance, cls):
            return instance
        else:
            return None

    @classmethod
    def login(cls, email, password):
        user = cls.query.filter_by(
            email=email
        ).one_or_none()
        if (not isinstance(user, cls)):
            return user
        if user.password == password:
            return user
        else:
            return False