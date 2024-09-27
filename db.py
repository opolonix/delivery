from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from typing import List, Literal
from sqlalchemy import Column, Boolean, String, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped

from datetime import datetime

class Сatalog(db.Model):
    __tablename__ = 'catalog'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    product_name: datetime = Column(String)
    price: int # рубли
    quota: int # доступное колличество
    sales: int # продажи

    unit: str # единица измерения и размер порции (нужно только для гарммовок) 100g устанавливается шаг с которым можно делать выбор
