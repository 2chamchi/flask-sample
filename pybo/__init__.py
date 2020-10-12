from flask import Flask

# ---------------------------------------- [edit] ---------------------------------------- #
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app
# ---------------------------------------- [edit] ---------------------------------------- #