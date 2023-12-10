# Raising Minds

### Web Application Preview:
<a href="https://imgur.com/cE2NYzk"><img src="https://i.imgur.com/cE2NYzk.png" title="source: imgur.com" /></a>
  
<!-- ABOUT THE PROJECT -->
# About The Project :School Donation Web Application
The economic crisis in Sri Lanka is a serious challenge for the country's education system. It is important to take steps to mitigate the impact of the crisis on schools and to ensure that all children have access to quality education.The group is determined to make a positive impact by designing a university project tailored specifically to support schools and improve learning opportunities for Sri Lankan children.Our group project is to create a donation website for schools in Sri Lanka. The aim of this website is to enable people worldwide to support these schools by making donations. These 
Funds will be used to provide essential supplies, recruit new teachers, and upgrade the infrastructure required for learning.

Our platform aims to connect compassionate individuals and deserving schools worldwide. Our belief is that education has the power to break down barriers and transform lives. By joining hands with us, you can become a catalyst for change.Donations made through our website go straight towards improving Sri Lankan schools' learning environment. The raised money is used to provide necessary supplies such as textbooks, stationery, laboratory equipment, and technology resources, providing essential tools for academic success.

#### Link:
<a href ="https://raisingminds.pythonanywhere.com/">RaisingMinds</a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#Built-with">Built With</a></li>
    <li><a href="#Features">Features</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#Installation">Installation</a></li>
    <li><a href="#Contributing">Contributing</a></li>
    <li><a href="#License">License</a></li>
    <li><a href="#Contact">Contact</a></li>
  </ol>
</details>

## Built-with

#### These are the frameworks/libraries used in our project.

* HTML
* CSS
* JavaScript [https://www.javascript.com/]
* Bootstrap [https://www.Bootstrap.com]
* Django [https://www.djangoproject.com/]
* python [https://www.python.org/]


<!-- Features -->
## Features

* A user-friendly interface allows donors to easily navigate and make donations.
* Schools can create school posts and access requests to administrators to approve posts.
* Users can display details about schools via school profiles. 
* Information pages about participating schools and their funding needs
* Admin panel to manage school profiles, user profiles, donations, and view posts
* responsive design for a seamless user experience on various devices.

## Prerequisites

Make sure you have the following software installed before setting up the project:
Python (https://www.python.org/)
Django (https://www.djangoproject.com/)
Web browser (Chrome, Firefox, Safari, etc.)

## Installation

1. Create Virtual Environment
    ```sh
   python -m venv venv
   ```
2. Activate Virtual Environment
   * On Windows
    ```sh
   venv\Scripts\activate
   ```
   * On macOS/Linux
    ```sh
   source venv\bin\activate
   ```
3. Clone the repository to your local machine:
   ```sh
   https://github.com/Coding-Hamsters/RaisingMinds
   ```
4. Find path of Requirement.txt file:
    ```sh
   RaisingMinds/RaisingMinds
   ```
5. Use to following command to install dependencies:
    ```sh
   pip install -r requirements.txt
   ```
6. Install PostgreSQL and Go to the pgadmin and create the database as 'RaisingMinds'

7. Find the location of settings.py
   ```sh
   RaisingMinds/RaisingMinds/RaisingMinds/Settings.py
   ```
8. Update django settings:
   In your Django project's settings('settings.py'),update the 'DATABASES' configuration to use 
   postgreSQL.Repalce 'yourpassword'and Change the USER as 'postgres'.
   
   ```sh
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'RaisingMinds',
        'USER': 'postgres',
        'PASSWORD': 'your password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
   }
    ```
9. Make Migrations:
   ```sh
   python manage.py makemigrations
   ```
10. Migrate Database:
   ```sh
   python manage.py migrate
   ```
11. Start the Django development server:
  * find path as RaisingMinds/RaisingMinds
   ```sh
   python manage.py runserver
   ```

<!-- CONTRIBUTING -->

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a request.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

<!-- LICENSE -->
## License

Distributed under the MIT License See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact
Raising Minds: raisingmindsfoundation@gmail.com

Project Link: [https://github.com/Coding-Hamsters/RaisingMinds]



