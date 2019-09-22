from app import app, admin, db, models
from flask_admin.contrib.sqla import ModelView
from flask import redirect, session, request, jsonify

class PrivateView(ModelView):
  def is_accessible(self):
    return session.get('authed')

admin.add_view(PrivateView(models.Project, db.session))
admin.add_view(PrivateView(models.Tech, db.session))

@app.route('/admin/login', methods=['POST'])
def login_admin():
  if request.form['password'] == app.config['ADMIN_PASSWORD']:
    session['authed'] = True
    return redirect('/admin')
  return 'ayelmao'


@app.route('/')
def index():
  return '<h1>hello world</h1>'

@app.route('/projects')
def get_all_projects():
  projects = models.Project.query.all()
  return jsonify(projects)

@app.route('/projects/<int:project_id>')
def get_project_by_id(project_id):
  project = models.Project.query.get(project_id)
  return jsonify(project)

