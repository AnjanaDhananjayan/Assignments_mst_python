from flask import Flask,render_template,request,session,url_for,redirect
import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='mysqlroot',database='taskmanagementsystem')
mycursor = conn.cursor()


# Create the flask Application
app=Flask(__name__)
app.secret_key='xyzsdfg'
#create a dictionary for login




# Define a route and corresponding view

@app.route('/')
def hello():
    if 'email' in session:
        return render_template("home.html")
    else:
      return render_template('index.html')

# Define a route and corresponding view Home page
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/emp_login', methods=['GET','POST'])
def emp_login():
    if request.method=='POST':
        email=request.form['email']
        pwd=request.form['passwordd']
        mycursor.execute(f"select email,passwordd from register1 where email='{email}'")
        data=mycursor.fetchone()
        if data and pwd == data[1]:
            session['email']=data[0]
            return render_template('home.html')
        else:
            
            return render_template("login.html",error="invalid email id or password")
    return render_template('login.html')
   
       
@app.route('/logout')
def logout():
   
    session.pop("email",None)
    return render_template("index.html")
@app.route('/register')
def reg():
    return render_template('register.html')
@app.route('/registerdtl', methods=['GET','POST'])
def registerdtl():
    if request.method=='POST':
        
        
        id=request.form['id']
        firstname=request.form['fname']
        lastname=request.form['lname']
        email=request.form['email']
        phonenumber=request.form['phonenumber']
        passwordd=request.form['passwordd']
        cpassword=request.form['cpassword']
        mycursor.execute(f"insert into register1 (id,fname,lname,email,phonenumber,passwordd,cpassword) values('{id}','{firstname}','{lastname}','{email}','{phonenumber}','{passwordd}','{cpassword}')")
        
        conn.commit()
        return render_template('login.html')
    return render_template('register.html')


@app.route('/view_task')
def view_task():
    user_id=session['email']
    
    mycursor.execute(f"SELECT id,project,task,description_prj,createdate,duedate,status_prj FROM task1 where user_id='{user_id}'")
    data = mycursor.fetchall()
    if not data:
        message = "No data found."
        return render_template('home.html', msg=message)
    else:
    
        return render_template('view.html',sqldata=data)

@app.route('/update')
def update():
    
    
    return render_template('update.html')

@app.route('/update_task/<int:id>',methods=['GET','POST'])
def update_task(id):
    
    mycursor.execute(f"select * from task1 where id='{id}'")
    data=mycursor.fetchone()
    conn.commit()
    return render_template('update.html',update_data=data)
@app.route('/update_task1/<int:id>',methods=['GET','POST'])
def update_task1(id):
    
     if request.method=='POST':
         
         project=request.form['project']
         task=request.form['task']
         description=request.form['description']
         cdate=request.form['cdate']
         ddate=request.form['ddate']
         status=request.form['status']
         user_id=session['email']
         mycursor.execute(f"update  task1 set id='{id}',project='{project}',task='{task}',description_prj='{description}',createdate='{cdate}',duedate='{ddate}',status_prj='{status}',user_id='{user_id}' where id='{id}'")
         conn.commit()
         return redirect(url_for('home'))
    
@app.route('/delete_task/<int:id>',methods=['GET','POST'])
def delete_task(id):
 
    mycursor.execute(f"delete from task1 where id='{id}'")
    conn.commit()
    return redirect(url_for('home'))
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_task',methods=['GET','POST'])
def create_task():
    if request.method=='POST':
        
        id=request.form['id']
        project=request.form['project']
        task=request.form['task']
        description=request.form['description']
        cdate=request.form['cdate']
        ddate=request.form['ddate']
        status=request.form['status']
        user_id=session['email']
        mycursor.execute(f"insert into task1(id,project,task,description_prj,createdate,duedate,status_prj,user_id) values('{id}','{project}','{task}','{description}','{cdate}','{ddate}','{status}','{user_id}')")
        conn.commit()
        return render_template('create.html',msg="successfully added....")
    return render_template("create.html")
@app.route('/search')
def search():
    return render_template('search.html')
@app.route('/searchresult',methods=['POST'])
def searchresult():
    user_id=session['email']
    status=request.form.get('status')
    query = (f"SELECT * FROM task1 WHERE status_prj='{status}' and user_id='{user_id}'")

    mycursor.execute(query)
    data = mycursor.fetchall()
    if not data:
        message = "No data found."
        return render_template('search.html', msg=message)
    else:
        return render_template('view.html',sqldata=data)
 # Run flask Applicationsss
if __name__=='__main__':
    app.run(debug=True)

    
    
