from peewee import *

db = SqliteDatabase('eldatabase/database_softbank.db')

class User(Model):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    cpf = CharField(unique=True)
    class Meta:
        database = db

class Account(Model):
    email = CharField()
    usuario = CharField()
    saldo = FloatField()
    cpf = CharField(unique=True)
    cartao = CharField(unique=True)
    senha = CharField()

    class Meta:
        database = db