from sqlalchemy import Column , Integer , String , Text
from database import Base

class Blog(Base):

    __tablename__ = "blogdb"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    content = Column(Text)

    
