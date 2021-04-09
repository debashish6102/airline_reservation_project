from project import db
class airport(db.Model):
    airport_name = db.Column(db.String(50), unique=True, nullable=False)
    airport_id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<airport %r>' % self.airport_id


class flight(db.Model):
    flight_no = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    city_source = db.Column(db.String(10), nullable=False)
    city_destination = db.Column(db.String(10), nullable=False)
    no_of_seats = db.Column(db.Integer, nullable=False)
    time_dept = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_arrival = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    time_duration = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<flight %r>' % self.flight_no


class user(db.Model):
    user_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(16), nullable=False)
    sex = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"user('{self.userid}', '{self.first_name}, '{self.last_name}', '{self.sex}')"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        spec_symbols = ['$', '@', '#', '%', '!', '*']
        val = True
        if len(password)<6:
            return 'error lenght should be at least 6'
        if len(password)>16:
            return 'error lenght should not be more than 16'
        if not any(x.isdigit() for x in password):
            return 'error password should have one numeral'
        if not any(x.isupper() for x in password):
            return 'error password should have one upper digit'
        if not any(x.islower() for x in password):
            return 'error password should have one lower digit'
        if not any(x in spec_symbols for x in password):
            return 'error password should have one special symbol(!,@,#,$,%,*)'
        else:
            return check_password_hash(self.password_hash, password)

class city(db.Model):
    city_name = db.Column(db.String(30), nullable=False)
    city_id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    state = db.Column(db.String(10), nullable=False)
    country = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return '<city %r>' % self.city_id