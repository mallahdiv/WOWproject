#                                                          WOW PROJECT
#                                                        JUSTICE LEAGUE 
#                                      By Kevin Harper, Darron McIntyre, Mallah-Divine Mallah


import sqlalchemy

from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base







app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://justiceleague:wowproject@localhost/officerDB'

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