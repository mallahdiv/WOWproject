#                                                          WOW PROJECT
#                                                        JUSTICE LEAGUE 
#                                      By Kevin Harper, Darron McIntyre, Mallah-Divine Mallah


import sqlalchemy

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base







app = Flask(__name__)

#created a awsDB and connected the database to the project

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:wowproject@justiceleague.cr2qomviop3w.us-east-2.rds.amazonaws.com/postgres'

db = SQLAlchemy(app)



Base = automap_base()
Base.prepare(db.engine,reflect=True)


allegations = Base.classes.allegations










@app.route('/',methods=["GET","POST"])
def home():
    officers = db.session.query(allegations).all()
    for officer in officers:
        print(officer.first_name, officer.last_name)
    
    return render_template('search.html')


# this allows the python file to run
if __name__ == "__main__":
    app.run()