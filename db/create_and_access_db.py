from tk_sql_app.db.queries import *
from faker import Faker

def populate_database(sess):

    stafftypes=[create_stafftype(sess, "Teacher"),
                create_stafftype(sess, "Support Staff"),
                create_stafftype(sess, "Local Governing Body"),
                create_stafftype(sess, "Volunteer"),
                create_stafftype(sess, "Agency Staff"),
                create_stafftype(sess, "Contractor")]

    countries=[create_country(sess, "UK")]

    add_country_stafftype(sess, countries, stafftypes)

    prerequisites = [create_prerequisite(sess, name="Identity Check"),
                     create_prerequisite(sess, name="Barred List Check"),
                     create_prerequisite(sess, name="DBS Check"),
                     create_prerequisite(sess, name="Prohibited List/GTCE list Check"),
                     create_prerequisite(sess, name="Section 128 Check (for those in management positions)"),
                     create_prerequisite(sess, name="Professional Qualifications Check"),
                     create_prerequisite(sess, name="Right To Work in UK Check"),
                     create_prerequisite(sess, name="Have They Lived or Worked Outside of The UK?"),
                     create_prerequisite(sess, name="EEA sanctions and restrictions check"),
                     create_prerequisite(sess, name="Regulated Activity?"),
                     create_prerequisite(sess, name="Does the volunteer (not in regulated activity) have a written risk assessment(SGF14) in place?"),
                     create_prerequisite(sess, name="Organisation/Company Name"),
                     create_prerequisite(sess, name="Length of Employment"),
                     create_prerequisite(sess, name="Is this adult going to return to the school within 30 days of end date?"),
                     create_prerequisite(sess, name="Identity Confirmed on Arrival")]

    staff = []

    training = [create_training(sess, name="Safeguarding Training Level 2", timeperiod=24),
                create_training(sess, name="DSL Level 3", timeperiod=36),
                create_training(sess, name="Mental Health Lead Training", timeperiod=12),
                create_training(sess, name="Safer Recruitment", timeperiod=6),
                create_training(sess, name="Safeguarding for governors and trustees", timeperiod=12),
                create_training(sess, name="TestTraining", timeperiod=8)]

    # Adding Some Training Dates to Teachers
    add_staff_trainings(sess, [1, 2, 3], [1, 2, 3, 4,5,6], datetime.today())
    # Adding Some Training Dates to Support Staff
    add_staff_trainings(sess, [4, 5, 6], [1, 2, 3], datetime.today())
    # Adding Some Training Dates to Governors
    add_staff_trainings(sess, [7, 8, 9], [1, 4, 5], datetime.today())
    # Adding Some Training Dates to Volunteers
    add_staff_trainings(sess, [10, 11, 12], [2, 3, 5], datetime.today())
    # Adding Some Training Dates to Agency Staff
    add_staff_trainings(sess, [13, 14, 15], [1, 3], datetime.today())
    # Adding Some Training Dates to Contractor
    add_staff_trainings(sess, [16, 17, 18], [1, 2, 3], datetime.today())




