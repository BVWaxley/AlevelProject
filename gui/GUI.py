# importing all the modules needed
from tk_sql_app.db.create_and_access_db import *
import math
import tkinter as tk
from tkinter import ttk
import tkinter.font as f

#Root for the frames
class TSACFS(tk.Tk):
    def __init__(self, sess):
        super().__init__()

        self.title("Global Single Central Record")

        self.sess = sess

        self.TitleFont = f.Font(size=30)

        self.profilesStafftype = 1
        self.search = None
        self.profilesScroll = 0
        self.prerequisitesScroll = 0
        self.trainingScroll = 0

        self.profile_info = []
        self.employ_info = []

        self.profileStaff_id = 1

        self.TrainingProfilesScroll = 0
        self.profileTraining_id = 1

        self.training_id = 1
        self.trainingStaffScroll = 0

        self.StaffToAddList = []
        self.StaffToAddScroll = 0

        self.StaffToAddDateList = []
        self.StaffToAddDateScroll = 0

        self.contact_id = None

        self.incompletePrerequisiteStaff_id = 1

        self.incompleteTraining_id = 1

        self.incompleteTraining_staff = []

        self.timeFrame = 0

        self.upcomingTraining_id = 1

        self.upcomingTraining_staff = []

        self.IncompletePrerequisitesScroll = 0

        self.StaffIncompletePrerequisitesScroll = 0

        self.IncompleteTrainingScroll = 0

        self.StaffIncompleteTrainingScroll = 0

        self.UpcomingTrainingScroll = 0

        self.StaffUpcomingTrainingScroll = 0


        self.frames = {}

        self.frames = {'MenuScreen': MenuScreen(self, self.sess),


                       'StaffProfilesScreen': StaffProfilesScreen(self, self.sess),

                       'StafftypeProfilesScreen': StafftypeProfilesScreen(self, self.sess, self.profilesStafftype, self.profilesScroll, self.search),

                       'CreateStaffProfileInfoScreen': CreateStaffProfileInfoScreen(self, self.sess, self.profilesStafftype),
                       'CreateStaffProfileEmployInfoScreen': CreateStaffProfileEmployInfoScreen(self, self.sess, self.profilesStafftype, self.profile_info),
                       'CreateStaffProfileNotesScreen': CreateStaffProfileNotesScreen(self, self.sess, self.profilesStafftype, self.profile_info, self.employ_info),

                       'IndvStaffProfileScreen': IndvStaffProfileScreen(self, self.sess, self.profileStaff_id, self.profileStaff_id),

                       'StaffInfoScreen': StaffInfoScreen(self, self.sess, self.profileStaff_id),
                       'StaffEmployInfoScreen': StaffEmployInfoScreen(self, self.sess, self.profileStaff_id),
                       'StaffPrerequisitesScreen': StaffPrerequisitesScreen(self, self.sess, self.profileStaff_id, self.prerequisitesScroll),
                       'StaffTrainingScreen': StaffTrainingScreen(self, self.sess, self.profileStaff_id, self.trainingScroll),
                       'StaffNotesScreen': StaffNotesScreen(self, self.sess, self.profileStaff_id),

                       'StaffAddTrainingScreen': StaffAddTrainingScreen(self, self.sess, self.profileStaff_id),
                       'StaffTrainingDatesScreen': StaffTrainingDatesScreen(self, self.sess, self.profileStaff_id, self.profileTraining_id),
                       'AddStaffTrainingDateScreen': AddStaffTrainingDateScreen(self, self.sess, self.profileStaff_id, self.profileTraining_id),


                       'TrainingScreen': TrainingScreen(self, self.sess, self.TrainingProfilesScroll),

                       'CreateTrainingScreen': CreateTrainingScreen(self, self.sess),
                       'TrainingProfileScreen': TrainingProfileScreen(self, self.sess, self.training_id),

                       'TrainingInfoScreen': TrainingInfoScreen(self, self.sess, self.training_id),
                       'TrainingStaffScreen': TrainingStaffScreen(self, self.sess, self.training_id, self.trainingStaffScroll),
                       'TrainingAddStaffScreen': TrainingAddStaffScreen(self, self.sess, self.training_id, self.StaffToAddScroll),
                       'TrainingSelectStaffToAddDateScreen': TrainingSelectStaffToAddDateScreen(self, self.sess, self.training_id, self.StaffToAddDateScroll),
                       'TrainingAddDateScreen': TrainingAddDateScreen(self, self.sess, self.training_id, self.StaffToAddDateList),
                       'TrainingContactsScreen': TrainingContactsScreen(self, self.sess, self.training_id),
                       'TrainingAddContactsScreen': TrainingAddContactsScreen(self, self.sess, self.training_id),

                       'ContactsScreen': ContactsScreen(self, self.sess),
                       'CreateContactScreen': CreateContactScreen(self, self.sess),
                       'ContactProfileScreen': ContactProfileScreen(self, self.sess, self.contact_id),
                       'ContactInfoScreen': ContactInfoScreen(self, self.sess, self.contact_id),
                       'ContactTrainingScreen': ContactTrainingScreen(self, self.sess, self.contact_id),
                       'ContactAddTrainingScreen': ContactAddTrainingScreen(self, self.sess, self.contact_id),


                       'NotificationsScreen': NotificationsScreen(self, self.sess),

                       'IncompletePrerequisitesScreen': IncompletePrerequisitesScreen(self, self.sess, self.IncompletePrerequisitesScroll),
                       'StaffsIncompletePrerequisitesScreen': StaffsIncompletePrerequisitesScreen(self, self.sess, self.incompletePrerequisiteStaff_id, self.StaffIncompletePrerequisitesScroll),

                       'IncompleteTrainingScreen': IncompleteTrainingScreen(self, self.sess, self.IncompleteTrainingScroll),
                       'IncompleteTrainingSelectStaffScreen': IncompleteTrainingSelectStaffScreen(self, self.sess, self.incompleteTraining_id, self.StaffIncompleteTrainingScroll),
                       'IncompleteTrainingAddDateScreen': IncompleteTrainingAddDateScreen(self, self.sess, self.incompleteTraining_id, self.incompleteTraining_staff),

                       'UpcomingTrainingTimeFrameScreen': UpcomingTrainingTimeFrameScreen(self, self.sess),
                       'UpcomingTrainingScreen': UpcomingTrainingScreen(self, self.sess, self.timeFrame, self.UpcomingTrainingScroll),
                       'UpcomingTrainingSelectStaffScreen': UpcomingTrainingSelectStaffScreen(self, self.sess, self.timeFrame, self.upcomingTraining_id, self.StaffUpcomingTrainingScroll),
                       'UpcomingTrainingAddDateScreen': UpcomingTrainingAddDateScreen(self, self.sess, self.upcomingTraining_id, self.upcomingTraining_staff)
                       }

        self.show_frame(self.frames['MenuScreen'])

    def set_profilesStafftype(self, val):
        self.profilesStafftype = val
        self.frames['StafftypeProfilesScreen'] = StafftypeProfilesScreen(self, self.sess, self.profilesStafftype, self.profilesScroll, self.search)
        self.show_frame(self.frames['StafftypeProfilesScreen'])

    def set_search(self, val):
        self.search = val
        self.frames['StafftypeProfilesScreen'] = StafftypeProfilesScreen(self, self.sess, self.profilesStafftype, self.profilesScroll, self.search)

    def reset_search(self):
        self.search = None
        self.frames['StafftypeProfilesScreen'] = StafftypeProfilesScreen(self, self.sess, self.profilesStafftype, self.profilesScroll, self.search)

    def set_profilesScroll(self, val):
        self.profilesScroll = val
        self.frames['StafftypeProfilesScreen'] = StafftypeProfilesScreen(self, self.sess, self.profilesStafftype, self.profilesScroll, self.search)

    def reset_profilesScroll(self):
        self.profilesScroll = 0
        self.frames['StafftypeProfilesScreen'] = StafftypeProfilesScreen(self, self.sess, self.profilesStafftype, self.profilesScroll, self.search)

    def set_prerequisitesScroll(self, val):
        self.prerequisitesScroll = val
        self.frames['StaffPrerequisitesScreen'] = StaffPrerequisitesScreen(self, self.sess, self.profileStaff_id, self.prerequisitesScroll)

    def reset_prerequisitesScroll(self):
        self.prerequisitesScroll = 0
        self.frames['StaffPrerequisitesScreen'] = StaffPrerequisitesScreen(self, self.sess, self.profileStaff_id, self.prerequisitesScroll)

    def reset_TrainingScreen(self):
        self.frames['TrainingScreen'] = TrainingScreen(self, self.sess, self.TrainingProfilesScroll)

    def reset_TrainingProfileScreen(self):
        self.frames['TrainingProfileScreen'] = TrainingProfileScreen(self, self.sess, self.training_id)

    def set_trainingScroll(self, val):
        self.trainingScroll = val
        self.frames['StaffTrainingScreen'] = StaffTrainingScreen(self, self.sess, self.profileStaff_id, self.trainingScroll)

    def reset_trainingScroll(self):
        self.trainingScroll = 0
        self.frames['StaffTrainingScreen'] = StaffTrainingScreen(self, self.sess, self.profileStaff_id, self.trainingScroll)

    def set_stafftypeProfileCreation(self, val):
        self.stafftypeProfileCreation = val
        self.frames['CreateStaffProfileInfoScreen'] = CreateStaffProfileInfoScreen(self, self.sess, self.stafftypeProfileCreation)
        self.show_frame(self.frames['CreateStaffProfileInfoScreen'])

    def set_profileStaff_id(self, val):
        self.profileStaff_id = val
        self.frames['IndvStaffProfileScreen'] = IndvStaffProfileScreen(self, self.sess, self.profilesStafftype, self.profileStaff_id)
        self.frames['StaffInfoScreen'] = StaffInfoScreen(self, self.sess, self.profileStaff_id)
        self.frames['StaffEmployInfoScreen'] = StaffEmployInfoScreen(self, self.sess, self.profileStaff_id)
        self.frames['StaffPrerequisitesScreen'] = StaffPrerequisitesScreen(self, self.sess, self.profileStaff_id, self.prerequisitesScroll)
        self.frames['StaffTrainingScreen'] = StaffTrainingScreen(self, self.sess, self.profileStaff_id, self.trainingScroll)
        self.frames['StaffNotesScreen'] = StaffNotesScreen(self, self.sess, self.profileStaff_id)

    def set_profileTraining_id(self, val):
        self.profileTraining_id = val

    def set_TrainingProfilesScroll(self, val):
        self.TrainingProfilesScroll = val

    def reset_TrainingProfilesScroll(self):
        self.TrainingProfilesScroll = 0

    def set_trainingStaffScroll(self, val):
        self.trainingStaffScroll = val

    def reset_trainingStaffScroll(self):
        self.trainingStaffScroll = 0

    def set_training_id(self, val):
        self.training_id = val

    def reset_TrainingInfoScreen(self):
        self.frames['TrainingInfoScreen'] = TrainingInfoScreen(self, self.sess, self.training_id)

    def reset_TrainingStaffScreen(self):
        self.frames['TrainingStaffScreen'] = TrainingStaffScreen(self, self.sess, self.training_id, self.trainingStaffScroll)

    def reset_TrainingAddStaffScreen(self):
        self.frames['TrainingAddStaffScreen'] = TrainingAddStaffScreen(self, self.sess, self.training_id, self.StaffToAddScroll)

    def reset_TrainingSelectStaffToAddDateScreen(self):
        self.frames['TrainingSelectStaffToAddDateScreen'] = TrainingSelectStaffToAddDateScreen(self, self.sess, self.training_id, self.StaffToAddDateScroll)

    def append_StaffToAddList(self, val):
        self.StaffToAddList.append(val)

    def clear_StaffToAddList(self):
        self.StaffToAddList = []

    def set_StaffToAddScroll(self, val):
        self.StaffToAddScroll = val

    def reset_StaffToAddScroll(self):
        self.StaffToAddScroll = 0

    def set_contact_id(self, val):
        self.contact_id = val

    def set_incompletePrerequisiteStaff_id(self, val):
        self.incompletePrerequisiteStaff_id = val

    def set_incompleteTraining_id(self, val):
        self.incompleteTraining_id = val

    def set_timeFrame(self, val):
        self.timeFrame = val

    def set_upcomingTraining_id(self, val):
        self.upcomingTraining_id = val

    def reset_StafftypeProfilesScreen(self):
        self.frames['StafftypeProfilesScreen'] = StafftypeProfilesScreen(self, self.sess, self.profilesStafftype, self.profilesScroll, self.search)

    def reset_StaffTrainingScreen(self):
        self.frames['StaffTrainingScreen'] = StaffTrainingScreen(self, self.sess, self.profileStaff_id, self.trainingScroll)

    def reset_StaffAddTrainingScreen(self):
        self.frames['StaffAddTrainingScreen'] = StaffAddTrainingScreen(self, self.sess, self.profileStaff_id)

    def reset_StaffTrainingDatesScreen(self):
        self.frames['StaffTrainingDatesScreen'] = StaffTrainingDatesScreen(self, self.sess, self.profileStaff_id, self.profileTraining_id)

    def reset_AddStaffTrainingDateScreen(self):
        self.frames['AddStaffTrainingDateScreen'] = AddStaffTrainingDateScreen(self, self.sess, self.profileStaff_id, self.profileTraining_id)

    def reset_CreateStaffProfileEmployInfoScreen(self):
        self.frames['CreateStaffProfileEmployInfoScreen'] = CreateStaffProfileEmployInfoScreen(self, self.sess, self.profilesStafftype, self.profile_info)

    def reset_CreateStaffProfileNotesScreen(self):
        self.frames['CreateStaffProfileNotesScreen'] = CreateStaffProfileNotesScreen(self, self.sess, self.profilesStafftype, self.profile_info, self.employ_info)

    def append_profile_info(self, newval):
        self.profile_info+=newval

    def append_employ_info(self, newval):
        self.employ_info+=newval

    def append_incompleteTraining_staff(self, newval):
        self.incompleteTraining_staff.append(newval)

    def append_upcomingTraining_staff(self, newval):
        self.upcomingTraining_staff.append(newval)

    def clear_profile_info(self):
        self.profile_info = []

    def clear_employ_info(self):
        self.employ_info = []

    def clear_incompleteTraining_staff(self):
        self.incompleteTraining_staff = []

    def clear_upcomingTraining_staff(self):
        self.upcomingTraining_staff = []

    def refresh_prerequisites_page(self):
        self.frames['StaffPrerequisitesScreen'] = StaffPrerequisitesScreen(self, self.sess, self.profileStaff_id, self.prerequisitesScroll)
        self.show_frame(self.frames['StaffPrerequisitesScreen'])

    def set_StaffToAddDateScroll(self, val):
        self.StaffToAddDateScroll = val

    def reset_StaffToAddDateScroll(self):
        self.StaffToAddDateScroll = 0

    def append_StaffToAddDateList(self, val):
        self.StaffToAddDateList.append(val)

    def clear_StaffToAddDateList(self):
        self.StaffToAddDateList = []

    def reset_TrainingAddDateScreen(self):
        self.frames['TrainingAddDateScreen'] = TrainingAddDateScreen(self, self.sess, self.training_id, self.StaffToAddDateList)

    def reset_IncompletePrerequisitesScreen(self):
        self.frames['IncompletePrerequisitesScreen'] = IncompletePrerequisitesScreen(self, self.sess, self.IncompletePrerequisitesScroll)

    def reset_StaffsIncompletePrerequisitesScreen(self):
        self.frames['StaffsIncompletePrerequisitesScreen'] = StaffsIncompletePrerequisitesScreen(self, self.sess, self.incompletePrerequisiteStaff_id, self.StaffIncompletePrerequisitesScroll)

    def reset_IncompleteTrainingScreen(self):
        self.frames['IncompleteTrainingScreen'] = IncompleteTrainingScreen(self, self.sess, self.IncompleteTrainingScroll)

    def reset_IncompleteTrainingSelectStaffScreen(self):
        self.frames['IncompleteTrainingSelectStaffScreen'] = IncompleteTrainingSelectStaffScreen(self, self.sess, self.incompleteTraining_id, self.StaffIncompleteTrainingScroll)

    def reset_IncompleteTrainingAddDateScreen(self):
        self.frames['IncompleteTrainingAddDateScreen'] = IncompleteTrainingAddDateScreen(self, self.sess, self.incompleteTraining_id, self.incompleteTraining_staff)

    def reset_UpcomingTrainingTimeFrameScreen(self):
        self.frames['UpcomingTrainingTimeFrameScreen'] = UpcomingTrainingTimeFrameScreen(self, self.sess)

    def reset_UpcomingTrainingScreen(self):
        self.frames['UpcomingTrainingScreen'] = UpcomingTrainingScreen(self, self.sess, self.timeFrame, self.UpcomingTrainingScroll)

    def reset_UpcomingTrainingSelectStaffScreen(self):
        self.frames['UpcomingTrainingSelectStaffScreen'] = UpcomingTrainingSelectStaffScreen(self, self.sess, self.timeFrame, self.upcomingTraining_id, self.StaffUpcomingTrainingScroll)

    def reset_UpcomingTrainingAddDateScreen(self):
        self.frames['UpcomingTrainingAddDateScreen'] = UpcomingTrainingAddDateScreen(self, self.sess, self.upcomingTraining_id, self.upcomingTraining_staff)

    def set_IncompletePrerequisitesScroll(self, val):
        self.IncompletePrerequisitesScroll = val

    def set_StaffIncompletePrerequisitesScroll(self, val):
        self.StaffIncompletePrerequisitesScroll = val

    def set_IncompleteTrainingScroll(self, val):
        self.IncompleteTrainingScroll = val

    def set_StaffIncompleteTrainingScroll(self, val):
        self.StaffIncompleteTrainingScroll = val

    def set_StaffAddDateForIncompleteTrainingScroll(self, val):
        self.StaffAddDateForIncompleteTrainingScroll = val

    def set_UpcomingTrainingScroll(self, val):
        self.UpcomingTrainingScroll = val

    def set_StaffUpcomingTrainingScroll(self, val):
        self.StaffUpcomingTrainingScroll = val

    def set_StaffAddDateForUpcomingTrainingScroll(self, val):
        self.StaffAddDateForUpcomingTrainingScroll = val

    def reset_IncompletePrerequisitesScroll(self):
        self.IncompletePrerequisitesScroll = 0

    def reset_StaffIncompletePrerequisitesScroll(self):
        self.StaffIncompletePrerequisitesScroll = 0

    def reset_IncompleteTrainingScroll(self):
        self.IncompleteTrainingScroll = 0

    def reset_StaffIncompleteTrainingScroll(self):
        self.StaffIncompleteTrainingScroll = 0

    def reset_StaffAddDateForIncompleteTrainingScroll(self):
        self.StaffAddDateForIncompleteTrainingScroll = 0

    def reset_UpcomingTrainingScroll(self):
        self.UpcomingTrainingScroll = 0

    def reset_StaffUpcomingTrainingScroll(self):
        self.StaffUpcomingTrainingScroll = 0

    def reset_StaffAddDateForUpcomingTrainingScroll(self):
        self.StaffAddDateForUpcomingTrainingScroll = 0

    def show_frame(self, frame_to_show):
        self.forget_frames()
        frame_to_show.grid(column=0, row=0)

    def forget_frames(self):
        widgets = self.winfo_children()
        # Forgets the frames/ widgets
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.grid_forget()


class MenuScreen(tk.Frame):
    def __init__(self, master, sess):
        super().__init__()
        self.master = master
        self.sess = sess
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.ProfilesPathButton = tk.Button(self, text="Staff Profiles", command=lambda: [self.master.reset_profilesScroll(), self.master.reset_search(), self.master.show_frame(self.master.frames['StaffProfilesScreen'])], font=self.master.TitleFont)
        self.ProfilesPathButton.grid(column=7, columnspan=5, row=3, rowspan=3, sticky='news')

        self.TrainingPathButton = tk.Button(self, text="Trainings", command=lambda: self.master.show_frame(self.master.frames['TrainingScreen']), font=self.master.TitleFont)
        self.TrainingPathButton.grid(column=7, columnspan=5, row=8, rowspan=3, sticky='news')

        self.NotificationsPathButton = tk.Button(self, text="Notifications", command=lambda: self.master.show_frame(self.master.frames['NotificationsScreen']), font=self.master.TitleFont)
        self.NotificationsPathButton.grid(column=7, columnspan=5, row=13, rowspan=3, sticky='news')


class StaffProfilesScreen(tk.Frame):
    def __init__(self, master, sess):
        super().__init__()
        self.master = master
        self.sess = sess
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):

        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu", command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesLabel = tk.Label(self, text="Staff Profiles")
        self.StaffProfilesLabel['font'] = self.master.TitleFont
        self.StaffProfilesLabel.grid(row=1, column=8, columnspan=2, sticky='news')

        self.TeachingStaffPathButton = tk.Button(self, text="Teaching Staff", command=lambda: [self.master.reset_profilesScroll(), self.master.reset_prerequisitesScroll(), self.master.set_profilesStafftype(1)])
        self.TeachingStaffPathButton.grid(column=7, columnspan=4, row=3, sticky='news')

        self.SupportStaffPathButton = tk.Button(self, text="Support Staff", command=lambda: [self.master.reset_profilesScroll(), self.master.reset_prerequisitesScroll(), self.master.set_profilesStafftype(2)])
        self.SupportStaffPathButton.grid(column=7, columnspan=4, row=5, sticky='news')

        self.LGBPathButton = tk.Button(self, text="Local Governing Body", command=lambda: [self.master.reset_profilesScroll(), self.master.reset_prerequisitesScroll(), self.master.set_profilesStafftype(3)])
        self.LGBPathButton.grid(column=7, columnspan=4, row=7, sticky='news')

        self.VolunteersPathButton = tk.Button(self, text="Volunteers", command=lambda: [self.master.reset_profilesScroll(), self.master.reset_prerequisitesScroll(), self.master.set_profilesStafftype(4)])
        self.VolunteersPathButton.grid(column=7, columnspan=4, row=9, sticky='news')

        self.AgencyStaffPathButton = tk.Button(self, text="Agency Staff", command=lambda: [self.master.reset_profilesScroll(), self.master.reset_prerequisitesScroll(), self.master.set_profilesStafftype(5)])
        self.AgencyStaffPathButton.grid(column=7, columnspan=4, row=11, sticky='news')

        self.ContractorsPathButton = tk.Button(self, text="Contractors", command=lambda: [self.master.reset_profilesScroll(), self.master.reset_prerequisitesScroll(), self.master.set_profilesStafftype(6)])
        self.ContractorsPathButton.grid(column=7, columnspan=4, row=13, sticky='news')


class StafftypeProfilesScreen(tk.Frame):
    def __init__(self, master, sess, stafftype, scroll, search):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.sess = sess
        self.stafftype = stafftype
        self.scroll = scroll
        self.search = search
        self.master.clear_profile_info()
        self.master.clear_employ_info()
        self.master.frames['CreateStaffProfileInfoScreen'] = CreateStaffProfileInfoScreen(self.master, self.master.sess, self.master.profilesStafftype)
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu", command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesButton = tk.Button(self, text="Staff Profiles", command=lambda: [self.master.reset_profilesScroll(), self.master.reset_search(), self.master.show_frame(self.master.frames['StaffProfilesScreen'])])
        self.StaffProfilesButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.StafftypeProfilesLabels = [tk.Label(self, text="Teacher Profiles", font=self.master.TitleFont),
                                        tk.Label(self, text="Support Staff Profiles", font=self.master.TitleFont),
                                        tk.Label(self, text="Governor Profiles", font=self.master.TitleFont),
                                        tk.Label(self, text="Volunteer Profiles", font=self.master.TitleFont),
                                        tk.Label(self, text="Agency Staff Profiles", font=self.master.TitleFont),
                                        tk.Label(self, text="Contactor Profiles", font=self.master.TitleFont)]
        self.StafftypeProfilesLabels[self.stafftype-1].grid(row=1, column=8, columnspan=2, sticky='news')

        self.CreateNewProfileButtons = [tk.Button(self, text="Create New Teacher Profile", command=lambda:self.master.set_stafftypeProfileCreation(1)),
                                        tk.Button(self, text="Create New Support Staff Profile", command=lambda:self.master.set_stafftypeProfileCreation(2)),
                                        tk.Button(self, text="Create New Governor Profile", command=lambda:self.master.set_stafftypeProfileCreation(3)),
                                        tk.Button(self, text="Create New Volunteer Profile", command=lambda:self.master.set_stafftypeProfileCreation(4)),
                                        tk.Button(self, text="Create New Agency Staff Profile", command=lambda:self.master.set_stafftypeProfileCreation(5)),
                                        tk.Button(self, text="Create New Contactor Profile", command=lambda:self.master.set_stafftypeProfileCreation(6))]
        self.CreateNewProfileButtons[self.stafftype-1].grid(row=2, column=4, columnspan=2, sticky='news')

        if self.search:
            self.staff = qry_search_stafftype(self.sess, self.stafftype, self.search)
        else:
            self.staff = qry_staff_of_stafftype(self.sess, self.stafftype)

        self.StaffProfileButtons = [tk.Button(self, text="{}".format(staffmember.name), command=lambda id=staffmember.id: [self.master.set_profileStaff_id(id), self.master.reset_trainingScroll(), self.master.show_frame(self.master.frames['IndvStaffProfileScreen'])]) for staffmember in self.staff]

        # algorithm to display all of the staff profile buttons for selected staff type given the value of scroll
        buttonsOnScreen = self.StaffProfileButtons[70 * self.scroll: 70 + (70 * self.scroll)]
        for Staffbutton in range(len(buttonsOnScreen)):
            buttonsOnScreen[Staffbutton].grid(row=(Staffbutton % 10) + 4, column=math.floor(Staffbutton / 10) + 3, sticky='news')

        self.ScrollDownProfilesButton = tk.Button(self, text="Down", command=lambda: [self.master.set_profilesScroll(self.scroll+1), self.master.reset_StafftypeProfilesScreen(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])
        self.ScrollUpProfilesButton = tk.Button(self, text="Up", command=lambda: [self.master.set_profilesScroll(self.scroll-1), self.master.reset_StafftypeProfilesScreen(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])

        if self.scroll < len(self.StaffProfileButtons)/70-1:
            self.ScrollDownProfilesButton.grid(column=10, row=15, sticky="news")

        if self.scroll>0:
            self.ScrollUpProfilesButton.grid(column=10, row=3, sticky="news")

        self.SearchEntry = tk.StringVar(self)
        self.StaffSearchBar = tk.Entry(self, textvariable=self.SearchEntry)
        self.StaffSearchBar.grid(row=2, column=7, columnspan=3, sticky='news')
        self.StaffSearchButton = tk.Button(self, text="Search", command=lambda: [self.submit_search, self.master.set_search(self.SearchEntry.get()), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])
        self.StaffSearchButton.grid(row=2, column=10, sticky='news')

        self.submit_search = lambda entry: self.SearchEntry.set("{}".format(self.SearchEntry.get()))


class CreateStaffProfileInfoScreen(tk.Frame):
    def __init__(self, master, sess, stafftype):
        super().__init__()
        self.master = master
        self.sess = sess
        self.stafftype = stafftype
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self,
                              text="Create {} Profile: Personal Info".format(self.sess.query(m.StaffType).filter(m.StaffType.id==self.stafftype).all()[0].name), font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.nameValue = tk.StringVar(self)
        self.ProfileNameLabel = tk.Label(self, text="Name:")
        self.ProfileName = tk.Entry(self, textvariable=self.nameValue)
        self.ProfileNameLabel.grid(column=5, columnspan=2, row=5, rowspan=2, sticky='nes')
        self.ProfileName.grid(column=8, columnspan=4, row=5, rowspan=2, sticky='news')

        self.addressValue = tk.StringVar(self)
        self.ProfileAddressLabel = tk.Label(self, text="Address:")
        self.ProfileAddress = tk.Entry(self, textvariable=self.addressValue)
        self.ProfileAddressLabel.grid(column=5, columnspan=2, row=7, rowspan=2, sticky='nes')
        self.ProfileAddress.grid(column=8, columnspan=4, row=7, rowspan=2, sticky='news')

        self.phoneNumValue = tk.StringVar(self)
        self.ProfilePhoneNumLabel = tk.Label(self, text="Phone No.:")
        self.ProfilePhoneNum = tk.Entry(self, textvariable=self.phoneNumValue)
        self.ProfilePhoneNumLabel.grid(column=5, columnspan=2, row=9, rowspan=2, sticky='nes')
        self.ProfilePhoneNum.grid(column=8, columnspan=4, row=9, rowspan=2, sticky='news')

        self.EmailValue = tk.StringVar(self)
        self.ProfileEmailLabel = tk.Label(self, text="Email:")
        self.ProfileEmail = tk.Entry(self, textvariable=self.EmailValue)
        self.ProfileEmailLabel.grid(column=5, columnspan=2, row=11, rowspan=2, sticky='nes')
        self.ProfileEmail.grid(column=8, columnspan=4, row=11, rowspan=2, sticky='news')

        self.CancelButton = tk.Button(self, text="Cancel", command=lambda: [self.master.reset_StafftypeProfilesScreen(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])
        self.CancelButton.grid(column=6, row=13, sticky='news')
        self.NextButton = tk.Button(self, text="Next", command=lambda:[self.master.append_profile_info([self.nameValue.get(), self.addressValue.get(), self.phoneNumValue.get(), self.EmailValue.get()]), self.master.reset_CreateStaffProfileEmployInfoScreen(), self.master.show_frame(self.master.frames['CreateStaffProfileEmployInfoScreen'])])
        self.NextButton.grid(column=11, row=13, sticky='news')


class CreateStaffProfileEmployInfoScreen(tk.Frame):
    def __init__(self, master, sess, stafftype, profile_info):
        super().__init__()
        self.master = master
        self.sess = sess
        self.stafftype = stafftype
        self.profile_info = profile_info
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self,
                              text="Create {} Profile: Employment Info".format(
                                  self.sess.query(m.StaffType).filter(m.StaffType.id == self.stafftype).all()[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.PositionValue = tk.StringVar(self)
        self.ProfilePositionLabel = tk.Label(self, text="Position:")
        self.ProfilePosition = tk.Entry(self, textvariable=self.PositionValue)
        self.ProfilePositionLabel.grid(column=5, columnspan=2, row=5, rowspan=2, sticky='nes')
        self.ProfilePosition.grid(column=8, columnspan=4, row=5, rowspan=2, sticky='news')

        self.SchoolEmailValue = tk.StringVar(self)
        self.ProfileSchoolEmailLabel = tk.Label(self, text="School Email:")
        self.ProfileSchoolEmail = tk.Entry(self, textvariable=self.SchoolEmailValue)
        self.ProfileSchoolEmailLabel.grid(column=5, columnspan=2, row=7, rowspan=2, sticky='nes')
        self.ProfileSchoolEmail.grid(column=8, columnspan=4, row=7, rowspan=2, sticky='news')

        self.EmployDateValue = tk.StringVar(self)
        self.ProfileEmployDateLabel = tk.Label(self, text="Date of Employment (YYYY-MM-DD):")
        self.ProfileEmployDate = tk.Entry(self, textvariable=self.EmployDateValue)
        self.ProfileEmployDateLabel.grid(column=5, columnspan=2, row=9, rowspan=2, sticky='nes')
        self.ProfileEmployDate.grid(column=8, columnspan=4, row=9, rowspan=2, sticky='news')

        self.CancelButton = tk.Button(self, text="Cancel",command=lambda: [self.master.reset_StafftypeProfilesScreen(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])
        self.CancelButton.grid(column=6, row=13, sticky='news')
        self.NextButton = tk.Button(self, text="Next", command=lambda: [self.master.append_employ_info([self.PositionValue.get(), self.SchoolEmailValue.get(), self.EmployDateValue.get()]), self.master.reset_CreateStaffProfileNotesScreen(), self.master.show_frame(self.master.frames['CreateStaffProfileNotesScreen'])])
        self.NextButton.grid(column=11, row=13, sticky='news')



class CreateStaffProfileNotesScreen(tk.Frame):
    def __init__(self, master, sess, stafftype, profile_info, employ_info):
        super().__init__()
        self.master = master
        self.sess = sess
        self.stafftype = stafftype
        self.profile_info = profile_info
        self.employ_info = employ_info
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()


    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Create {} Profile: Notes".format(self.sess.query(m.StaffType).filter(m.StaffType.id == self.stafftype).all()[0].name), font=self.master.TitleFont)
        self.Title.grid(row=1, column=6, columnspan=6, sticky='news')

        self.NotesValue = tk.StringVar(self)
        self.ProfileNotesLabel = tk.Label(self, text="Notes:")
        self.ProfileNotes = tk.Entry(self, textvariable=self.NotesValue)
        self.ProfileNotesLabel.grid(column=3, columnspan=2, row=5, sticky='nes')
        self.ProfileNotes.grid(column=4, columnspan=10, row=6, rowspan=10, sticky='news')

        self.CancelButton = tk.Button(self, text="Cancel", command=lambda: [self.master.reset_StafftypeProfilesScreen(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])
        self.CancelButton.grid(column=4, row=16, sticky='news')
        self.DoneButton = tk.Button(self, text="Done", command=lambda: [create_staff(self.sess, self.profile_info[0], self.profile_info[1], self.profile_info[2], self.profile_info[3], self.employ_info[1], self.employ_info[0], datetime.strptime(self.employ_info[2], '%Y-%m-%d'), self.NotesValue.get(), self.stafftype, 1, self.stafftype), self.master.reset_StafftypeProfilesScreen(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])
        self.DoneButton.grid(column=13, row=16, sticky='news')


class IndvStaffProfileScreen(tk.Frame):
    def __init__(self, master, sess, stafftype, staffmember):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.sess = sess
        self.stafftype = stafftype
        self.staffmember = staffmember
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu", command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesButton = tk.Button(self, text="Staff Profiles", command=lambda: [self.master.show_frame(self.master.frames['StaffProfilesScreen'])])
        self.StaffProfilesButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.StafftypeProfilesButton = [tk.Button(self, text="Teacher Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame( self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Support Staff Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame( self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Governor Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame( self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Volunteers Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame( self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Agency Staff Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame( self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Contractor Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame( self.master.frames['StafftypeProfilesScreen'])])]
        self.StafftypeProfilesButton[qry_staff_member(self.sess, self.staffmember)[0].stafftype_id-1].grid(column=0, columnspan=2, row=7, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="{}".format(qry_staff_member(self.sess, self.staffmember)[0].name), font=self.master.TitleFont)
        self.Title.grid(row=1, column=8, columnspan=2, sticky='news')

        self.ProfileInfoButton = tk.Button(self, text="Personal Info", command=lambda: self.master.show_frame(self.master.frames['StaffInfoScreen']))
        self.ProfileInfoButton.grid(column=7, columnspan=4, row=3, rowspan=2, sticky='news')

        self.ProfileEmployInfoButton = tk.Button(self, text="Employment Info", command=lambda: self.master.show_frame(self.master.frames['StaffEmployInfoScreen']))
        self.ProfileEmployInfoButton.grid(column=7, columnspan=4, row=6, rowspan=2, sticky='news')

        self.ProfilePrerequisitesButton = tk.Button(self, text="Checks/ Prerequisites", command=lambda: self.master.show_frame(self.master.frames['StaffPrerequisitesScreen']))
        self.ProfilePrerequisitesButton.grid(column=7, columnspan=4, row=9, rowspan=2, sticky='news')

        self.ProfileTrainingButton = tk.Button(self, text="Training", command=lambda: self.master.show_frame(self.master.frames['StaffTrainingScreen']))
        self.ProfileTrainingButton.grid(column=7, columnspan=4, row=12, rowspan=2, sticky='news')

        self.ProfileNotesButton = tk.Button(self, text="Notes", command=lambda: self.master.show_frame(self.master.frames['StaffNotesScreen']))
        self.ProfileNotesButton.grid(column=7, columnspan=4, row=15, rowspan=2, sticky='news')


class StaffInfoScreen(tk.Frame):
    def __init__(self, master, sess, staffmember):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu", command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesButton = tk.Button(self, text="Staff Profiles", command=lambda: [self.master.show_frame(self.master.frames['StaffProfilesScreen'])])
        self.StaffProfilesButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.StafftypeProfilesButton = [tk.Button(self, text="Teacher Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Support Staff Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Governor Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Volunteers Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Agency Staff Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Contractor Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])]
        self.StafftypeProfilesButton[qry_staff_member(self.sess, self.staffmember)[0].stafftype_id-1].grid(column=0, columnspan=2, row=7, rowspan=2, sticky='news')

        self.IndvStaffProfileButton = tk.Button(self, text="{}".format(qry_staff_member(self.sess, self.staffmember)[0].name), command=lambda: self.master.show_frame(self.master.frames['IndvStaffProfileScreen']))
        self.IndvStaffProfileButton.grid(column=0, columnspan=2, row=9, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="{}'s Personal Info".format(qry_staff_member(self.sess, self.staffmember)[0].name), font=self.master.TitleFont)
        self.Title.grid(row=1, column=8, columnspan=2, sticky='news')

        self.addressValue = tk.StringVar(self)
        self.ProfileAddressLabel = tk.Label(self, text="Address:")
        self.ProfileAddress = tk.Entry(self, textvariable=self.addressValue)
        self.addressValue.set(qry_staff_member(self.sess, self.staffmember)[0].address)
        self.ProfileAddressLabel.grid(column=5, columnspan=2, row=5, rowspan=2, sticky='nes')
        self.ProfileAddress.grid(column=8, columnspan=4, row=5, rowspan=2, sticky='news')

        self.phoneNumValue = tk.StringVar(self)
        self.ProfilePhoneNumLabel = tk.Label(self, text="Phone No.:")
        self.ProfilePhoneNum = tk.Entry(self, textvariable=self.phoneNumValue)
        self.phoneNumValue.set(qry_staff_member(self.sess, self.staffmember)[0].phonenum)
        self.ProfilePhoneNumLabel.grid(column=5, columnspan=2, row=7, rowspan=2, sticky='nes')
        self.ProfilePhoneNum.grid(column=8, columnspan=4, row=7, rowspan=2, sticky='news')

        self.EmailValue = tk.StringVar(self)
        self.ProfileEmailLabel = tk.Label(self, text="Email:")
        self.ProfileEmail = tk.Entry(self, textvariable=self.EmailValue)
        self.EmailValue.set(qry_staff_member(self.sess, self.staffmember)[0].email)
        self.ProfileEmailLabel.grid(column=5, columnspan=2, row=9, rowspan=2, sticky='nes')
        self.ProfileEmail.grid(column=8, columnspan=4, row=9, rowspan=2, sticky='news')


class StaffEmployInfoScreen(tk.Frame):
    def __init__(self, master, sess, staffmember):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesButton = tk.Button(self, text="Staff Profiles", command=lambda: [
            self.master.show_frame(self.master.frames['StaffProfilesScreen'])])
        self.StaffProfilesButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.StafftypeProfilesButton = [tk.Button(self, text="Teacher Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Support Staff Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Governor Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Volunteers Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Agency Staff Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Contractor Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])]
        self.StafftypeProfilesButton[qry_staff_member(self.sess, self.staffmember)[0].stafftype_id - 1].grid(column=0, columnspan=2, row=7, rowspan=2, sticky='news')

        self.IndvStaffProfileButton = tk.Button(self,
                                                text="{}".format(qry_staff_member(self.sess, self.staffmember)[0].name), command=lambda: self.master.show_frame(self.master.frames['IndvStaffProfileScreen']))
        self.IndvStaffProfileButton.grid(column=0, columnspan=2, row=9, rowspan=2, sticky='news')

        self.Title = tk.Label(self,
                              text="{}'s Employment Info".format(qry_staff_member(self.sess, self.staffmember)[0].name), font=self.master.TitleFont)
        self.Title.grid(row=1, column=8, columnspan=2, sticky='news')

        self.PositionValue = tk.StringVar(self)
        self.ProfilePositionLabel = tk.Label(self, text="Position:")
        self.ProfilePosition = tk.Entry(self, textvariable=self.PositionValue)
        self.PositionValue.set(qry_staff_member(self.sess, self.staffmember)[0].position)
        self.ProfilePositionLabel.grid(column=5, columnspan=2, row=5, rowspan=2, sticky='nes')
        self.ProfilePosition.grid(column=8, columnspan=4, row=5, rowspan=2, sticky='news')

        self.SchoolEmailValue = tk.StringVar(self)
        self.ProfileSchoolEmailLabel = tk.Label(self, text="School Email:")
        self.ProfileSchoolEmail = tk.Entry(self, textvariable=self.SchoolEmailValue)
        self.SchoolEmailValue.set(qry_staff_member(self.sess, self.staffmember)[0].schoolemail)
        self.ProfileSchoolEmailLabel.grid(column=5, columnspan=2, row=7, rowspan=2, sticky='nes')
        self.ProfileSchoolEmail.grid(column=8, columnspan=4, row=7, rowspan=2, sticky='news')

        self.EmployDateValue = tk.StringVar(self)
        self.ProfileEmployDateLabel = tk.Label(self, text="Date of Employment:")
        self.ProfileEmployDate = tk.Entry(self, textvariable=self.EmployDateValue)
        self.EmployDateValue.set(qry_staff_member(self.sess, self.staffmember)[0].employdate)
        self.ProfileEmployDateLabel.grid(column=5, columnspan=2, row=9, rowspan=2, sticky='nes')
        self.ProfileEmployDate.grid(column=8, columnspan=4, row=9, rowspan=2, sticky='news')


class StaffPrerequisitesScreen(tk.Frame):
    def __init__(self, master, sess, staffmember, prerequisitesScroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.prerequisitesScroll = prerequisitesScroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesButton = tk.Button(self, text="Staff Profiles", command=lambda: [
            self.master.show_frame(self.master.frames['StaffProfilesScreen'])])
        self.StaffProfilesButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.StafftypeProfilesButton = [tk.Button(self, text="Teacher Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Support Staff Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Governor Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Volunteers Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Agency Staff Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Contractor Profiles", command=lambda: [self.master.reset_prerequisitesScroll(), self.master.show_frame(self.master.frames['StafftypeProfilesScreen'])])]
        self.StafftypeProfilesButton[qry_staff_member(self.sess, self.staffmember)[0].stafftype_id - 1].grid(column=0, columnspan=2, row=7, rowspan=2, sticky='news')

        self.IndvStaffProfileButton = tk.Button(self, text="{}".format(qry_staff_member(self.sess, self.staffmember)[0].name), command=lambda: self.master.show_frame(self.master.frames['IndvStaffProfileScreen']))
        self.IndvStaffProfileButton.grid(column=0, columnspan=2, row=9, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="{}'s Checks/ Prerequisites".format(qry_staff_member(self.sess, self.staffmember)[0].name), font=self.master.TitleFont)
        self.Title.grid(row=1, column=6, columnspan=2, sticky='news')

        self.prerequisitesList = [row for row in self.sess.query(m.Staff_Prerequisites).filter(m.Staff_Prerequisites.staff_id==self.staffmember).all()]
        self.prerequisites_to_show = self.prerequisitesList[self.prerequisitesScroll*5:(self.prerequisitesScroll*5)+5]
        self.prerequisitesWidgetsList = []
        self.ValuesList = []


        for pr in range(len(self.prerequisites_to_show)):
            self.ValuesList.append([tk.IntVar(self), tk.StringVar(self), tk.StringVar(self), tk.StringVar(self)])
            self.ValuesList[pr][0].set(self.prerequisites_to_show[pr].completed)
            self.ValuesList[pr][1].set(self.prerequisites_to_show[pr].confirmationDate)
            self.ValuesList[pr][2].set(self.prerequisites_to_show[pr].confirmedBy)
            self.ValuesList[pr][3].set(self.prerequisites_to_show[pr].extra)
            self.prerequisitesWidgetsList.append([tk.Label(self, text="{}".format(qry_prerequisites(self.sess, [self.prerequisites_to_show[pr].prerequisite_id])[0][0].name)),
                                                  tk.Checkbutton(self, text="Completed?", variable=self.ValuesList[pr][0], onvalue=1, offvalue=0),
                                                  tk.Label(self, text="Date Confirmed:"),
                                                  tk.Entry(self, textvariable=self.ValuesList[pr][1]),
                                                  tk.Label(self, text="Confirmed By:"),
                                                  tk.Entry(self, textvariable=self.ValuesList[pr][2]),
                                                  tk.Label(self, text="Extra Info:"),
                                                  tk.Entry(self, textvariable=self.ValuesList[pr][3]),
                                                  tk.Button(self, text="Confirm", command=lambda x=pr: self.update_staff_prerequisite_function(x))])

            self.prerequisitesWidgetsList[pr][0].grid(column=3, columnspan=10, row=(2*pr)+3, sticky='nsw')
            self.prerequisitesWidgetsList[pr][1].grid(column=3, row=(2*pr)+4, sticky='news')
            self.prerequisitesWidgetsList[pr][2].grid(column=4, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][3].grid(column=5, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][4].grid(column=6, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][5].grid(column=7, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][6].grid(column=8, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][7].grid(column=9, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][8].grid(column=10, row=(2 * pr) + 4, sticky='news')

        self.ScrollDownPrerequisitesButton = tk.Button(self, text="Down", command=lambda: [self.master.set_prerequisitesScroll(self.prerequisitesScroll + 1), self.master.show_frame(self.master.frames['StaffPrerequisitesScreen'])])
        self.ScrollUpPrerequisitesButton = tk.Button(self, text="Up", command=lambda: [self.master.set_prerequisitesScroll(self.prerequisitesScroll - 1), self.master.show_frame(self.master.frames['StaffPrerequisitesScreen'])])

        if self.prerequisitesScroll < len(self.prerequisitesList)/5-1:
            self.ScrollDownPrerequisitesButton.grid(column=10, row=15, sticky="news")

        if self.prerequisitesScroll>0:
            self.ScrollUpPrerequisitesButton.grid(column=10, row=14, sticky="news")

    def update_staff_prerequisite_function(self, pr_ref):
        self.ValuesList[pr_ref][0].set("{}".format(self.ValuesList[pr_ref][0].get()))
        self.ValuesList[pr_ref][1].set("{}".format(self.ValuesList[pr_ref][1].get()))
        self.ValuesList[pr_ref][2].set("{}".format(self.ValuesList[pr_ref][2].get()))
        self.ValuesList[pr_ref][3].set("{}".format(self.ValuesList[pr_ref][3].get()))
        update_staff_prerequisite(self.sess, self.staffmember, self.prerequisites_to_show[pr_ref].prerequisite_id,
                                  self.ValuesList[pr_ref][0].get(),
                                  self.ValuesList[pr_ref][1].get(),
                                  self.ValuesList[pr_ref][2].get(),
                                  self.ValuesList[pr_ref][3].get())

        self.master.refresh_prerequisites_page()


class StaffTrainingScreen(tk.Frame):
    def __init__(self, master, sess, staffmember, trainingScroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.trainingScroll = trainingScroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesButton = tk.Button(self, text="Staff Profiles", command=lambda: [
            self.master.show_frame(self.master.frames['StaffProfilesScreen'])])
        self.StaffProfilesButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.StafftypeProfilesButton = [tk.Button(self, text="Teacher Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Support Staff Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Governor Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Volunteers Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Agency Staff Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Contractor Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])])]
        self.StafftypeProfilesButton[qry_staff_member(self.sess, self.staffmember)[0].stafftype_id - 1].grid(column=0,
                                                                                                             columnspan=2,
                                                                                                             row=7,
                                                                                                             rowspan=2,
                                                                                                             sticky='news')

        self.IndvStaffProfileButton = tk.Button(self,
                                                text="{}".format(qry_staff_member(self.sess, self.staffmember)[0].name),
                                                command=lambda: [self.master.reset_trainingScroll(), self.master.show_frame(
                                                    self.master.frames['IndvStaffProfileScreen'])])
        self.IndvStaffProfileButton.grid(column=0, columnspan=2, row=9, rowspan=2, sticky='news')

        self.Title = tk.Label(self,
                              text="{}'s Training".format(qry_staff_member(self.sess, self.staffmember)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=8, columnspan=2, sticky='news')

        self.TrainingList = [row for row in qry_staff_training(self.sess, self.staffmember)]
        self.TrainingToShow = self.TrainingList[self.trainingScroll*5:(self.trainingScroll*5)+5]
        self.TrainingWidgetsList = []

        for tr in range(len(self.TrainingToShow)):
            self.TrainingWidgetsList.append([tk.Button(self, text="{}".format(self.TrainingToShow[tr].name),
                                                       command=lambda tr_id=tr:[self.master.set_profileTraining_id(self.TrainingToShow[tr_id].id),
                                                                       self.master.reset_StaffTrainingDatesScreen(),
                                                                       self.master.show_frame(self.master.frames['StaffTrainingDatesScreen'])]),
                                             tk.Label(self, text=qry_staff_training_duedate(self.sess, self.staffmember,
                                                                                                         self.TrainingToShow[tr].id))])
            self.TrainingWidgetsList[tr][0].grid(column=5, columnspan=4, row=(2*tr)+5, rowspan=2, sticky='news')
            self.TrainingWidgetsList[tr][1].grid(column=9, columnspan=2, row=(2*tr)+5, rowspan=2, sticky='news')

        self.TrainingLabel = tk.Label(self, text="Training")
        self.TrainingLabel.grid(column=5, columnspan=4, row=3, rowspan=2, sticky='news')
        self.DueDateLabel = tk.Label(self, text="Due Date")
        self.DueDateLabel.grid(column=9, columnspan=2, row=3, rowspan=2, sticky='news')
        self.ScrollDownTrainingButton = tk.Button(self, text="Down", command=lambda: [self.master.set_trainingScroll(self.trainingScroll + 1), self.master.show_frame(self.master.frames['StaffTrainingScreen'])])
        if self.trainingScroll < len(self.TrainingList)/5-1:
            self.ScrollDownTrainingButton.grid(column=11, row=14, sticky="news")
        self.ScrollUpTrainingButton = tk.Button(self, text="Up", command=lambda: [self.master.set_trainingScroll(self.trainingScroll - 1), self.master.show_frame(self.master.frames['StaffTrainingScreen'])])
        if self.trainingScroll>0:
            self.ScrollUpTrainingButton.grid(column=11, row=5, sticky="news")

        self.addTrainingButton = tk.Button(self, text="Add Training", command=lambda: [self.master.reset_StaffAddTrainingScreen(), self.master.show_frame(self.master.frames['StaffAddTrainingScreen'])])
        self.addTrainingButton.grid(column=11, columnspan=2, row=3, rowspan=2, sticky='news')



class StaffAddTrainingScreen(tk.Frame):
    def __init__(self, master, sess, staffmember):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self,
                              text="Add to {}'s Training".format(qry_staff_member(self.sess, self.staffmember)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=6, columnspan=2, sticky='news')
        self.current_training = [tr.id for tr in qry_staff_member(self.sess, self.staffmember)[0].training]
        self.all_training_list = self.sess.query(m.Training)
        self.new_training = []
        self.selected_training = []
        for tr in self.all_training_list:
            if tr.id not in self.current_training:
                self.new_training.append(tr)

        self.new_training_buttons = []
        for trai in range(len(self.new_training)):
            self.new_training_buttons.append(tk.Button(self, text=self.new_training[trai].name, command=lambda id=self.new_training[trai].id, ref=trai: [self.selected_training.append(id),  self.new_training_buttons[ref].grid_forget()]))
            self.new_training_buttons[trai].grid(row=(trai % 8) + 4, column=math.floor(trai / 8) + 3, sticky='news')

        self.cancel_button = tk.Button(self, text="Cancel", command=lambda: [self.master.show_frame(self.master.frames['StaffTrainingScreen'])])
        self.confirm_button = tk.Button(self, text="Confirm", command=lambda: [add_staff_trainings(self.sess, [self.staffmember], self.selected_training, date.today()), self.master.reset_StaffTrainingScreen(), self.master.show_frame(self.master.frames['StaffTrainingScreen'])])

        self.cancel_button.grid(column=3, row=15, rowspan=2, sticky='news')
        self.confirm_button.grid(column=8, row=15, rowspan=2, sticky='news')


class StaffTrainingDatesScreen(tk.Frame):
    def __init__(self, master, sess, staffmember, training):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.training = training
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesButton = tk.Button(self, text="Staff Profiles", command=lambda: [
            self.master.show_frame(self.master.frames['StaffProfilesScreen'])])
        self.StaffProfilesButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.StafftypeProfilesButton = [tk.Button(self, text="Teacher Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Support Staff Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Governor Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Volunteers Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Agency Staff Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Contractor Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])])]
        self.StafftypeProfilesButton[qry_staff_member(self.sess, self.staffmember)[0].stafftype_id - 1].grid(column=0,
                                                                                                             columnspan=2,
                                                                                                             row=7,
                                                                                                             rowspan=2,
                                                                                                             sticky='news')

        self.IndvStaffProfileButton = tk.Button(self,
                                                text="{}".format(qry_staff_member(self.sess, self.staffmember)[0].name),
                                                command=lambda: [self.master.reset_trainingScroll(),
                                                                 self.master.show_frame(
                                                                     self.master.frames['IndvStaffProfileScreen'])])
        self.IndvStaffProfileButton.grid(column=0, columnspan=2, row=9, rowspan=2, sticky='news')

        self.ProfileTrainingButton = tk.Button(self, text="Training", command=lambda: [self.master.reset_StaffTrainingScreen(), self.master.show_frame(self.master.frames['StaffTrainingScreen'])])
        self.ProfileTrainingButton.grid(column=0, columnspan=2, row=11, rowspan=2, sticky='news')

        self.Title = tk.Label(self,
                              text="{}'s {} Dates of Completion".format(qry_staff_member(self.sess, self.staffmember)[0].name, qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=5, columnspan=10, sticky='news')

        self.TrainingOccurances = self.sess.query(m.Staff_Training).filter(m.Staff_Training.staff_id==self.staffmember, m.Staff_Training.training_id==self.training).all()

        self.datesList = [tr.date for tr in self.TrainingOccurances]
        self.datesList.reverse()

        self.datesLabelsList = []
        for date in range(len(self.datesList)):
            self.datesLabelsList.append(tk.Label(self, text="{}".format(self.datesList[date])))
            self.datesLabelsList[date].grid(column=math.floor(date / 8) + 4, row=(date % 8) + 5, sticky='news')

        self.AddDateButton = tk.Button(self, text="Add Date", command=lambda: [self.master.reset_AddStaffTrainingDateScreen(), self.master.show_frame(self.master.frames['AddStaffTrainingDateScreen'])])
        self.AddDateButton.grid(column=4, columnspan=2, row=3, rowspan=2, sticky='news')


class AddStaffTrainingDateScreen(tk.Frame):
    def __init__(self, master, sess, staffmember, training):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.training = training
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self,
                              text="Add Date To {}'s {}".format(
                                  qry_staff_member(self.sess, self.staffmember)[0].name,
                                  qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=5, columnspan=10, sticky='news')

        self.formatLabel = tk.Label(self, text='YYYY-MM-DD')
        self.formatLabel.grid(column=8, columnspan=4, row=6, sticky='news')
        self.DateValue = tk.StringVar(self)
        self.DateEntry = tk.Entry(self, textvariable=self.DateValue)
        self.DateEntry.grid(column=8, columnspan=4, row=7, rowspan=2, sticky='news')

        self.cancelButton = tk.Button(self, text="Cancel", command=lambda: self.master.show_frame(self.master.frames['StaffTrainingDatesScreen']))
        self.cancelButton.grid(column=7, row=10, sticky='news')
        self.confirmButton = tk.Button(self, text="Confirm", command=lambda: [self.DateValue.set(self.DateValue.get()), add_staff_trainings(self.sess, [self.staffmember], [self.training], datetime.strptime(self.DateValue.get(), '%Y-%m-%d')), self.master.reset_StaffTrainingDatesScreen(), self.master.show_frame(self.master.frames['StaffTrainingDatesScreen'])])
        self.confirmButton.grid(column=12, row=10, sticky='news')


class StaffNotesScreen(tk.Frame):
    def __init__(self, master, sess, staffmember):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.StaffProfilesButton = tk.Button(self, text="Staff Profiles", command=lambda: [
            self.master.show_frame(self.master.frames['StaffProfilesScreen'])])
        self.StaffProfilesButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.StafftypeProfilesButton = [tk.Button(self, text="Teacher Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Support Staff Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Governor Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Volunteers Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Agency Staff Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])]),
                                        tk.Button(self, text="Contractor Profiles",
                                                  command=lambda: [self.master.reset_prerequisitesScroll(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['StafftypeProfilesScreen'])])]
        self.StafftypeProfilesButton[qry_staff_member(self.sess, self.staffmember)[0].stafftype_id - 1].grid(column=0,
                                                                                                             columnspan=2,
                                                                                                             row=7,
                                                                                                             rowspan=2,
                                                                                                             sticky='news')

        self.IndvStaffProfileButton = tk.Button(self,
                                                text="{}".format(qry_staff_member(self.sess, self.staffmember)[0].name),
                                                command=lambda: self.master.show_frame(
                                                    self.master.frames['IndvStaffProfileScreen']))
        self.IndvStaffProfileButton.grid(column=0, columnspan=2, row=9, rowspan=2, sticky='news')

        self.Title = tk.Label(self,
                              text="{}'s Personal Info".format(qry_staff_member(self.sess, self.staffmember)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=8, columnspan=2, sticky='news')

        self.NotesValue = tk.StringVar(self)
        self.ProfileNotesLabel = tk.Label(self, text="Notes:")
        self.ProfileNotes = tk.Entry(self, textvariable=self.NotesValue)
        self.NotesValue.set(qry_staff_member(self.sess, self.staffmember)[0].notes)
        self.ProfileNotesLabel.grid(column=3, columnspan=2, row=5, sticky='nes')
        self.ProfileNotes.grid(column=4, columnspan=10, row=6, rowspan=10, sticky='news')


class TrainingScreen(tk.Frame):
    def __init__(self, master, sess, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="Training", font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.TrainingButtons = [tk.Button(self, text="{}".format(training.name), command=lambda id=training.id: [self.master.set_training_id(id), self.master.reset_TrainingProfileScreen(), self.master.reset_TrainingProfilesScroll(),self.master.show_frame(self.master.frames['TrainingProfileScreen'])]) for training in self.sess.query(m.Training).all()]

        buttonsOnScreen = self.TrainingButtons[40 * self.scroll: 40 + (40 * self.scroll)]
        for Trainingbutton in range(len(buttonsOnScreen)):
            buttonsOnScreen[Trainingbutton].grid(row=(Trainingbutton % 10) + 4, column=math.floor(Trainingbutton / 10)*2 + 3, columnspan=2, sticky='news')

        self.ScrollDownTrainingButton = tk.Button(self, text="Down", command=lambda: [self.master.set_TrainingProfilesScroll(self.scroll+1), self.master.reset_TrainingScreen(), self.master.show_frame(self.master.frames['TrainingScreen'])])
        self.ScrollUpTrainingButton = tk.Button(self, text="Up", command=lambda: [self.master.set_TrainingProfilesScroll(self.scroll-1), self.master.reset_TrainingScreen(), self.master.show_frame(self.master.frames['TrainingScreen'])])

        if self.scroll < len(self.TrainingButtons)/40-1:
            self.ScrollDownTrainingButton.grid(column=10, row=15, sticky="news")

        if self.scroll>0:
            self.ScrollUpTrainingButton.grid(column=10, row=3, sticky="news")

        self.CreateNewTrainingButton = tk.Button(self, text="Create New Training",
                                                  command=lambda: self.master.show_frame(self.master.frames['CreateTrainingScreen']))
        self.CreateNewTrainingButton.grid(row=2, column=3, columnspan=2, sticky='news')



class CreateTrainingScreen(tk.Frame):
    def __init__(self, master, sess):
        super().__init__()
        self.master = master
        self.sess = sess
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Create Training", font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.nameValue = tk.StringVar(self)
        self.nameLabel = tk.Label(self, text="Training:")
        self.name = tk.Entry(self, textvariable=self.nameValue)
        self.nameLabel.grid(column=5, columnspan=2, row=5, rowspan=2, sticky='nes')
        self.name.grid(column=8, columnspan=4, row=5, rowspan=2, sticky='news')

        self.timeperiodValue = tk.IntVar(self)
        self.timeperiodLabel = tk.Label(self, text="Months Between Completion:")
        self.timeperiod = tk.Entry(self, textvariable=self.timeperiodValue)
        self.timeperiodLabel.grid(column=5, columnspan=2, row=7, rowspan=2, sticky='nes')
        self.timeperiod.grid(column=8, columnspan=4, row=7, rowspan=2, sticky='news')

        self.descriptionValue = tk.StringVar(self)
        self.descriptionLabel = tk.Label(self, text="Description:")
        self.description = tk.Entry(self, textvariable=self.descriptionValue)
        self.descriptionLabel.grid(column=5, columnspan=2, row=9, rowspan=2, sticky='nes')
        self.description.grid(column=8, columnspan=4, row=9, rowspan=4, sticky='news')

        self.CancelButton = tk.Button(self, text="Cancel", command=lambda: [self.master.show_frame(self.master.frames[
                                                                                                       'TrainingScreen'])])
        self.CancelButton.grid(column=4, row=16, sticky='news')
        self.DoneButton = tk.Button(self, text="Done", command=lambda: [
            create_training(self.sess, self.nameValue.get(), self.timeperiodValue.get(), self.descriptionValue.get()), self.master.reset_TrainingScreen(),
            self.master.show_frame(self.master.frames['TrainingScreen'])])
        self.DoneButton.grid(column=13, row=16, sticky='news')


class TrainingProfileScreen(tk.Frame):
    def __init__(self, master, sess, training):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.TrainingScreenButton = tk.Button(self, text="Training", command=lambda: self.master.show_frame(self.master.frames['TrainingScreen']))
        self.TrainingScreenButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="{}".format(qry_training(self.sess, self.training)[0].name), font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.TrainingInfoButton = tk.Button(self, text="Training Info", command=lambda: [self.master.reset_TrainingInfoScreen(), self.master.show_frame(self.master.frames['TrainingInfoScreen'])])
        self.TrainingInfoButton.grid(column=7, columnspan=4, row=5, rowspan=2, sticky='news')

        self.TrainingStaffButton = tk.Button(self, text="Staff", command=lambda: [self.master.reset_TrainingStaffScreen(), self.master.show_frame(self.master.frames['TrainingStaffScreen'])])
        self.TrainingStaffButton.grid(column=7, columnspan=4, row=9, rowspan=2, sticky='news')


class TrainingInfoScreen(tk.Frame):
    def __init__(self, master, sess, training):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.TrainingScreenButton = tk.Button(self, text="Training", command=lambda: self.master.show_frame(
            self.master.frames['TrainingScreen']))
        self.TrainingScreenButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.TrainingProfileButton = tk.Button(self, text='{}'.format(qry_training(self.sess, self.training)[0].name), command=lambda: self.master.show_frame(self.master.frames['TrainingProfileScreen']))
        self.TrainingProfileButton.grid(column=0, columnspan=2, row=7, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="{} Info".format(qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.timeperiodValue = tk.StringVar(self)
        self.timeperiodLabel = tk.Label(self, text="Must be re-completed every:")
        self.timeperiod = tk.Entry(self, textvariable=self.timeperiodValue)
        self.timeperiodValue.set(str(qry_training(self.sess, self.training)[0].timeperiod) + " Months")
        self.timeperiodLabel.grid(column=5, columnspan=2, row=5, rowspan=2, sticky='nes')
        self.timeperiod.grid(column=8, columnspan=4, row=5, rowspan=2, sticky='news')

        self.descriptionValue = tk.StringVar(self)
        self.descriptionLabel = tk.Label(self, text="Description:")
        self.description = tk.Entry(self, textvariable=self.descriptionValue)
        self.descriptionValue.set(qry_training(self.sess, self.training)[0].description)
        self.descriptionLabel.grid(column=5, columnspan=2, row=7, rowspan=2, sticky='nes')
        self.description.grid(column=8, columnspan=4, row=7, rowspan=4, sticky='news')


class TrainingStaffScreen(tk.Frame):
    def __init__(self, master, sess, training, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.TrainingScreenButton = tk.Button(self, text="Training", command=lambda: self.master.show_frame(
            self.master.frames['TrainingScreen']))
        self.TrainingScreenButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.TrainingProfileButton = tk.Button(self, text='{}'.format(qry_training(self.sess, self.training)[0].name),
                                               command=lambda: self.master.show_frame(
                                                   self.master.frames['TrainingProfileScreen']))
        self.TrainingProfileButton.grid(column=0, columnspan=2, row=7, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="{} Staff".format(qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.StaffLabels = [tk.Label(self, text=staffmember.name) for staffmember in qry_training(self.sess, self.training)[0].members]

        LabelsOnScreen = self.StaffLabels[70 * self.scroll: 70 + (70 * self.scroll)]
        for StaffLabel in range(len(LabelsOnScreen)):
            LabelsOnScreen[StaffLabel].grid(row=(StaffLabel % 10) + 4, column=math.floor(StaffLabel / 10) + 3, sticky='news')

        self.ScrollDownStaffButton = tk.Button(self, text="Down",
                                                  command=lambda: [self.master.set_TrainingProfilesScroll(self.scroll + 1),
                                                                   self.master.reset_TrainingStaffScreen(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['TrainingStaffScreen'])])
        self.ScrollUpStaffButton = tk.Button(self, text="Up",
                                                command=lambda: [self.master.set_TrainingProfilesScroll(self.scroll - 1),
                                                                 self.master.reset_TrainingStaffScreen(),
                                                                 self.master.show_frame(
                                                                     self.master.frames['TrainingStaffScreen'])])

        if self.scroll < len(self.StaffLabels) / 70 - 1:
            self.ScrollDownStaffButton.grid(column=10, row=15, sticky="news")

        if self.scroll > 0:
            self.ScrollUpStaffButton.grid(column=10, row=3, sticky="news")

        self.AddStaffButton = tk.Button(self, text="Add Staff", command=lambda: [self.master.reset_StaffToAddScroll(), self.master.clear_StaffToAddList(), self.master.reset_TrainingAddStaffScreen(), self.master.show_frame(self.master.frames['TrainingAddStaffScreen'])])
        self.AddStaffButton.grid(column=3, row=3, sticky='news')
        self.AddDateButton = tk.Button(self, text="Add a Date", command=lambda: [self.master.reset_TrainingSelectStaffToAddDateScreen(), self.master.show_frame(self.master.frames['TrainingSelectStaffToAddDateScreen'])])
        self.AddDateButton.grid(column=12, row=3, sticky='news')


class TrainingAddStaffScreen(tk.Frame):
    def __init__(self, master, sess, training, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Add Staff to {}".format(qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.currentStaff = qry_training(self.sess, self.training)[0].members

        self.Staff = []

        for staff in self.sess.query(m.Staff).all():
            if staff not in self.currentStaff:
                self.Staff.append(staff)

        self.StaffButtons = []

        for st in range(len(self.Staff)):
            self.StaffButtons.append(tk.Button(self, text="{}".format(self.Staff[st].name), command=lambda id=self.Staff[st].id, ref=st: [self.master.append_StaffToAddList(id), self.StaffButtons[ref].grid_forget()]))
            self.StaffButtons[st].grid(row=(st % 10) + 4, column=math.floor(st / 10) + 3, sticky='news')

        self.ScrollDownStaffButton = tk.Button(self, text="Down",
                                               command=lambda: [self.master.set_StaffToAddScroll(self.scroll + 1),
                                                                self.master.reset_TrainingAddStaffScreen(),
                                                                self.master.show_frame(
                                                                    self.master.frames['TrainingAddStaffScreen'])])
        self.ScrollUpStaffButton = tk.Button(self, text="Up",
                                             command=lambda: [self.master.set_StaffToAddScroll(self.scroll - 1),
                                                              self.master.reset_TrainingAddStaffScreen(),
                                                              self.master.show_frame(
                                                                  self.master.frames['TrainingAddStaffScreen'])])

        if self.scroll < len(self.StaffButtons) / 70 - 1:
            self.ScrollDownStaffButton.grid(column=10, row=15, sticky="news")

        if self.scroll > 0:
            self.ScrollUpStaffButton.grid(column=10, row=3, sticky="news")

        self.CancelButton = tk.Button(self, text="Cancel", command=lambda: self.master.show_frame(self.master.frames['TrainingStaffScreen']))
        self.CancelButton.grid(column=3, row=16, sticky='news')
        self.ConfirmButton = tk.Button(self, text="Confirm", command=lambda: [add_staff_trainings(self.sess, self.master.StaffToAddList, [self.training]), self.master.reset_TrainingStaffScreen(), self.master.show_frame(self.master.frames['TrainingStaffScreen'])])
        self.ConfirmButton.grid(column=12, row=16, sticky='news')


class TrainingSelectStaffToAddDateScreen(tk.Frame):
    def __init__(self, master, sess, training, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Select Staff To Add Date for {}".format(qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.StaffButtons = []

        for staffmember in range(len(qry_training(self.sess, self.training)[0].members)):
            self.StaffButtons.append(tk.Button(self, text="{}".format(qry_training(self.sess, self.training)[0].members[staffmember].name), command=lambda id=qry_training(self.sess, self.training)[0].members[staffmember].id, ref=staffmember: [self.master.append_StaffToAddDateList(id), self.StaffButtons[ref].grid_forget()]))

        ButtonsOnScreen = self.StaffButtons[70 * self.scroll: 70 + (70 * self.scroll)]
        for StaffButton in range(len(ButtonsOnScreen)):
            ButtonsOnScreen[StaffButton].grid(row=(StaffButton % 10) + 4, column=math.floor(StaffButton / 10) + 3,
                                            sticky='news')

        self.ScrollDownStaffButton = tk.Button(self, text="Down",
                                               command=lambda: [self.master.set_StaffToAddDateScroll(self.scroll + 1),
                                                                self.master.reset_TrainingSelectStaffToAddDateScreen(),
                                                                self.master.show_frame(
                                                                    self.master.frames['TrainingSelectStaffToAddDateScreen'])])
        self.ScrollUpStaffButton = tk.Button(self, text="Up",
                                             command=lambda: [self.master.set_StaffToAddDateScroll(self.scroll - 1),
                                                              self.master.reset_TrainingSelectStaffToAddDateScreen(),
                                                              self.master.show_frame(
                                                                  self.master.frames['TrainingSelectStaffToAddDateScreen'])])

        if self.scroll < len(self.StaffButtons) / 70 - 1:
            self.ScrollDownStaffButton.grid(column=10, row=15, sticky="news")

        if self.scroll > 0:
            self.ScrollUpStaffButton.grid(column=10, row=3, sticky="news")

        self.CancelButton = tk.Button(self, text="Cancel",
                                      command=lambda: self.master.show_frame(self.master.frames['TrainingStaffScreen']))
        self.CancelButton.grid(column=3, row=16, sticky='news')
        self.ConfirmButton = tk.Button(self, text="Confirm", command=lambda: [
            self.master.reset_TrainingAddDateScreen(), self.master.show_frame(self.master.frames['TrainingAddDateScreen'])])
        self.ConfirmButton.grid(column=12, row=16, sticky='news')


class TrainingAddDateScreen(tk.Frame):
    def __init__(self, master, sess, training, staff):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.staff = staff
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Add Date for {}".format(
            qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.formatLabel = tk.Label(self, text='YYYY-MM-DD')
        self.formatLabel.grid(column=7, columnspan=4, row=6, sticky='news')
        self.DateValue = tk.StringVar(self)
        self.DateEntry = tk.Entry(self, textvariable=self.DateValue)
        self.DateEntry.grid(column=7, columnspan=4, row=7, rowspan=2, sticky='news')

        self.CancelButton = tk.Button(self, text="Cancel",
                                      command=lambda: self.master.show_frame(self.master.frames['TrainingStaffScreen']))
        self.CancelButton.grid(column=3, row=16, sticky='news')
        self.ConfirmButton = tk.Button(self, text="Confirm", command=lambda: [
            self.DateValue.set(self.DateValue.get()),
            add_staff_trainings(self.sess, self.staff, [self.training], datetime.strptime(self.DateValue.get(), '%Y-%m-%d')),
            self.master.reset_TrainingStaffScreen(),
            self.master.show_frame(self.master.frames['TrainingStaffScreen'])])
        self.ConfirmButton.grid(column=12, row=16, sticky='news')


class TrainingContactsScreen(tk.Frame):
    def __init__(self, master, sess, training):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        pass


class TrainingAddContactsScreen(tk.Frame):
    def __init__(self, master, sess, training):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        pass


class ContactsScreen(tk.Frame):
    def __init__(self, master, sess):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        pass


class CreateContactScreen(tk.Frame):
    def __init__(self, master, sess):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        pass


class ContactProfileScreen(tk.Frame):
    def __init__(self, master, sess, contact):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        pass


class ContactInfoScreen(tk.Frame):
    def __init__(self, master, sess, contact):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        pass


class ContactTrainingScreen(tk.Frame):
    def __init__(self, master, sess, contact):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        pass


class ContactAddTrainingScreen(tk.Frame):
    def __init__(self, master, sess, contact):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        pass


class NotificationsScreen(tk.Frame):
    def __init__(self, master, sess):
        super().__init__()
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.IncompletePrerequisitesScreenButton = tk.Button(self, text="Incomplete Prerequisites",
                                            command=lambda: [self.master.reset_IncompletePrerequisitesScroll(), self.master.reset_IncompletePrerequisitesScreen(),
                                                             self.master.show_frame(
                                                    self.master.frames['IncompletePrerequisitesScreen'])],
                                            font=self.master.TitleFont)
        self.IncompletePrerequisitesScreenButton.grid(column=7, columnspan=5, row=3, rowspan=3, sticky='news')

        self.IncompleteTrainingScreenButtonButton = tk.Button(self, text="Incomplete Training", command=lambda: [self.master.reset_IncompleteTrainingScroll(), self.master.reset_IncompleteTrainingScreen(), self.master.show_frame(
            self.master.frames['IncompleteTrainingScreen'])], font=self.master.TitleFont)
        self.IncompleteTrainingScreenButtonButton.grid(column=7, columnspan=5, row=8, rowspan=3, sticky='news')

        self.UpcomingTrainingScreenButton = tk.Button(self, text="Upcoming Training", command=lambda: [self.master.reset_UpcomingTrainingScroll(), self.master.reset_UpcomingTrainingTimeFrameScreen(), self.master.show_frame(
            self.master.frames['UpcomingTrainingTimeFrameScreen'])], font=self.master.TitleFont)
        self.UpcomingTrainingScreenButton.grid(column=7, columnspan=5, row=13, rowspan=3, sticky='news')


class IncompletePrerequisitesScreen(tk.Frame):
    def __init__(self, master, sess, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.NotificationsButton = tk.Button(self, text="Notifications", command=lambda:[self.master.show_frame(self.master.frames['NotificationsScreen'])])
        self.NotificationsButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.Title = tk.Label(self,
                              text="Staff With Incomplete Prerequisites",
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')
        self.Staff = qry_staff_with_incomplete_prerequisites(self.sess)

        self.StaffButtons = []

        for staffmember in range(len(self.Staff)):
            self.StaffButtons.append(tk.Button(self, text="{}".format(self.Staff[staffmember][0].name), command=lambda id=self.Staff[staffmember][0].id: [self.master.set_incompletePrerequisiteStaff_id(id), self.master.reset_StaffsIncompletePrerequisitesScreen(), self.master.show_frame(self.master.frames['StaffsIncompletePrerequisitesScreen'])]))

        self.ButtonsOnScreen = self.StaffButtons[70 * self.scroll: 70 + (70 * self.scroll)]

        for Staffbutton in range(len(self.ButtonsOnScreen)):
            self.ButtonsOnScreen[Staffbutton].grid(row=(Staffbutton % 10) + 4, column=math.floor(Staffbutton / 10) + 3, sticky='news')

        self.ScrollDownProfilesButton = tk.Button(self, text="Down",
                                                  command=lambda: [self.master.set_IncompletePrerequisitesScroll(self.scroll + 1),
                                                                   self.master.reset_IncompletePrerequisitesScreen(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['IncompletePrerequisitesScreen'])])
        self.ScrollUpProfilesButton = tk.Button(self, text="Up",
                                                command=lambda: [self.master.set_IncompletePrerequisitesScroll(self.scroll - 1),
                                                                   self.master.reset_IncompletePrerequisitesScreen(),
                                                                   self.master.show_frame(
                                                                       self.master.frames['IncompletePrerequisitesScreen'])])

        if self.scroll < len(self.Staff) / 70 - 1:
            self.ScrollDownProfilesButton.grid(column=10, row=15, sticky="news")

        if self.scroll > 0:
            self.ScrollUpProfilesButton.grid(column=10, row=3, sticky="news")


class StaffsIncompletePrerequisitesScreen(tk.Frame):
    def __init__(self, master, sess, staffmember, Scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.staffmember = staffmember
        self.Scroll = Scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.NotificationsButton = tk.Button(self, text="Notifications", command=lambda: [
            self.master.show_frame(self.master.frames['NotificationsScreen'])])
        self.NotificationsButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.IncompletePrerequisitesButton = tk.Button(self, text="Incomplete Prerequisites", command=lambda:[self.master.reset_IncompletePrerequisitesScreen(), self.master.show_frame(self.master.frames['IncompletePrerequisitesScreen'])])
        self.IncompletePrerequisitesButton.grid(column=0, columnspan=2, row=7, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="{}'s Incomplete Checks/ Prerequisites".format(
            qry_staff_member(self.sess, self.staffmember)[0].name), font=self.master.TitleFont)
        self.Title.grid(row=1, column=6, columnspan=2, sticky='news')

        self.prerequisitesList = [row for row in qry_incomplete_staff_prerequisites(self.sess, self.staffmember)]
        self.prerequisites_to_show = self.prerequisitesList[
                                     self.Scroll * 5:(self.Scroll * 5) + 5]
        self.prerequisitesWidgetsList = []
        self.ValuesList = []

        for pr in range(len(self.prerequisites_to_show)):
            self.ValuesList.append([tk.IntVar(self), tk.StringVar(self), tk.StringVar(self), tk.StringVar(self)])
            self.ValuesList[pr][0].set(self.prerequisites_to_show[pr].completed)
            self.ValuesList[pr][1].set(self.prerequisites_to_show[pr].confirmationDate)
            self.ValuesList[pr][2].set(self.prerequisites_to_show[pr].confirmedBy)
            self.ValuesList[pr][3].set(self.prerequisites_to_show[pr].extra)
            self.prerequisitesWidgetsList.append([tk.Label(self, text="{}".format(
                qry_prerequisites(self.sess, [self.prerequisites_to_show[pr].prerequisite_id])[0][0].name)),
                                                  tk.Checkbutton(self, text="Completed?",
                                                                 variable=self.ValuesList[pr][0], onvalue=1,
                                                                 offvalue=0),
                                                  tk.Label(self, text="Date Confirmed:"),
                                                  tk.Entry(self, textvariable=self.ValuesList[pr][1]),
                                                  tk.Label(self, text="Confirmed By:"),
                                                  tk.Entry(self, textvariable=self.ValuesList[pr][2]),
                                                  tk.Label(self, text="Extra Info:"),
                                                  tk.Entry(self, textvariable=self.ValuesList[pr][3]),
                                                  tk.Button(self, text="Confirm", command=lambda
                                                      x=pr: self.update_staff_prerequisite_function(x))])

            self.prerequisitesWidgetsList[pr][0].grid(column=3, columnspan=10, row=(2 * pr) + 3, sticky='nsw')
            self.prerequisitesWidgetsList[pr][1].grid(column=3, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][2].grid(column=4, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][3].grid(column=5, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][4].grid(column=6, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][5].grid(column=7, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][6].grid(column=8, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][7].grid(column=9, row=(2 * pr) + 4, sticky='news')
            self.prerequisitesWidgetsList[pr][8].grid(column=10, row=(2 * pr) + 4, sticky='news')

        self.ScrollDownPrerequisitesButton = tk.Button(self, text="Down", command=lambda: [
            self.master.set_StaffIncompletePrerequisitesScroll(self.Scroll + 1),
            self.master.reset_StaffsIncompletePrerequisitesScreen(),
            self.master.show_frame(self.master.frames['StaffsIncompletePrerequisitesScreen'])])

        self.ScrollUpPrerequisitesButton = tk.Button(self, text="Up", command=lambda: [
            self.master.set_StaffIncompletePrerequisitesScroll(self.Scroll - 1),
            self.master.reset_StaffsIncompletePrerequisitesScreen(),
            self.master.show_frame(self.master.frames['StaffsIncompletePrerequisitesScreen'])])

        if self.Scroll < len(self.prerequisitesList) / 5 - 1:
            self.ScrollDownPrerequisitesButton.grid(column=10, row=15, sticky="news")

        if self.Scroll > 0:
            self.ScrollUpPrerequisitesButton.grid(column=10, row=14, sticky="news")

    def update_staff_prerequisite_function(self, pr_ref):
        self.ValuesList[pr_ref][0].set("{}".format(self.ValuesList[pr_ref][0].get()))
        self.ValuesList[pr_ref][1].set("{}".format(self.ValuesList[pr_ref][1].get()))
        self.ValuesList[pr_ref][2].set("{}".format(self.ValuesList[pr_ref][2].get()))
        self.ValuesList[pr_ref][3].set("{}".format(self.ValuesList[pr_ref][3].get()))
        update_staff_prerequisite(self.sess, self.staffmember, self.prerequisites_to_show[pr_ref].prerequisite_id,
                                  self.ValuesList[pr_ref][0].get(),
                                  self.ValuesList[pr_ref][1].get(),
                                  self.ValuesList[pr_ref][2].get(),
                                  self.ValuesList[pr_ref][3].get())

        self.master.reset_StaffsIncompletePrerequisitesScreen()
        self.master.show_frame(self.master.frames['StaffsIncompletePrerequisitesScreen'])


class IncompleteTrainingScreen(tk.Frame):
    def __init__(self, master, sess, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.NotificationsButton = tk.Button(self, text="Notifications", command=lambda: [
            self.master.show_frame(self.master.frames['NotificationsScreen'])])
        self.NotificationsButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.Title = tk.Label(self,
                              text="Incomplete Training",
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')
        self.Training = qry_overdue_training(self.sess)

        self.TrainingButtons = []

        for training in range(len(self.Training)):

            self.TrainingButtons.append(tk.Button(self, text="{}".format(self.Training[training][0].name),
                                               command=lambda id=self.Training[training][0].id: [
                                                   self.master.set_incompleteTraining_id(id),
                                                   self.master.reset_IncompleteTrainingSelectStaffScreen(),
                                                   self.master.show_frame(
                                                       self.master.frames['IncompleteTrainingSelectStaffScreen'])]))

        self.ButtonsOnScreen = self.TrainingButtons[40 * self.scroll: 40 + (40 * self.scroll)]

        for Trainingbutton in range(len(self.ButtonsOnScreen)):
            self.ButtonsOnScreen[Trainingbutton].grid(row=(Trainingbutton % 10) + 4, column=(math.floor(Trainingbutton / 10))*2 + 3,
                                                   sticky='news')

        self.ScrollDownProfilesButton = tk.Button(self, text="Down",
                                                  command=lambda: [
                                                      self.master.set_IncompleteTrainingScroll(self.scroll + 1),
                                                      self.master.reset_IncompleteTrainingScreen(),
                                                      self.master.show_frame(
                                                          self.master.frames['IncompleteTrainingScreen'])])
        self.ScrollUpProfilesButton = tk.Button(self, text="Up",
                                                command=lambda: [
                                                    self.master.set_IncompleteTrainingScroll(self.scroll - 1),
                                                    self.master.reset_IncompleteTrainingScreen(),
                                                    self.master.show_frame(
                                                        self.master.frames['IncompleteTrainingScreen'])])

        if self.scroll < len(self.Training) / 40 - 1:
            self.ScrollDownProfilesButton.grid(column=10, row=15, sticky="news")

        if self.scroll > 0:
            self.ScrollUpProfilesButton.grid(column=10, row=3, sticky="news")


class IncompleteTrainingSelectStaffScreen(tk.Frame):
    def __init__(self, master, sess, training, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Select Staff To Add Date for {}".format(
            qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.StaffButtons = []

        for staffmember in range(len(qry_staff_with_overdue_training(self.sess, self.training))):
            self.StaffButtons.append(
                tk.Button(self, text="{}".format(qry_staff_with_overdue_training(self.sess, self.training)[staffmember][0].name),
                          command=lambda id=qry_staff_with_overdue_training(self.sess, self.training)[staffmember][0].id,
                                         ref=staffmember: [self.master.append_incompleteTraining_staff(id),
                                                           self.StaffButtons[ref].grid_forget()]))

        ButtonsOnScreen = self.StaffButtons[70 * self.scroll: 70 + (70 * self.scroll)]
        for StaffButton in range(len(ButtonsOnScreen)):
            ButtonsOnScreen[StaffButton].grid(row=(StaffButton % 10) + 4, column=math.floor(StaffButton / 10) + 3,
                                              sticky='news')

        self.ScrollDownStaffButton = tk.Button(self, text="Down",
                                               command=lambda: [self.master.set_StaffIncompleteTrainingScroll(self.scroll + 1),
                                                                self.master.reset_IncompleteTrainingSelectStaffScreen(),
                                                                self.master.show_frame(
                                                                    self.master.frames[
                                                                        'IncompleteTrainingSelectStaffScreen'])])
        self.ScrollUpStaffButton = tk.Button(self, text="Up",
                                             command=lambda: [self.master.set_StaffIncompleteTrainingScroll(self.scroll - 1),
                                                              self.master.reset_IncompleteTrainingSelectStaffScreen(),
                                                              self.master.show_frame(
                                                                  self.master.frames[
                                                                      'IncompleteTrainingSelectStaffScreen'])])

        if self.scroll < len(self.StaffButtons) / 70 - 1:
            self.ScrollDownStaffButton.grid(column=10, row=15, sticky="news")

        if self.scroll > 0:
            self.ScrollUpStaffButton.grid(column=10, row=3, sticky="news")

        self.CancelButton = tk.Button(self, text="Cancel",
                                      command=lambda: self.master.show_frame(self.master.frames['IncompleteTrainingScreen']))
        self.CancelButton.grid(column=3, row=16, sticky='news')
        self.ConfirmButton = tk.Button(self, text="Confirm", command=lambda: [
            self.master.reset_IncompleteTrainingAddDateScreen(),
            self.master.show_frame(self.master.frames['IncompleteTrainingAddDateScreen'])])
        self.ConfirmButton.grid(column=12, row=16, sticky='news')


class IncompleteTrainingAddDateScreen(tk.Frame):
    def __init__(self, master, sess, training, staff):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.staff = staff
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Add Date for {}".format(
            qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.formatLabel = tk.Label(self, text='YYYY-MM-DD')
        self.formatLabel.grid(column=7, columnspan=4, row=6, sticky='news')
        self.DateValue = tk.StringVar(self)
        self.DateEntry = tk.Entry(self, textvariable=self.DateValue)
        self.DateEntry.grid(column=7, columnspan=4, row=7, rowspan=2, sticky='news')

        self.CancelButton = tk.Button(self, text="Cancel",
                                      command=lambda: self.master.show_frame(self.master.frames['IncompleteTrainingScreen']))
        self.CancelButton.grid(column=3, row=16, sticky='news')
        self.ConfirmButton = tk.Button(self, text="Confirm", command=lambda: [
            self.DateValue.set(self.DateValue.get()),
            add_staff_trainings(self.sess, self.staff, [self.training],
                                datetime.strptime(self.DateValue.get(), '%Y-%m-%d')),
            self.master.reset_IncompleteTrainingScreen(),
            self.master.show_frame(self.master.frames['IncompleteTrainingScreen'])])
        self.ConfirmButton.grid(column=12, row=16, sticky='news')


class UpcomingTrainingTimeFrameScreen(tk.Frame):
    def __init__(self, master, sess):
        super().__init__()
        self.master = master
        self.sess = sess
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.NotificationsButton = tk.Button(self, text="Notifications", command=lambda: [
            self.master.show_frame(self.master.frames['NotificationsScreen'])])
        self.NotificationsButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.Title = tk.Label(self, text="Set Time Frame For Upcoming Training",
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.sliderVal = tk.IntVar(self)
        self.slider = ttk.LabeledScale(self, from_=1, to=12, variable=self.sliderVal)
        self.slider.grid(column=7, columnspan=4, row=8, rowspan=2, sticky='news')

        self.confirmButton = tk.Button(self, text="Confirm", command=lambda: [self.master.set_timeFrame(self.sliderVal.get()), self.master.reset_UpcomingTrainingScreen(), self.master.show_frame(self.master.frames['UpcomingTrainingScreen'])])
        self.confirmButton.grid(column=8, columnspan=2, row=10, rowspan=2, sticky='news')

class UpcomingTrainingScreen(tk.Frame):
    def __init__(self, master, sess, time_frame, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.time_frame = time_frame
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.MenuButton = tk.Button(self, text="Menu",
                                    command=lambda: [self.master.show_frame(self.master.frames['MenuScreen'])])
        self.MenuButton.grid(column=0, columnspan=2, row=3, rowspan=2, sticky='news')

        self.NotificationsButton = tk.Button(self, text="Notifications", command=lambda: [
            self.master.show_frame(self.master.frames['NotificationsScreen'])])
        self.NotificationsButton.grid(column=0, columnspan=2, row=5, rowspan=2, sticky='news')

        self.changeTimeFrameButton = tk.Button(self, text="Change Time Frame", command=lambda: self.master.show_frame(self.master.frames['UpcomingTrainingTimeFrameScreen']))
        self.changeTimeFrameButton.grid(column=0, columnspan=2, row=7, rowspan=2, sticky='news')

        self.Title = tk.Label(self,
                              text="Training Upcoming Over the Next {} Months".format(self.time_frame),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=3, columnspan=10, sticky='news')
        self.Training = qry_upcoming_training(self.sess, self.time_frame)

        self.TrainingButtons = []

        for training in range(len(self.Training)):
            self.TrainingButtons.append(tk.Button(self, text="{}".format(self.Training[training][0].name),
                                                  command=lambda id=self.Training[training][0].id: [
                                                      self.master.set_upcomingTraining_id(id),
                                                      self.master.reset_UpcomingTrainingSelectStaffScreen(),
                                                      self.master.show_frame(
                                                          self.master.frames['UpcomingTrainingSelectStaffScreen'])]))

        self.ButtonsOnScreen = self.TrainingButtons[40 * self.scroll: 40 + (40 * self.scroll)]

        for Trainingbutton in range(len(self.ButtonsOnScreen)):
            self.ButtonsOnScreen[Trainingbutton].grid(row=(Trainingbutton % 10) + 4,
                                                      column=(math.floor(Trainingbutton / 10)) * 2 + 3,
                                                      sticky='news')

        self.ScrollDownProfilesButton = tk.Button(self, text="Down",
                                                  command=lambda: [
                                                      self.master.set_UpcomingTrainingScroll(self.scroll + 1),
                                                      self.master.reset_UpcomingTrainingScreen(),
                                                      self.master.show_frame(
                                                          self.master.frames['UpcomingTrainingScreen'])])
        self.ScrollUpProfilesButton = tk.Button(self, text="Up",
                                                command=lambda: [
                                                    self.master.set_UpcomingTrainingScroll(self.scroll - 1),
                                                    self.master.reset_UpcomingTrainingScreen(),
                                                    self.master.show_frame(
                                                        self.master.frames['UpcomingTrainingScreen'])])

        if self.scroll < len(self.Training) / 40 - 1:
            self.ScrollDownProfilesButton.grid(column=10, row=15, sticky="news")

        if self.scroll > 0:
            self.ScrollUpProfilesButton.grid(column=10, row=3, sticky="news")




class UpcomingTrainingSelectStaffScreen(tk.Frame):
    def __init__(self, master, sess, time_frame, training, scroll):
        super().__init__()
        self.master = master
        self.sess = sess
        self.time_frame = time_frame
        self.training = training
        self.scroll = scroll
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Select Staff To Add Date for {}".format(
            qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.StaffButtons = []

        for staffmember in range(len(qry_staff_with_upcoming_duedate(self.sess, self.training, self.time_frame))):
            self.StaffButtons.append(
                tk.Button(self, text="{}".format(
                    qry_staff_with_upcoming_duedate(self.sess, self.training, self.time_frame)[staffmember][0].name),
                          command=lambda
                              id=qry_staff_with_upcoming_duedate(self.sess, self.training, self.time_frame)[staffmember][0].id,
                              ref=staffmember: [self.master.append_upcomingTraining_staff(id),
                                                self.StaffButtons[ref].grid_forget()]))

        ButtonsOnScreen = self.StaffButtons[70 * self.scroll: 70 + (70 * self.scroll)]
        for StaffButton in range(len(ButtonsOnScreen)):
            ButtonsOnScreen[StaffButton].grid(row=(StaffButton % 10) + 4, column=math.floor(StaffButton / 10) + 3,
                                              sticky='news')

        self.ScrollDownStaffButton = tk.Button(self, text="Down",
                                               command=lambda: [
                                                   self.master.set_StaffUpcomingTrainingScroll(self.scroll + 1),
                                                   self.master.reset_UpcomingTrainingSelectStaffScreen(),
                                                   self.master.show_frame(
                                                       self.master.frames[
                                                           'UpcomingTrainingSelectStaffScreen'])])
        self.ScrollUpStaffButton = tk.Button(self, text="Up",
                                             command=lambda: [
                                                 self.master.set_StaffUpcomingTrainingScroll(self.scroll - 1),
                                                 self.master.reset_UpcomingTrainingSelectStaffScreen(),
                                                 self.master.show_frame(
                                                     self.master.frames[
                                                         'UpcomingTrainingSelectStaffScreen'])])

        if self.scroll < len(self.StaffButtons) / 70 - 1:
            self.ScrollDownStaffButton.grid(column=10, row=15, sticky="news")

        if self.scroll > 0:
            self.ScrollUpStaffButton.grid(column=10, row=3, sticky="news")

        self.CancelButton = tk.Button(self, text="Cancel",
                                      command=lambda: self.master.show_frame(
                                          self.master.frames['UpcomingTrainingScreen']))
        self.CancelButton.grid(column=3, row=16, sticky='news')
        self.ConfirmButton = tk.Button(self, text="Confirm", command=lambda: [
            self.master.reset_UpcomingTrainingAddDateScreen(),
            self.master.show_frame(self.master.frames['UpcomingTrainingAddDateScreen'])])
        self.ConfirmButton.grid(column=12, row=16, sticky='news')




class UpcomingTrainingAddDateScreen(tk.Frame):
    def __init__(self, master, sess, training, staff):
        super().__init__()
        self.master = master
        self.sess = sess
        self.training = training
        self.staff = staff
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.grid()
        for column in range(20):
            self.columnconfigure(column, minsize=self.screenwidth / 20)
        for row in range(30):
            self.rowconfigure(row, minsize=self.screenheight / 30)
        self.create_widgets()

    def create_widgets(self):
        self.Logo = tk.PhotoImage(file='Logo.png')
        self.LogoLabel = tk.Label(self, image=self.Logo)
        self.LogoLabel.grid(row=17, column=1, sticky='news')

        self.softwareLogo = tk.PhotoImage(file='G-SCR Logo.png')
        self.softwareLogoLabel = tk.Label(self, image=self.softwareLogo)
        self.softwareLogoLabel.grid(row=0, column=0, rowspan=2, columnspan=2, sticky='nw')

        self.myLogo = tk.PhotoImage(file='BV.png')
        self.myLogoLabel = tk.Label(self, image=self.myLogo)
        self.myLogoLabel.grid(row=17, column=0, sticky='news')

        self.Title = tk.Label(self, text="Add Date for {}".format(
            qry_training(self.sess, self.training)[0].name),
                              font=self.master.TitleFont)
        self.Title.grid(row=1, column=4, columnspan=10, sticky='news')

        self.formatLabel = tk.Label(self, text='YYYY-MM-DD')
        self.formatLabel.grid(column=7, columnspan=4, row=6, sticky='news')
        self.DateValue = tk.StringVar(self)
        self.DateEntry = tk.Entry(self, textvariable=self.DateValue)
        self.DateEntry.grid(column=7, columnspan=4, row=7, rowspan=2, sticky='news')

        self.CancelButton = tk.Button(self, text="Cancel",
                                      command=lambda: self.master.show_frame(
                                          self.master.frames['UpcomingTrainingScreen']))
        self.CancelButton.grid(column=3, row=16, sticky='news')
        self.ConfirmButton = tk.Button(self, text="Confirm", command=lambda: [
            self.DateValue.set(self.DateValue.get()),
            add_staff_trainings(self.sess, self.staff, [self.training],
                                datetime.strptime(self.DateValue.get(), '%Y-%m-%d')),
            self.master.reset_UpcomingTrainingScreen(),
            self.master.show_frame(self.master.frames['UpcomingTrainingScreen'])])
        self.ConfirmButton.grid(column=12, row=16, sticky='news')


Session, exists = establish_path()
with Session() as session:
    if not exists:
        populate_database(session)
    app = TSACFS(session)
    app.mainloop()
