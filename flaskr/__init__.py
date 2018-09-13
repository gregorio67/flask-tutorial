import os

from flask import Flask

app = object()

def create_app(config_name):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py', silent=True)

    app.config.update()
    app.logger.debug("configuration : {}".format(app.config.items()))

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    #     app.logger.debug("configuration : {}".format(app.config.items()))
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    #DB Initializing
    from . import db
    db.init_app(app)

    #Auth application register
    from . import auth
    app.register_blueprint(auth.bp)

    app.logger.info("auth is registered")
    from . import blog
    app.register_blueprint(blog.bp)

    app.add_url_rule('/', endpoint='index')
    app.logger.info("blog is registered")


    return app

# if __name__ == '__main__':
#     app.run(port=9000)
