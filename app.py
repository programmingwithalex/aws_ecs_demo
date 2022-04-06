from flask import Flask
# import os
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# from secrets_manager import get_secret

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    return 'Hello world!'


# db_config = get_secret('aws-ecs-demo-db-cred')

# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f'postgresql+psycopg2://{db_config["username"]}:' +
#     f'{db_config["password"]}@' +
#     f'{db_config["host"]}/' +
#     f'{db_config["db_name"]}'
# )

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# class Transaction(db.Model):
#     __tablename__ = 'transactions'

#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String())
#     last_name = db.Column(db.String())
#     amount = db.Column(db.Float)

#     def __init__(self, first_name: str, last_name: str, amount: float) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.amount = amount

#     def __repr__(self) -> str:
#         return f'{self.first_name} {self.last_name} spent {self.amount}'

# @app.route('/list_db')
# def list_db() -> str:
#     transactions = Transaction.query.all()
#     return '\n'.join([str(transaction) for transaction in transactions])


if __name__ == '__main__':
    app.run(host='0.0.0.0')
