## C3 Experiential Learning Private Limited Internship Task

## API Documentation

Given below are the api endpoints 

- add_pizza (POST): api endpoint to add a pizza.
Usage: http://127.0.0.1:8000/add_pizza/?type=Square&size=Small&toppings=Tomatos,Onions,Olives
Note: type, size and toppings can be added in any order. There can be one or many toppings as required.
Return Type: HttpResponse
- show_pizza (GET): api endpoint to show all pizzas in the database.
Usage: http://127.0.0.1:8000/show_pizza/
Return Type: Json
- update_pizza (POST): api endpoint to update any pizza by id.
Usage: http://127.0.0.1:8000/update_pizza/?id=19&type=Square&size=Small&toppings=Tomatos,Onions,Olives
Note: type, size and toppings are optional arguments, only one of these is required to update pizza but at least one of them shoild be present. id is mandatory argument.
Return Type: HttpResponse
- delete_pizza (POST): api endpoint to delete a pizza by id
Usage: http://127.0.0.1:8000/delete_pizza/?id=19
Return Type: HttpResponse
- filter_pizzas (POST): api endpoint to filter and return pizzas by size or type
Usage: http://127.0.0.1:8000/filter_pizzas/?size=Small  OR  http://127.0.0.1:8000/filter_pizzas/?type=Square
Return Type: Json

## Steps to run the project:

- Create a MongoDB database in community server by the name "newdatabase" and a sample collection "newcollection"
- Run the following commands: 
pip install -r requirements.txt
- In the manage.py folder run the command:
python manage.py makemigrations
python manage.py migrate

- Run the server by running command:
python manage.py runserver

Now, the server is active and requests can be sent using Postman or other tools.

