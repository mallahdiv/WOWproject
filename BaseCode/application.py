#                                                          WOW PROJECT
#                                                        JUSTICE LEAGUE 
#                                      By Kevin Harper, Darron McIntyre, Mallah-Divine Mallah


from flask.globals import session
import sqlalchemy
import json

from flask import Flask, request, render_template, redirect 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base







app = Flask(__name__)
app.secret_key = 'wow'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://justiceleague:wowproject@localhost/officerDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




Base = automap_base()
Base.prepare(db.engine,reflect=True)


allegations = Base.classes.allegations




@app.route('/',methods=["GET","POST"])
def home():
    
    if request.form:
        search_input = request.form.get("officer")
        search_input = str(search_input)

        # stores the search_input in a dict called session that is only availabe while the app is running.
        # session can be accessed in any route
        session['search_input'] = search_input
        
        return redirect('/results')
        
        
        
    
    
    
        
        
    return render_template('index.html')

@app.route('/results',methods=["GET","POST"])
def results():
    search_input = session.get('search_input',None)
    unique_officers_list = []
    officer_list = []
    no_results = False
    #search by badge number
    if search_input.isdigit():
        #retrieve data by badge number
        officers = db.session.query(allegations).filter(allegations.shield_no == search_input)
        set_List_Of_officers(officers,officer_list)
        json_names = convert_to_JSON(officer_list)
        #drop duplicate officers by converting to set
        officer_set = set(json_names)
        unique_officers_list = list(officer_set)
        unique_officers_list = convert_to_dict(unique_officers_list)
        
        
    
    #search by officer last name        
    else:
        if search_input == '':
            no_results = True
        else:
            #retrieve data by officer last name using SQL LIKE statement which searches for a specified pattern in the data
            officers = db.session.query(allegations).filter(allegations.last_name.like(search_input.capitalize() + "%"))
            set_List_Of_officers(officers,officer_list)
            json_names = convert_to_JSON(officer_list)
            #drops duplicate officers by converting to set
            officer_set = set(json_names)
            unique_officers_list = list(officer_set)
            unique_officers_list = convert_to_dict(unique_officers_list)

    # determines whether no results were found          
    if len(unique_officers_list) == 0:
        no_results = True
    else:
        no_results = False        
        
    print(no_results)
    
    return render_template('results.html',officers = unique_officers_list,no_results=no_results)


@app.route('/officer_results/<unique_mos_id>',methods=["GET","POST"])
def officer_results(unique_mos_id):
    search_input = session.get('search_input',None)
    officer_allegations = []
    if search_input.isdigit():
        #retrieve data by badge number
        officers = db.session.query(allegations).filter(allegations.shield_no == search_input)
        officer_allegations = get_allegations_info(officers,unique_mos_id)

    else:
        #retrieve data by officer last name using SQL LIKE statement which searches for a specified pattern in the data
        officers = db.session.query(allegations).filter(allegations.last_name.like(search_input.capitalize() + "%"))
        officer_allegations = get_allegations_info(officers,unique_mos_id)
        print(officer_allegations[0]['shield_no'])
                

    

    return render_template('officer_results.html',officer_allegations=officer_allegations)




# helper function that creates a list of dictionaries with officer info in them
def set_List_Of_officers(officers,officer_list):
    for officer in officers:
        officer_info = {'first':officer.first_name,'last':officer.last_name,'command_now':officer.command_now,'rank_now':officer.rank_now,'unique_mos_id':officer.unique_mos_id}
        officer_list.append(officer_info)


#helper function that converts each officer dictionary to JSON in the list   
def convert_to_JSON(officer_list):
    officers = []
    for officer in officer_list:
        officer_string = json.dumps(officer)
        officers.append(officer_string)
    return officers


#helper function that converts each officer JSON back to dictionary in the list
def convert_to_dict(officer_list):
    officers = []
    for officer in officer_list:
        loaded_officer = json.loads(officer)
        officers.append(loaded_officer)
    return officers

# helper function to get allegations for an officer
def get_allegations_info(officers,unique_mos_id):
    officer_allegations = []
    for officer in officers:
        if officer.unique_mos_id == int(unique_mos_id):
            if officer.complainant_gender == 'n/a':
                #change to no data
                allegation_info = {'name':officer.first_name + ' '+officer.last_name,'shield_no':officer.shield_no,'allegation':officer.fado_type +': '+officer.allegation,'complainant_details':'Unknown','ccrb_con':officer.board_disposition}
                officer_allegations.append(allegation_info)
            else:
                if officer.complainant_age_incident == 0:
                    allegation_info = {'name':officer.first_name + ' '+officer.last_name,'shield_no':officer.shield_no,'allegation':officer.fado_type +': '+officer.allegation,'complainant_details':officer.complainant_ethnicity+' '+officer.complainant_gender+', Unknown','ccrb_con':officer.board_disposition}
                    officer_allegations.append(allegation_info)
                else:
                    allegation_info = {'name':officer.first_name + ' '+officer.last_name,'shield_no':officer.shield_no,'allegation':officer.fado_type +': '+officer.allegation,'complainant_details':officer.complainant_ethnicity+' '+officer.complainant_gender+', '+str(officer.complainant_age_incident)+' years old','ccrb_con':officer.board_disposition}
                    officer_allegations.append(allegation_info)
    return officer_allegations





# this allows the python file to run
if __name__ == "__main__":
    app.run()
    