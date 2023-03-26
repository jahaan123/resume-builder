import Resume
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
from tkinter import font
from docx import Document
from docx.shared import Pt

class Application(tk.Frame):
    name = city = state = zip_code = phone = email = job = skills = education = ''
    experiences = []

    def __init__(self, master=None):
        super().__init__(master)
        self.cv = ''
        self.master = master
        self.pack()
        self.create_widgets()
        self.master.geometry(f"750x750")
        self.adjustedResume = ''
        self.font = font.nametofont("TkDefaultFont")
        self.update()


    def update_geometry(self):
        # Update the geometry of the window
        self.master.geometry(f"{self.winfo_reqwidth()+100}x{self.winfo_reqheight()+100}")

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
        self.nameB = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.nameB.pack()

        tk.Label(self, text="City:").pack()
        self.cityB = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.cityB.pack()

        tk.Label(self, text="State:").pack()
        self.stateB = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.stateB.pack()

        tk.Label(self, text="Zip Code:").pack()
        self.zip_codeB = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.zip_codeB.pack()

        tk.Label(self, text="Phone:").pack()
        self.phoneB = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.phoneB.pack()

        tk.Label(self, text="Email:").pack()
        self.emailB = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.emailB.pack()

        tk.Label(self, text="Job:").pack()
        self.jobB = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.jobB.pack()

        tk.Label(self, text="Skills:").pack()
        self.skillsB = tk.Text(self, height=3, width=30, font=(font, 20), bg="#F9F8F8", wrap="word")
        self.skillsB.pack()
        scrollb = tk.Scrollbar(self, command=self.skillsB.yview)
        self.skillsB['yscrollcommand'] = scrollb.set

        tk.Label(self, text="Education:").pack()
        self.educationB = tk.Text(self, height=3, width=30, font=(font, 20), bg="#F9F8F8", wrap="word")
        self.educationB.pack()

        # create submit button for the next form
        self.submit2 = tk.Button(self, text="Submit", command=self.submit_choice2)
        self.submit2.pack()


    def submit_choice2(self):
        # retrieve data from the fields
        self.name = self.nameB.get("1.0",'end-1c')
        self.city = self.cityB.get("1.0",'end-1c')
        self.state = self.stateB.get("1.0",'end-1c')
        self.zip_code = self.zip_codeB.get("1.0",'end-1c')
        self.phone = self.phoneB.get("1.0",'end-1c')
        self.email = self.emailB.get("1.0",'end-1c')
        self.job = self.jobB.get("1.0",'end-1c')
        self.skills = self.skillsB.get("1.0",'end-1c')
        self.education = self.educationB.get("1.0",'end-1c')
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
        tk.Label(self, text="Write all about the experience then press submit. Once you are done, click create resume.").pack()

        tk.Label(self, text="Company Name:").pack()
        self.comp = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.comp.pack()

        tk.Label(self, text="Job Name:").pack()
        self.job = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.job.pack()

        tk.Label(self, text="Location:").pack()
        self.location = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.location.pack()

        tk.Label(self, text="Dates:").pack()
        self.dates = tk.Text(self, height=1, width=30, font=(font, 20), bg="#F9F8F8")
        self.dates.pack()

        tk.Label(self, text="Company Description:").pack()
        self.compDesc = tk.Text(self, height=3, width=30, font=(font, 20), bg="#F9F8F8", wrap="word")
        self.compDesc.pack()

        tk.Label(self, text="Job Description:").pack()
        self.jobDesc = tk.Text(self, height=3, width=30, font=(font, 20), bg="#F9F8F8", wrap="word")
        self.jobDesc.pack()

        tk.Label(self, text="Achievements:").pack()
        self.achievements = tk.Text(self, height=3, width=30, font=(font, 20), bg="#F9F8F8", wrap="word")
        self.achievements.pack()

        self.submit4 = tk.Button(self, text="Submit", command=self.submit_choice4)
        self.submit4.pack()

        self.submit5 = tk.Button(self, text="Create Resume", command=self.resume_create)
        self.submit5.pack()



    def submit_choice4(self):
        compN = self.comp.get("1.0",'end-1c')
        jobN = self.job.get("1.0",'end-1c')
        locationN = self.location.get("1.0",'end-1c')
        datesN = self.dates.get("1.0",'end-1c')
        compDescN = self.compDesc.get("1.0",'end-1c')
        jobDescN = self.jobDesc.get("1.0",'end-1c')
        achievementsN = self.achievements.get("1.0",'end-1c')
        self.experiences.append([compN, jobN, locationN, datesN, compDescN, jobDescN, achievementsN])
        self.comp.delete("1.0","end")
        self.job.delete("1.0","end")
        self.location.delete("1.0","end")
        self.dates.delete("1.0","end")
        self.compDesc.delete("1.0","end")
        self.jobDesc.delete("1.0","end")
        self.achievements.delete("1.0","end")

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

        self.resume = tk.Label(self, wraplength=500, text=self.cv).pack()
        self.option = tk.Label(self, text="Write any adjustments you would like in the box below, if none then just press save.")
        self.option.pack()
        self.adjustments = tk.Text(self, height=3, width=30, font=(font, 20), bg="#F9F8F8", wrap="word")
        self.adjustments.pack()
        self.adjust = tk.Button(self, text="Rewrite", command=self.rewrite_resume)
        self.adjust.pack()

        self.save = tk.Button(self, text="Save", command=self.save_resume)
        self.save.pack()
        self.update()
        self.after(0, self.update_geometry)


    def new_resume_show(self, res):
        self.clear_all()

        self.resume = tk.Label(self, wraplength=700, text=res).pack()
        self.option = tk.Label(self, text="Write any new adjustments you would like in the box below, if none then just press save.")

        self.adjustments = tk.Text(self, height=5, width=40, font=(font, 20), bg="#F9F8F8", wrap="word")
        self.adjustments.pack()
        self.adjust = tk.Button(self, text="Rewrite", command=self.rewrite_resume)
        self.adjust.pack()

        self.save = tk.Button(self, text="Save", command=self.save_resume)
        self.save.pack()
        self.update()
        self.after(0, self.update_geometry)


    def rewrite_resume(self):
        self.toAdjust = self.adjustments.get("1.0",'end-1c')
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
