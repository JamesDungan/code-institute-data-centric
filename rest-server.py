from flask import Flask, request, render_template, url_for
from flask_restful import reqparse, abort, Api, Resource
import os
import libs.database as db

app = Flask(__name__, static_url_path="")
api = Api(app)


def abort_if_recipe_doesnt_exist(recipes,recipe_id):
    if recipe_id not in recipes:
        abort(404, message="Recipe {} doesn't exist".format(recipe_id))

parser = reqparse.RequestParser()
parser.add_argument('task')####


class Recipe(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(Recipe, self).__init__()
        
    def get(self, recipe_id):
        recipes = db.find()
        abort_if_recipe_doesnt_exist(recipes, recipe_id)
        return #

    def delete(self, recipe_id):
        recipes = db.find()
        abort_if_recipe_doesnt_exist(recipes, recipe_id)
        del recipes[recipe_id]
        return '', 204

    def put(self, recipe_id):
        recipes = db.find()
        args = parser.parse_args()
        task = {'task': args['task']}
        recipes[recipe_id] = task
        return task, 201


class RecipeList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(RecipeList, self).__init__()
        
    def get(self):
        recipes = db.find()
        return recipes

    def post(self):
        args = parser.parse_args()
###############################
        return 

api.add_resource(Recipe, '/reciplease/api/v1.0/recipe/<recipe_id>', endpoint='recipe')
api.add_resource(RecipeList, '/reciplease/api/v1.0/recipes', endpoint='recipes')

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)),debug=True)