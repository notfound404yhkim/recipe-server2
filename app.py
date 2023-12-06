# flask 프레임워크를 이용한 ,  Restful API 서버 개발

from flask import Flask
from flask_restful import Api

from resources.recipe import RecipeListResource,RecipeResource, RecipePublishResource
from resources.user import UserRegisterResource

app = Flask(__name__)

api = Api(app)

# API를 구분해서 실행시키는 것은,
# HTTP METHOD 와 URL의 조합 이다.

# 경로(path)와 리소스(API 코드) 를 연결한다.
api.add_resource(RecipeListResource ,'/recipes')

api.add_resource(RecipeResource  , '/recipes/<int:recipe_id>') # 경로 변수화(숫자형식) 

api.add_resource(RecipePublishResource  , '/recipes/<int:recipe_id>/publish') # 경로 변수화(숫자형식) 

api.add_resource(UserRegisterResource ,'/user/register')


if __name__ == '__main__':
    app.run()




