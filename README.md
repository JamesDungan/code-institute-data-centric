# full-stack-frameworks-django

ReciPlease is a Single Page Application (SPA) developed as part of the Code Institute Full Stack Software Development Diploma - DATA CENTRIC DEVELOPMENT module. It uses HTML CSS (Bootstrap) and JavaScript on the client side. The backend consists of a REST API created using Flask RESTful which allows data to flow to and from a mongo database.

 
## UX

The site has been designed for food lovers and recipe enthusiasts. Users can view, edit, submit and delete recipes.

### User stories: 

#### Managing recipes
- ##### As a user I want to add new recipes to the site
  - ###### Acceptace Criteria
    - From the list view I will click the 'Create new recipe' button and the new recipe input form will appear in a modal. This will contain all recipe fields and three buttons ('Back to List', 'Reset', 'Submit')
    - I will enter recipe details. Clicking 'Submit' will close the modal and update the recipe list view where new recipe will be visible. Clicking 'Reset' will clear the form. Clicking 'Back to List' will take me back to the list of recipes with no data saved. 
- ##### As a user I want to delete recipes from the site
    - ###### Acceptace Criteria 
        - From list view or from individual recipe view I will click the 'Delete' button. The recipe will be deleted and I will be taken back to the list of recipes.

- ##### As a user I want to edit recipes on the site
    - ###### Acceptace Criteria
        - From list view or from individual recipe view I will click the 'Edit' button and a recipe edit form will appear with details of selected recipe in place for editing and three buttons ('Back to List', 'Reset', 'Submit')
        - I will edit some fields. Clicking 'Submit' will load the edited recipe's view where the changes will be visible. Clicking 'Back to List' will take me back to the list of recipes with no data saved.


## Features

A user of the site can view a list of recipes and can view a full recipe page by clicking 'Read More'
Users can add new recipes
Recipes can be deleted or Edited
 

## Technologies Used

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation. This is what allows the SPA to function. The main HTML is contained in a single file which is loaded initially and the javascript shows and hides sections based on the users activity. 

- [JQuery Ajax](http://api.jquery.com/jquery.ajax/)
    - jquery.ajax was used in this project to interact with the backend REST API

- [mustache.js](https://mustache.github.io/)
    - mustache.js is a templating language which was ustilised to enhance the site and make it a true single page application. 

- [mongodb](https://www.mongodb.com/)


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
