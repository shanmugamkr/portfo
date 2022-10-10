#-------------------------------------------------------------------
# Section - 282 - Portfolio-1 
# HTML Templates - http://www.mashup-template.com/preview.html?template=univers
# From now on .html ,.js , .css will carry the same prefix as serverX.py ( this is for my use only) - example index3.html , server3.py,style.css , script3.js
#1.Go to the Website : http://www.mashup-template.com/preview.html?template=univers
#2.Download the HTML Content as Zip file
#3.Unzip and remove unwanted unwanted html files
#4.Create a NEW FOLDER as PORTFOLIO_1 in D Drive
#5.Set the Flask settings
#6.Move the HMTL files from zip to portfolio_1 TEMPLATES folder
#7.Move the JS,CSS and other files to from zip to portfolio_1 STATIC folder
#8.Update the reference locations in  index.html (add ./static)
#9GET 
#	-Sending the information through the URL is done by GET
#POST
#	-Sending the information other than URL is by POST
#10.Store the data in a mongo DB database -To be looked into
#11.Deploy using pythonanywere website
#-------------------------------------------------------------------

from flask import Flask , render_template, url_for,request,redirect
import os
import csv

app = Flask(__name__)    

@app.route('/') 
def my_home(): 
    return render_template('./index.html') 

@app.route('/<string:page_name>') # Dynamic URL Routing for HTML Pages
def html_page(page_name): 
    return render_template(page_name,name = ' Shanmugam ' , mystring = ' Python Developer') 

def write_to_csv(data):
    #path = 'C:/Users/shanmugam.renganatha/Documents/D Drive/Python/4_ZTM_Python_Developer/19_Web_Development/Portfolio_1/database.csv'
    with open('database.csv' ,newline ='',mode = 'a') as myfile2:
        #with open(path ,mode = 'a') as myfile1:
        #print(data)
        email   = data['email']
        subject = data['subject']
        message = data['message']
        print(email)
        #print(subject)
        #print(message)
        csv_writer = csv.writer(myfile2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #print(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save it to DB'
    else:
        return 'Something Went Wrong , Try Again'


  