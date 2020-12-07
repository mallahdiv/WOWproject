#                                                          WOW PROJECT
#                                                        JUSTICE LEAGUE 
#                                      By Kevin Harper, Darron McIntyre, Mallah-Divine Mallah


from flask import Flask, request,render_template


app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def home():
    return render_template('home.html')


# this allows the python file to run
if __name__ == "__main__":
    app.run()
