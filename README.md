# WOWproject

The Justice League WOW Project was birthed in the spirit of transparency between the community and law enforcement.This project currently allows users to search our database for civilian complaints against police officers in New York City. We want communities to be able to research what type of officers are patroling their communites. Is the officer an asset to the community or a liability. The project will develop over time and to have information on the Neighborhood Coordination Officers(NCOs) that are assigned to a neighborhood to serve as a medium between the police and the community. In further development stages the app will also have the command structure and contact information for the local precincts.\

Technologies used:\
Backend:\
    python\ 
    Flask framework\ 
    PostgreSQl for database storage and queries.\
Frontend:\
    HTML\ 
    CSS\
    Javascript\




Funtionality:\
    The app allows a user to search in the search bar an officer's last name or badge # to find results.
    If you don't know how to spell the exact name of an officer, you can type any combination of letters in the search box and it will pull back a list of officers that match those sequence of letters in their last name.



    There is two ways to run our web application:\
        First:\
         -go to https://jtcfinalproject1.herokuapp.com/ and you can access the project live on the web.\\ 

        Second:\
          -Download our project from github and unzip files.\ 

          Make sure you have python 3.9 or later installed.\ 
          pip install flask\
          pip install flask-sqlAlchemy\
          pip install psycopg2-binary\
          pip install sqlAlchemy\

          The database we are using is postgreSQL and it was deployed on a AWS RDS database to allow users to access the data from any location.\\ 

          To run the file go to directory of the application.py file and run as python file in terminal: python application.py or python3 application.py (whichever applies for your machine)









