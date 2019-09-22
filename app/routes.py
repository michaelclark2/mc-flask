from app import app, admin, db, models, github
from flask_admin.contrib.sqla import ModelView
from flask import redirect, session, request, jsonify
from werkzeug.security import check_password_hash

"""Admin stuff"""
class PrivateView(ModelView):
  def is_accessible(self):
    return session.get('authed')

admin.add_view(PrivateView(models.Project, db.session))
admin.add_view(PrivateView(models.Tech, db.session))

@app.route('/admin/login', methods=['POST'])
def login_admin():
  if check_password_hash(app.config['ADMIN_PASSWORD'], request.form['password']):
    session['authed'] = True
  else:
    session['pass_failed'] = True
  return redirect('/admin')

"""App routes"""
@app.route('/')
def index():
  routes = []
  for route in app.url_map.iter_rules():
    if not 'admin' in route.rule and not 'static' in route.rule:
      routes.append(route.rule)
  return jsonify(sorted(routes))

@app.route('/projects')
def get_all_projects():
  projects = models.Project.query.all()
  return jsonify(projects)

@app.route('/projects/<int:project_id>')
def get_project_by_id(project_id):
  project = models.Project.query.get(project_id)
  return jsonify(project)

@app.route('/techs')
def get_all_techs():
  techs = models.Tech.query.all()
  return jsonify(techs)

@app.route('/repos')
def update_languages():
  repos = github.get('/users/michaelclark2/repos')
  languages = {}
  for repo in repos:
    r = github.get(repo['languages_url'])
    languages.update(r)
  return jsonify(languages)
