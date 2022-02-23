try:
    from flask import Flask
    from flask_restful import Resource, Api
    import sys
    import os
    import json
    from flask import app, Flask, request
    from flask_restful import Resource, Api, reqparse
except Exception:
    pass

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):

    def get(self):
        DATABASENAME = os.getenv("DATABASENAME")

        return json.dumps({
            "Database": "working...well"
        })


api.add_resource(HelloWorld, "/")

if __name__ == '__main__':
    app.run(host="0.0.0.0",Debug=True)
