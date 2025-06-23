# wild_atlantic_wares
  Wild atlantic wares

## Code Institute - Portfolio Project 5 - ECommerce 

  Wild Atlamtic Wares is an online ecommerce platform bringing our hand crafted pottery to its target audience.
  This platform allows users to browse our current catalogue and share their experiences by reviewing products they have purchased.
  Wild Atlantic Wares features full CRUD frunctionality and web marketing initiatives like email subscription and social media.
## Demo
  ![How the website looks on different devices](/static/docs/images/amiresponsive.PNG)

  A live demo of the site can be found [here](https://wild-atlantic-wares-858dcca4bf04.herokuapp.com/)

## Tabe of Contents
  - [Site Goals](#site-goals)
  - [UI/UX](#ui-ux)
  - [Project Planning](#project-planning)
    - [Agile](#agile)
      - [User Stories](#user-stories)
      - [MoSCow Prioritization](#moscow)
      - [GitHub Projects](#github-projects)
      - [Issues/sprints](#issues-sprints)
      - [Milestones](#milestones)
    - [Wireframes](#wireframes)
    - [Design](#design)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Database Model](#database-model)
    - [CRUD](#crud)
    - [Category Model](#category-model)
    - [Product Model](#product-model)
    - [Review Model](#review-model)
    - [Order Model](#order-model)
    - [OrderLineItem Model](#orderlineitem-model)
    - [Contact Model](#contact-model)
    - [UserProfile Model](#userprofile-model)

  - [Messaging & Error Handling]('messaging-errorhandling)
    - [Toasts](#toasts)
    - [Try Exceptions](#try-exceptions)
    - [Error 500](#error500)
  - [Technologies Used](#technologies-used)
    - [Development Environment and Hosting](#development-environment-and-hosting)
    - [Libraries](#libraries)
      - [Python](#python)
      - [Django](#django)
      - [BOOTSTRAP](#bootstrap)
      - [All Auth](#all-auth)
      - [Crispy Forms](#crispy-forms)
    - [PostgresSQL](#postgres-sql)
    - [Amazon Web Services](#amazon-web-services)
    - [Stripe](#stripe)
  - [Web Marketing](#web-marketing)
  - [Search Engine Optimization](#seo)  
  - [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Forking and Cloning](#forking-and-cloning)
  - [Testing](#testing)
    - [Testing file](#testing-file)
    - [Bugs](#bugs)
      - [Challenges](#challenges)
      - [Bugs Fixed](#bugs-fixed)
      - [Bugs Remaining](#bugs-remaining)
  - [Credits](#credits)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)


## Site Goals
  - To provide a website where users can browse for and buy Irish handmade pottery.
  - To engage with users and enable them to review and rate products and experiences.
  - To encourage would be visitors to buy products by sharing reviews and ratings.
  - Use review feedback to improve the products and user experience. 
  - To provide a means whereby users can find more content via links, social media and a newsletter subscription.


## UI/UX
  This website is aimed at people who have an interest in handmade craft and wish to buy handmade pottery. Its objective is to encourage users to buy sustainably and hand produced pottery.

- **Strategy**: 
  The goal is to sell pottery products and promote Irish craft.

- **Scope**: 
  To include features that enhance the user experience and provide value to the user.

- **Structure**: 
  The user is presented with a landing page which ... From here the user can browse to more detailed product information or follow the navigation links for different sections of the page.  

  **_Website Sections:_**
  - **_Home / Landing Page:_** A page with links to the shop and specific categories of products.
  - **_Header:_** A header containg navigation links to other pages and sections of the website.
  - **_Product Page:_** A page displaying all available products.
  - **_Product Detail:_** A page containing detailed product information.
  - **_Register:_** A page to register for a user account.
  - **_Login:_** A page where users to log in.
  - **_Logout:_** A page where users log out.
  - **_Profile:_** A page with profile users shipping details, order history and link to reviews.
  - **_Order History:_** A page detailing the profile users order history.
  - **_Reviews:_** A page with a review form.
  - **_About:_** A page detailing the crafters story.
  - **_FAQ:_** A page with a list of frequently asked questions.
  - **_Contact:_** A page with a contact form.
  - **_Privacy Policy:_** A page containing the sites privacy policy.
  - **_Footer:_** A footer containing links to pages, social media links and a newsletter subscription form.

- **Skeleton**:
  The website is desinged with a simple hierarchical structure which the user can navigate through with ease.

- **Surface**:
  A uniform design has been used throught with consistent colour schemes and font to provide a seamless user experience.
  More on this is the design section below.


### Agile
  This project was designed and built using the agile approach. The first step in this process was to create the user stories which address the expectations and needs of the site users.
  Tasks were then created and updated as the project moved along and acceptance criteria was met, until all tasks were completed.

#### User Stories
  The following User Stories were created to fulfill the expectations and needs of the site users.

  | **User Stories** |
  | --- |
  | As a site user I can view a list of products so that I can make a purchase. |
  | As a site user I can view a specific category so that I can find items I am interested in. |
  | As a Site User I can sort a list of products so that I can find items based on my needs. |
  | As a Site User I can sort a category of products so that I can identify items based on my needs. |
  | As a Site User I can search for a product so that I can find items I want to buy. |
  | As a Site User I can view product details so that I can purchase the correct item. |
  | As a Site User I can view deals and offers so that I can make savings on purchases. |
  | As a Site User I can view the total of my shopping cart so that I avoid over spending. |
  | As a Site User I can select the quantity of a product so that I can purchase the correct amount. |
  | As a Site User I can view the items in my shopping cart so that I can ensure they are correct and that I can view the total cost.|
  | As a Site User I can adjust the items in my shopping cart so that I buy only what I want to. |
  | As a Site User I can enter my payment and shipping details so that I can complete my purchase |
  | As a Site User I can view an order confirmation so that I can verify that my purchase has been successful.|
  | As a Site User I can receive an email order confirmation so that I can keep a record of my purchase. |
  | As a Site User I can register an account so that I can create a personal profile.|
  | As a Site User I can login to my personalized account so that I can view my purchase history.|
  | As a Site User I can review a product so that I can provide feedback and inform future customers.|
  | As a Site Administrator I can add a product so that I can add new items to my shop. |
  | As a Site Administrator I can update a product so that I can make changes to items in my shop. |
  | As a Site Administrator I can delete a product so that I can remove items that are no longer in stock|


#### Github Project
  I created a GitHub Project to help manage the development of the site [GitHub project](https://github.com/users/lorrainescanlon/projects/5).
  Issues were created for user stories with acceptance criteria defined for each. Tasks were created for user stories and grouped into epics with milestones applied to epics. 
  Tasks were managed through the various stages and states using a Kanban board ![Kanban](/static/docs/images/github_project)

#### MosCow Priorization
  Based on MoSCow Prioritization principles (Must have, Should have, Could have, Won't have), the following feature sets were identified.
  Must Have Features
    - Product browsing
    - Product filtering
    - Product sorting
    - Product search
    - Shopping basket and checkout
    - Payment processing
    - Status messages
    - Email notifications
    - Product management

  Should Have Features
    - User profile order history
    - Use profile reviews
    - User profile management

  Could Have Features
    - Newletter Subscription
    - Related Products recommendations
    - Contact form

  Won't have Features
    - Social media login integration
    - Wishlist functionality


### Wireframes
  Wireframes were created using Balsamiq software. The initial designs met basic early requirements that have evolved since. View the wireframe designs here

  ![Wireframes](/static/docs/wireframes.pdf)



### Design
  There is a consistent colour scheme used throughout the site as shown on the colour palette below. These colours are complimented by rich images of ceramic ware that add interest and enhance the user experience.
 
  ![colour palate](/static/docs/images/colour_palette.PNG)


## Features

### Existing Features

#### Navigation Bar
 - Navbar displays the website name which acts as a home link.
 - The search box is located to the left of the navigation bar and colapses to the burger menu on mobile devices.
 - If user is authenticated/logged in they are presented with appropriate account links.
 - A realtime basket total is displayed underneath the basket icon on the navbar.
 - The navbar contains navigation links for the various product categories.

 ![Nav Bar](/static/docs/images/navbar.PNG)

 - The navbar becomes a collapsible burger menu with drop-down list on small to medium sized screens.

 ![Mobile nav](/static/docs/images/mobile_nav.PNG)

 
#### Footer
 - The footer contains sections for internal links, external links, social media links and a subcription box.

 ![Footer](/static/docs/images/)

 - The sections stack vertically on mobile screens.

 ![Mobile footer](/static/docs/images/)

#### Hero Image
 - A hero image is displayed on the home page.
 - It depicts a potter at work scene.
 
 ![Hero](/static/docs/images/)

 - An overlay section invites the visitor to shop their products.

 ![Mobile hero](/static/docs/images/)

#### Product List
 - Products are displayed as card items in a grid structure and paginated to display ? per page. 

 ![Product grid](/static/docs/images/)

 - Product cards stack vertically on mobile devices.

 ![Mobile grid](/static/docs/images/)

#### Product Description
 - This section gives some detail of the product, like description, image and rating.

 ![Product details](/static/docs/images/)


 ![Mobile detail](/static/docs/images/mobdetails.jpg)

#### Filter and Sort 

#### Shopping Basket

#### Checkout

#### Review Form
 - The review form allows logged in users to submit a review on a product that they have purchased.
 - The review form allows logged in users to submit a review on a their experience.
 - The form contains two textareas and a drop down menu to select a star rating.

 ![Review form](/static/docs/images/)


#### Register
 - Registration form to become a site user.
 - Username and Password fields are required and validated.

 ![Register](/static/docs/images/)

#### Login
 - Login form to authenticate user.

 ![Login](/static/docs/images/)
  
#### Profile


#### Logout
 - Log out button to log user out.

  ![Logout](/static/docs/images/)

#### About Us

#### Contact form
 - Contact form to enable users to provide feedback and/or contact the site administrator.

  ![Contact](/static/docs/images/)

#### Privacy Policy
 - The link provides access to the sites privacy policy.
 

 ![Privacy Policy](/static/docs/images/)


### Future Features
 - A favourites option so that registered users could make a list of items they would like to buy.
 - A weddings list feature.
 - Content to include videos and interview with other Irish crafters.
 - Have a review like button, for users to like if they found a review helpful.
 

## Database Model
The database model evolved from the needs of the user stories.  
The diagram was created using [Lucidchart](https://lucidchart.com)

![DBModel](/static/docs/images/)

### Product Model
 - The market model stores data for featured farmers markets. 


### Order Model
 - The pictures model contains image urls for market pictures. These pictures are displayed on the image carousel on the markets detail page.

### OrderLineItem
 - Records contact messages sent via the form on the contact.html page.

### UserProfile
- Records UserPorfile record and default shipping details.

### Review Model
 - The review model records reviews that are submitted for a particular item from the profile app.

### Contact Model
 - The cotact model records contact messages sent by users of the website

### Faq Model
 - The Faq model stores frequently asked questions.


### CRUD

The CRUD principle was at the center of the design process for this project. 

**Create:**
 - A user can create an account which is written to the database User model.
 - An authenticated user can create and submit a review that is written to the Review model.
 - An authenticated admin user can add a new product record.

**Read:**
 - A user can read detailed product information and review data returned from the Product and Review database models.
 - A user can search for products by name and details. Results are retuend from the Products model.

**Update:**
 - An authenticated user can update or edit their default shipping information attached to their profile.
 - An authenticated admin user can edit a product.

**Delete:**
 - An authenticated user can .
 -  An authenticated admin user can delete a product.


## Technologies Used

### Development Enviornment and Hosting
 - [Balsamiq](https://balsamiq.com) - Wireframes.
 - [Lucid](https://lucid.app/) - Database ERD.
 - [GitHub](https://github.com/) - Version control.
 - [Visual Studio Code](https://code.visualstudio.com) - IDE.
 - [Heroku](https://heroku.com) - Website hosting platform.
 - [Amazon](https://aws.com/) - Image hosting platform.

### Libraries

#### Python
 - [Gunicorn](https://gunicorn.org/) - Python Http server for WSGI applications.
 - [pyscopg2](https://pypi.org/project/psycopg2/) - Python PostgresSQL Database adapter.

#### Django
 - [Django-allauth](https://docs.allauth.org/en/latest/) - An integrated set of Django applications used for user authentication and account management.
 - [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used for styled and responsive forms with validation.

#### Bootstrap
 - [Bootstrap4](https://getbootstrap.com/) - Front-end framework used to simplify html, css and responsive design features.

#### Summernote
 - [Summernote](https://summernote.org/) - WYSIWYG editor used by the site admin in the admin panel.

### PostgresSql
 - [PostgresSQL](https://www.postgresql.org/) - An object-relational database management system (ORDMBS) is used as the backend for this project.

### Amazon
 - [Amazon Web Services](#amazon-web-services) - Platform for hosting images and video.
 
### Stripe
- [Stripe](#stripe) - Used to take secure payments over the web.

## Web Marketing

### Facebook
 - [Facebook](https://www.facebook.com/people/Wild-Atlantic-Wares/61576963876705/)
  Facebook is a popular social media platform used by over 2 billion worldwide users monthly. 

### MailChimp
 - [MailChimp](https://mailchimp.com)  - Email marketing platform
 Screenshot of subscribe section and emails showing on mailchimp
 Setup a newsletter subscription service using Mailchimp

## SEO
 
### Meta Data
 - [Meta Data](#meta-data) - Meta Data keywords and decription.
    Meta Data keywords and decription are used to increase search engine optimisation.
    ```
    <meta name="description" content="Hand crafted pottery on Irelands Wild Atlantic Way">
            <meta name="keywords" content="handmade pottery, Irish pottery, ceramic gifts, ceramic vases, ceramic cups, 
                ceramic mugs, cermic plates, ceramic bowls, wild atlantic way craft, Dingle craft, pottery Dingle, sustainable pottery ">
    ```

 
### Sitemap
 - [Sitemap](#sitemap) - link it here
  Sitemap created at 

### Robots
 - [Robots](#robots) - link it here
  Robots file created to disallow certain sections of your website. I have disallowed the profile and basket dierctories.

## Deployment

### Pre-requisites
Ensure the following are installed and added to requirements.txt prior to deployment to Heroku.
- Gunicorn, required by Heroku to run Django.
- Pyscopg2, required to connect to PostgreSQL.
- Amazon bucket to host images and video files.
- Stripe account to enable payments.

### Heroku Deployment
- The site was deployed to Heroku, the steps used were as follows: 
  - Create and login to your heroku account. 
  - On your heroku dashboard, click the new button and 'create new app' from the dropdown menu.
  - Enter the name of the app 'farmers-market-review', select region as 'Europe' and click the 'Create app' button
  - On the app screen select the 'Settings' tab.
  - Find the 'Config Vars' section and populate the following Key : Value pairs
    - AWS_ACCESS_KEY_ID *your key value*
    - AWS_SECRET_ACCESS_KEY *your key value*
    - DATABASE_URL *your key value* 
    - EMAIL_HOST_PASSWORD *your key value*
    - EMAIL_HOST_USER *your key value*
    - SECRET_KEY *your key value*
    - STRIPE_PUBLIC_KEY *your key value*
    - STRIPE_SECRET_KEY *your key value*
    - STRIPE_WH_SECRET_KEY *your key value*
    - USE_AWS *your key value*
    - GMAPS_API *your key value*
  - Scroll back to the top of this page and find the Deploy tab. 
  - On this page find 'Deployment method' and select 'GitHub'.
  - In the 'Connect to Github' section enter the name of your repository and click 'Connect'.
  - On the deploy page select your preferred deployment type I choose 'Enable Automatic Deploys'.
  - The app will be built on your next push to github.
  - Once created the app appears on your heroku dashboard. 
  - Click on app and your dashboard and 'Open app' from the app page. 
  - The app opens in a console loaded in a browser window.

### Forking and Cloning
You can choose to fork or clone your project for development purposes. Forking creates a separate repository that shares code and visibility settings with the original repository. You can make changes to a forked repsotitory without affecting the original repository.
You can clone your repository to create a local copy on your computer and sync between the two locations. Changes made to a clone repository will affect the original repository.

To Fork
- Log in to GitHub.
- Find the repository for your project.
- Click the Fork button in the top right corner of the screen.

To Clone
- Log in to GitHub.
- Find the repository for this project.
- Click the Code button and select whether you would like to clone with HTTPS, SSH or GitHub CLI. Copy the link displayed.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied in the previous steps. 

## Testing

### Testing File
For detailed testing, validation and results please refer to the [Testing Document](TESTING.md)

### Bugs

#### Challenges

 - Populating review form products drop ModelChoiceField.
    I had issues understanding/grasping the various instances and relationships involved here so had inconsistencies in my querysets caused errors.
    I created a review form with a ‘product’ field set as a ModelChoiceField using a queryset to populate it in the form init method. The queryset returns items that a profile user has purchased from the OrderLineItem model. The OrderLineItem model had a profile_user field which was populated with each record written from the checkout_request view in the checkout app. (This also caused problems for non authenticated users which required an if statement to be used)
    When the review form is submitted it should save the review to the Review model but it was throwing errors when trying to submit the form. 

    ![review-form-error](/static/docs/Bugs/review_form_error.png)

    With the help of tutor assistance I could see that there was a mismatch in the instances I was querying and trying to save.
    My initial implementation had the form submit method trying to save an instance of Orderlineitem to the review model as opposed to an instance of Product it was expecting expected as this is its foreign key.
    So we reconfigured the init method in order to retrieve an instance of Product. Using the user's OrderLineItems, we return a queryset of Products with the ids from the items the user has ordered. 

          def __init__(self, profile, *args, **kwargs):
              super(ReviewForm, self).__init__(*args, **kwargs)

              orderded_items = OrderLineItem.objects.filter(user_profile=profile)
              product_ids = orderded_items.values_list('product__id',
                                                      flat=True).distinct()

              self.fields['product'].queryset = Product.objects.filter(
                  id__in=product_ids)

    Then a similar error with the User instance, 

          'Cannot assign "<UserProfile: HPotter>": "Review.user" must be a "User" instance.'

    The review form was being populated by an instance of user from UserProfile model but the Review model had a foreign key with the auth User model.
    I changed the foreign key to point to the UserProfile model as only users with profiles could submit reviews and it resolved the issue.
    During Code Refactoring and cleanup, I decided to take a look at this review form again. I realised that there was a much simpler way to implement the queryset using the existing relationship between UserProfile and Order as opposed to needing a relationship between UserProfile and LineOrderItem. So, I came up with the following code.

    def __init__(self, profile, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        orderded_items = OrderLineItem.objects.filter(
            order__user_profile=profile)
        product_ids = orderded_items.values_list(
            'product__id', flat=True).distinct()

        self.fields['product'].queryset = Product.objects.filter(
            id__in=product_ids)

    This worked correctly during testing so I removed the profile_user field from the OrderLineItem as it was now redundant.


#### Bugs Resolved

 - Stripe not defined. 
    I had applied some changes to resolve html validation errors and was testing to ensure that they were resolved by placing an order. 
    However when I proceeded form the basket to the checkout page the card element was not populating. The div was empty.

    ![stripe-element-issue](/static/docs/Bugs/stripe_element_problem.PNG)

    I checked on the stipe developers dashboard and a payment intent had gone through, triggered when I clicked the checkout button. 
    I tested on the live website and the same issue was present a payment intent was created but the card element was not loading. 
    I opened the chrome developer tools and an error was being displayed on the console 

    ![stripe_error](/static/docs/Bugs/stripe_error.PNG)

    I google this message and the following thread was returned.

      https://stackoverflow.com/questions/43172843/uncaught-referenceerror-stripe-is-not-defined-stripe-error

    All the answers pointed to loading javascript in the head - which I had already done when stripe was setup. 
    But in an attempt to improve lighthouse performance tests I had added defer to a number of script tags. 
    I removed the defer attribute from the stripe script tag in the head and it worked correctly again.


 - Database migration. 
    I didn’t use fixture files or json files to populate product or category data as used in the walkthrough project. 
    So when it came to migrating to the production database I had to create these json files retrospectively.  
    I used the following commands to create the json files.

    ```
    python manage.py dumpdata  products.Category > category.json
    python manage.py dumpdata  products.Product > product.json
    ```

    I followed advice from the following threads to accomplish this.
    https://learndjango.com/tutorials/django-fixtures-dumpdata-loaddata 
    https://stackoverflow.com/questions/6153113/how-to-create-a-fixture-file

    I then encountered problems when loading the file data to the production database.

    “UnicodeDecodeError: 'utf8' codec can't decode byte 0xff in position 0: invalid start byte”

    To resolve this issue I opened the file in notepad selected ‘save as’ in the Encoding drop down select ‘UTF-8’ and save.  .as detailed in the following thread.
    https://stackoverflow.com/questions/17843630/python-can-dumpdata-cannot-loaddata-back-unicodedecodeerror 


#### Bugs Remaining

 - Sorting Bug

    Sort by ratings bug encountered when testing. When sorting items by rating low to high products are displayed as expected with lowest stars to highest 
    stars and then products with no ratings. When sorted from high to low, products with no ratings are returned first then highest rated to lowest. 
    The opposite happens in the test environment.

      ```
      products = Product.objects.annotate(rating=Avg(('reviews__rating')))
      ```

    Ratings are calculated in all_products and product_detail views and returned with the queryset using the annotate function.


 - Summernote Bug 

    Summernote editor was installed to enable admin to add and update faqs via the admin console. 
    When I edited an faq and refreshed the page the html tags appeared in the body of the text.
    I then added the | safe filter but this then affected the data-toggle collapse, which did not work properly when the | safe filter was used.
    The paragraphs expanded when clicked but would not collapse again.

    ![faq-problem](/static/docs/bugs/faq_problem.PNG)

    I have reverted to unedited text for the faqs for now. 


 - More link Bug
    A bug exists in the implementation of the more link from the products detail page.

    ![more-link](/static/docs/bugs/product_detail_morelink.PNG)

    ```
    <a href="{% url 'products' %}?category={{ product.category.name }}&menu={{ product.category.friendly_name }}">
    ```
    When the link is clicked the user is returned the products page which displays all products in that category.

    ```
    <div class="row">
            <div class="col text-center pt-2">
                {% if search_term != None %}
                    <h4 class="menu-font mt-sm-4 mt-md-3">{{ search_term }} - {{ products|length }} found</h4>
                        {% if products|length == 0 %}
                            <p style="font-size: large;">Please try a different search word</p>
                            <p style="font-size: large;">Or</p>
                            <a href="{% url 'products' %}?menu=All+Products" class="btn btn-outline-dark" aria-label="Shop now">
                                <span class="text-black">Shop All</span>
                                <span class="icon"><i class="fas fa-chevron-right"></i></span>
                            </a>
                        {% endif %}
                {% else %}
                    <h4 class="menu-font mt-sm-4 mt-md-3">{{ display_category }}</h4>
                {% endif %}
    ```
        
    ![correct-menu-heading](/static/docs/bugs/category_menu_correct.PNG)

    The problem is in the menu display heading at the top of the page, which is set using the display_category.
    When naviagting to this page using the more link on the products detail page the category name is only partially displayed.  

    ![partial-menu-heading](/static/docs/bugs/category_menu_bug.PNG)

    This is affecting category names that contain spaces only, i.e for Cups & Mugs only Mugs is being displayed.
    
    An error was also returned for this issue during html validation for the product details page.
    The link is passing a space within the variable {{ product.category.friendly_name }}.
    
    ![product-detail-validation-error](/static/docs/Bugs/product-detail-validation-error.PNG)






## Credits

### Media
- Images were taken from pexel and unsplash
 - Hero image Photo by Wendy Wei [Pexels](https://www.pexels.com/photo/radish-and-carrots-1656663/)
 - Caherdaniel market card picture by Paréj Richárd [Unsplash](https://unsplash.com/photos/clear-glass-jars-on-brown-wooden-shelf-F20_xtNvis4?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)

 - Fonts were taken from [Fontawesome](https://fontawesome.com/)
 - Content was written by myself.

### Code
 - I used the Boutique Ado walkthrough project as a basis for this project. I followed the same basic structure and file layout. 
 - Google Maps 
 - Django documentation 




### Acknowledgements
- Thank you to my mentor Medale Oluwanfemi for his advice and guidance on this project.
- The tutoring team for their help at troubleshooting during the project.