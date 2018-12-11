from flask import Flask, request, render_template, url_for
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
import os
import libs.database as db
from bson import ObjectId
from collections import Iterable

app = Flask(__name__, static_url_path="")
api = Api(app)

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
        self.reqparse.add_argument('_id', type=str, required=True, location='json')
        self.reqparse.add_argument('name', type=str, required=False, location='json')
        self.reqparse.add_argument('method', type=str,required=False, location='json')
        self.reqparse.add_argument('prep_time', type=int,required=False, location='json')
        super(Recipe, self).__init__()
        
    def get(self):
        args = self.reqparse.parse_args()
        oid = ObjectId(args['_id'])
        fltr = {'_id': oid}
        result = db.findOne(fltr)
        if any('error' in r for r in result):
            return result, 500
        return recipe, 200

    def delete(self):
        args = self.reqparse.parse_args()
        oid = ObjectId(args['_id'])
        fltr = {'_id': oid}
        result = db.deleteOne(fltr)
        if isinstance(result, Iterable):
            if any('error' in r for r in result):
                return result, 500
        return 'document deleted', 204

    def put(self):
        args = self.reqparse.parse_args()
        oid = ObjectId(args['_id'])
        fltr = {'_id': oid}
        updte = {'$set': {'name': args['name'],
                'method': args['method'], 
                'prep_time':args['prep_time']}
                }
        result = db.updateOne(fltr, updte)
        if isinstance(result, Iterable):
            if any('error' in r for r in result):
                return result, 500
        return 'database updated', 201

class RecipeList(Resource):
    #@marshal_with(recipe_fields) could not get marshaling to work
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, location='json')
        self.reqparse.add_argument('method', type=str, required=True, location='json')
        self.reqparse.add_argument('prep_time', type=int, required=True, location='json')
        super(RecipeList, self).__init__()
   
    def get(self):
        result = db.find()
        if any('error' in r for r in result):
            return result, 500
        return result, 200

    def post(self):
        args = self.reqparse.parse_args()
        doc = {'name':args['name'],
                'method':args['method'],
                'prep_time':args['prep_time']
                }
        result = db.insert(doc)
        if isinstance(result, Iterable):
            if any('error' in r for r in result):
                return result, 500
        return  'database updated', 201

api.add_resource(Recipe, '/reciplease/api/v1.0/recipe', endpoint='recipe')
api.add_resource(RecipeList, '/reciplease/api/v1.0/recipes', endpoint='recipes')
if __name__ == '__main__':
    # app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)),debug=True)
    app.run(debug=True)