from sqlalchemy import String ,Column, Integer,Boolean
from data_base.dbcore import Base

class Category(Base):
    __tablename__='category'

    id=Column(Integer,primary_key=True)
    name=Column(String,index=True)
    is_active=Column(Boolean)
  

    def __str__(self) -> str:
        return self.name
