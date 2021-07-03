from flask import Flask,jsonify
from app.recommend_system import recommnend_data
from app.train import train_data
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
@app.route('/recommend/train',methods=['GET'])
def train():
    try:
        train=train_data()
        return jsonify(train)
    except:
        return jsonify([])