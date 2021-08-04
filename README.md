# Zendesk Coding Challenge

Hello, below you will find instructions to use my submission of the Zendesk Ticket Viewer. Thank you!

# Install
 1. Download all files
 2. Keep files in this structure
 
 ![Screen Shot 2021-08-04 at 1 08 08 AM](https://user-images.githubusercontent.com/63125608/128125221-9e017f4b-e53a-49e0-a3aa-467605830eab.png)

 4. Make sure requests, bottle, and boddle, python are all installed
 - for python: http://www.python.org/download/
 - pip install bottle
 - pip install requests
 - pip install boddle

Bottle will help in creating the local host. used for fast web service. Requests will help in making the API calls and Boddle will help in running unit tests for the bottle functionalities.

# Set Up
1. Wherever you see {subdomain} in app.py replace with your subdomain. Same with user and pw. Please change those with your username and password.
2. In the command line submit "$ python app.py" and it will initiate the local host. Then paste in http://localhost:8080/get_tickets to your browser after seeing "Listening on https://localhost:8080/". The page will load up in a few seconds.

# Views
All ticket view:

You will at first see the first page with 25 tickets. You may scroll to the bottom and click on a different page number or click on any ticket ID you'd like. **Click on ID of ticket to see the single view.**

<img width="1352" alt="Screen Shot 2021-08-03 at 4 20 10 PM" src="https://user-images.githubusercontent.com/63125608/128080685-bff4b86b-464d-419e-83dc-78e6ab6072a7.png">

Single ticket view:

Once you click on a ticket ID you will be taken to another page with info on that ticket you selected. The top is the subject line, under that is the status, then below that are the Requester ID and Date. Finally the description of that ticket.

<img width="662" alt="Screen Shot 2021-08-03 at 4 21 06 PM" src="https://user-images.githubusercontent.com/63125608/128080807-44ffab5f-b986-44f9-9ddc-89c2d3b16d46.png">

Once you are ready to leave, you may click on "Return to Tickets". From here you can continue to page to another set of tickets and click on other ticket IDs to see their single view.

# Testing

In order to test just run '$ python tests.py' in your terminal out of the folder

# Misc

1. If you termiante the local host session, and want to start back up again, make sure you use the same starting link http://localhost:8080/get_tickets when initiating a new local host session
