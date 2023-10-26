# Social Fun

This project is designed and developed to create a better user experience for the users/members of a community. The users can register and log in to the site and view the events posted by the admin/community responsible person. The users are also able to register for events, like and comment on an event, and edit and delete their comments. The functionality of category & profile pages and search bar are also added for user convenience and better user experience.

The website is created for real-life situations but embedded with fictitious data for checking purposes. The site is showcasing Python (Django framework), JavaScript, HTML, CSS, Bootstrap, PostgreSQL database, Herokuapp, and Gitpod for Project Portfolio 4.

And can be accessed by this [link.](https://socialfun-9d543c215b26.herokuapp.com/)

![Responsive Mockup Screenshot](/media/images/mockup.png)

## Contents
<a name="contents"></a>

- [UX](#ux)
  - [Strategy](#strategy)
    - [User Stories](#user-stories)
  - [Scope](#scope)
    - [Simple and intuitive User Experience](#simple-and-intuitive-user-experience)
    - [Relevant content](#relevant-content)
    - [Features for upgraded experience](#features-for-upgraded-experience)
    - [Different account types for Participants and staff members / Admin](#different-account-types-for-participants-and-staff-members--admin)
    - [Responsiveness](#responsiveness)
  - [Structure](#structure)
  - [Skeleton](#structure)
    - [Wireframes](#wireframes)
    - [Database](#database)
  - [Surface(Design)](#surface-design)
    - [Color Scheme](#color-scheme)
    - [Imagery](#imagery)
    - [Typography](#typography)
- [Agile Methodology](#agile-methodology)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Python Packages](#python-packages)
  - [Programs Used](#programs-used)
- [Testing](#testing)
  - [Google Chrome Lighthouse](#google-chrome-lighthouse)
  - [Validator Testing](#validator-testing)
    - [Python Validator - PEP8](#python-validator-pep8)
    - [HTML W3C Validator](#html-w3c-validator)
    - [CSS Jigsaw Validator](#css-jigsaw-validator)
    - [Jshint Validator](#jshint-validator)
  - [Manual Testing](#manual-testing)
    - [Frontend](#frontend)
    - [Backend / Admin Panel](#backend--admin-panel)
  - [Testing User Stories](#testing-user-stories)
     - [User Goals](#user-goals)
     - [Site Administrator Goals](#site-administrator-goals)
  - [Bugs / Issues](#bugs--issues)
  - [Unresolved Bugs / Issues](#unresolved-bugs-or-issues)
- [Deployment](#deployment)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Fork the repository](#fork-the-repository)
  - [Making a Local Clone](#making-a-local-clone)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Code](#code)
- [Acknowledgements](#Acknowledgements)


## UX
### Strategy
The objective of the site is to provide a common platform for all users to view and register for community events. The site allows users to share their thoughts, and leave comments through commenting and liking/unliking events. 
#### User Stories
- **User Goals**:
  - As a Site User I can find the navigation items so that I can navigate the site easily.
  - As a Site User I can view a paginated list of events so that I select an event to view.
  - As a Site User I can view a list of events so that I can select one to check for more details.
  - As a Site User I can click on an event so that I can read the full content.
  - As a Site User / Admin I can view the number of likes on each event so that I can see which is the most viral.
  - As a Site User / Admin I can view the number of participants on each event so that I can view how many people have registered for the event.
  - As a Site User I can register an account so that I can comment, like, and participate in events.
  - As a Site User I can login & logout of the site so that I can access the site securely.
  - As a Site User / Admin I can view comments on an individual event so that I can read the conversation.
  - As a Site User I can leave comments on an event so that I can be involved in the conversation.
  - As a Site User I can edit and delete my comments so that I revise/update and remove the contents.
  - As a Site User I can like or unlike an event so that I can interact with the content.
  - As a Site User I can register for an event so that I can participate.
  - As a Site User I can click on the event category so that I can view the events for selected category.
  - As a Site User I can search for desired event so that I can find it more easily and quickly.
  - As a Site User I can view my profile so that I can check and update it.
  - As a Site User I can edit my profile so that I can keep it up-to-date.
  - As a Site User I can upload a profile picture so that my profile looks good and modern.
  - As a Site User I can receive different alert messages so that I know the status of different actions happened.
<br>

- **Site Administrator Goals**:
  - As a Site Admin I can create, read, update, and delete events so that I can manage the event content.
  - As a Site Admin I can create, edit, update and delete event categories so that I can manage the event categories.
  - As a Site Admin I can create draft events so that I can finish writing the content later.
  - As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.
  - To handle any potential errors appropriately and consistently.
  - To keep security-sensitive information hidden.

### Scope
#### Simple and intuitive User Experience
 - Ensure the site title and logo provide first-hand information regarding the site;
 - Ensure the navigation menu is visible and functional at every step;
 - Ensure every page has a suggestive name that fits its content;
 - Ensure the user will get visual feedback when navigating through pages;
 - Ensure the design matches the theme of the event and does not confuse the user.

 #### Relevant content
 - Add information about the event such as name, category, venue, description, author, participants, created_on, start_date, end_date, registeration_deadline, and status;
 - Create relevant navigation buttons for each section;
 - Create a section for comments, categories, and profiles.

#### Features for upgraded experience
- Create a paginated list of events that allows the user to view all events along with all their details;
- Create an event detail page that allows users to like/unlike the event, register for an event, leave, edit, and delete comments;
- Create a category page with dropdown options that allow users to view all events related to the selected category;
- Create a profile page that allows the user to view and edit his profile. The user can also view how many events it has created and registered to;
- The search bar in the navigation area gives the user the ability to search for events quickly and easily.

#### Different account types for Participants and staff members / Admin
- Participants can register for events while the admin can add events, and categories and approve comments;
- Participants can like/unlike and leave comments on events; edit and delete their comments but the comments will be approved by the admin and will be published;
- Participants have access only to their Profile page for managing it;
- Staff members/ admin has access to the admin panel to manage events, comments, category, and both types of accounts.

#### Responsiveness
- Create a responsive design for desktop, tablet, and mobile devices.

### Structure
The structure of the website is divided into nine pages but the content depends on authentication and authorization of users.
- **Register/Login** pages give the user the possibility to create an account and authenticate for accessing different features;
- **Logout** feature is a modal that helps user to exit the site securely;
- **Home** page is open and visible to all types of user irrespective of registeration and authorization and includes list of all events;
- **Event Detail** page is visible only to logged-in user and displays the detail of selected event. The page also allows user to like/unlike and register to an event. The user also has the ability to leave, edit and delete comments related to the event;
- **The Registration Confirmation** page is visible only to logged-in user and allows the user to complete the event registeration process.
- **Event Category** page is visible only to logged-in user and allows the user to view the list of events for a selected category.
- **Profile** page is visible only to logged-in user and allows the user to view and update its contents.
- **Search Bar** feature is visible to all users and allows the user to search for matching events based on the typed characters. However, the actual link to display the details of the event is only visible to logged-in users.
- **The Admin Panel** page is visible only to staff members with admin rights/admin to manage the events, comments, category, profile, and user accounts.

### Skeleton
#### Wireframes
Wireframe is used to plan and sketch the website.

##### Mobile Devices
- [Home Page. Mobile Screen](/media/images/home_page_mobile.png)
- [Event Detail Page. Mobile Screen](/media/images/event_detail_page_mobile.png)
- [Event Registration Confirmation Page. Mobile Screen](/media/images/registeration_confirmation_mobile.png)
- [Category Page. Mobile Screen](/media/images/category_page_mobile.png)
- [Profile Page. Mobile Screen](/media/images/profile_page_mobile.png)
- [Sign Up Page. Mobile Screen](/media/images/signup_page_mobile.png)
- [Login Page. Mobile Screen](/media/images/login_page_mobile.png)
- [Logout Page. Mobile Screen](/media/images/logout_page_mobile.png)

##### Desktop 
- [Home Page. Desktop Screen](/media/images/home_page_desktop.png)
- [Event Detail Page. Desktop Screen](/media/images/event_detail_page_desktop.png)
- [Event Registeration Confirmation Page. Desktop Screen](/media/images/registeration_confirmation_desktop.png)
- [Category Page. Desktop Screen](/media/images/category_page_desktop.png)
- [Profile Page. Desktop Screen](/media/images/profile_page_desktop.png)
- [Sign Up Page. Desktop Screen](/media/images/signup_page_desktop.png)
- [Login Page. Desktop Screen](/media/images/login_page_desktop.png)
- [Logout Page. Desktop Screen](/media/images/logout_page_desktop.png)

#### Database
PostgreSQL relational database is used to store the website data. The database model diagram is designed using [Lucidchart](https://lucid.app/).
<details>
  <summary>Database Schema</summary>
<img src="media/images/database_erd_model.png"><br>
</details>

### Surface (Design)
#### Color Scheme
All colors were selected with the eyedropper plugin from the website logo to maintain chromatic harmony.
- Radial-gradient (circle at 74.2% 50.9%, rgb(14, 72, 222) 5.2%, RGB (3, 22, 65) 75.3%) is used as the main color for the header and footer sections.<br>
![#Blue Gradient](/media/images/gradient.png)
- (#E84610) color is used as hover and active color for header and footer sections. The color is also used for deleting buttons and links.<br>
![#E84610](/media/images/e84610.png)
- (#0D6EFD) is used as text color for event heading and description, for buttons except indicated separately, and for image flash.<br>
![#0D6EFD](/media/images/0d6efd.png)
- (#000) is used as the text color for event-subtitle.<br>
![#000](/media/images/000.png)
- (#F6F6F6) is used as the main background color.<br>
![#F6F6F6](/media/images/f6f6f6.png)
- (#FFF) is used as the main text color for the header and footer sections, event titles and buttons' text color.<br>
![#FFF](/media/images/fff.png)
- Few other limited colors are used as border and shading colors.

#### Imagery
- The website logo that describes the website's purpose is taken from [Freepik](https://www.freepik.com/).
- The fictitious pictures used in the website are taken from [Pexcels](https://www.pexcels.com/).

#### Typography
- EB Garamond font is used as the main font for headings.<br>
![EB Garamond Font](/media/images/eb_garamond_font.png)
- Roboto font is used as the main font for paragraphs.<br>
![Roboto Font](/media/images/roboto_font.png)
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Agile Methodology
This project was developed using the Agile methodology.
All user stories implementation progress was registered using [socialfun_project](https://github.com/users/Ahmad-Hazrati/projects/6). As the user stories were accomplished, they were moved from the kanban board **To Do**, to **Progress** and finally to **Done** lists.

## Features 
### Existing Features

- __Home Page__ 
  - When the website loads, the home page will load as well as the default page to all users whether authenticated or not. 
  - The home page is paginated and contains list of all events published by the authorized community user/admin. 
  - The event's name, author, excerpt, image, date created, and number of likes are displayed on the home page. 
  - If the user is authenticated then the event name and excerpt will be an active navigational link to the event detail page. 
  ![Home Page](/media/images/home_page.png)<br><br>
- __Event Detail Page__ 
  - This page is only visible to authorized users and contains all details of the event. 
  - The page also contains the event registeration link and comment sections. 
  - The registeration button is visible in case the user has not yet registered to the event, otherwise, registeration confirmation message will be displayed.
  - The user can leave, read, edit and delete comments. 
  - The comments will be visible to other users once has been approved and published by the admin but can be seen, edited and deleted by the comments' owner.
  ![Event Detail Page](/media/images/event_detail_page.png)<br><br>
- __Event Registeration Page__
  - This page is only visible to authorized user and contains the event details and registeration confirmation button. 
  - The user has also the ability to go back to the event detail page by clicking the back button.
  ![Event Detail Page](/media/images/event_registeration_page.png)<br><br>
- __Category Page__ 
  - The category page is only visible to authorized user and contains the list of all event related to selected category.
  - The category page can be accessed from the navbar dropdown link and is dynamic. The category dropdown updates when a new category is added by the admin.
  - The event in the category page is navigable and prompt the user to the event detail page once selected.
  ![Category Page](/media/images/category_page.png)<br><br>
- __Profile Page__ 
  - The profile page is only visible to authorized user and comprises profile properties, an edit button, and the latest events created by the user.
  - The user can edit their profile avatar and bio here.
  ![Profile Page](/media/images/profile_page.png)<br><br>
- __Logout Page__ 
  - The logout page is only visible to authorized users and allows the user to logout securely from the website.
  ![Logout Page](/media/images/logout_page.png)<br><br>
- __Register Page__ 
  - The register page is only visible to unauthorized users and allows the user to create an account and securely access the website.
  - The page allows the user to fill out the form and sign up. The page includes a login button to navigate the user to login page in case already has an account.
  ![Register Page](/media/images/register_page.png)<br><br>
- __Login Page__ 
  - The login page is only visible to unauthorized user and allows the user to log in and securely access the website.
  - The page allows the user to fill out his/her username or email and password to log in. The page also comprises a register button to navigate the user to register page in case not have created an account yet.
  ![Login Page](/media/images/login_page.png)<br><br>
- __Builtin Admin Page__ 
  - The builtin admin page is only visible to authorized user and allows the user with admin rights to log in and securely access the website administration panel.
  - The page allows the admin to create, read, update and delete the contents of the event, comment, category and profile pages. 
  ![Builtin Admin Page](/media/images/admin_page.png)<br><br>
- __Base Page__ 
  - This page is the base template that encompases the header and footer, css files, script files, links to external APIs and loads the contents to all other pages when is called.<br><br>

### Features Left to Implement
Initially, the idea was that the venue should be a separate model and user could create, edit and delete venue and event, but due to limited time couldn't implemented.
Further features inclusive (cited above) to implement are:
- another feature couldn't be that user could perform CRUD operations on events and venues from the profile page;
- a review page will be a better feature to be added to the app.
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Technologies Used

### Languages Used
- **Python, JavaScript, HTML, and CSS** are used extensively during the project.
- **Markdown**: Used exclusively for README.

### Python Packages
- **django**
- **gunicorn**
- **dj-database-URL**
- **psycopg2**
- **dj3-cloudinary-storage**
- **whitenoise**
- **jinja2**
- **django-allauth**
- **django-crispy-forms**
- **autopep8**

### Programs Used
[Bootstrap5](https://getbootstrap.com/): used to add predefined styled elements and responsiveness.<br>
[Git](https://git-scm.com/): used for version control.<br>
[GitHub](https://github.com/): used to host the source code of the program.<br>
[Gitpod](https://gitpod.io/): used to write and test the code.<br>
[Heroku](https://dashboard.heroku.com/): used to deploy the project.<br>
[Cloudinary](https://cloudinary.com/): used to store static files.<br>
[Summernote](https://summernote.org/): used to online editors.<br>
[PostgreSQL](https://www.elephantsql.com/): used to store the website data.<br>
[Balsamiq](https://balsamiq.com/wireframes/): used to sketch the project contents.<br>
[Lucid](https://lucid.app/): used to design the database model.<br>
[TinyPNG](https://tinypng.com/): used to compress the images.<br>
[Favicon.io](https://favicon.io/): used to generate the website favicon.<br>
[Font Awesome](https://fontawesome.com/): used for creating attractive UX with icons.<br>
[Google Fonts](https://fonts.google.com/): used for project typography.<br>
[JsHint](https://jshint.com/): used to validate the scripts.<br>
[CI Python Linter](https://pep8ci.herokuapp.com/#/): used to perform check of Python code.<br>
[HTML - W3C HTML Validator](https://validator.w3.org/#validate_by_uri+with_options): used to valid the HTML pages.<br>
[CSS - Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_uri): used to valid the CSS.<br>
[Chrome Del Tools](https://developer.chrome.com/docs/devtools/): used for project debugging purpose.<br>
[W.A.V.E.](https://wave.webaim.org/): used for testing accessibility.<br>
[Freepik](https://www.freepik.com/): used to generate the website logo.<br>
[Pexels](https://www.pexels.com/): used to generate the website images.<br>
[Gradients](https://gradients.shecodes.io/gradients/398#gradient): used to generate the header and footer gradient color.<br>
**Light House**: used to test the website performance.<br>
<br><a href="#contents">BACK TO CONTENTS 🔼</a>

## Testing 
Testing has taken place continuously throughout the development of the project. Each view was tested regularly. When the outcome was not as expected, debugging took place at that point.

### Google Chrome Lighthouse
Google Chrome lighthouse checks and generates a comprehensive report regarding the website's performance, accessibility, best practices, and SEO.
![Home Page. Lighthouse Report](/media/images/lighthouse_home_page.png)
![Event Detail Page. Lighthouse Report](/media/images/lighthouse_event_detail_page.png)
![Event Registration Page. Lighthouse Report](/media/images/lighthouse_event_registeration_page.png)
![Category Page. Lighthouse Report](/media/images/lighthouse_category_page.png)
![Profile Page. Lighthouse Report](/media/images/lighthouse_profile_page.png)
![Logout Page. Lighthouse Report](/media/images/lighthouse_logout_page.png)
![Register Page. Lighthouse Report](/media/images/lighthouse_register_page.png)
![Login Page. Lighthouse Report](/media/images/lighthouse_login_page.png)

### Validator Testing 
#### Python Validator - PEP8
- Python testing was done using the PEP8 Online to ensure there were no syntax errors in the project. All python files were entered into the online checker and no errors were found in any of the custom codes.
**Event admin.py** : No errors or warnings to show.
![Event admin.py PEP8](/media/images/pep8_event_admin.png)
**Event app.py** : No errors or warnings to show.
![Event app.py PEP8](/media/images/pep8_event_app.png)
**Event context_processor.py** : No errors or warnings to show.
![Event context_processor.py PEP8](/media/images/pep8_event_context_processor.png)
**Event forms.py** : No errors or warnings to show.
![Event forms.py PEP8](/media/images/pep8_event_forms.png)
**Event models.py** : No errors or warnings to show.
![Event models.py PEP8](/media/images/pep8_event_models.png)
**Event urls.py** : No errors or warnings to show.
![Event urls.py PEP8](/media/images/pep8_event_urls.png)
**Event views.py** : No errors or warnings to show.
![Event views.py PEP8](/media/images/pep8_event_views.png)
**Profile admin.py** : No errors or warnings to show.
![profile admin.py PEP8](/media/images/pep8_profile_admin.png)
**Profile apps.py** : No errors or warnings to show.
![profile apps.py PEP8](/media/images/pep8_profile_apps.png)
**Profile forms.py** : No errors or warnings to show.
![profile forms.py PEP8](/media/images/pep8_profile_forms.png)
**Profile models.py** : No errors or warnings to show.
![profile models.py PEP8](/media/images/pep8_profile_models.png)
**Profile urls.py** : No errors or warnings to show.
![profile urls.py PEP8](/media/images/pep8_profile_urls.png)
**Profile views.py** : No errors or warnings to show.
![profile views.py PEP8](/media/images/pep8_profile_views.png)
**Socialfun settings.py** : No errors or warnings to show.
![profile settings.py PEP8](/media/images/pep8_socialfun_settings.png)
**Socialfun urls.py** : No errors or warnings to show.
![profile urls.py PEP8](/media/images/pep8_socialfun_urls.png)
**Socialfun wsgi.py** : No errors or warnings to show.
![profile wsgi.py PEP8](/media/images/pep8_socialfun_wsgi.png)


#### HTML W3C Validator
As this is a Django project, the HTML couldn't be tested via the site's URL, due to Django tags and Jinja templating language in HTML files. Instead, the source code of each page was pasted into the validator directly.<br>
**Home Page**: No errors or warnings to show.
![Home Page](/media/images/w3c_validator_home_page.png)<br><br>
**Event Detail Page**: 4 errors are returned.
![Event Detail Page](/media/images/w3c_validator_event_detail_page.png)
**Fix**:
- 1. Change the **p** element into **div** element as the validator did not read the closing **p** element.<br>
- 2. Remove the <strong> element.
- 3. Add a data attribute to the comment_id of Delete button.
- 4. Add a data attribute to the comment_id of Edit button.<br><br>
**Event Registration Page**: No errors or warnings to show.
![Event Registration Page](/media/images/w3c_validator_event_registeration_page.png)
**Fix**:
- 1. Change the **p** element into **div** element as the validator did not read the closing **p** element.<br><br>
**Category Page**: No errors or warnings to show.
![Category Page](/media/images/w3c_validator_category_page.png)<br><br>
**Profile Page**: No errors or warnings to show.
![Profile Page](/media/images/w3c_validator_profile_page.png)<br><br>
**Logout Page**: No errors or warnings to show.
![Logout Page](/media/images/w3c_validator_logout_page.png)<br><br>
**Register Page**: No errors or warnings to show.
![Register Page](/media/images/w3c_validator_register_page.png)

<br><br>

**Login Page**: No errors or warnings to show.
![Login Page](/media/images/w3c_validator_login_page.png)<br><br>

#### CSS Jigsaw Validator
No errors were found when passing through the official W3C CSS.
![STYLE CSS](/media/images/jigsaw_css_validator.png)


#### Jshint Validator
No errors were found when passing through the JSHint.
  ![JSHint validator comments.js](/media/images/jshint_comments.png)
  ![JSHint validator message_box](/media/images/jshint_message_box.png)


### Manual Testing

- __Frontend__
  - The header loads and functions properly. The navigation bar sticks to the top of the page and is always accessible to the user. The navigation items, links, dropdown menus, and search bar work and function as expected.
  - The footer loads and functions properly. The social links open in a new tab and navigate the user to the right page.
  - The home page is displayed as default page when the website loads and allows the user to register or login to the website.
  - The events are displayed with correct format and design as expected.
  - The pagination functionality on the home page works without any issue. It adds another pages after 3 events on the page.
  - The signup, login, and logout functionalities are working and have no issues. It shows the right interactive message to the user.
  - The event detail page loads normally when the user clicks the link to the event detail page.
  - The functionalities to like/unlike and register to an event are working properly and displays the right interactive message to the user.
  - The comment form has no issues and it submits a new comment once the form is completed by a registered user. The comment is displayed once the submit button is pressed. The interactive message for this action is working without errors.
  - The functionality to edit and delete a comment works without any issue. The buttons only visible to the authorized user / user own the comment.
  - The event registration page loads successfully and registration functions as expected. 
  - The event categories are updated and loaded normally. The filtered events by category are listed and displayed without issue.
  - The profile page loads normally. It displays the user information and image without any issues. The form to edit the profile image and bio also works properly.

- __Backend / Admin Panel__
  - The admin panel has been tested repeatedly without any issues. 
  - All models are working properly.
  - The admin user can perform CRUD operation on all models (event, comment, category, and profile) without any issue.
  - The admin user can approve comments and publish events.

### Testing User Stories
User Stories are fully achieved. They are discussed in [**User Stories**](#user-stories) section under **Strategy** and for more details please refer to [Github Repository](https://github.com/users/Ahmad-Hazrati/projects/6/views/1).

<a href="#contents">BACK TO CONTENTS 🔼</a>

### Bugs / Issues

<table  width = 100% cellspacing="0" cellpadding="0">
   <tr>
   <th>Issue/Bug</th>
   <th>Solution</th>
   </tr>
   <tr>
   <td>The website images were not loading from Cloudinary and displaying the error "Must supply API key"</td>
   <td>The issue is rectified by updating the Cloudinary URL in Heroku.</td>
   </tr>
   <tr>
   <td>Issue with JS error "Uncaught TypeError: Cannot read properties of null".</td>
   <td>The issue is rectified by adding an if statement to the code to check the message and execute when it is not null.</td>
   </tr>
   <tr>
   <td>Issue with deployment to Heroku due to failed to build backports.zoneinfo.</td>
   <td>The issue is rectified by updating the version of backports.zoneinfo from 0.2.1 to 3.9.</td>
   </tr>
   <tr>
   <td>Issue with deployment to Heroku due to Node.js.</td>
   <td>Node.js is removed from Heroku build packs and the issue is rectified. </td>
   </tr>
   <tr>
   <td>Issue with deployment due to crispy-bootstrap4 and Django version.</td>
   <td>The issue is rectified by adding the context_processor.py and updatet the relevant code in the view.py.</td>
   </tr>
   <tr>
   <td>Category page was not loading when the user wanted to access from another page.</td>
   <td>The issue is rectified by adding the crispy-bootstrap4.</td>
   </tr>
   <tr>
   <td>Issue with error "Reverse for 'event_detail' with no argument not found".</td>
   <td>The issue is rectified by passing the event slug in the url along with event_detail.</td>
   </tr>
   <tr>
   <td>Issue with error "MultipleObjectsReturned" while deleting a comment.</td>
   <td>The issue is rectified by removing the queryset and post variables from the delete function.</td>
   </tr>
  </table>

### Unresolved Bugs or Issues
- Issue with crispy forms is not resolved due to the required version of Django. The required version for crispy-forms is 4.2 while the existing PostgreSQL (ElephantSQL) database is version 6.
 <br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Deployment

### Deploying to Heroku
* This site was deployed by completing the following steps:

1. Log in to [Heroku](https://id.heroku.com) or create an account.
2. On the main page click the button labelled New in the top right corner and from the drop-down menu select Create New App.
3. You must enter a unique app name.
4. Next select your region.
5. Click on the Create App button
6. The next page is the project’s Deploy Tab. Click on the Settings Tab and scroll down to Config Vars.
7. Click Reveal Config Vars and enter the following variables and values:
    - Add "PORT" and its value.
    - Add "CLOUDINARY_URL" and its value.
    - Add "DATABASE_URL" and its value.
    - Add "SECRET_KEY" and its value.
8. Next, scroll down to the Buildpack section click Add Buildpack select Python, and click Save Changes.
9. Scroll to the top of the page and choose the Deploy tab.
10. Select Github as the deployment method.
11. Confirm you want to connect to GitHub.
12. Search for the repository name and click the connect button.
13. Scroll to the bottom of the deploy page and select the preferred deployment type.
14. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.

### Fork the repository
To create a copy of the repository on your account and change it without affecting the original project, use **Fork** directly from GitHub:
1. On [My Repository Page](https://github.com/Ahmad-Hazrati/django-event), press Fork in the top right of the page
2. A forked version of my project will appear in your repository

### Making a Local Clone

1. Log in to Github and locate the [Github Repository.](https://github.com/Ahmad-Hazrati/django-event)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>

## Credits 
### Content 
- The idea of the project and most of the contents were taken from P4 walkthrough project. 
- The other contents are fictitious.

### Media
- The site logo image is taken from the [Freepik](https://www.freepik.com/) and the other site images are taken from [Pexels](https://www.pexels.com/).

### Code
- The code used for most parts of the website is taken from the [Django Blog Webinar](https://www.youtube.com/watch?v=YH--VobIA8c).
- The code to add pagination and search functionality to the app are taken from [Codemy's tutorial](https://www.youtube.com/watch?v=HHx3tTQWUx0&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy).
- The code used for event registeration is taken from [Dennis Ivy's Github](https://github.com/divanov11/codebattles.dev).
- The code to create the profile page is taken from [Dee-McG's tutorial](https://github.com/Dee-McG/Recipe-Tutorial/tree/main).
- The code used to create the category page is written with the support of mentor.

## Acknowledgements
- Thanks to my Code Institute mentor Mr. Aleksei Konovalov for his guidance, insight, and constant confidence boost to help me in the right direction.
- Thanks to Code Institute for material and support (Tutor Assistance), Slack Community, and other valuable online resources.
<br><br>
<a href="#contents">BACK TO CONTENTS 🔼</a>