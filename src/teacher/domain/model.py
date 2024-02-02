from config import Base
from sqlalchemy import Column, BigInteger, String, Enum
import enum

class Subject(enum.Enum):
    UNDEFINED = "미정"
    MATH = "수학"
    ENGLISH = "영어"

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(16), nullable=False)
    phone_number = Column(String(32), nullable=False)
    subject = Column(Enum(Subject), nullable=False, default=Subject.UNDEFINED)