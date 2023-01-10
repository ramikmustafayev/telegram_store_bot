from sqlalchemy import Column, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from models.product import Product
from data_base.dbcore import Base


class Order(Base):
   
    __tablename__ = 'orders'

 
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey('product.id'))
    user_id = Column(Integer)

    # для каскадного удаления данных из таблицы
    products = relationship(
        Product,
        backref=backref('orders',
                        uselist=True,
                        cascade='delete,all'))

    def __str__(self):
        return f"{self.quantity} {self.data}"
