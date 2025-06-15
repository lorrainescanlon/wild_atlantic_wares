# Farmers Market Review TESTING.md

## Table of Contents
- [Manual Testing](#manual-testing)
    - [Navigation](#navigation)
    - [User Stories Testing](#user-stories-testing)
    - [Search Function](#search)
    - [App Testing](#app-functionality)
    - [Account/Authentication](#account-authentication)
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
| Home link | To be redirected to home page | Pass |
| Register link | To be directed to regitration user page | Pass |
| Login link | To be directed to user log in page | Pass |
| Contact link | To be directed to site contact page | Pass |
| Logout link | To be directed to the user log out page | Pass |
| Category link |  | Pass |
| All Products link | | Pass |
| Facebook link | To be directed to the facebook website | Pass |


### User Story Testing

| **User Story** | **Expected Outcome** | **Result** |
|----------------|----------------------|------------|
| As a site user I can  |  |  |
| As a site user I can  |  | |
| As a Site User I can  |  |
| As a Site User I can  |  |  |
| As a Site User I can  | |  |
| As a Site Admin I can  |  |  |
| As a Site Admin I can |  |  |
| As a Site Admin I can  |  |  |
| As a Site Admin I can  |  |  |
| As a Site Administrator I can |  |  |

### Search Function

| **Feature**| **Expected Outcome** |  **Testing Perfomed** | **Outcome** | **Result** | 
| -----------| -------------------- | --------------------- | ----------- | ---------- |
| Search for Product by name |  |  |  |  | 
| Search for Product by description | One or more results containing serach query in Product name or description are returned or 'No Product found' message |  |  |  |
| Search for Product not in the database | 'No Products found' message returned | |  | |
| Search empty query | 'No Products found' message returned | Search for '' |   | 

### Order By Function

| **Feature**| **Expected Outcome** |  **Testing Perfomed** | **Outcome** | **Result** | 
| -----------| -------------------- | --------------------- | ----------- | ---------- |
| Order Product by Category |  |  |  |  | 
| Order Product by Rating |  |  |  |  | 
| Order Product by Price |  |  |  |  | 
| Order Product by Rating Ascending |  |  |  |  | 
| Order Product by Price Ascending |  |  |  |  | 


### App Functionality

 **Create**                                                  

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| User account creation | Complete and submit the registration form | User can login using username and password. Porfile menu changes to include logout an profile page links |  |
| Submit a review | A registered user logs in and navigates to the profile page. Here they fill in the review form and submit | Form is submitted successfully message is displayed and the review awaits admin approval. Once approved by admin it is committed to the database. | |
| Add new Product to Shop | Create and submit a new Product | Product added sucess messsage. Product appears on the shop to buy. | |  



### Testing App functionality

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



**User Profile**

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| View default shipping details  |   |  |
| View order history |   |  |
| Create a review |   |  |

**Contact Form**

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
|  |   |  |

 **Delete** 

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| |  |   | |


### Authentication 

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


### Social Links
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