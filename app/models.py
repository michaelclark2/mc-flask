from app import db

association_table = db.Table('association', db.metadata,
  db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
  db.Column('tech_id', db.Integer, db.ForeignKey('tech.id')))

class Project(db.Model):
  __tablename__ = 'project'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200), index=True, unique=True)
  desc = db.Column(db.String(2000))
  techs = db.relationship("Tech", secondary=association_table)

  def __repr__(self):
    return '<Project {}>'.format(self.title)

class Tech(db.Model):
  __tablename__ = 'tech'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), index=True, unique=True)
  icon = db.Column(db.String(500), index=True, unique=True)

  def __repr__(self):
    return '<Tech {}>'.format(self.name)
