from app import db
from flask_login import UserMixin
from dataclasses import dataclass

association_table = db.Table('project_techs', db.metadata,
  db.Column('project_id', db.Integer, db.ForeignKey('projects.id')),
  db.Column('tech_id', db.Integer, db.ForeignKey('techs.id')))


@dataclass
class Tech(db.Model):
  id: int
  name: str
  icon: str

  __tablename__ = 'techs'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), index=True, unique=True)
  icon = db.Column(db.String(500), index=True, unique=True)

  def __repr__(self):
    return '<Tech {}>'.format(self.name)

  def __str__(self):
    return self.name

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
