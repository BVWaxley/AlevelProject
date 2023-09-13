""" Module sets up the database tables using SQLAlchemy"""

# tk_sql_app/db/models.py

from sqlalchemy import (
    Column, ForeignKey, ForeignKeyConstraint, Table, UniqueConstraint, event,
    Boolean, Date, Integer, Text, String
)
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Sets up a link table with activity_id and person_id as foreign keys
# Base.metadata is a container object that keeps together many different features of a database

training_contacts = Table('training_contacts',
                         Base.metadata,
                         Column('id', Integer, primary_key=True),
                         Column('training_id', ForeignKey('training.id')),
                         Column('contact_id', ForeignKey('contact.id')),
                         )

country_stafftype = Table('country_stafftype',
                          Base.metadata,
                          Column('id', Integer, primary_key=True),
                          Column('country_id', ForeignKey('country.id')),
                          Column('stafftype_id', ForeignKey('stafftype.id'))
                          )


class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    phonenum = Column(String)
    email = Column(String)
    schoolemail = Column(String)
    position = Column(String)
    employdate = Column(Date)
    notes = Column(Text)
    stafftype_id = Column(ForeignKey('stafftype.id'))
    country_id = Column(ForeignKey('country.id'))
    country_stafftype_id = Column(ForeignKey('country_stafftype.id'))
    training = relationship("Training",
                            secondary="staff_training",
                            back_populates="members")
    prerequisites = relationship("Prerequisite",
                                 secondary="staff_prerequisites",
                                 back_populates="staff")




class Training(Base):
    __tablename__ = 'training'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    timeperiod = Column(Integer)
    description = Column(Text)
    members = relationship("Staff",
                           secondary="staff_training",
                           back_populates="training")
    contacts = relationship("Contact",
                            secondary=training_contacts,
                            back_populates="training")




class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phonenum = Column(String)
    email = Column(String)
    website = Column(String)
    training = relationship("Training",
                            secondary=training_contacts,
                            back_populates='contacts')



class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    stafftype = relationship("StaffType",
                             secondary=country_stafftype,
                             back_populates='country')


class StaffType(Base):
    __tablename__ = 'stafftype'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country = relationship("Country",
                           secondary=country_stafftype,
                           back_populates='stafftype')


class Prerequisite(Base):
    __tablename__ = 'prerequisite'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    staff = relationship("Staff",
                         secondary="staff_prerequisites",
                         back_populates='prerequisites')


class Staff_Prerequisites(Base):
    __tablename__ = 'staff_prerequisites'
    id = Column(Integer, primary_key=True)
    staff_id = Column('staff_id', ForeignKey('staff.id'))
    prerequisite_id = Column('prerequisite_id', ForeignKey('prerequisite.id'))
    completed = Column('completed', Boolean)
    confirmationDate = Column('confirmationDate', String)
    confirmedBy = Column('confirmedBy', String)
    extra = Column('extra', String)


class Staff_Training(Base):
    __tablename__ = 'staff_training'
    id = Column(Integer, primary_key=True)
    staff_id = Column('staff_id', ForeignKey('staff.id'))
    training_id = Column('training_id', ForeignKey('training.id'))
    date = Column('date', Date)
