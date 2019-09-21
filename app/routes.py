from app import app, admin, db, models, login
from flask_admin.contrib.sqla import ModelView
from flask import redirect, session, request

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


