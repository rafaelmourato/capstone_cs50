# Shopping List

## Intro

This is the final Project from **CS50's Web Programming with Python and JavaScript**.  
Instructors: Brian Yu and David J. Malan

## Objective

In the final project from the CS50 course, the challenge was to create a solution off my own, using python, javascript and everything learned during the course. 

This project was conceived from an actual problem I often face in my day-to-day life: the price of food has grown constantly over time, but my income hasn't. Therefore, choosing where to buy my groceries is always an important aspect of helping me save money. In addition to that, I am a forgetful person, so I tend to return home from the store realizing I missed something.

Understanding both of these problems, I developed a solution to solve them together: a shopping list application. This tool enables users to maintain multiple lists—such as one for a barbecue, another for a party, or separate lists for the weekend and the month. Once a list is created, the user can see which local markets provide those products and, more importantly, which specific market offers the lowest total price for that list


## Distinctiveness and Complexity


The complexity of this project is rooted in the relational logic and the asynchronous user interface. The backend manages a complex relationship between Users, Products, and Supermarkets. Specifically, the PriceMkt model acts as a sophisticated intermediary that allows different supermarkets to set unique prices for the same global Product object.

Although the application utilizes a single model for the User, it implements a functional duality between supermarkets and buyers. Depending on the account type, the user is presented with a vastly different experience, including unique views and specific backend functions tailored to their role, this was made in a way that you can implement in a simpler code different experiences tha complement each other, one focused on the B2C and other the B2B.

Another complexity was making it mobile responsive, it makes sense once it's an application with the function of beeing pratical and daily usable, since it's a tool for helping with daily buys, and was also a requirement for the project, so it suited well. That merge with a dinamic front-end utilizing the JavaScript Fetch API. Users can create lists, add products to those lists, and supermarkets can update their location data or product prices—all without a page reload. This required careful management of CSRF tokens within JavaScript and dynamic DOM manipulation to reflect database changes in real-time.

The core complexity lies in the multi-layered data processing within views.py. When a user initiates a comparison, the application executes a series of relational queries to map a user's List objects to the PriceMkt junction table. It doesn't just display prices, it performs real-time arithmetic to calculate totals, identifies missing items, and returns a structured data object. That was essential to make this a usefull tool not only a consulting page.

My project, Shopping List, is distinct both in utility and architecture. It processes and treats data to provide actionable insights that support real-world decision-making, by utilizing a custom algorithm and a matrix-based data structure, it dosen't work only by doing actions in the CRUD(create, read, update, delete), but by using mathematics to present useful information.

Something distinct about my application is that it utilizes the same model for different purposes, wich also provides two different experiencies for each user. The idea was to make a simpler code that could handle an experience to a user and another experience to a business in the same plataform, in a way that they can comunicate without having to connect different plataforms, but doing everything in a unique application.

The idea is that supermarkets are provided a localized management dashboard to manipulate their specific inventory, while consumers receive a personalized shopping and comparison hub. By synthesizing a unified global product database with multi-vendor pricing matrices, Shopping List introduces a level of algorithmic processing and distinct data intersection that is entirely unique from the coursework.

Most of what was done before were simple applications focused in using diferent aspects of django by themselves, this project not only utilizes most of was taught troughout the course, as introduces more, like mapping,  a new algorithm, a light adjustable front both in the browser and in a mobile enviroment, using javascript in a way that improves the experience and putting things like paginator to good use.

## What’s contained in each file you created.

### ShoppingList (Project Folder)
Main Django project configuration. When creating through the terminal my Django application these files are auto generated.

### ShoppingList (Application)
- `settings.py`  
  Contains project settings, authentication configuration, installed apps, and user model configuration. There i added the listapp on the apps avaiable, and the auth user so it could run.

- `urls.py`  
  Main URL configuration. I had to include the routes from `listapp.url`.

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
      - Unit of measure, needed to comparison

  - **PriceMkt**  
    Defines the relationship between a supermarket and a product.  
    Stores the price of each product in each supermarket.

- `views.py`  
  Contains the main application logic and request handling. It connects with the urls so our application has a logic beetween pages and functions.
  The imports made were necessary to apply them inthe views created after and to help with handling the html.
  - **Index**  
    The main page, on it i defined the paginator and the logic to change pages to make the viewing of the products look better, in a way that in the same page you can see and explore: Products, Supermarkets avaiable and if you are logged in your lists.
  - **Listpage**  
    The listpage reffers to a page where you can see an especific list and you can only access your lists and if you're logged in. In the list you are able to add products directly, that's why the view has a post method, and the json response so you can add it without refreshing using js. it sends the list, the products on the lis and another list with all the products so you can add it.
  - **Userpage**  
    The view for the user that is not a supermarket, it will open a page with all the lists the user created, and enable the user to create more lists alson using javascript to not refresh the page when created.  
  - **Updateadress**  
    This function was created so the javascript could update the adress on the supermarketpage.  
  - **Supermarketpage**  
    This view is made for the user supermarket, it's made in a way that you can see the supermarket and it's products, and at the same time if you're the supermarket, you can add, edit an address and add products to you account.
  - **Productpage**  
    Brings to a page all the information off a product, and validate if it's a user, beeing a user it sends your lists so you can add the product to one of your lists.
  - **Prices**  
    This is my favorite part of the code, it has a logic in a way that when you click go shopping and call this function, it will use python to calculate how many of the products on the list are in this supermarket and at the same time, how much you would spend on it, and displaying it on a page to the user.
  - **login**  
    The standard login view.
  - **logout**  
    The standard logout view.
  - **register**  
    The standard register view.

- `admin.py`  
  Where i created the admin information so i can see what happens when i create a superuser, able to create in the backend a user, product, price or list.

- `urls.py`  
  Defines the routes for the application, including the index page, routes for login, logout and register, the user page with it's lists, the list page, the supermarket page, the product page, the comparing prices page and the url to update the adress with js.

- `tests.py`  
  A simple test file responsible for automatic tests made to ensure changes don't affect the code main functions.

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
  Here it has a working mechanism that allows you to see wich supermarket has more products, and wich is cheaper or more expensive at the same time, it has an intuitive layout so you can analise and also let's you enter the supermarket page.


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

- **Standardized Product Catalog**: To ensure data integrity, I intentionally restricted the ability of regular users or supermarkets to create new Product entries. This prevents the fragmentation of data—for example, avoiding separate entries for "Egg" vs. "Eggs." By maintaining a centralized catalog, the application ensures that the Comparison Engine can accurately match the same product across various supermarket inventories, providing a reliable price analysis.

**Administrative Control**: The global product database is managed via the Django Admin interface. This allows for high-level quality control over product names, units of measurement, and imagery, ensuring a consistent experience for all users of the platform.

**Future Roadmap**: For this MVP, the focus was on the creation and comparison of multiple shopping lists. Moving forward, I plan to implement additional management features, such as the ability to delete or archive old lists and the implementation of a user-requested product suggestion system to safely expand the catalog.


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