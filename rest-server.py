from flask import Flask, request, render_template, url_for
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
import os
import libs.database as db

app = Flask(__name__, static_url_path="")
api = Api(app)

def abort_if_recipe_doesnt_exist(recipes,recipe_id):
    if recipe_id not in recipes:
        abort(404, message="Recipe {} doesn't exist".format(recipe_id))

# recipe_fields = {
#     'name': fields.String,
#     'method': fields.String,
#     'prep_time': fields.String
#     'ingredients': fields.List
# } 
#could not get marshaling to work

class Recipe(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, location='json')
        self.reqparse.add_argument('method', type=str,required=True, location='json')
        self.reqparse.add_argument('prep_time', type=int,required=True, location='json')
        super(Recipe, self).__init__()
        
    def get(self, recipe_id):
        recipes = db.find()
        abort_if_recipe_doesnt_exist(recipes, recipe_id)
        return #

    def delete(self, recipe_id):
        recipes = db.find()
        abort_if_recipe_doesnt_exist(recipes, recipe_id)
        #
        return '', 204

    def put(self, recipe_id):
        args = self.reqparse.parse_args()
        
        
        return #

class RecipeList(Resource):
    #@marshal_with(recipe_fields) could not get marshaling to work
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, location='json')
        self.reqparse.add_argument('method', type=str, required=True, location='json')
        self.reqparse.add_argument('prep_time', type=int, required=True, location='json')
        super(RecipeList, self).__init__()
   
    def get(self):
        recipes = db.find()
        return recipes

    def post(self):
        args = self.reqparse.parse_args()
        doc = {
            'name':args['name'],
            'method':args['method'],
            'prep_time':args['prep_time']
        }
        result = db.insert(doc)
        return  'database updated', 201

api.add_resource(Recipe, '/reciplease/api/v1.0/recipe/<recipe_id>', endpoint='recipe')
api.add_resource(RecipeList, '/reciplease/api/v1.0/recipes', endpoint='recipes')

if __name__ == '__main__':
    # app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)),debug=True)
    app.run(debug=True)