from flask import Flask
# import os
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from dotenv import load_dotenv

# from secrets_manager import get_secret

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    return 'Hello world! How are you?'


# db_config = get_secret('aws-ecs-demo-db-credentials', region_name='us-east-1')

# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f'postgresql+psycopg2://{db_config["POSTGRES_USER"]}:' +
#     f'{db_config["POSTGRES_PW"]}@' +
#     f'{db_config["POSTGRES_HOST"]}/' +
#     f'{db_config["POSTGRES_DB"]}'
# )

# load_dotenv()

# app.config['SQLALCHEMY_DATABASE_URI'] = (
#     f'postgresql+psycopg2://{os.getenv("POSTGRES_USER")}:' +
#     f'{os.getenv("POSTGRES_PW")}@' +
#     f'{os.getenv("POSTGRES_HOST")}/' +
#     f'{os.getenv("POSTGRES_DB")}'
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
#     if transactions:
#         return '\n'.join([str(transaction) for transaction in transactions])
#     else:
#         return 'No transactions, yet!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
