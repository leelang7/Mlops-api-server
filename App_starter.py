from flask import Flask
from flask_restx import Api, Resource, reqparse
import os

if __name__ == '__main__':
    app = Flask(__name__)

    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc="/api-docs")

    test_api = api.namespace('test', description='조회 API')

    @test_api.route('/')
    class Test(Resource):
        def get(self):
            return 'Hello World!'

  
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8888)), debug=True)

    @app.after_request
    def set_response_headers(r):
        r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        r.headers['Pragma'] = 'no-cache'
        r.headers['Expires'] = '0'
        return r
