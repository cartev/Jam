# Jam
Personal Website 
/ Personal Music Catalogue 
/ Django App for Recommending New Music

### Deploying Project Locally

After cloning and prior to starting the Django Development Server, you must first install the required dependencies using the command: 

`(myproject_env)$ pip install -r requirements.txt`

To start the Django Development Server run command:

`(myproject_env)$ python3 manage.py runserver`

  **Note:**
  Parts of this project are dependent on running the server in Python 3 (which is what I have defined in my runtime.txt file) instead of 2.7, particularly, in pitchfork_api.py, which uses an imported package named `pitchfork` that does not work with Python 2.*. You may find more about the issues involving that particular package [here](https://github.com/michalczaplinski/pitchfork).

In your browser of choice, visit URL: http://127.0.0.1:8000/time/

### Extraneous yet Important details about the project outside this repo

I have excluded all of my static files from this repo and they only exist locally on my computer and hosted on my [website](http://www.evancarter.me) which is deployed on Heroku.

I have also excluded my SQLite database binary files, which contain all the existing tables and entry rows necessary to fully see the functionality of this application such as serving specific content of individual album reviews, album covers, and (at some point soon) profile details.

The purpose of these files here are to 1) first and foremost serve my version control needs 2) show the architecture and implementation of Django Framework features I have used and be of use to anyone to explore.

### On the Topic of UI / UX used in this project

I am in the process of switching & adding components of my front end, the “View” part of the MVC design of my project. (Not to be confused with Django’s definition of Views, which refers to the “Controller” component of MVC design patterns). 

Django provides in its framework for placing and structuring Model data into Views, Html Files, and Templates through its features such as Template Tags and Template Variables, which I have been using for the most part when it came to dynamically providing specific content on pages, eg. feature pages. After having some recent exposure to React and testing out some of their tutorials, I have decided to migrate some of my front end development to the React Framework. (Which, if you are curious enough, examples, downloads, and tutorials for React.js can be found on [Facebook’s React Github Page](https://github.com/reactjs/react-tutorial)).

My Two cents on Django’s Front End Framework vs using React. React is incredibly intuitive and matches many ideas Django has implemented as well, such as mixing in special syntaxes in HTML files that mimic behaviors of a standard coding language many programmers use daily, which act as a way for 1. pushing data into views and 2. effectively rendering data systematically in HTML elements. But that is where React has an edge, the syntax is standard, where Django’s Framework is unique. Additionally, I think React does a better at representing the composition of how HTML elements are structured and gives understanding of DOM trees to users, an topic Django is silent on. Finally, it is, as its name suggest, is reactive to changes in the Data Model and displays such changes naturally, without extra effort from a coder or user (as far as I know, Django does not have any framework for this and front end data changes / updates are user dependent — and ultimately come from the backend anyway).

Obviously, here I will be using Django and React together. I do find the hierarchy of Django Templates for HTML files very nice and eliminates a lot of redundancy when it comes to building the *skeleton* of pages and *React picks up very nicely after that*. 