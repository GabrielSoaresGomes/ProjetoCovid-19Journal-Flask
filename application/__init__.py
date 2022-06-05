from flask import Flask
import os

app = Flask(__name__,
            static_folder = os.path.abspath("application/views/static"),
            template_folder = os.path.abspath("application/views/templates"),
             )

from application.controllers import home_controller
from application.controllers import estado_controller
from application.controllers import home_controller
from application.controllers import error_controller
from application.controllers import noticia_controller