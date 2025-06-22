# Farmers Market Review TESTING.md

## Table of Contents
- [Manual Testing](#manual-testing)
    - [Navigation](#navigation)
    - [User Stories Testing](#user-stories-testing)
    - [Search Function](#search)
    - [App Testing](#app-functionality)
    - [Account/Authentication](#account-authentication)
    - [Site Admin Testing](#site-admin)
    - [Social Links](#social-links)
- [Lighthouse Testing](#lighthouse-testing)
    - [Mobile](#mobile)
    - [Laptop PC](#Laptop-PC)
- [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [Python](#python)
    - [JavaScript](#javascript)
- [Browser Compatibility](#browser-compatibility)

## Manual Testing
### Navigation

| **Feature** | **Expected Outcome** | **Result** |
| ----------- | -------------------- | ---------- |
| Wild Atlantic Wares home link | To be redirected to home page | Pass |
| Register link | To be directed to sign up page | Pass |
| Login link | To be directed to user log in page | Pass |
| Logout link | To be directed to the log out page | Pass |
| Basket link | To be directed to the shopping basket page | Pass |
| All Products By Price link | To be directed to a page with all products arranged by price | Pass |
| All Products By Rating link | To be directed to a page with all products arranged by rating | Pass |
| All Products By Category link | To be directed to a page with all products arranged by category | Pass |
| Tableware Link | To be directed to a page with tableware products | Pass |
| Cups & Mugs Link | To be directed to a page with cups and mugs | Pass |
| All Kitchen Dining Link | To be directed to a page displaying tableware, cups and mugs | Pass |
| Pots & Vases Link | To be directed to a page with pots and vases | Pass |
| Lighting & Candles Link | To be directed to a page with candles and lighting products | Pass |
| All Living Decor Link | To be directed to a page with pots, vases, lighting and candles | Pass |
| Deals Link | To be directed to a page with product deals | Pass |
| Clearance Link | To be directed to a page with clearance products | Pass |
| All Special Offers Link | To be directed to a page with both deals and clearnace products | Pass |
| Shop Now button | To be directed to all products page | Pass |
| Kitchen Dining image link | To be directed to all kitchen and dining products | Pass |
| Living Decor image link | To be directed to all living and decor products | Pass |
| Special Offer image link | To be directed to all special offer products | Pass |
| About Us Link | To be directed to a page with information about the company | Pass |
| FAQ Link | To be directed to a page with a list of the most frequently asked questions | Pass |
| Contact Us Link | To be directed to a page with contact information and a contact form | Pass |
| Privacy Policy Link | To be directed to a page with the business privacy policy | Pass |
| Connect with Us | Address, mail and telephone to currently direct users to the contact us page | Pass |
| Back to Top button | Scroll to the top of the current page | Pass |


### User Story Testing

| **User Story** | **Expected Outcome** | **Result** |
|----------------|----------------------|------------|
| As a site user I can view a list of products so that I can make a purchase  | A list of all products are displayed | Pass |
| As a site user I can view a specific category so that I can find items I am interested in | Products can be viewed by category | Pass |
| As a Site User I can sort a list of products so that I can find items based on my needs | Products can be sorted | Pass |
| As a Site User I can sort a category of products so that I can identify items based on my needs | Product categories can be sorted | Pass |
| As a Site User I can search for a product so that I can find items I want to buy | Products can be searched for by words or phrases | Pass |
| As a Site User I can view product details so that I can purchase the correct item | Details for individual products can be displayed | Pass |
| As a Site User I can view deals and offers so that I can make savings on purchases | Products can be categorised as deals and special offers | Pass  |
| As a Site User I can view the total of my shopping basket so that I avoid over spending | Shopping cart totals are visible to the user | Pass |
| As a Site User I can select the quantity of a product so that I can purchase the correct amount | A quantity button allowing a user to increase or decrease quantity | Pass |
| As a Site User I can view the items in my shopping basket so that I can ensure they are correct and that I can view the total cost | A shopping basket page detailing items and totals | Pass |
| As a Site User I can adjust the items in my shopping basket so that I buy only what I want to | Items can have their quantity adjusted and items can be removed from the shopping basket | Pass |
| As a Site User I can enter my payment and shipping details so that I can complete my purchase | A secure payment method using stripe is available to the user | Pass |
| As a Site User I can view an order confirmation so that I can verify that my purchase has been successful | Users can view an order confirmation once a payment has been verified | Pass |
| As a Site User I can receive an email order confirmation so that I can keep a record of my purchase | Users recieve an order confirmation via email once a payment has been verified | Pass |
| As a Site User I can register an account so that I can create a personal profile | Registered users can create user profiles | Pass |
| As a Site User I can login to my personalized account so that I can view my purchase history | Order history can be accessed via the users Profile | Pass |
| As a Site User I can review a product so that I can provide feedback and inform future customers | Reviews can be submitted for items purchased | Pass |
| As a Site Admin I can add a product so that I can add new items to my shop | New items can be added by authenticated and authorised users | Pass |
| As a Site Admin I can update a product so that I can make changes to items in my shop | Items can be updated by authenticated and authorised users | Pass |
| As a Site Admin I can delete a product so that I can remove items that are no longer in stock | items can be deleted by authenticated and authorised users | Pass |



### Search Function

| **Feature**| **Expected Outcome** |  **Testing Perfomed** | **Outcome** | **Result** | 
| -----------| -------------------- | --------------------- | ----------- | ---------- |
| Search for Product by name | One or more results containing serach query in product name or description are returned | Search for 'cup' | 2 products are returned | Pass | 
| Search for Product by description | One or more results containing serach query in Product name or description are returned | Search for 'white' | 11 products are returned | Pass |
| Search for Product not in the database | '0 Found' message returned | Search for 'chair' | 'Chair - 0 Found' message returned | Pass |
| Search empty query | Toast Error Message - Search Criteria can not be blank. Direct to All Products page with 'Please enter a valid search word' | Search for '' | Error Message - Search Criteria can not be blank displayed and directed to All Products page with 'Please enter a valid search word'| Pass |


### Filter Function

### Sort By Function

| **Feature**| **Expected Outcome** |  **Testing Perfomed** | **Outcome** | **Result** | 
| -----------| -------------------- | --------------------- | ----------- | ---------- |
| Sort Product by Category |  |  |  |  | 
| Sort Product by Rating |  |  |  |  | 
| Sort Product by Price |  |  |  |  | 
| Sort Product by Rating Ascending |  |  |  |  | 
| Sort Product by Price Ascending |  |  |  |  | 


### App Functionality

 **Products App**

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| View All Products |  |  | |
| View Products by Category |  |  | |
| Sort Products by Price |  |  | |
| Sort Products by Rating |  |  | |
| Sort Products by Category|  |  | |
| View Product details |  |  | |
| Add Product to shopping basket|  |  | |

 **Basket App** 

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| |  |  | |
|  |  | |  |      
|  |  |  |

 **Checkout App** 

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| |  |  | |
|  |  | |  |      
|  |  |  |



**Profiles App**

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| View Profile Menu | Click on 'My Account' and Login with valid username and password | 'My Profile' link appears on 'My Account' menu | Pass |
| View default delivery details | As an authenticated user click on 'My Profile' from the 'My Account' menu | A profile page appears with Default Delivery Details Form | Pass |
| Update default delivery details | Updated Address 1 and click the Update button | The form data is updated with the new data and a Toast Success message 'Profile Updated' id displayed | Pass |
| View order history | From the Profile page choose 'Order History' from the menu on the left of the page | A list of orders associated with that profile are displayed | Pass |
| View order summary | Click on an order from the list displayed on the view order history page | An order summary page is displayed with details of that particular order | Pass |
| Create a review | From the Profile page choose 'Submit Review' from the menu on the left of the page. Fill out the form by selecting a product from the Product drop down menu, enter a Product review, select a star rating and enter feedback on user experience click the Submit button | The form is submitted with a Toast Success message 'Thank you for your review!" and user is redirected to the profile page | Pass |


*Update delivery details form validation*

| **Testing Perfomed** | **Action** | **Expected Outcome** | **Outcome** | **Result** |
| -------------------- | ---------- | -------------------- | ----------- | ---------- |
| Update Telephone number | Changed the last 2 didgits in the telephone number and clicked Update | The form should submit, the updated data should now be visible on the default delivery details form and a Toast Success message appear with 'Profile Updated'| Profile default delivery details were updated and success message displayed | Pass |
| Delete Telephone number | Cleared the telephone number field and clicked Update | The form should submit, the telephone number should now be blank on the form and a Toast Success message appear with 'Profile Updated' | Form Submitted, telephone number field is now blank on default delivery details form and Profile Updated Success message displayed | Pass |
| Update Street Address 1 | Changed Address 1 field and clicked Update | The form should submit, the updated data should now be visible on the default delivery details form and a Toast Success message appear with 'Profile Updated'| Form submitted, Street Address 1 updated on default delivery details form and success message displayed | Pass |
| Delete Street Address 1 | Cleared Address 1 field and clicked Update | The form should submit, street address 1 should now be blank on default delivery details form and a Toast Success message appear with 'Profile Updated' | Form Submitted, Street Address 1 is now clear on default delivery details form and Profile Updated Success message displayed | Pass |
| Update Street Address 2 | Changed Address 2 field and clicked Update | The form should submit, the updated data should now be visible on the default delivery details form and a Toast Success message appear with 'Profile Updated'| Form submitted, Street Address 2 updated on default delivery details form and success message displayed | Pass |
| Delete Street Address 2 | Cleared Address 2 field and clicked Update | The form should submit, street address 1 should now be blank on default delivery details form and a Toast Success message appear with 'Profile Updated' | Form Submitted, Street Address 2 is now clear on default delivery details form and Profile Updated Success message displayed | Pass |
| Update Town or City | Changed Town or City field and clicked Update | The form should submit, the updated data should now be visible on the default delivery details form and a Toast Success message appear with 'Profile Updated'| Form submitted, Town or City updated on default delivery details form and success message displayed | Pass |
| Delete Town or City | ClearedTown or City field and clicked Update | The form should submit, Town or City should now be blank on default delivery details form and a Toast Success message appear with 'Profile Updated' | Form Submitted, Town or City is now clear on default delivery details form and Profile Updated Success message displayed | Pass |
| Update County | Changed County field and clicked Update | The form should submit, the updated data should now be visible on the default delivery details form and a Toast Success message appear with 'Profile Updated'| Form submitted, County updated on default delivery details form and success message displayed | Pass |
| Delete County | Cleared County field and clicked Update | The form should submit, County should now be blank on default delivery details form and a Toast Success message appear with 'Profile Updated' | Form Submitted, County is now clear on default delivery details form and Profile Updated Success message displayed | Pass |
| Update Postcode | Changed Postcode field and clicked Update | The form should submit, the updated data should now be visible on the default delivery details form and a Toast Success message appear with 'Profile Updated'| Form submitted, Postcode updated on default delivery details form and success message displayed | Pass |
| Delete Postcode | Cleared Postcode field and clicked Update | The form should submit, Postcode should now be blank on default delivery details form and a Toast Success message appear with 'Profile Updated' | Form Submitted, Postcode is now clear on default delivery details form and Profile Updated Success message displayed | Pass |
| Update Country | Changed Country field and clicked Update | The form should submit, the updated data should now be visible on the default delivery details form and a Toast Success message appear with 'Profile Updated'| Form submitted, Country updated on default delivery details form and success message displayed | Pass |
| Delete Country | Cleared Country field and clicked Update | The form should submit, Country should now be blank on default delivery details form and a Toast Success message appear with 'Profile Updated' | Form Submitted, Country is now clear on default delivery details form and Profile Updated Success message displayed | Pass |


*Create Review form validation*

| **Testing Perfomed** | **Action** | **Expected Outcome** | **Outcome** | **Result** |
| -------------------- | ---------- | -------------------- | ----------- | ---------- |
| Submit an incomplete review | Do not select a product from the Product drop down menu. Continue to enter a Product review, select a star rating and enter feedback on user experience click the Submit button | The form should not submit and a message telling the user that a product needs to be selected should be displayed | The form did not submit, the select drop down was highlighted but no message was displayed | Fail |
| Submit an incomplete review | Fill out the form by selecting a product from the Product drop down menu, do not enter a Product review, select a star rating and enter feedback on user experience click the Submit button | The form should not submit and a message telling the user that the field can not be blank should be displayed | The form did not sumit and a message saying 'Please fill out this field' is displayed | Pass |
| Submit an incomplete review | Fill out the form by selecting a product from the Product drop down menu, enter a Product review, select a star rating and leave feedback on user experience blank. click the Submit button | The form should not submit and a message telling the user that the field can not be blank should be displayed | The form did not sumit and a message saying 'Please fill out this field' is displayed | Pass |

**About App**

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| Contact Form  |   |  |
| Faq Page |   |  |



### Authentication 

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| User account creation | Complete and submit the registration form | User can login using username and password. Porfile menu changes to include logout an profile page links |  |
| Submit a review | A registered user logs in and navigates to the profile page. Here they fill in the review form and submit | Form is submitted successfully message is displayed and the review awaits admin approval. Once approved by admin it is committed to the database. | |
| Add new Product to Shop | Create and submit a new Product | Product added sucess messsage. Product appears on the shop to buy. | |  
 
**Acount Registration** 

| **Test** | **Expected Outcome** | **Result** |
| -------- | -------------------- | ---------- |
| Register new User with valid username, email and password |  |  |
| Register new User with valid username and password, no email |  |  |
| Register new User with valid username, no password and no email |   |  |
| Register new User with valid password, no username and no email |   |  |
| Register new User with valid username, invalid password and no email |   |  |

**Account Login**
| **Test** | **Expected Outcome** | **Result** |
| -------- | -------------------- | ---------- |
| Login with a valid username and password |  |  |
| Login with a valid username and no password |  |  |
| Login with a valid username and incorrect password | |  |
| Login with a no username and no password |  | |
| Login with a no username and a password |  |  |

**Account Logout**
| **Test** | **Expected Outcome** | **Result** |
| -------- | -------------------- | ---------- |
| Logout using 'Log Out' button on Logout page | Account logout successfull, 'You have signed out' message appears and logged in as status changes to 'You are not logged in' | Pass |


### Site Admin Testing

**Admin Account**
| **Test** | **Expected Outcome** | **Result** |
| -------- | -------------------- | ---------- |
| Login with a valid username and password | My Account Menu list items to change |  |
| View Products detail page| Links to edit and delete product should be displayed  |  |
| Add Product |  |  |
| Edit Product |  |  |
| Delete Product |  |  |

**Admin Console**
| **Test** | **Expected Outcome** | **Result** |
| -------- | -------------------- | ---------- |
| Login with a valid username and password | |  |
| View Model Data | |  |
| Add Product |  |  |
| Edit Product |  |  |
| Delete Product |  |  |

[Site Admin Testing](#site-admin)

### Social Links
| **Feature** | **Expected Outcome** | **Result** |
| ----------- | -------------------- | ---------- |
| Facebook icon link | To be directed to the facebook website which opens in a new browser window | Pass |
| Instagram icon link | Currently direct users to the Instagram homepage which opens in a new browser window | Pass |
| YouTube icon link | Currently direct users to the YouTube homepage which opens in a new browser window  | Pass |
 
 Social media links tested on both mobile and desktop. 
 Social links tested in multiple browsers successfully.
 All open in a separate browser window.


### Lighthouse Testing
Lighthouse testing was carried out on both desktop and mobile devices using chrome developer tools.

#### Mobile
![Mobile Lighhouse Test]()

#### Laptop/PC
![Desktop Lighthouse Test]()


## Code Validaton

### HTML Validation [W3C validator](https://validator.w3.org/)
As this project contains Django tags and Jinja templating language the source code of each page was pasted into the validator directly as opposed to using the websites url.

**Home page**

**Products page**

**Product detail page**

**Basket page**

**Checkout page**

**Profile page**

**Sales History page**

**Reviews page**

**About us page**

**Contact Page page**

**Privacy Policy page**

Error reported in realtion to parameter value passed to google maps url. There are spaces in the location name.

![Market details validation error](/static/docs/images/markedetailvalidation.PNG)

![Error highlight in code](/static/docs/images/mapserror.PNG)

**Search results page**
Document checking completed. No errors or warnings to show.

**Register page**

**Login page**


**Logout page**


**Contact page**


**Reviews page**


### CSS Validation [Jigsaw](https://jigsaw.w3.org/css-validator/)
No errors reported 

![css validation]()

### Javascript Validation [JSHint](https://jshint.com/)
No errors reported 

![javascript validation]()


### Python Validation
I installed and used the pycodestyle tool to validate the projects python code. 


## Browser Compatibility
This site was tested on the following browsers for functionality, consistency and responsiveness:
 - Google Chrome - *Pass*
 - Microsoft Edge - *Pass*
 - Mozilla Firefox - *Pass*