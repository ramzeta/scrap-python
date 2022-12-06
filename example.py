'''
import requests
from bs4 import BeautifulSoup
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)


'''


from bs4 import BeautifulSoup
import requests


url = requests.get('https://www.xataka.com/tag/python')

soup = BeautifulSoup(url.content, 'html.parser')
entries = soup.find_all('header')
print(entries)
for entry in entries:
  title = entry.title
  summary = entry.summary
  #print(f"Title: {title}  Summary{summary}")

  #import beautifulsoup and request here
from bs4 import BeautifulSoup
import requests
import json
#dfrom flask import Flask, render_template

#app = Flask(__name__)
#@app.route("/")
def displayJobDetails():
    #write a code to give call to json file and then render html page

    return render_template('index.html',responseJSON = responseJSON)

#function to get job list from url f'https://www.talent.com/jobs?k={role}&l={location}'
def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    # Complete the missing part of this function here
    response = requests.get(url, params={"k": role, "l": location})
    jobs = BeautifulSoup(response.text, 'html.parser')
    job_descriptions = []
    jobCards = jobs.find_all('div', class_='card card__job')

    # loop through jobCards
    for link in jobCards:
        # find job title
        jobTitle = link.find('h2', class_='card__job-title').string.strip()

        # find company name
        companyName = link.find('div', class_='card__job-empname-label').children
        # iterate through children
        for child in companyName:
            companyName = child
            break
        companyName = companyName.string.strip()

        # find job description
        description = link.find('p', class_='card__job-snippet').string.strip()

        # find salary
        salary = link.find('div', class_='card__job-badge-salary')
        # not all jobs include salary
        if salary == None:
            salary = "Salary not listed"
        else:
            salary = salary.string.strip()

        # append info to list and print out
        jobInfo = "Job Title: " + jobTitle + "\nCompany Name: " + companyName + "\nDescription: " + description + "\nSalary: " + salary
        job_descriptions.append(jobInfo)
        print(jobInfo + "\n\n")
    return job_descriptions

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    for i in range(len(jobDetails)):
        jobDetails[i] = jobDetails[i].replace("\n",", ")
    json_file = open("jobDetails.json", "w")
    json.dump(jobDetails, json_file)
    json_file.close()
    print("Saved job details to JSON file.")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("\nEnter desired location")
    location = input()
    print("\nYou entered: " + role + ", " + location + ".\n")

    jobDetails = getJobList(role, location)
    saveDataInJSON(jobDetails)

if __name__ == '__main__':
    main()