import Resume
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from docx import Document
from docx.shared import Pt
import re

class Application(tk.Frame):
    name = city = state = zip_code = phone = email = job = skills = education = ''
    experiences = []

    def __init__(self, master=None):
        super().__init__(master)
        self.cv = ''
        self.master = master
        self.pack()
        self.create_widgets()

        self.master.geometry("750x750")
        self.adjustedResume = ''

    def create_widgets(self):
        # create label
        self.label = tk.Label(self, text="Choose your level:")
        self.label.pack()

        # create radio buttons
        self.level = tk.StringVar()
        self.radio1 = tk.Radiobutton(self, text="Entry Level", variable=self.level, value="Entry Level")
        self.radio2 = tk.Radiobutton(self, text="Mid Level", variable=self.level, value="Mid Level")
        self.radio3 = tk.Radiobutton(self, text="Senior Level", variable=self.level, value="Senior Level")
        self.radio4 = tk.Radiobutton(self, text="Executive Level", variable=self.level, value="Executive Level")
        self.radio1.pack()
        self.radio2.pack()
        self.radio3.pack()
        self.radio4.pack()

        # create submit button
        self.submit = tk.Button(self, text="Submit", command=self.submit_choice)
        self.submit.pack()

    def submit_choice(self):
        self.resumeLevel = self.level.get()

        # destroy current widgets
        self.label.destroy()
        self.radio1.destroy()
        self.radio2.destroy()
        self.radio3.destroy()
        self.radio4.destroy()
        self.submit.destroy()

        # create new widgets for the next form
        tk.Label(self, text="Name:").pack()
        self.nameB = tk.Entry(self)
        self.nameB.pack()

        tk.Label(self, text="City:").pack()
        self.cityB = tk.Entry(self)
        self.cityB.pack()

        tk.Label(self, text="State:").pack()
        self.stateB = tk.Entry(self)
        self.stateB.pack()

        tk.Label(self, text="Zip Code:").pack()
        self.zip_codeB = tk.Entry(self)
        self.zip_codeB.pack()

        tk.Label(self, text="Phone:").pack()
        self.phoneB = tk.Entry(self)
        self.phoneB.pack()

        tk.Label(self, text="Email:").pack()
        self.emailB = tk.Entry(self)
        self.emailB.pack()

        tk.Label(self, text="Job:").pack()
        self.jobB = tk.Entry(self)
        self.jobB.pack()

        tk.Label(self, text="Skills:").pack()
        self.skillsB = tk.Entry(self)
        self.skillsB.pack()

        tk.Label(self, text="Education:").pack()
        self.educationB = tk.Entry(self)
        self.educationB.pack()

        # create submit button for the next form
        self.submit2 = tk.Button(self, text="Submit", command=self.submit_choice2)
        self.submit2.pack()

    def submit_choice2(self):
        # retrieve data from the fields
        self.name = self.nameB.get()
        self.city = self.cityB.get()
        self.state = self.stateB.get()
        self.zip_code = self.zip_codeB.get()
        self.phone = self.phoneB.get()
        self.email = self.emailB.get()
        self.job = self.jobB.get()
        self.skills = self.skillsB.get()
        self.education = self.educationB.get()
        self.clear_fields()

    def clear_fields(self):
        # destroy widgets
        for widgets in self.winfo_children():
            widgets.destroy()
        self.experience_choice()

    def experience_choice(self):
        # create label
        self.label = tk.Label(self, text="How many experiences do you have?")
        self.label.pack()

        # create radio buttons
        self.choice = tk.IntVar()
        self.radio1 = tk.Radiobutton(self, text="1", variable=self.choice, value=1)
        self.radio2 = tk.Radiobutton(self, text="2", variable=self.choice, value=2)
        self.radio3 = tk.Radiobutton(self, text="3", variable=self.choice, value=3)
        self.radio4 = tk.Radiobutton(self, text="4", variable=self.choice, value=4)
        self.radio1.pack()
        self.radio2.pack()
        self.radio3.pack()
        self.radio4.pack()

        # create submit button
        self.submit3 = tk.Button(self, text="Submit", command=self.submit_choice3)
        self.submit3.pack()

    def submit_choice3(self):
        self.num = self.choice.get()
        self.label.destroy()
        self.radio1.destroy()
        self.radio2.destroy()
        self.radio3.destroy()
        self.radio4.destroy()
        self.submit3.destroy()
        self.experience()

    def experience(self):
        tk.Label(self,
                 text="Write all about the experience then press submit. Once you are done, click create resume.").pack()

        tk.Label(self, text="Company Name:").pack()
        self.comp = tk.Entry(self)
        self.comp.pack()

        tk.Label(self, text="Job Name:").pack()
        self.job = tk.Entry(self)
        self.job.pack()

        tk.Label(self, text="Location:").pack()
        self.location = tk.Entry(self)
        self.location.pack()

        tk.Label(self, text="Dates:").pack()
        self.dates = tk.Entry(self)
        self.dates.pack()

        tk.Label(self, text="Company Description:").pack()
        self.compDesc = tk.Entry(self)
        self.compDesc.pack()

        tk.Label(self, text="Job Description:").pack()
        self.jobDesc = tk.Entry(self)
        self.jobDesc.pack()

        tk.Label(self, text="Achievements:").pack()
        self.achievements = tk.Entry(self)
        self.achievements.pack()

        self.submit4 = tk.Button(self, text="Submit", command=self.submit_choice4)
        self.submit4.pack()

        self.submit5 = tk.Button(self, text="Create Resume", command=self.resume_create)
        self.submit5.pack()


    def submit_choice4(self):
        compN = self.comp.get()
        jobN = self.job.get()
        locationN = self.location.get()
        datesN = self.dates.get()
        compDescN = self.compDesc.get()
        jobDescN = self.jobDesc.get()
        achievementsN = self.achievements.get()
        self.experiences.append([compN, jobN, locationN, datesN, compDescN, jobDescN, achievementsN])
        self.comp.delete(0, tk.END)
        self.job.delete(0, tk.END)
        self.location.delete(0, tk.END)
        self.dates.delete(0, tk.END)
        self.compDesc.delete(0, tk.END)
        self.jobDesc.delete(0, tk.END)
        self.achievements.delete(0, tk.END)

    def clear_all(self):
        for widget in self.winfo_children():
            widget.destroy()

    def resume_create(self):
        self.clear_all()
        print(self.resumeLevel)
        if self.resumeLevel == "Entry Level":
            self.cv = Resume.entryLevel(self.name, self.city, self.state, self.zip_code, self.phone, self.email,
                                        self.job, self.skills, self.education, self.experiences)
        elif self.resumeLevel == "Mid Level":
            self.cv = Resume.midLevel(self.name, self.city, self.state, self.zip_code, self.phone, self.email, self.job,
                                      self.skills, self.education, self.experiences)
        elif self.resumeLevel == "Senior Level":
            self.cv = Resume.seniorLevel(self.name, self.city, self.state, self.zip_code, self.phone, self.email,
                                         self.job, self.skills, self.education, self.experiences)
        elif self.resumeLevel == "Executive Level":
            self.cv = Resume.executiveLevel(self.name, self.city, self.state, self.zip_code, self.phone, self.email,
                                            self.job, self.skills, self.education, self.experiences)
        pattern = r'\\u[^"]*'
        self.resume = tk.Label(self, wraplength=500, text=self.cv).pack()
        self.option = tk.Label(self, text="Write any adjustments you would like in the box below, if none then just press save.")

        self.adjustments = tk.Entry(self, width=150)
        self.adjustments.pack()
        self.adjust = tk.Button(self, text="Rewrite", command=self.rewrite_resume)
        self.adjust.pack()

        self.save = tk.Button(self, text="Save", command=self.save_resume)
        self.save.pack()

    def new_resume_show(self, res):
        self.clear_all()
        pattern = r'\\u[^"]*'
        self.resume = tk.Label(self, wraplength=700, text=res).pack()
        self.option = tk.Label(self, text="Write any new adjustments you would like in the box below, if none then just press save.")

        self.adjustments = tk.Entry(self, width=150)
        self.adjustments.pack()
        self.adjust = tk.Button(self, text="Rewrite", command=self.rewrite_resume)
        self.adjust.pack()

        self.save = tk.Button(self, text="Save", command=self.save_resume)
        self.save.pack()

    def rewrite_resume(self):
        self.toAdjust = self.adjustments.get()
        self.adjustedResume = Resume.adjust(self.toAdjust, self.cv)
        self.new_resume_show(self.adjustedResume)

    def save_resume(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".doc", filetypes=[("Word Document", "*.docx")])
        document = Document()
        style = document.styles['Normal']
        font = style.font
        font.size = Pt(16)
        if file_path:
            # Save the file
            with open(file_path, "a+") as file:
                if self.adjustedResume != '':
                    document.add_paragraph(self.adjustedResume)
                    document.save(file_path)
                else:
                    document.add_paragraph(self.cv)
                    document.save(file_path)

            # Notify the user that the file has been saved
            messagebox.showinfo("Resume saved", f"The resume has been saved at {file_path}")
        self.clear_all()
        self.experiences = []
        self.create_widgets()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
