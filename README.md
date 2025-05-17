# wild_atlantic_wares
Wild atlantic wares

## Code Institute - Portfolio Project 5 - ECommerce 

Wild Atlantic Wares is an ecommerce website featuring full CRUD frunctionality and web marketing.
This platform allows users to share their experiences and rate products they have purchased as well as their shopping experience.

## Demo
![How the website looks on different devices](/static/docs/images/)

A live demo of the site can be found [here]()

## Tabe of Contents
- [Site Goals](#site-goals)
- [UI/UX](#ui-ux)
- [Project Planning](#project-planning)
  - [Agile](#agile)
    - [User Stories](#user-stories)
    - [MoSCow Prioritization](#moscow)
    - [GitHub Projects](#github-projects)
    - [Issues/sprints](#issues-sprints)
  - [Wireframes](#wireframes)
  - [Design](#design)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Database Model](#database-model)
  - [CRUD](#crud)
  - [Market Model](#market-model)
  - [Review Model](#review-model)
  - [Ratings Model](#ratings-model)
  - [Picture Model](#picture-model)
  - [Contact Model](#contact-model)
- [Technologies Used](#technologies-used)
  - [Development Environment and Hosting](#development-environment-and-hosting)
  - [Libraries](#libraries)
    - [Python](#python)
    - [Django](#django)
    - [BOOTSTRAP](#bootstrap)
    - [All Auth](#all-auth)
    - [Crispy Forms](#crispy-forms)
  - [PostgresSQL](#postgres-sql)
  - [Cloudinary](#cloudinary)
- [Testing](#testing)
  - [Testing file](#testing-file)
  - [Bugs](#bugs)
    - [Bugs Fixed](#bugs-fixed)
    - [Bugs Remaining](#bugs-remaining)
- [Deployment](#deployment)
  - [Heroku Deployment](#heroku-deployment)
  - [Forking and Cloning](#forking-and-cloning)
- [Credits](#credits)
  - [Media](#media)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)


## Site Goals
- To provide a website where users can browse for and buy Irish handmade craft.
- To engage with users and enable them to review and rate products and experiences.
- To encourage would be visitors to buy products by sharing reviews and ratings.
- Use review feedback to improve the products and user experience. 
- To provide a means site users can find more content via links, social media and a newsletter subscription.


## UI/UX
This website is aimed at people who wish to buy ceramic wear. 

- **Strategy**: 
The goal is to sell pottery products and promote Irish craft.

- **Scope**: 
To include features that enhance the user experience and provide value to the user.

- **Structure**: 
The user is presented with a landing page which ... From here the user can browse to more detailed product information or follow the navigation links for different sections of the page.  

  **_Website Sections:_**
  - **_Home / Landing Page:_** A.
  - **_Header:_** A header containg navigation links to other pages of the website.
  - **_Product Detail:_** A page containing detailed market information and reviews.
  - **_Register:_** A page to register for a user account.
  - **_Login:_** A page where users to log in.
  - **_Logout:_** A page where users log out.
  - **_Contact:_** A page with a contact form.
  - **_About:_** A page detailing the crafters story.
  - **_Footer:_** A footer containing social media links and newsletter subscription.

- **Skeleton**:
The website is desinged with a simple hierarchical structure which the user can navigate through with ease.

- **Surface**:
A uniform design has been used throught with consistent colour schemes and font to provide a seamless user experience.
More on this is the design section below.


### Agile
This project was designed and built using the agile approach. The first step in this process was to create the user stories which address the expectations and needs of the site users.
Each user story had acceptance criteria defined and was managed through stages on a Kanban board

#### User Stories

| **User Stories** |
| --- |
| As a site user I can  |
| As a site user I can  |
| As a Site User I can  |
| As a Site User I can  |
| As a Site User I can |
| As a Site Admin I can |
| As a Site Admin I can |
| As a Site Admin I can |
| As a Site Admin I can |
| As a Site Administrator I |

#### MosCow Priorization
Based on MoSCow Prioritization principles (Must have, Should have, Could have, Won't have), the following feature sets were identified.
Must Have Features
    - 

Should Have Features
    -

Could Have Features
    -

Won't have Features
    -


I created a [GitHub project](https://github.com/users/lorrainescanlon/projects/3) and utilised the provided Kanban board method to manage user stories and tasks. Tasks were grouped into epics with milestones applied to epics.
The Kanban board was updated as the project moved along and acceptance criteria was met, until all tasks were completed.

![Kanban](/static/docs/images/)


### Wireframes
Wireframes were created using Figma software. The initial designs met basic early requirements that have evolved since. View the wireframe designs here ![Wireframes](/static/docs/)

![Wireframe1](/static/docs/images/)

![Wireframe2](/static/docs/images/)


### Design
There is a consistent colour scheme used throughout the site as shown on the colour palette below. These colours are complimented by rich images of ceramic ware that add interest and enhance the user experience.
 
![colour palate](/static/docs/images/)


## Features

### Existing Features

#### Navigation Bar
 - Navbar with website name, and page navigation links.
 - If user is authenticated/logged in they are presented with appropriate navigation links.
 - An active link is highlighted ?? text.
 - The search box is located to the left of the navigation bar and colapses to the burger menu on mobile devices.

 ![Nav Bar](/static/docs/images/)

 - A logged in display tells the user whether they are logged in or not.

 ![Mobile nav](/static/docs/images/)

 - The navbar becomes a collapsible burger menu with drop-down list on small to medium sized screens.

 ![Nav burger](/static/docs/images/navburger.jpg)

#### Footer
 - The footer contains sections for internal links, external links, social media links and a subcription box.

 ![Footer](/static/docs/images/)

 - The secstion stack vertically on mobile screens.

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



#### Review Form
 - The review form allows logged in users to submit a review on a product.
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
  

#### Logout
 - Log out button to log user out.

  ![Logout](/static/docs/images/)


#### Contact form
 - Contact form to enable users to provide feedback and/or contact the site administrator.

  ![Contact](/static/docs/images/)

#### Privacy Policy
 - The link provides access to the sites privacy policy.
 

 ![News](/static/docs/images/)


### Future Features
 - Monthly Newsletter with calendar of events taking place like workshops, popup markets, seasonal products and competitions.
 - Content to include videos and interview with other Irish crafters.
 - Have a review like button, for users to like if they found a review helpful.
 - A favourites option so that registered users could make a list of items they would like to buy.



## Database Model
The database model evolved from the needs of the user stories.  
The diagram was created using [Lucidchart](https://lucidchart.com)

![DBModel](/static/docs/images/)

### Product Model
 - The market model stores data for featured farmers markets. 


### Order Model
 - The pictures model contains image urls for market pictures. These pictures are displayed on the image carousel on the markets detail page.

### Order Line Item
 - Records contact messages sent via the form on the contact.html page.

### UserProfile

### Review Model
 - The review model records reviews that are submitted for the markets stored in the market model.


### CRUD

The CRUD principle was at the center of the design process for this project. 

**Create:**
 - A user can create an account which is written to the database User model.
 - An authenticated user can create and submit a review that is written to the Review model.

**Read:**
 - A user can read detailed product information and review data returned from the Product and Review database models.
 - A user can search for markets by name and location details returned from the Market model.

**Update:**
 - An authenticated user can update or edit their own.

**Delete:**
 - An authenticated user can .


## Technologies Used

### Development Enviornment and Hosting
 - [Figma](https://figma.com) - Wireframes.
 - [Lucid](https://lucid.app/) - Database ERD.
 - [GitHub](https://github.com/) - Version control.
 - [Visual Studio Code](https://code.visualstudio.com) - IDE.
 - [Heroku](https://heroku.com) - Website hosting platform.
 - [Amazon](https://cloudinary.com/) - Image hosting platform.

### Libraries

#### Python
 - [Gunicorn](https://gunicorn.org/) - Python Http server for WSGI applications.
 - [pyscopg2](https://pypi.org/project/psycopg2/) - Python PostgresSQL Database adapter.

#### Django
 - [Django-allauth](https://docs.allauth.org/en/latest/) - An integrated set of Django applications used for user authentication and account management.
 - [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used for styled and responsive forms with validation.

#### Bootstrap
 - [Bootstrap5](https://getbootstrap.com/) - Front-end framework used to simplify html, css and responsive design features.

#### Whitenoise
 - [Whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html) - Middleware used by Django to handle serving of the static files.

#### Summernote
 - [Summernote](https://summernote.org/) - WYSIWYG editor used by the site admin in the admin panel.

### PostgresSql
 - [PostgresSQL](https://www.postgresql.org/) - An object-relational database management system (ORDMBS) is used as the backend for this project.

### Google Maps API
 - [Google Maps](https://developers.google.com/maps) - Platform used to render maps on the website.

### Amazon
 - [Amazon]() - Platform for hosting images and video.

## Testing

### Testing File
For detailed testing, validation and results please refer to the [Testing Document](TESTING.md)

### Bugs

#### Bugs Resolved
 - Bug 1. 

 - Bug 2

#### Bugs Remaining


## Deployment

### Pre-requisites
Ensure the following are installed and added to requirements.txt prior to deployment to Heroku.
- Gunicorn, required by Heroku to run Django.
- Pyscopg2, required to connect to PostgreSQL.
- Whitenoise, to enable the serving of static files in prodution environment.
- Amazon bucket to host images and video files.
- Stripe account to enable payments.

### Heroku Deployment
- The site was deployed to Heroku, the steps used were as follows: 
  - Create and login to your heroku account. 
  - On your heroku dashboard, click the new button and 'create new app' from the dropdown menu.
  - Enter the name of the app 'farmers-market-review', select region as 'Europe' and click the 'Create app' button
  - On the app screen select the 'Settings' tab.
  - Find the 'Config Vars' section and populate the following Key : Value pairs
    - CLOUDINARY_URL *your key value*
    - DATABASE_URL *your key value* 
    - GMAPS_API_KEY *your key value*
    - SECRET_KEY *your key value*
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