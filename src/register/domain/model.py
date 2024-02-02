from config import Base
from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, Integer
from datetime import datetime

class Register(Base):
    __tablename__ = "registers"

    id = Column(BigInteger, primary_key=True)
    class_id = Column(BigInteger, ForeignKey("classes.id"))
    student_id = Column(BigInteger, ForeignKey("students.id"))

class Payment(Base):
    __tablename__ = "payments"
    id = Column(BigInteger, primary_key=True)
    register_id = Column(BigInteger, ForeignKey("registers.id"))
    payment_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    amount = Column(Integer, nullable=False)
