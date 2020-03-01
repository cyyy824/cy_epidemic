import os
import sys
import click
from flask_script import Manager
from flask_migrate import Migrate, upgrade, MigrateCommand
from app import create_app, db
from app.models import Department,Article,Epidemic
import app.models
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

def make_shell_context():
    return dict(app=app, db=db, Department=Department)

@manager.command
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    db.create_all()
    Department.insert_departments()


@manager.command
def make_fake():
    Article.generate_fake()
    Epidemic.generate_fake()


if __name__ == '__main__':
    manager.run()
