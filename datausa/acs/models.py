from datausa.acs.abstract_models import BaseAcs5, GeoId, AcsOccId
from datausa.acs.abstract_models import db


class Acs5_Yg(BaseAcs5, GeoId):
    __tablename__ = "yg"
    median_moe = 1

    year = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Float)
    age_moe = db.Column(db.Float)
    age_rank = db.Column(db.Integer)
    pop = db.Column(db.Float)
    pop_moe = db.Column(db.Float)
    pop_rank = db.Column(db.Integer)
    income = db.Column(db.Float)
    income_moe = db.Column(db.Float)
    income_rank = db.Column(db.Integer)


class Acs5_Yg_Income(BaseAcs5, GeoId):
    __tablename__ = "yg_income"
    median_moe = 1.2

    year = db.Column(db.Integer, primary_key=True)
    income = db.Column(db.Float)
    income_moe = db.Column(db.Float)


class Acs5_Ygo_Num_Emp(BaseAcs5, GeoId, AcsOccId):
    __tablename__ = "ygo_num_emp"
    median_moe = 2

    year = db.Column(db.Integer, primary_key=True)
    num_emp = db.Column(db.Float)
    num_emp_moe = db.Column(db.Float)
    num_emp_rca = db.Column(db.Float)
    num_emp_male = db.Column(db.Float)
    num_emp_moe_male = db.Column(db.Float)
    num_emp_female = db.Column(db.Float)
    num_emp_moe_female = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {"geo": GeoId.LEVELS, "acs_occ": AcsOccId.LEVELS}


class Acs5_Ygo_Earnings(BaseAcs5, GeoId, AcsOccId):
    __tablename__ = "ygo_earnings"
    median_moe = 2

    year = db.Column(db.Integer, primary_key=True)
    earnings = db.Column(db.Float)
    earnings_moe = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {"geo": GeoId.LEVELS, "acs_occ": AcsOccId.LEVELS}

class Acs5_Yg_Conflict(BaseAcs5, GeoId):
    __tablename__ = "yg_conflict"
    median_moe = 2

    year = db.Column(db.Integer, primary_key=True)
    total_vets = db.Column(db.Float)
    total_vets_moe = db.Column(db.Float)
    wwii = db.Column(db.Float)
    wwii_moe = db.Column(db.Float)
    korea = db.Column(db.Float)
    korea_moe = db.Column(db.Float)
    vietnam = db.Column(db.Float)
    vietnam_moe = db.Column(db.Float)
    gulf90s = db.Column(db.Float)
    gulf90s_moe = db.Column(db.Float)
    gulf01 = db.Column(db.Float)
    gulf01_moe = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {"geo": GeoId.LEVELS}