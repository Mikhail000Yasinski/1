from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key that anybody could to repeat"

#Класс форм (создаём формы, которые можно будет заполнять, ну или тыкать, если это кнопка...)
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")
    #Другие формы тут: flask-wtf.readthedocs.io

#Функции для различных страничек веб приложения
@app.route("/")

def index():
     #Просто пример заполнения главной страницы, тренируемся обращаться со списками и т.п...
    first_name = "April"
    stuff = "This is bold Text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)
'''ФИЛЬТРЫ ДЛЯ ФОРМАТИРОВАНИЯ ТЕКСТА:
safe
capitalize
lower
upper
title
trim
strings
'''


@app.route("/user/<name>")   

def user(name):
    return render_template("user.html", user_name=name)

@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"), 500   

@app.route('/name', methods=['GET', 'POST'])

def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = '' 
        #Уведомления, штобы было красиво:
        flash("Submitted Successfully")
    return render_template("name.html", name=name, form=form)


if __name__ == "__main__":
    app.run(debug=True)