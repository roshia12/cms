from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import string, inter, text, data
class Base (DeclarativeBase):
    pass
class Task(Base):
    __tablename__="tasks"
id:Mapped[int]=Mapped_column(integer, primary_key=True)
title:Mapped[str]=Mapped_column(string(200),nullable=False)
description:Mapped[str]=Mapped_column(Text, nullable=False)
priority:Mapped[str]=Mapped_column(string(20),default="Medium")
status: Mapped[str]=Mapped_column (String(20),default="pending")
deadline:Mapped[str]=Mapped_column(Date, naullable=True)