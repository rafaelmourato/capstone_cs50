# Shopping List

## Intro

This is the final Project from **CS50's Web Programming with Python and JavaScript**.  
Instructors: Brian Yu and David J. Malan

## Objective

In the final project from the CS50 course, we're challenged to create a solution off my own, using python, javascript and everything learned to do so. 
For my project, i developed an application that works as a shopping list, the goal is to be abble to add things to your shopping list everytime you miss something at your home, and when you go out to do the groceries, it will find the places that have all or most off the items on your shopping list.

## Distinctiveness and Complexity: Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.
- [x] Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those. A: The idea that i brought with this application is diferente from each one of the projects made so far, other than that, it also has some complexity to it for beeing more than just a list, but also helping you to decide where to go, and analise not only what you want to buy, but also wich one is closer and wich one is cheaper. 
- [x] A project that appears to be a social network is a priori deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected. 
A: The project has no intention on creating a social inviroment, it's purpose is to act as a tool.
- [x] A project that appears to be an e-commerce site is strongly suspected to be indistinct from Project 2, and your README.md file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected. 
A: It is not a place for buying, it's a place that serves the purpose of not only helping you remenber the things you want to buy, but also directing you to it.
- [ ] Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end. A:
- [ ] Your web application must be mobile-responsive. A:

## What’s contained in each file you created.

### ShoppingList (Project Folder)
Main Django project configuration.

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
    Custom user model used for both regular users and supermarkets.  
    Supermarkets have an additional `address` field to allow distance comparison.

  - **List**  
    Represents a shopping list created by a user.  
    Contains:
      - The owner (User)
      - The list name
      - The selected products

  - **Product**  
    Represents a product available in supermarkets.  
    Contains:
      - Name
      - Picture
      - Unit of measure

  - **PriceMkt**  
    Defines the relationship between a supermarket and a product.  
    Stores the price of each product in each supermarket.

- `views.py`  
  Contains the main application logic and request handling.

- `urls.py`  
  Defines the routes for the application, including the index page.

## How to run your application.

## Any other additional information the staff should know about your project.

## If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a requirements.txt file!

### Specifications

#### New Post
- [x] Users who are signed in should be able to write a new text-based post by filling in text into a text area and then clicking a button to submit the post.
- [x] The screenshot at the top of this specification shows the “New Post” box at the top of the “All Posts” page. You may choose to do this as well, or you may make the “New Post” feature a separate page.
#### All Posts
- [x] The “All Posts” link in the navigation bar should take the user to a page where they can see all posts from all users, with the most recent posts first.
- [x] Each post should include the username of the poster, the post content itself, the date and time at which the post was made, and the number of “likes” the post has (this will be 0 for all posts until you implement the ability to “like” a post later).
#### Profile Page
- [x] Clicking on a username should load that user’s profile page. This page should: 
- [x] Display the number of followers the user has, as well as the number of people that the user follows.
- [x] Display all of the posts for that user, in reverse chronological order.
- [x] For any other user who is signed in, this page should also display a “Follow” or “Unfollow” button that will let the current user toggle whether or not they are following this user’s posts. Note that this only applies to any “other” user: a user should not be able to follow themselves.
#### Following
- [x] The “Following” link in the navigation bar should take the user to a page where they see all posts made by users that the current user follows.
This page should behave just as the “All Posts” page does, just with a more limited set of posts.
- [x] This page should only be available to users who are signed in.
### Pagination: 
- [x] On any page that displays posts, posts should only be displayed 10 on a page. If there are more than ten posts, a “Next” button should appear to take the user to the next page of posts (which should be older than the current page of posts). If not on the first page, a “Previous” button should appear to take the user to the previous page of posts as well. See the Hints section for some suggestions on how to implement this.
### Edit Post: 
- [x] Users should be able to click an “Edit” button or link on any of their own posts to edit that post.
- [x] When a user clicks “Edit” for one of their own posts, the content of their post should be replaced with a textarea where the user can edit the content of their post.
The user should then be able to “Save” the edited post. Using JavaScript, you should be able to achieve this without requiring a reload of the entire page.
For security, ensure that your application is designed such that it is not possible for a user, via any route, to edit another user’s posts.
### “Like” and “Unlike”: 
- [x] Users should be able to click a button or link on any post to toggle whether or not they “like” that post. 
- [x] Using JavaScript, you should asynchronously let the server know to update the like count (as via a call to fetch) and then update the post’s like count displayed on the page, without requiring a reload of the entire page.

### Links

- [🔗 Project Specification](https://cs50.harvard.edu/web/projects/final/capstone/)  


### Author
Rafael Mourato (Rafael.mourato@hotmail.com) - Student of Informational Systems at Federal University of Pernambuco.

### License
This project is for educational purposes only and is not affiliated with any company.