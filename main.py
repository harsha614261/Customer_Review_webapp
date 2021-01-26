from flask import Flask,jsonify,abort,render_template
from flask_restful import Resource,Api,request
from flask_httpauth import HTTPBasicAuth
from flask_wtf import FlaskForm
from wtforms import Form,TextField,TextAreaField,validators,StringField,SubmitField
app=Flask(__name__)
app.config['SECRET_KEY']="LongAndRandomSecretKey"
class Review_form(FlaskForm):
    Name=StringField('Name:',validators=[validators.DataRequired()])
    Product=StringField('Product Name:',validators=[validators.DataRequired()])
    Review=StringField('Review:',validators=[validators.DataRequired()])
    Submit=SubmitField('Submit')
@app.route('/',methods=('GET','POST'))
def index1():
    form1=Review_form()
    #if form1.validate_on_submit():
        #return "<h3>Name:-{}. Product:-{}.  Review:-{}".format(form1.Name.data,form1.Product.data,form1.Review.data)
    if form1.is_submitted():
        Name=request.form['Name']
        Product=request.form['Product']
        Review=request.form['Review']
        result={}
        result["Name"] = Name
        result["Product"]=Product
        result["Review"]=Review
        return render_template('review.html',result=result)
    return render_template('index1.html',form=form1)
if (__name__)=="__main__":
    app.run(debug=True)