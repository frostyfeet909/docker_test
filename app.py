import flask


def create_app():
    app = flask.Flask(__name__, instance_relative_config=True)

    @app.route("/index", methods=["GET"])
    def index():
        print("Index got called")
        return flask.jsonify("hey there")

    return app


def start_flask_app(port: int = 9090):
    flask_app = create_app()
    flask_app.config["DEBUG"] = False
    print("Created app")
    flask_app.run(port=port, host="0.0.0.0", threaded=True)


if __name__ == "__main__":
    # Init Flask App context
    start_flask_app()


