# Shopping List

## Intro

This is the final Project from **CS50's Web Programming with Python and JavaScript**.  
Instructors: Brian Yu and David J. Malan

## Objective

In the final project from the CS50 course, we're challenged to create a solution off my own, using python, javascript and everything learned to do so. 
For my project, i developed an application that works as a shopping list, the goal is to be abble to add things to your shopping list everytime you miss something at your home, and when you go out to do the groceries, it will find the places that have all or most off the items on your shopping list and the one with the best price, it serves as a tool to help your decision making.

## Distinctiveness and Complexity: Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.
- [x] Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those. 
A: The idea that i brought with this application is diferente from each one of the projects made so far, other than that, it also has complexity to it for beeing more than just a list, but also helping you to decide where to go, and analise not only what you want to buy, but also wich one has most of what you want and wich one is cheaper. 
- [x] A project that appears to be a social network is a priori deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected. 
A: The project has no intention on creating a social inviroment, it's purpose is to act as a tool.
- [x] A project that appears to be an e-commerce site is strongly suspected to be indistinct from Project 2, and your README.md file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected. 
A: It is not a place for buying, it's a place that serves the purpose of not only helping you remenber the things you want to buy, but also directing you to it.
- [x] Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end. A: Created 4 models and js on the front to edit and save the supermarket adress, to add products in the list and ina supermarket.
- [x] Your web application must be mobile-responsive. 
A: The layout that i used in the pages of my application where designed in a way that made them easily mobile responsive.

## What’s contained in each file you created.

### ShoppingList (Project Folder)
Main Django project configuration.

### ShoppingList (Application)
- `settings.py`  
  Contains project settings, authentication configuration, installed apps, and user model configuration.

- `urls.py`  
  Main URL configuration. Includes the routes from `listapp`.

---

### listapp (Application)
Core application containing the business logic of the project.

- `models.py`  
  Defines the database structure:

  - **User**  
    Custom user model used for both regular users and supermarkets, this way the supermarket could have a login, in order to determine it's own prices on the platform.  
    Supermarkets have an additional `address` field to allow finding the place.

  - **List**  
    Represents a shopping list created by a user.  
    Contains:
      - The owner (User)
      - The list name
      - The selected products

  - **Product**  
    Represents a product available.  
    Contains:
      - Name
      - Picture (opitional)
      - Unit of measure

  - **PriceMkt**  
    Defines the relationship between a supermarket and a product.  
    Stores the price of each product in each supermarket.

- `views.py`  
  Contains the main application logic and request handling. It connects with the urls so our application has a logic beetween pages and functions.
  - **Index**  
    The main page, on it i defined the paginator and the logic to change pages to make the viewing of the products look better, in a way that in the same page you can see and explore: Products, Supermarkets avaiable and if you are logged in your lists.
  - **Listpage**  
    The listpage reffers to a page where you can see an especific list and you can only access your lists and if you're logged in. In the list you are able to add products directly, that's why the view has a post method, and the json response so you can add it without refreshing using js. it sends the list, the products on the lis and another list with all the products so you can add it.
  - **Userpage**  
    The view for the user that is not a supermarket, it will open a page with all the lists the use rcreated, and enable the user to create more lists alson using java to not refresh thhe page when created.  
  - **Updateadress**  
    This function was created so the java could update dthe adress on the supermarketpage.  
  - **Supermarketpage**  
    This view is made for the user supermarket, it's made in a way that you can see the supermarket and it's products, and at the same time if you're the supermarket, you can add, edit an address and add products to you account.
  - **Productpage**  
    Brings to a page all the information off a product, and validate if it's a user, beeing a user it sends your lists so you can add the product to one of your lists.
  - **Prices**  
    This is my favorite part of the code, it has a logic in a way that when you click go shopping and call this function, it will use python to calculate how many of the prdoucts on the list are in this supermarket and at the same time, how much you would spend on it, and displaying it on a page to the user.
  - **login**  
    The standard login view.
  - **logout**  
    The standard logout view.
  - **register**  
    The standard register view.

- `admin.py`  
  Where i created the admin information so i can see what happens when i create a superuser, able to create in the backend a user, product, price or list.

- `urls.py`  
  Defines the routes for the application, including the index page, routes for login, logout and register.

- `tests.py`  
  File responsible for automatic tests made to ensure changes don't affect the code main functions.

#### templates
  Defines the templates for the project. I used bootstrap in everypage so i could have a more asthetic and padronized layout for my whole application, all the scripts were made in another file, script.js.

  - `layout.html`  
  Responsible for the main layout of the pages, so i can replicate a main layout and the header with the information that adapts itself if you are logged in or not, and if you are a supermarket or not.

  - `index.html`  
  The main page, where you can see all products and supermarketsand, if you are logged in, also your lists.

  - `register.html`  
  The page where a user can register.

  - `login.html`  
  The page where a user can login in it's account.

  - `logout.html`  
  The page where a user can logout in it's account.

  - `listpage.html`  
  It is a template for the page off a list, where you can see the products on it if you are logged in and the list is yours, also on it you are able to add a product that you didn't have before.

  - `productpage.html`  
  If you want to take a look at a especific product, you can enter it's page, and if you are logged in as a user not supermarket you can add it to any list that it hasnt been added before.

  - `supermarketpage.html`  
  To see a supermarket and wich products are avaiable, you can enter the supermarket page see it's address if it's registered and if you are the supermarket off the page, add or edit an address, and also add products and set it's prices..

  - `userpage.html`  
  This is your page, where you can see your lists, open to see the details on each one and also cerate new lists.

  - `prices.html`
  Here it has a working mechanism that allows you to see wich supermarket has more products, and wich is cheaper or expensiver at the same time, it has an intuitive layout so you can analise and also let's you enter the supermarket page.


#### static
  - `script.js`  
    This file handles all the asynchronous behavior of the application. It manages the **Fetch API** calls to the Django backend. Specifically, it:
    - Handles the dynamic addition of products to lists on the `listpage` and `supermarketpage` without refreshing.
    - Manages the "Edit/Save Address" toggle functionality on the supermarket profile.
    - Handles the creation of new lists on the user dashboard.
    - Manages the CSRF token security for all `POST` and `PUT` requests.

## How to run your application.

1.  **Install dependencies**:  
    Ensure you have Python installed. Run:  
    `pip install -r requirements.txt`  
    *(Note: If you haven't created one yet, ensure Pillow is installed for images: `pip install Pillow`)*

2.  **Apply Migrations**:  
    `python manage.py makemigrations`  
    `python manage.py migrate`

3.  **Create a Superuser** (to add initial products to the database):  
    `python manage.py createsuperuser`

4.  **Run the server**:  
    `python manage.py runserver`

5.  **Access the App**:  
    Open your browser to `http://127.0.0.1:8000/`.


## Any other additional information the staff should know about your project.

- **Dual User Logic**: When registering, a user chooses if they are a "Customer" or a "Supermarket." The UI changes significantly based on this role.
- **Comparison Engine**: The comparison on the `prices.html` page isn't just a list; it calculates the "missing items" vs "available items" ratio for your specific list at every registered market.


### Specifications

#### Custom User Model
- [x] Utilizes a custom User model that distinguishes between clients and supermarkets via a boolean field.
#### AJAX Integration
- [x] Users can add products to lists and supermarkets can update addresses/prices using the Fetch API, providing a seamless user experience without full page reloads.
#### Data-Driven Comparison
- [x] The application iterates through many-to-many relationships in the database to calculate real-time price totals for a user's unique list across multiple vendors.
#### Pagination
- [x] The main product catalog on the index page is paginated (6 products per page) to ensure fast loading times as the database grows.
#### Mobile Responsiveness
- [x] Every template utilizes the Bootstrap grid system (containers, rows, and columns) and media queries to ensure functionality on mobile devices.

### Links

- [🔗 Project Specification](https://cs50.harvard.edu/web/projects/final/capstone/)  

### Author
Rafael Mourato (Rafael.mourato@hotmail.com) - Student of Informational Systems at Federal University of Pernambuco.

### License
This project is for educational purposes only and is not affiliated with any company.