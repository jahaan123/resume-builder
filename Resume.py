import openai
import pandas as pd
import prompt
import json
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

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

def prompts_completion(level):
    data = pd.read_excel(io="Resume.xlsx")
    x = data[data['Level'] == level]
    prompts1 = [x.loc[x.index[0], 'Prompt 1'], x.loc[x.index[1], 'Prompt 1']]
    completions1 = [x.loc[x.index[0], 'Completion 1'], x.loc[x.index[1], 'Completion 1']]
    prompts2 = [x.loc[x.index[0], 'Prompt 2'], x.loc[x.index[1], 'Prompt 2']]
    completions2 = [x.loc[x.index[0], 'Completion 2'], x.loc[x.index[1], 'Completion 2']]
    return prompts1, prompts2, completions1, completions2

def level():
    print("Please select the level of resume you want to create as the number option:")
    print("1) Entry Level")
    print("2) Mid Level")
    print("3) Senior Level")
    print("4) Executive Level")
    choice = input()
    return choice


def entryLevel(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    data = pd.read_excel(io="Resume.xlsx")
    x = data[data['Level'] == "Entry"]
    prompts = [x.loc[x.index[0], 'Prompt 1'], x.loc[x.index[1], 'Prompt 1']]
    completions = [x.loc[x.index[0], 'Completion 1'], x.loc[x.index[1], 'Completion 1']]
    resume = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an accredited resume writer. You have been writing resumes for over 20 years and have landed your clients jobs in some of the world's largest companies. You specialize in writing Entry Level resumes that are short and concise."},
            {"role": "user", "content": prompts[0]},
            {"role": "assistant", "content": completions[0]},
            {"role": "user", "content": prompts[1]},
            {"role": "assistant", "content": completions[1]},
            {"role": "user", "content": json.dumps(
                prompt.createEntry(name, city, state, zip_code, phone, email, job, skills, education, experiences))}
        ],
        temperature = 0.6
    )
    return resume["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")


def midLevel(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    prompts1, prompts2, completions1, completions2 = prompts_completion("Mid")
    basic = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an accredited resume writer. You have been writing resumes for over 20 years and have landed your clients jobs in some of the world's largest companies. You specialize in writing Mid Level resumes that are short and concise."},
            {"role": "user", "content": prompts1[0]},
            {"role": "assistant", "content": completions1[0]},
            {"role": "user", "content": prompts1[1]},
            {"role": "assistant", "content": completions1[1]},
            {"role": "user",
             "content": json.dumps(prompt.create(name, city, state, zip_code, phone, email, job, skills, education))}],
        temperature = 0.6
    )
    experiences = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an accredited resume writer. You have been writing resumes for over 20 years and have landed your clients jobs in some of the world's largest companies. You specialize in writing Mid Level resumes that are short and concise."},
            {"role": "user", "content": prompts2[0]},
            {"role": "assistant", "content": completions2[0]},
            {"role": "user", "content": prompts2[1]},
            {"role": "assistant", "content": completions2[1]},
            {"role": "user", "content": json.dumps(prompt.expCreate(experiences))}],
        temperature = 0.4
    )
    basic = basic["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")
    experiences = experiences["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")
    resume = basic + experiences
    return resume


def seniorLevel(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    prompts1, prompts2, completions1, completions2 = prompts_completion("Senior")
    basic = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an accredited resume writer. You have been writing resumes for over 20 years and have landed your clients jobs in some of the world's largest companies. You specialize in writing Senior Level resumes that are short and concise."},
            {"role": "user", "content": prompts1[0]},
            {"role": "assistant", "content": completions1[0]},
            {"role": "user", "content": prompts1[1]},
            {"role": "assistant", "content": completions1[1]},
            {"role": "user",
             "content": json.dumps(prompt.create(name, city, state, zip_code, phone, email, job, skills, education))}],
        temperature = 0.6
    )
    experiences = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an accredited resume writer. You have been writing resumes for over 20 years and have landed your clients jobs in some of the world's largest companies. You specialize in writing Senior Level resumes that are short and concise."},
            {"role": "user", "content": prompts2[0]},
            {"role": "assistant", "content": completions2[0]},
            {"role": "user", "content": prompts2[1]},
            {"role": "assistant", "content": completions2[1]},
            {"role": "user", "content": json.dumps(prompt.expCreate(experiences))}],
        temperature = 0.4
    )
    basic = basic["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "").replace(r".!\application.!entry11", "").replace(r".!application.!entry11", "")
    experiences = experiences["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "").replace(r"\u", "")
    resume = basic + experiences
    return resume.replace(r"\xa0", "")


def executiveLevel(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    prompts1, prompts2, completions1, completions2 = prompts_completion("Executive")
    basic = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an accredited resume writer. You have been writing resumes for over 20 years and have landed your clients jobs in some of the world's largest companies. You specialize in writing Executive Level resumes that are short and concise."},
            {"role": "user", "content": prompts1[0]},
            {"role": "assistant", "content": completions1[0]},
            {"role": "user", "content": prompts1[1]},
            {"role": "assistant", "content": completions1[1]},
            {"role": "user",
             "content": json.dumps(prompt.create(name, city, state, zip_code, phone, email, job, skills, education))}],
        temperature = 0.4
    )
    experiences = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an accredited resume writer. You have been writing resumes for over 20 years and have landed your clients jobs in some of the world's largest companies. You specialize in writing Executive Level resumes that are short and concise."},
            {"role": "user", "content": prompts2[0]},
            {"role": "assistant", "content": completions2[0]},
            {"role": "user", "content": prompts2[1]},
            {"role": "assistant", "content": completions2[1]},
            {"role": "user", "content": json.dumps(prompt.expCreate(experiences))}],
        temperature = 0.4
    )
    basic = basic["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")
    experiences = experiences["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")
    resume = basic + experiences
    return resume

def adjust(prompt, resume):
    newResume = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an accredited resume writer. You have been writing resumes for over 20 years and have landed your clients jobs in some of the world's largest companies. Edit the current resume according to the prompt"},
            {"role": "user", "content": resume + " And this is the prompt " + prompt}
            ],
        temperature = 0.4
    )

    return newResume["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")