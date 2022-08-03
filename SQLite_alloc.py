from flask_sqlalchemy import SQLAlchemy
from flask import Flask




db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(64), nullable=False)
    LastName = db.Column(db.String(64), nullable=False)
    Email = db.Column(db.String(11), nullable=False)

    def __init__(self, FirstName, LastName, Email):
       
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email

