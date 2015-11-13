from datausa.database import db
from datausa.attrs.models import Geo, Soc, Naics, PumsNaics
from datausa.core.models import BaseModel
from datausa.attrs.consts import NATION, STATE, MSA, ALL


class Bls(BaseModel):
    source_title = 'Bureau of Labor Statistics'
    __table_args__ = {"schema": "bls"}


class GrowthO(db.Model, Bls):
    __tablename__ = 'growth_o'
    median_moe = 1

    soc = db.Column(db.String, primary_key=True)
    emp_2012_thousands = db.Column(db.Float)
    emp_2022_thousands = db.Column(db.Float)
    emp_pct_2012 = db.Column(db.Float)
    emp_pct_2022 = db.Column(db.Float)
    change_thousands = db.Column(db.Float)
    change_thousands = db.Column(db.Float)
    pct_change = db.Column(db.Float)
    pct_change = db.Column(db.Float)
    openings_thousands = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {
            "soc": [ALL, "0", "1", "2", "3"]
        }

class GrowthI(db.Model, Bls):
    __tablename__ = 'growth_i'
    median_moe = 2

    naics = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    emp_2002_thousands = db.Column(db.Float)
    emp_2012_thousands = db.Column(db.Float)
    emp_2022_thousands = db.Column(db.Float)
    emp_change_2002_2022 = db.Column(db.Float)
    emp_pct_change_2012_2022 = db.Column(db.Float)
    output_2002 = db.Column(db.Float)
    output_2012 = db.Column(db.Float)
    output_2022 = db.Column(db.Float)
    output_carc_2002_2012 = db.Column(db.Float)
    output_carc_2012_2022 = db.Column(db.Float)
    emp_carc_2002_2012 = db.Column(db.Float)
    emp_carc_2012_2022 = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {
            "naics": [ALL, "0", "1", "2", "3", "4"]
        }

class BlsCrosswalk(db.Model, Bls):
    __tablename__ = 'bls_crosswalk'
    pums_naics = db.Column(db.String, db.ForeignKey(PumsNaics.id),
                           primary_key=True)
    bls_naics = db.Column(db.String, primary_key=True)


class OesYgo(db.Model, Bls):
    __tablename__ = 'oes_ygo'

    median_moe = 2

    year = db.Column(db.Integer, primary_key=True)
    geo = db.Column(db.String, db.ForeignKey(Geo.id), primary_key=True)
    soc = db.Column(db.String, db.ForeignKey(Soc.id), primary_key=True)

    tot_emp = db.Column(db.Integer)
    tot_emp_prse = db.Column(db.Float)
    avg_wage = db.Column(db.Float)
    avg_wage_prse = db.Column(db.Float)
    tot_emp_rca = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {
            "geo": [ALL, NATION, STATE, MSA],
            "soc": [ALL, "0", "1", "2", "3"]
        }

    @classmethod
    def geo_filter(cls, level):
        if level == ALL:
            return True
        level_map = {NATION: "010", STATE: "040", MSA: "050"}
        level_code = level_map[level]
        return cls.geo.startswith(level_code)


class QcewYgi(db.Model, Bls):
    __tablename__ = 'qcew_ygi'
    median_moe = 2

    year = db.Column(db.Integer, primary_key=True)
    geo = db.Column(db.String, db.ForeignKey(Geo.id), primary_key=True)
    naics = db.Column(db.String, db.ForeignKey(Naics.id), primary_key=True)

    naics_level = db.Column(db.Integer)
    avg_annual_pay = db.Column(db.Float)
    total_annual_wages = db.Column(db.Float)
    annual_contributions = db.Column(db.Float)
    annual_avg_emplvl = db.Column(db.Float)
    total_annual_wages_rca = db.Column(db.Float)
    annual_avg_estabs = db.Column(db.Float)
    taxable_annual_wages = db.Column(db.Float)
    annual_avg_wkly_wage = db.Column(db.Float)

    @classmethod
    def get_supported_levels(cls):
        return {
            "geo": [ALL, NATION, STATE, MSA],
            "naics": [ALL, "0", "1", "2", "3", "4"]
        }

    @classmethod
    def geo_filter(cls, level):
        if level == ALL:
            return True
        level_map = {NATION: "010", STATE: "040", MSA: "050"}
        level_code = level_map[level]
        return cls.geo.startswith(level_code)

    @classmethod
    def naics_filter(cls, level):
        if level == ALL:
            return True
        return cls.naics_level == level
