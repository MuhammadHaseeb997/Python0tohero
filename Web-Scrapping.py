from bs4 import BeautifulSoup
import requests
import time
print("Write Skills Whihc youa are not familiar")
unfimiliar_skills = input('>')
print(f'Filterning out {unfimiliar_skills}')
 
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate (jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date: 
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfimiliar_skills not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company name: {company_name.strip()}")
                    f.write(f"Required Skills: {skills.strip()}")
                    f.write(f"Description: {more_info}")
                print(f'File Saved: {index}')    

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} Minutes...')
        time.sleep(time_wait * 60)

