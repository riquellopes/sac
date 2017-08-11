import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app.api import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(
    host='0.0.0.0', port=int(os.environ.get("PORT", 5000))))

if __name__ == '__main__':
    manager.run()