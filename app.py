from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

def create_app():
    app = Flask(__name__)
    # CORS(app)
    
    # allow CORS on a given route. you use a decorator

    @app.route('/api')
    @cross_origin()
    def api():
        return jsonify({'data' : 'It is now working!'})

    return app



# from flask import Flask, session
# from flask_cors import CORS



# app = Flask(__name__)
# # Resource specific CORS

# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# @app.route("/api/v1/users")
# def list_users():
#   return "user example"



# if __name__ == "__main__":
#     app.run(debug=True)