import json

import openai
import pandas as pd

import prompt
from cleantext import clean

API_KEY = "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"

# Returns the relevant system prompt according to the level
def getSystemPrompt(level):
    if level=="entry":
        return "As an experienced and accredited resume writer, your specialty is crafting well-written Entry Level resumes that effectively showcase a candidate\'s skills and experience. Your task is to write a compelling Entry Level resume for a someone who is seeking a job.\r\n\r\nYour response should clearly highlight the candidate\'s relevant education, internships, volunteer work, or other experiences that demonstrate their qualifications for the position they are applying for. The resume should be formatted in a clear and professional manner with attention to detail, spelling, and grammar, and if any field is not provided (such as education) then leave it out of the resume and do not write it.\r\n\r\nPlease note that you should highlight key skills and achievements that align with the requirements of the position. "
    else:
        return f"As an experienced and accredited resume writer, your task is to create a high-quality {level} level resume that will effectively showcase the client\'s skills and experience. Your goal is to craft a compelling document that highlights the client\'s achievements and qualifications in a clear and concise manner.\r\n\r\nYour final product should be well-written, error-free, and tailored specifically to the client\'s needs. It should include a professional summary or objective statement, a list of relevant skills and achievements, detailed descriptions of previous job roles highlighting specific accomplishments related to each role, education history if applicable, certifications or licenses earned if applicable.\r\n\r\nPlease note that while you specialize in writing Mid-Level resumes for clients who want jobs in large companies; your response should still allow for flexibility in terms of industries or positions desired by the client, and if any field is not provided (such as education) then leave it out of the resume and do not write it.."


# This function takes a level parameter and returns two lists of prompts and two lists of completions from an Excel file named "Resume.xlsx"
# The prompts and completions correspond to the specified level.
# The function first reads the Excel file using pandas and filters the data by the specified level.
# It then extracts the prompts and completions from the filtered data and stores them in separate lists.
# Finally, the function returns the two lists of prompts and two lists of completions.
def prompts_completion(level):
    # Read the Excel file using pandas
    data = pd.read_excel(io="Resume.xlsx")

    # Filter the data by the specified level and extract the prompts and completions
    x = data[data['Level'] == level]
    prompts1 = [x.loc[x.index[0], 'Prompt 1'], x.loc[x.index[1], 'Prompt 1']]
    completions1 = [x.loc[x.index[0], 'Completion 1'], x.loc[x.index[1], 'Completion 1']]
    prompts2 = [x.loc[x.index[0], 'Prompt 2'], x.loc[x.index[1], 'Prompt 2']]
    completions2 = [x.loc[x.index[0], 'Completion 2'], x.loc[x.index[1], 'Completion 2']]

    # Return the two lists of prompts and two lists of completions
    return prompts1, prompts2, completions1, completions2


# Entry level resume generation
def entryLevel(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    data = pd.read_excel(io="Resume.xlsx")
    x = data[data['Level'] == "Entry"]
    prompts = [x.loc[x.index[0], 'Prompt 1'], x.loc[x.index[1], 'Prompt 1']]
    completions = [x.loc[x.index[0], 'Completion 1'], x.loc[x.index[1], 'Completion 1']]
    resume = openai.ChatCompletion.create(
        api_key=API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": getSystemPrompt("entry")},
            {"role": "user", "content": prompts[0]},
            {"role": "assistant", "content": completions[0]},
            {"role": "user", "content": prompts[1]},
            {"role": "assistant", "content": completions[1]},
            {"role": "user", "content": json.dumps(
                prompt.createEntry(name, city, state, zip_code, phone, email, job, skills, education, experiences))}
        ],
        temperature=0.6
    )
    return clean(resume["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", ""), lower=False)


# Mid level resume generation
def midLevel(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    prompts1, prompts2, completions1, completions2 = prompts_completion("Mid")
    basic = openai.ChatCompletion.create(
        api_key=API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": getSystemPrompt("mid")},
            {"role": "user", "content": prompts1[0]},
            {"role": "assistant", "content": completions1[0]},
            {"role": "user", "content": prompts1[1]},
            {"role": "assistant", "content": completions1[1]},
            {"role": "user",
             "content": json.dumps(prompt.create(name, city, state, zip_code, phone, email, job, skills, education))}],
        temperature=0.6
    )
    experiences = openai.ChatCompletion.create(
        api_key=API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": getSystemPrompt("mid")},
            {"role": "user", "content": prompts2[0]},
            {"role": "assistant", "content": completions2[0]},
            {"role": "user", "content": prompts2[1]},
            {"role": "assistant", "content": completions2[1]},
            {"role": "user", "content": json.dumps(prompt.expCreate(experiences))}],
        temperature=0.4
    )
    basic = basic["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")
    experiences = experiences["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")
    resume = basic + experiences
    return clean(resume, lower=False)

# Senior level resume generation
def seniorLevel(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    prompts1, prompts2, completions1, completions2 = prompts_completion("Senior")
    basic = openai.ChatCompletion.create(
        api_key=API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": getSystemPrompt("senior")},
            {"role": "user", "content": prompts1[0]},
            {"role": "assistant", "content": completions1[0]},
            {"role": "user", "content": prompts1[1]},
            {"role": "assistant", "content": completions1[1]},
            {"role": "user",
             "content": json.dumps(prompt.create(name, city, state, zip_code, phone, email, job, skills, education))}],
        temperature=0.6
    )
    experiences = openai.ChatCompletion.create(
        api_key=API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": getSystemPrompt("senior")},
            {"role": "user", "content": prompts2[0]},
            {"role": "assistant", "content": completions2[0]},
            {"role": "user", "content": prompts2[1]},
            {"role": "assistant", "content": completions2[1]},
            {"role": "user", "content": json.dumps(prompt.expCreate(experiences))}],
        temperature=0.4
    )
    basic = basic["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "").replace(
        r".!\application.!entry11", "").replace(r".!application.!entry11", "")
    experiences = experiences["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "").replace(r"\u",
                                                                                                                 "")
    resume = basic + experiences
    return clean(resume, lower=False)

# Executive level resume generation
def executiveLevel(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    prompts1, prompts2, completions1, completions2 = prompts_completion("Executive")
    basic = openai.ChatCompletion.create(
        api_key=API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": getSystemPrompt("executive")},
            {"role": "user", "content": prompts1[0]},
            {"role": "assistant", "content": completions1[0]},
            {"role": "user", "content": prompts1[1]},
            {"role": "assistant", "content": completions1[1]},
            {"role": "user",
             "content": json.dumps(prompt.create(name, city, state, zip_code, phone, email, job, skills, education))}],
        temperature=0.4
    )
    experiences = openai.ChatCompletion.create(
        api_key=API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": getSystemPrompt("executive")},
            {"role": "user", "content": prompts2[0]},
            {"role": "assistant", "content": completions2[0]},
            {"role": "user", "content": prompts2[1]},
            {"role": "assistant", "content": completions2[1]},
            {"role": "user", "content": json.dumps(prompt.expCreate(experiences))}],
        temperature=0.4
    )
    basic = basic["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")
    experiences = experiences["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", "")
    resume = basic + experiences
    return clean(resume, lower=False)

# Adjust resume generation
def adjust(prompt, resume):
    newResume = openai.ChatCompletion.create(
        api_key=API_KEY,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "As an experienced and accredited resume writer, your task is to edit a client's existing resume according to their request. Your goal fulfills the client's request exactly by updating the provided resume while maintaining everything else as it was."},
            {"role": "user", "content": f"Here is the users resume:\n{resume}\n\nHere is the users request:{prompt}"}
        ],
        temperature=0.4
    )

    return clean(newResume["choices"][0]["message"]["content"].replace("\\n", "\n").replace("\r", ""), lower=False)
