""" Database Queries"""
import os
import pathlib
from datetime import *
from dateutil.relativedelta import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tk_sql_app.settings import ROOT_DIR
from tk_sql_app.db import models as m


def establish_path():
    # establishes path to database
    sql_path = pathlib.Path(ROOT_DIR).joinpath('var', 'db.sqlite')
    exists = True
    # changes exists to False if database is not yet established
    if not (os.path.exists(sql_path)):
        exists = False
    engine = create_engine(f'sqlite:///{pathlib.Path(sql_path)}', echo=True)
    m.Base.metadata.create_all(engine)
    # returns session and whether database yet exists in case things need to be established
    return sessionmaker(bind=engine), exists


# create functions to add records to tables


def create_staff(session, name, address=None, phonenum=None, email=None, schoolemail=None, position=None, employdate=None, notes=None,
                 stafftype_id=None, country_id=None, country_stafftype_id=None):
    new_staff = m.Staff(name=name, address=address, phonenum=phonenum, email=email, schoolemail=schoolemail, position=position,
                        employdate=employdate, notes=notes, stafftype_id=stafftype_id, country_id=country_id,
                        country_stafftype_id=country_stafftype_id)
    session.add(new_staff)
    session.commit()
    if country_stafftype_id == 1:
        add_staff_prerequisites(session, [new_staff.id], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    elif country_stafftype_id == 2:
        add_staff_prerequisites(session, [new_staff.id], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    elif country_stafftype_id == 3:
        add_staff_prerequisites(session, [new_staff.id], [10, 1, 2, 3, 5, 7, 8, 9])
    elif country_stafftype_id == 4:
        add_staff_prerequisites(session, [new_staff.id], [10, 11, 1, 2, 3, 12, 8, 9])
    elif country_stafftype_id == 5:
        add_staff_prerequisites(session, [new_staff.id], [12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    elif country_stafftype_id == 6:
        add_staff_prerequisites(session, [new_staff.id], [12, 10, 13, 14, 15, 1, 2, 3])

    return new_staff


def create_training(session, name, timeperiod, description=None):
    new_training = m.Training(name=name, timeperiod=timeperiod, description=description)
    session.add(new_training)
    session.commit()
    return new_training


def create_contact(session, name, phonenum=None, email=None, website=None):
    new_contact = m.Contact(name=name, phonenum=phonenum, email=email, website=website)
    session.add(new_contact)
    session.commit()
    return new_contact


def create_country(session, name):
    newcountry = m.Country(name=name)
    session.add(newcountry)
    session.commit()
    return newcountry


def create_stafftype(session, name):
    newstafftype = m.StaffType(name=name)
    session.add(newstafftype)
    session.commit()
    return newstafftype


def create_prerequisite(session, name):
    newprerequisite = m.Prerequisite(name=name)
    session.add(newprerequisite)
    session.commit()
    return newprerequisite


# add functions to add records to relationship tables


def add_country_stafftype(session, countries, stafftypes):
    for country in range(len(countries)):
        for stafftype in range(len(stafftypes)):
            session.execute(m.country_stafftype.insert().values(country_id=country + 1, stafftype_id=stafftype + 1))
            session.commit()


def add_staff_prerequisites(session, staff, prerequisites):
    for staffmember in staff:
        for prerequisite in prerequisites:
            session.add(m.Staff_Prerequisites(staff_id=staffmember, prerequisite_id=prerequisite, completed=False))
    session.commit()


def add_staff_trainings(session, staff, trainings, date=None):
    for staffmember in staff:
        for training in trainings:
            session.add(m.Staff_Training(staff_id=staffmember, training_id=training, date=date))
    session.commit()


def add_training_contacts(session, trainings, contacts):
    for training in trainings:
        for contact in contacts:
            session.execute(m.training_contacts.insert().values(training_id=training, contact_id=contact))
    session.commit()


# Functions to update information


# Updates one of a staff's prerequisite information
def update_staff_prerequisite(session, staff_id, prerequisite_id, completed, confirmationDate=None, confirmedBy=None,
                              extra=None):
    session.query(m.Staff_Prerequisites).filter(m.Staff_Prerequisites.staff_id == staff_id,
                                                m.Staff_Prerequisites.prerequisite_id == prerequisite_id). \
        update({m.Staff_Prerequisites.completed: completed, m.Staff_Prerequisites.confirmationDate: confirmationDate,
                m.Staff_Prerequisites.confirmedBy: confirmedBy, m.Staff_Prerequisites.extra: extra})
    print(f'{staff_id} changes to {confirmationDate}')
    session.commit()


# Qry functions to query from database


# finds all staff given a stafftype
def qry_staff_of_stafftype(session, stafftype_id):
    qry = session.query(m.Staff).filter(m.Staff.stafftype_id == stafftype_id)
    return [row for row in qry.all()]


# finds the record of a staff given the staff_id
def qry_staff_member(session, staff_id):
    qry = session.query(m.Staff).filter(m.Staff.id == staff_id)
    return qry.all()


# finds all staff records given a list of 'staff_id's
def qry_staff_members(session, staff):
    staffList = []
    for staff_id in staff:
        staffList.append(session.query(m.Staff).filter(m.Staff.id == staff_id).all())
    return staffList


# finds all records of a given stafftype with names similar to the search input
def qry_search_stafftype(session, stafftype_id, search):
    qry = session.query(m.Staff).filter(m.Staff.stafftype_id == stafftype_id, m.Staff.name.like("%{}%".format(search)))
    return [row for row in qry.all()]


# finds all prerequisite records given a list of 'prerequisite_id's
def qry_prerequisites(session, prerequisite_ids):
    qry = []
    for prerequisite_id in prerequisite_ids:
        qry.append(session.query(m.Prerequisite).filter(m.Prerequisite.id == prerequisite_id).all())
    return qry


# finds all prerequisites of a staff given the staff_id
def qry_staff_prerequisites(session, staff_id):
    qry = session.query(m.Staff).filter(m.Staff.id == staff_id)[0].prerequisites
    return qry


# finds all staff with prerequisites marked as incomplete
def qry_staff_with_incomplete_prerequisites(session):
    staff = []
    qry = session.query(m.Staff_Prerequisites).filter(m.Staff_Prerequisites.completed == False)
    for row in qry:
        if row.staff_id not in staff:
            staff.append(row.staff_id)
    return qry_staff_members(session, staff)


# finds all incomplete prerequisites of a given staff member
def qry_incomplete_staff_prerequisites(session, staff_id):
    prerequisites = []
    qry = session.query(m.Staff_Prerequisites).filter(m.Staff_Prerequisites.completed == False,
                                                      m.Staff_Prerequisites.staff_id == staff_id)
    return qry


# finds the training record given a training_id
def qry_training(session, training_id):
    qry = session.query(m.Training).filter(m.Training.id == training_id)
    return qry.all()


# finds all trainings of a staff member
def qry_staff_training(session, staff_id):
    qry = session.query(m.Staff).filter(m.Staff.id == staff_id)[0].training
    return qry


# finds the duedate for a staff members training
def qry_staff_training_duedate(session, staff_id, training_id):
    qry = session.query(m.Staff_Training).filter(m.Staff_Training.staff_id == staff_id,
                                                 m.Staff_Training.training_id == training_id)
    qry = qry[-1]
    training = qry_training(session, training_id)
    try:
        duedate = qry.date + relativedelta(months=training[0].timeperiod)
    except:
        duedate = None
    return duedate


# finds all training that must be completed by atleast one staff member before a given timeframe
def qry_upcoming_training(session, timeframe):
    qry = session.query(m.Staff_Training)
    training = []
    for row in qry:
        try:
            if (qry_staff_training_duedate(session, row.staff_id, row.training_id) < (date.today() +
                                                                                      relativedelta(
                                                                                          months=timeframe))) and (
                    qry_training(session, row.training_id) not in training):
                training.append(qry_training(session, row.training_id))
        except:
            pass
    return training


# finds all staff who need to complete a given training by the given timeframe
def qry_staff_with_upcoming_duedate(session, training_id, timeframe):
    staff = []
    qry = session.query(m.Staff_Training).filter(m.Staff_Training.training_id == training_id)
    for row in qry:
        try:
            if (qry_staff_training_duedate(session, row.staff_id, row.training_id) < (date.today() +
                                                                                      relativedelta(
                                                                                          months=timeframe))) and (
                    qry_staff_member(session, row.staff_id) not in staff):
                staff.append(qry_staff_member(session, row.staff_id))
        except:
            pass
    return staff


# finds all trainings which are overdue to be completed
def qry_overdue_training(session):
    return qry_upcoming_training(session, 0)


# finds all staff who have missed the deadline to complete a given training
def qry_staff_with_overdue_training(session, training_id):
    return qry_staff_with_upcoming_duedate(session, training_id, 0)
