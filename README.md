# data-centric-development

[ReciPlease](https://code-institute-data-centric.herokuapp.com/) is a Single Page Application (SPA) developed as part of the Code Institute Full Stack Software Development Diploma - DATA CENTRIC DEVELOPMENT module. It uses HTML CSS (Bootstrap) and JavaScript on the client side. The backend consists of a REST API created using Flask RESTful which allows data to flow to and from a mongo database. Amazon S3 was used to store all image files relating to the recipes. 

### What is this site for?
 
This website's primary function is to display recipes. Users can browse a recipe list, view individual recipe pages, submit new recipes and edit or delete current recipes.
 
### How does it work
 
This site is a single page application powered by the Flask and Flask-RESTful frameworks. The core of the app is a rest-server which is used to serve data to the various templates. These templates are managed by the [mustache.js](https://mustache.github.io/) javaScript library. All data is stored in a [mongodb](https://www.mongodb.com/) database hosed using [mLab](https://mlab.com/welcome/). The rest-server resources call the appropriate functions in the database module which use the [pymongo](https://api.mongodb.com/python/current/) api. [JQuery Ajax](http://api.jquery.com/jquery.ajax/) is used extensively on the front end to make calls to the API and feed data to the mustache templates.

 
## UX

The site has been designed for food lovers and recipe enthusiasts. Users can view, edit, submit and delete recipes.

### User stories: 

#### Managing recipes
- ##### As a user I want to add new recipes to the site
  - ##### Acceptace Criteria
    - From the list view I will click the 'Create new recipe' button and the new recipe input form will appear in a modal. This will contain all recipe fields and three buttons ('Back to List', 'Reset', 'Submit')
    - I will enter recipe details. Clicking 'Submit' will close the modal and update the recipe list view where new recipe will be visible. Clicking 'Reset' will clear the form. Clicking 'Back to List' will take me back to the list of recipes with no data saved. 
- ##### As a user I want to delete recipes from the site
    - ##### Acceptace Criteria 
        - From list view or from individual recipe view I will click the 'Delete' button. The recipe will be deleted and I will be taken back to the list of recipes.

- ##### As a user I want to edit recipes on the site
    - ##### Acceptace Criteria
        - From list view or from individual recipe view I will click the 'Edit' button and a recipe edit form will appear with details of selected recipe in place for editing and three buttons ('Back to List', 'Reset', 'Submit')
        - I will edit some fields. Clicking 'Submit' will load the edited recipe's view where the changes will be visible. Clicking 'Back to List' will take me back to the list of recipes with no data saved.


## Features

A user of the site can view a list of recipes and can view a full recipe page by clicking 'Read More'
Users can add new recipes
Recipes can be deleted or Edited
 

## Technologies Used


- [flask](http://flask.pocoo.org/docs/1.0/#user-s-guide) & [flask restful](https://flask-restful.readthedocs.io/en/latest/)
    - The **Flask** web development micro-framework was used on the back end. This was used in conjunction with the **Flask Restful** extension to build a lightweight resful api to serve the recipes in JSON format.

- [mongodb](https://www.mongodb.com/)
    - A **mongodb** document based database was chosen to persist data for reciplease

- [Amazon S3](https://aws.amazon.com/s3/?nc2=h_m1)
    - Amazon AWS S3 (Simple Storage Solution) was used to store all images - links to the image files in the cloud were stored in the Mongo database

- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - Boto is the Amazon Web Services (AWS) SDK for Python. It was used to send and delete recipe image files. 

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation. This is what allows the SPA to function. The main HTML is contained in a single file which is loaded initially and the javascript shows and hides sections based on the users activity. 

- [JQuery Ajax](http://api.jquery.com/jquery.ajax/)
    - **jquery.ajax** was used in this project to interact with the backend REST API

- [mustache.js](https://mustache.github.io/)
    - **mustache.js** is a templating language which was ustilised to enhance the site and make it a true single page application. 




## Testing

Testing has been automated using the python unittest library. A testcase was created for each server class (Recipe & RecipeList) with individual functions testing the endpoints. mock.Patch was used to mock calls to the database module. Tests are contained in [test_rest_server.py](https://github.com/JamesDungan/code-institute-data-centric/blob/production/test_rest_server.py)

To run these tests run this command from your terminal when at the root of the project: `python3 -m unittest`

**Please note** You will need to replace MONGODB_URI, DBS_NAME and COLLECTION_NAME in database.py with your own database credentials for this to work. 

## Deployment

### Heroku

The site was deployed to Heroku via new branch (production) which was based on the master branch. A new app was created in the Heroku environment. Environment variables used for the database and the access keys for the Amazon S3 storage were replaced with corresponding config vars via the heroku dev center. Gunicorn server was installed as a dependency and a Procfile was created with the settings required to run the app using gunicorn. 

### Locally

If you would like to run this code locally, follow these instructions:

1. Clone the repository 
  * (with ssh) `git clone git@github.com:JamesDungan/code-institute-data-centric.git` 
  * (with https) `https://github.com/JamesDungan/code-institute-data-centric.git`
2. Open the folder in your favorite IDE
3. Install [python3](https://www.python.org/downloads/) on your machine 
4. Open a terminal and from the root of this project create a virtual environment where you will install all of your dependancies
5. Then activate the virtual environment and run `pip install -r requirements.txt` from the root of the project.
6. You will have to replace MONGODB_URI, DBS_NAME and COLLECTION_NAME in database.py with your own database credentials.     
6. Now that all of your dependancies have been installed you can run the app by running `python3 rest-server`

