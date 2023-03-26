def expCreate(experiences):
    xp = ''
    for i in range(0, len(experiences)):
        temp = f'''Experience {i+1}:
        “
        Company Name: {experiences[i][0]}
        Title of Position: {experiences[i][1]}
        Location: {experiences[i][2]}
        Dates: {experiences[i][3]}
        Description of Company: “{experiences[i][4]}”
        Job Description: “{experiences[i][5]}"
        Achievements:”{experiences[i][6]}”
        "

        '''
        xp = xp + temp
    return xp


def create(name, city, state, zip_code, phone, email, job, skills, education):
    prompt = f'''Name: {name}
        City: {city}
        State: {state}
        Zip: {zip_code}
        Email: {email}
        Phone: {phone}
        Title: {job}
        Skills:”{skills}”
        Education: “{education}”
        '''
    return prompt

def createEntry(name, city, state, zip_code, phone, email, job, skills, education, experiences):
    prompt = f'''Name: {name}
        City: {city}
        State: {state}
        Zip: {zip_code}
        Email: {email}
        Phone: {phone}
        Title: {job}
        Skills:”{skills}”
        Education: “{education}”
        '''
    xp = expCreate(experiences)
    prompt = prompt + xp
    return prompt