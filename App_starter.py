from flask import Flask
from flask_restx import Api, Resource, reqparse
import os

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc='/api-docs')

    test_api = api.namespace('test', description='Test API') # 콜 받는 주소
    data = api.namespace('getdata', description='데이터 get API')

    @test_api.route('/')
    class Test(Resource):
        def get(self):
            return "Hello World. This is Test."
    
    @data.route('/')
    class GetData(Resource):
        def get(self):
            pass

    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 9999)), debug=True)
