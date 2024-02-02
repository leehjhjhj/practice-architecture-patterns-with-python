from config import Base
from sqlalchemy import Column, BigInteger, DateTime, Boolean, String

class Student(Base):
    __tablename__ = "students"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(16), nullable=False)
    phone_number = Column(String(32), nullable=False)
    nok_phone_number = Column(String(32), nullable=False)
    birthday = Column(DateTime, nullable=False)
    is_quit = Column(Boolean, default=False)
    is_stop = Column(Boolean, default=False)