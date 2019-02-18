from flask import Flask, request, jsonify, render_template, url_for
from flask_restful import reqparse, abort, Api, Resource, fields, marshal_with
import os
import libs.database as db
from bson import ObjectId
from collections import Iterable

app = Flask(__name__, static_url_path="")
api = Api(app)


class Recipe(Resource):
    def __init__(self):
        super(Recipe, self).__init__()
        
    def get(self, id):
        fltr = {'_id': id}
        result = db.findOne(fltr)
        if any('error' in r for r in result):
            return result, 500
        return result, 200

    def delete(self, id):
        fltr = {'_id': id}
        result = db.deleteOne(fltr)
        if isinstance(result, Iterable):
            if any('error' in r for r in result):
                return result, 500
        return 'document deleted', 204

    def put(self, id):
        fltr = {'_id': id}
        json_data = request.get_json(force=True)
        updte = {'$set': {'name':json_data['name'],
                        'method':json_data['method'],
                        'summary':json_data['summary'],
                        'prep_time':json_data['prep_time'],
                        'cook_time':json_data['cook_time'],
                        'ingredients':json_data['ingredients']
                        }
                }
        result = db.updateOne(fltr, updte)
        if isinstance(result, Iterable):
            if any('error' in r for r in result):
                return result, 500
        return 'database updated', 201

class RecipeList(Resource):
    def __init__(self):
        super(RecipeList, self).__init__()
   
    def get(self):
        result = db.find()
        if any('error' in r for r in result):
            return result, 500
        return result, 200

    def post(self):
        json_data = request.get_json(force=True)

        doc = {'name':json_data['name'],
                'method':json_data['method'],
                'summary':json_data['summary'],
                'prep_time':json_data['prep_time'],
                'cook_time':json_data['cook_time'],
                'ingredients':json_data['ingredients']
                }
        result = db.insert(doc)
        if isinstance(result, Iterable):
            if any('error' in r for r in result):
                return result, 500
        return  'database updated', 201

api.add_resource(Recipe, '/reciplease/api/v1.0/recipe/<id>', endpoint='recipe')
api.add_resource(RecipeList, '/reciplease/api/v1.0/recipes', endpoint='recipes')
# if __name__ == '__main__':
#     app.run(debug=True)