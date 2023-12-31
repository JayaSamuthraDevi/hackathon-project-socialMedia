from flask import Blueprint, jsonify
import psycopg2
from app.utils.recommendationEngine import engineGetInterest

interests_bp = Blueprint('interests', __name__)


@interests_bp.route('/recommended-interests/<user>', methods=['GET'])
def get_recommended_interests(user):
    result = engineGetInterest(int(user))
    return jsonify(result)



@interests_bp.route('/get',methods=['GET'])
def get():
    conn = psycopg2.connect(
            dbname='ConnectHubDb',
            user='postgres',
            password='1234',
            host='localhost'
        )
    print("Database connection established successfully.")
    cursor = conn.cursor()
    cursor.execute("select * from interests")
    arr=cursor.fetchall()
    return jsonify(arr)
