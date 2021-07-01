from flask import Flask,jsonify
from app.recommend_system import recommnend_data
from flask_cors import CORS
app =Flask(__name__)
CORS(app)
@app.route('/',methods=['GET'])
def index():
    return jsonify("Wellcome....")
@app.route('/recommend/<string:id>',methods=["GET"])
def recommend(id):
    try:
        recommnend=recommnend_data(id)
        return jsonify(recommnend)
    except:
        return jsonify([])