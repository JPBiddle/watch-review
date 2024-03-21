# Joel's Watch Club

## Code Institute Milestone Project 3

![Portfolio Mockup](reviews/static/assets/img/readme_img/review_mockup.png)
[Click here to view the live project]()

- [Joel's Watch Club](#joels-watch-club)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [UX](#ux)
  - [Features](#features)
  - [Issues and Bugs](#issues-and-bugs)
  - [Technology Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Introduction

Joel's Watch Club is a website designed to build a community around people who have an interest in watches or who have an interest in making a purchase of a watch.

The funcitonality of the website is very simple - designed so the different user types can get what they want as soon as they enter the website.

This was the third Milestone Projects as part of my course at the Code Institute. The main requirements were to make a website that utilised a CRUD database, using flask and SQLAlchemy.

---

## UX

### Demographics

The aim for me is to create a website that appeals to:

- New users
- Current users

### User Stories

#### New Users

- As a new user, I want to be able to read other users reviews as soon as I enter the site. 
- As a new user, I want to be able to create a unique user ID to login with in future.
- As a new user, I want to be able to be able to post a new review after I create my unique user.

#### Current Users

- As a current user, I want to be able to login to access a view of my reviews.
- As a current user, I want to be able to edit or delete my previous reviews as well as post new ones.
- As a current user, I want to be able to view the latest posts on the home page easily.

---

## Development Planes



#### Strategy

The strategy was 

- roles

  - Current users
  - New Users
  - Users looking for new content related to watches

- Demographic

  - Typically aspirational adults, male or female
  - Residing in the UK or USA (English spoken)
  - An interest in watches
  - Looking to view others opinions and share their own

- Psychographic
  - Lifestyles
    - Looking at luxury products for own purchases
    - Potentially a collector of watches
  - Personality and Attitudes
    - Aspirational
    - Open to others ideas and opinions
    - Values community
- Values
  - Interested in watches and the associated qualities (horology, craftsmenship, hand made etc.)
  - Interested in sharing ideas

This website needs to enable the user to:

- Create a unique user with a secure password
- Post reviews with title, subtitle and content
- Edit the same categories of the reviews as stated above (title, subtitle,content)
- Delete unwanted reviews



With this in mind I have produced a short diagram representing the viability of elements versus importance within the site.

<details>

<summary>Viability chart</summary>

![viability](reviews/static/assets/img/readme_img/viability_chart.jpg)

</details>

[Back to top](#joels-watch-club)

---

### Scope

Based on the requirements of the Strategy plane, I have identified two categories.

- Content Requirements:

  - A home page populated with the reviews
  - Ability to open said reviews into their own page to view full content
  - A listed view of users own reviews

- Function Requirements:
  - A sign up and sign in function
  - Log out function
  - Create new review function
  - Edit review function
  - Delete review function

---

### Structure

Based on the information so far, I intend to have a home page with links to everything a user needs to get started. From there, links to sign up will appear, and if the user is signed in a logout button will appear.

Users will not be able to post a review or view the user dashboard without being logged in. 

The intended path will be as follows:

#### Unregistered User

 - View Reviews on home page
 - Add review -> login required, please sign in (sign in redirect)
 - Sign in (No user? sign up here -> Sign Up -> Login (redirect) -> User Dashboard (redirect)

#### Existing User

 - View Reviews on home page
 - Add review -> login required, please sign in (sign in redirect)
 - Sign in -> User Dashboard (redirect)
 - Add review -> User dashboard (redirect after post)
 - User dashboard -> Edit post -> User dashboard (redirect after edit)
 - Log out -> Sign in (redirect)

Below is a map created using Balsamiq - 

<details>

<summary>Site Map</summary>

![Map](reviews/static/assets/img/readme_img/map.png)

</details>

---

### Skeleton

Wireframes were produced using balsamiq. These will showcase the site as intended on mobile and desktop.

<details>

<summary>Wireframes</summary>

<details>

<summary>Home</summary>

![Home](reviews/static/assets/img/readme_img/home.png)

</details>

<details>

<summary>View Review</summary>

![Home](reviews/static/assets/img/readme_img/posted_review.png)

</details>

<details>

<summary>Add Review</summary>

![Home](reviews/static/assets/img/readme_img/add_review.png)

</details>

<details>

<summary>User Dashboard</summary>

![Home](reviews/static/assets/img/readme_img/dashboard.png)

</details>

<details>

<summary>Sign In</summary>

![Home](reviews/static/assets/img/readme_img/sign_in.png)

</details>

<details>

<summary>Sign Up</summary>

![Home](reviews/static/assets/img/readme_img/sign_up.png)

</details>

<details>

<summary>Edit Review</summary>

![Home](reviews/static/assets/img/readme_img/edit_review.png)

</details>

<details>

<summary>About</summary>

![Home](reviews/static/assets/img/readme_img/about.png)

</details>

</details>

---

### Surface

The majority of the colour will be very simple for readability. Background will be white, text will be a very dark grey for subtlety and elegance. 

With the navigation will be white to stand out against the banner images.

I have decided to keep the colour palette simple as the website is heavily focused on what users create.

The delete post button will be red to reflect a warning that this is permanent.

<details>
<summary>Colour Palette</summary>

![viability](reviews/static/assets/img/readme_img/palette.png)

</details>

### Typography

The typography I will use will be from Google Fonts.

The titles will be 'lusitana'. In keeping with this, the rest of the text in the site will be 'lusitana'. Back up font will be 'Georgia'.

Both are uncomplicated and elegant fonts chosen for readability.

### Imagery

All imagery will be from Hodinkee, a watch news site, and urls will be passed from there to simulate user reviews. Credit will be listed at the bottom of ReadMe.

[Back to top](#joels-watch-club)

---

## Features

The website features a set of functions which enable new users to engage with content quickly and allow existing users to return and access their content. Functions are as follows;

---

### Sign Up

Users will be able to choose a unique username to be entered into the database.
The username will be case insensitive. If a username already exists, user will be notified with a flash message. 

Along with a username, user will be able to create a password to be associated with this username. The password will be hashed unpon entering the database and user will be asked to confirm the password before its allowed to be submitted on the create user form.

This is part of the 'Create/C' in CRUD as part of the milestone project.


---

### Sign In

After a user has been created, they will be able to sign in, which will be a simple form that checks if the username entered exists in the database, then checks the password (hashed) against the password associated with this username.

Username and password will be required fields.

If a password is matched, they will be redirected to the user dashboard, where the reviews that are related to this user are displayed and a flash message (success) will be displayed.

---

### Logout

Using flask logout functionality, the logout function will end the user session and redirect them to the sign in page. If flask logout is notused, session.pop will be user, however, flask logout preferred.
Username and password will be required fields.

---

### Add review

A form will be available in the html which will allow the user (if logged in) to create their own review, consisting of a title, subtitle and content, as well as url's for a banner image and content image to display at the bottom of the text content.

All fields will be required for creating a review.

When entered, all content will be added to the review database, along with the date and time when it was entered. This data will be related to the user which created it, which is why only logged in users can access this page.

CKeditor was used to ensure proper formatting when calling review data from the database.

This is also part of the Create part of CRUD for the project.

---

### Delete review

Deleting a review will be a function available on the user dashboard. Login will be required as the page will only display a list of reviews that are related in the database to the current user.

Deleting the review will simply remove all data for the review selected in the database. 

To protect against accidental deletion, a modal will be use to confirm the user wants to delete the post.

A confirm message will let the user know that the review is deleted.

This is the Delete/'D' part of CRUD for the project.

---

### Edit review

Users will be give access to an edit form on the dashboard page, which will lead them to a form which is pre filled with the title, subtitle and content of the review selected.

The user can then edit the content of the review, with all parts of the form required, and re submit this form to the database, replacing the current review data. CKeditor used for same purpose as add review.

A flash message will confirm that the user has edited the review.

This is the Update/'U' part of CRUD for the project.

---

### Home page features

From the home page, users will be given a list of the reviews that have been posted.

These will render the title, subtitle, username and date posted of individual reviews, along the with banner image of the reviews as a background/thumbnail.

The list will be populated with a for loop which runs through the database and presents each review which will be clickable to view the whole content.

Content will display with the latest reviews at the top of the page, which will be filtered using the date of the review in the review database.

Login won't be required to view this.

This is the Read/'R' part of CRUD for the project.

---

### Individual review page features

After clicking on an individual review on the home page, a new page will be loaded which will display the title, subtitle, username and date posted on a banner, which will be the banner image submitted by the user for this particular review, at the top of the page.

Below this will be the review content and at the bottom will be the content image of said review.

Like the home page, login won't be required and this is an additional part of Read for CRUD.

---

### Future features

Due to time constraints I was unable to implement the following functions, however the would make a nice addition to the website:

- A search function to allow users to search through reviews
- A star rating for users to rate, which will also allow filtering of results on home page
- Page pagination, as user reviews on home page will affect loading if there were many reviews.
- Admin page to allow deletion of reviews or users 
- An intergrated image upload to avoid using external urls for images
- User password and username editing
- User profile page accessible by other users to find other reviews by same 'author', user profile image and bio would be part of this

[Back to top](#joels-watch-club)

---

## Issues and Bugs

### Logout not working in workspace

When writing the function for logging out, my workspace (codeanywhere) did not allow this to work in my preview. I contacted Sarah, a tutor at code institute for help as was unsure why this was happening. 

Code anywhere was protecting against Logout and the function had to be renamed to signout to fix this bug.



### Login Required not preventing new user access

A simple issue with the setup of Flask login - the login view was not correctly set up so the @login_required function of flask login was not preventing unregistered access. 



### Multiple of the same user in database

When the login function was initially created, it was not case insensitive, which meant that a user with name 'test' and 'Test' were both accepted.

Case insensitive was added by including .lower onto function for querying database to match with the user create form.

---

## Technologies Used

### Main Languages Used

- HTML5
- CSS
- Jinja
- Python
- Limited use of javascript
- Flask
- SQAlchemy
- CK editor
- Werkzeug security

### Frameworks, Libraries and Programs

- Google Fonts
  - GoogleFonts was used to import the Shizuru and Gloria Hallelujah fonts which were used in this project.
- Font Awesome
  - Font Awesome was used to import the Speaker icon for muting music.
- CodeAnywhere
  - CodeAnywhere was used for writing code, commiting and pushing to GitHub.
- GitHub
  - GitHub was used to store the project.
- Balsamiq
  - Balsamiq was used to create wireframes at the beginning of the project.
- Coolors
  - Coolors was used to create a simple colour palette for the website.
- FreeFormatter
  - FreeFormatter was used to beautify my HTML and CSS code and ensure it was optimal for reading.
- W3C Validator
  - W3C Validator was used at the end of the project to check forany errors written in my code for both HTML and CSS.
- w3Schools
  - Here I learned how to implement audio and change class items such as the background images.
- Flask Login
  - The documentation for Flask login was used for this application
- Werkzeug
  - Documentation used for password hashing
- CKeditor 
  Documentation used for using ckeditor
---

## Testing

Please view full testing document [here](https://github.com/JPBiddle/watch-review/blob/main/TESTING.md)

---

## Deployment

---

This project was developed using CodeAnywhere and was then committed to GitHub using the GitPod terminal.

### Deploying

---

To deploy this page to GitHub Pages from its GitHub repository, the following steps were taken:

- 
- 
- 
- 
- 
- 
- 

---

## Credits

---

- Images and review content from Hodinkee (https://www.hodinkee.com/)
- CleanBlog was used as a theme to start project (https://startbootstrap.com/theme/clean-blog)
- The Thorin and Task Manager projects from Code Institute were invaluable for assisting with creating this project
---

## Acknowledgements

---

- I would like to thank my family and friends for helping with testing and developing the user experience.
- I Would like to thank my mentor, Seun, for their guidance and experience, and my tutors, Oisin and Sarah for helping me with any difficulties with bugs.
- I'd also like to thank the Code Institute Slack community who are always available for help.

[Back to top](#joels-watch-club)

---