from app import db
from dataclasses import dataclass

"""An associaction table for project techs"""
association_table = db.Table('project_techs', db.metadata,
  db.Column('project_id', db.Integer, db.ForeignKey('projects.id')),
  db.Column('tech_id', db.Integer, db.ForeignKey('techs.id')))


@dataclass
class Tech(db.Model):
  # Define the what I want from JSON using @dataclass
  id: int
  name: str
  icon: str
  in_prod: bool

  # SQLAlchemy definitions
  __tablename__ = 'techs'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), index=True, unique=True)
  icon = db.Column(db.String(500), index=True, unique=True)
  in_prod = db.Column(db.Boolean)

  def __repr__(self):
    return '<Tech {}>'.format(self.name)

  def __str__(self):
    return self.name

  def __hash__(self):
    return self.id

@dataclass
class Project(db.Model):
  id: int
  title: str
  desc: str
  github: str
  url: str
  thumbnail: str
  techs: Tech

  __tablename__ = 'projects'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), index=True, unique=True)
  desc = db.Column(db.String(2000))
  github = db.Column(db.String(200))
  url = db.Column(db.String(200))
  thumbnail = db.Column(db.String(500))
  techs = db.relationship("Tech", secondary=association_table)

  def __repr__(self):
    return '<Project {}>'.format(self.title)

  def __str__(self):
    return self.title
