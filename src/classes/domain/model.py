from config import Base
from sqlalchemy import Column, BigInteger, String, Enum, ForeignKey
from teacher.domain.model import Subject

class Class(Base):
    __tablename__ = "classes"

    id = Column(BigInteger, primary_key=True)
    teacher_id = Column(BigInteger, ForeignKey('teachers.id'))
    subject = Column(Enum(Subject), nullable=False)
    name = Column(String(16), nullable=False)
    detail = Column(String(512), nullable=True)