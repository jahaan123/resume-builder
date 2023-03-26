def getvariables():
    print("First input your general information below.\n")
    name = input("Name: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("Zip Code: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    job = input("Job Goal: ")
    print("Next please list all relavant skills you have below:")
    skills = input()
    print(
        "Now list your education in the following format:\ncollege or high school, major, any other information (optional), year. Separate each education with a .")
    education = input()
    return name, city, state, zip_code, phone, email, job, skills, education


def experiences():
    exp = []
    num = input("How many experiences do you have (max 4): ")
    for i in range(0, int(num)):
        company = input("Company Name: ")
        job = input("Job Title: ")
        location = input("Location: ")
        dates = input("Dates: ")
        comp_desc = input("Company description: ")
        job_desc = input("Job Description: ")
        achievements = input("Achievements: ")
        exp.append([company, job, location, dates, comp_desc, job_desc, achievements])
    return exp