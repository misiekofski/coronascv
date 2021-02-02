from app import db

class VaccinesByDate(db.Model):
    __tablename__ = 'vaccines'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    vaccinated_people_num = db.Column(db.Integer)

    def __init(self,date=None, vaccinated_people_num=None):
        self.date = date
        self.vaccinated_people_num = vaccinated_people_num