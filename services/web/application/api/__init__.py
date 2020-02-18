from flask_restplus import Api

from application.api.ping import ping_namespace
from application.api.auth import auth_namespace
from application.api.users.views import users_namespace

api = Api(version="1.0", title="Users API", doc="/doc")

api.add_namespace(ping_namespace, path="/ping")
api.add_namespace(users_namespace, path="/users")
api.add_namespace(auth_namespace, path="/auth")
