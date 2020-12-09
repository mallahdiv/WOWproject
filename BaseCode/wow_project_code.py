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
    full_name = ' '
    if request.form:
        full_name = request.form.get("officer")
    full_name = (str(full_name))
    first_and_last = full_name.split(' ')
    
    officers = db.session.query(allegations).filter(allegations.first_name == first_and_last[0] and allegations.last_name == first_and_last[1])
    for officer in officers:
        print(officer.first_name, officer.last_name)
    
    return render_template('search.html')


# this allows the python file to run
if __name__ == "__main__":
    app.run()