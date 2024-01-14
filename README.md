# **_Bakers Hub - Project Portfolio 4 - Full Stack_**

Bakers Hub is a dynamic online platform that serves as a community hub for baking enthusiasts and professionals. This project is designed to provide a comprehensive experience for users, offering both a user-friendly front-end for accessing and sharing baking recipes and a robust back-end management system for contributors and administrators. I wanted to keep this application very simple and sleek, with room for improvement, I wanted the application to be purely about the baking and not about anything flashy.

This is for the real bakers and for aspiring!

You can view the live site here - <a href="https://bakershub-2af44a4fc0e7.herokuapp.com/" target="_blank" rel="noopener">Bakers Hub</a>

# Contents

* [**Objective**](<#objective>)
* [**User Experience UX**](<#user-experience-ux>)
    * [User Stories](<#user-stories>)
    * [Design Prototype](<#design-prototype>)
    * [Site Structure](<#site-structure>)
    * [Design Choices](<#design-choices>)
    *  [Typography](<#typography>)
    *  [Colour Scheme](<#colour-scheme>)
    * [Project Management](<#project-management>)
* [**Existing Features (Site User)**](<#existing-features-for-site-user>)
    * [Site Navigation Bar](<#site-responsive-navigation-bar>)
    * [Article](<#article>)
    * [Article Details](<#article-details>)
    * [Footer](<#footer>)
    * [Sign Up](<#sign-up>)
    * [Login](<#login>)
    * [Like](<#like>)
    * [Comment](<#comment>)
    * [404 & 500 Pages](<#404-and-500-error-pages>)
* [**Existing Existing Features (Staff Member)**](<#existing-features-for-staff-member>)
    * [Articles](<#Articless>)
    * [Comments](<#comments>)
    * [Likes](<#likes>)
    * [Accounts](<#accounts>)
* [**Future Features**](<#future-features>)
    * [Article Creation](<#article-creation>)
    * [Gallery](<#gallery>)
    * [User Profile Page](<#user-profile-page>)
* [**Technologies Used**](<#technologies-used>)
* [**Python Packages**](<#python-packages>)
* [**Bugs and Fixes**](<#bugs-and-fixes>)
* [**Testing**](<#testing>)
* [**Deployment To Heroku**](<#deployment-to-heroku>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
*  [**Acknowledgments**](<#acknowledgements>)

# Objective

For my fourth project, I aim to develop a practical platform for a baking community, showcasing my proficiency in various technologies. The primary goal is to create an authentic and user-friendly website that can be seamlessly applied in a real-world context. This project will serve as a testament to my expertise in HTML, CSS, JavaScript, Python, and the Django Framework, highlighting attention to detail testing practices throughout the development process.

[Back to top](<#contents>)

# User Experience (UX)

## User Stories

### Site User

|  | | |
|:-------:|:--------|:--------|
| As a Site User | I can view a list of posts so that I can select one to read | &check; |
| As a Site User | I can click on a post so that I can read the full text | &check; |
| As a Site User | I can view the number of likes on each post so that I can see which is the most popular or viral | &check; |
| As a Site User | I can view comments on an individual post so that I can read the conversation | &check; |
| As a Site User | I can register an account so that I can comment and like | &check; |
| As a Site User | I can leave comments on a post so that I can be involved in the conversation | &check; |
| As a Site User | I can like or unlike a post so that I can interact with the content| &check; |

### Site Admin

|  | | |
|:-------:|:--------|:--------|
| As a Site Admin | I can view the number of likes on each post so that I can see which is the most popular or viral | &check; |
| As a Site Admin | I can view comments on an individual post so that I can read the conversation | &check; |
| As a Site Admin | I can create, read, update and delete posts so that I can manage my blog content| &check; |
| As a Site Admin | I can create draft posts so that I can finish writing the content later| &check; |
| As a Site Admin | I can approve or disapprove comments so that I can filter out objectionable comments | &check; |

## Design Prototype

The design wireframes were created using [Figma](https://www.figma.com/). I created a very basic wire frame as I knew that I didn't wannt the webpage to be too complicated, I wanted the focus to just be on recipes and I wanted it to be accessable for all- complicated webpages reduce accessibility and I highly wanted to avoid this. This is an extremely important part of the design process as it allows me to understand what components I want to add where.<br /><br />


![Figma](images/home%20wire.png)
![Figma](images/detail%20wire.png)
![Figma](images/sign%20in%20wire.png)
![Figma](images/sign%20up%20wire.png)

[Back to top](<#contents>)

## Site Structure

* Main User Website
    * Home, Sign Up, Article Detail, Login.
    * Accessible, simple and cohesive design.
    * Simple, easy viewing of different recipes.
    * Interaction is easy with just liking and commenting- no overstimulation.

* Admin
    * Functionality to manage and add to articles, comments and accounts.
