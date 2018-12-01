# User Stories
### Managing recipes
- #### As a user I want to add new recipes to the site
  - ###### Acceptace Criteria
    - From the list view I will click the 'Create new recipe' button and the new recipe input form will appear in a modal. This will contain all recipe fields and two buttons ('Save', 'Cancel')
    - I will enter recipe details. Clicking 'save' will close the modal and update the recipe list view where new recipe will be visible. Clicking 'cancel' will just close the modal with no data saved. 
- #### As a user I want to delete recipes from the site
    - ###### Acceptace Criteria 
        - From list view or from individual recipe view I will click the 'Delete' button. A Modal will appear asking if I am sure I want to delete this recipe.
        - Clicking 'Yes' will delete the recipe from the database, close the modal and load the unfiltered full recipe list. The deleted recipe will no longer appear in the list.
        - Clicking 'No' will just close the modal with no changes to recipe database. View (list/recipe) will remain unchanged.
- #### As a user I want to edit recipes on the site
    - ###### Acceptace Criteria
        - From list view or from individual recipe view I will click the 'Edit' button and a recipe edit form will appear in a modal with details of selected recipe in place for editing and two buttons ('Save, 'Cancel').
        - I will edit some fields. Clicking 'save' will close the modal and load the edited recipe's view where the changes will be visible. Clicking 'cancel' will just close the modal with no data changed.
### Viewing recipes based on categories
- #### As a user I want to view a recipe 'home' page showing all recipe categories
    - ###### Acceptace Criteria
        - I will navigate to the 'home' page. All categories will be listed as clickable buttons/links. There will also be a button/link to view all recipes.
- #### As a user I want to click on a category and be shown a list of all recipes in that category
    - ###### Acceptace Criteria
        - I will click on one of the categories on the home page. A filtered list of all recipes in that category will be loaded. Each of these listed recipes will contain an image, recipe name, category name, brief summary and 'read-more' button. This list view will also contain statistics about the list.
    - ###### Note
        - This list view will be the same as the one used for viewing all recipes.
### Viewing all recipes and filtering
- #### As a user I want to view a list of all recipes and see statistics about this list
    - ###### Acceptace Criteria
        - From the home page I will click the 'view all recipes' button. A list of all recipes will be loaded. I will be able to apply filters to this list. Each of these listed recipes will contain an image, recipe name, category name, brief summary and ‘read-more’ button. This list view will also contain statistics about the list.
- #### As a user I want to filter the list of recipes based on attributes
    - ###### Acceptace Criteria
        - From the recipe list view I will apply filters and the list view will be updated accordingly
- #### As a user I want to view a recipe after clicking on it from within the list
    - ###### Acceptace Criteria
        - From the recipe list view I will click the 'read-more' button of one of the recipes in the list and that recipe's view will be loaded.