from flask import Flask, render_template, url_for,request,redirect
import csv
app=Flask(__name__)
print(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/<string:any_page>')
def About(any_page):
    return render_template(any_page)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email=data['Email']
        Subject=data['Subject']
        Message=data['Message']
        file = database.write(f'\n{email},{Subject},{Message}')
    return file

def write_to_file_csv(data):
    with open('database2.csv', newline='', mode='a') as database1:
        email=data['Email']
        Subject=data['Subject']
        Message=data['Message']
        file = csv.writer(database1, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([email,Subject,Message])
        return file

@app.route('/Submit_form',methods =['GET','POST'])
def Submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file_csv(data)
        return redirect('/thank_you.html')
    else:
        return "Something went wrong.Please try again"








