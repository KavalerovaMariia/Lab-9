#Используя фреймворк Flask с базой данных на основе Flask-SqlAlchemy,
# создайте веб-приложение согласно вашему варианту.
# HTML-страницу следует минимально оформить: задать фон, заголовок и шапку.
#Вариант 4
#Количество шагов с указанием суммарного количества.
#Поля ввода данных: количество шагов, дата. БД: steps, date

from flask import Flask, render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func
app = Flask('Steps counter')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    steps = db.Column(db.Integer)

    def __repr__(self):
        return f'Product{self.id}. {self.date} - {self.steps}'

@app.route('/')
def main():
    products = Product.query.all()
    total_steps = 0
    for i in products:
        total_steps += i.steps if i.steps is not None else 0
    return render_template('index.html', products_list=products, total_steps2=total_steps )

@app.route('/add', methods=['POST'])
def add_product():
    data = request.json
    product = Product(**data)
    db.session.add(product)
    db.session.commit()

    return 'OK'
@app.route('/clear', methods=['delete'])
def clear_data():
    cleary = db.session.query(Product).delete()
    db.session.commit()
    return jsonify({cleary})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



