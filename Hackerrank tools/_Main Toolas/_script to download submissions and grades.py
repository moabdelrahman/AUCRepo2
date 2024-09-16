from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import json
import os

cookies = '__utma=74197771.497241019.1633190584.1684404854.1684433358.218;__utmb=74197771.15.9.1684433377204;__utmc=74197771;__utmt=1;__utmz=74197771.1651036066.90.5.utmcsr=cu.blackboard.com|utmccn=(referral)|utmcmd=referral|utmcct=/;_biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%2C%22Frm%22%3A%221%22%7D;_biz_nA=3349;_biz_pendingA=%5B%5D;_biz_sid=6ef968;_biz_uid=1c2bb74ccaa549feab765913feb6a065;_ce.clock_data=-110672%2C45.247.73.90%2C1;_ce.clock_event=1;_ce.s=v~39c5107d0ad109593d80d69385f866a7212704fb~vpv~5~lcw~1684108673099~lcw~1684433380962;_clck=11pytcs|1|f5q|0;_fcdscst=MTY4NDQzMzM3OTU1MQ==;_fcdscv=eyJDdXN0b21lcklkIjoiOWUyMDZiMGQtMDAxNC00MmI5LThkMzktYzJiOTA5NGEyNzMxIiwiVmlzaXRvciI6eyJFbWFpbCI6bnVsbCwiRXh0ZXJuYWxWaXNpdG9ySWQiOiI3NTdkOTBkNy05OWQ0LTRmODItYWJiNC05OGYxNzc4YTQ5YzEifSwiVmlzaXRzIjpbXSwiQWN0aXZpdGllcyI6W10sIkRpYWdub3N0aWNNZXNzYWdlIjpudWxsfQ==;_ga=GA1.2.497241019.1633190584;_ga_0QME21KCCM=GS1.1.1684433381.5.1.1684433485.0.0.0;_ga_4G810X81GK=GS1.1.1684433381.5.1.1684433485.0.0.0;_ga_BCP376TP8D=GS1.1.1684433381.6.1.1684433485.0.0.0;_ga_R0S46VQSNQ=GS1.1.1684433382.5.1.1684433485.0.0.0;_ga_X2HP4BPSD7=GS1.1.1684433381.6.1.1684433485.0.0.0;_ga_ZDWKWB1ZWT=GS1.1.1684433382.5.1.1684433485.0.0.0;_gcl_au=1.1.1417843098.1676845522;_gid=GA1.2.1716822114.1684405237;_hjAbsoluteSessionInProgress=0;_hjid=a0059dde-0ebb-464d-8e7b-e9ca4103d610;_hjIncludedInSessionSample_2036154=0;_hjSession_2036154=eyJpZCI6Ijc1MzUwNzExLTAxOGUtNDI2OS1hMzI0LTdlOGZkNjM5Yzc0OCIsImNyZWF0ZWQiOjE2ODQ0MzM1MDAzOTMsImluU2FtcGxlIjpmYWxzZX0=;_hjSessionUser_2036154=eyJpZCI6Ijc5YjkxNjQ3LTQyMmEtNTgzMC1hOTE2LTI3YWI1YjJmNGFjYSIsImNyZWF0ZWQiOjE2Mzc2MTY2Njk4NTAsImV4aXN0aW5nIjp0cnVlfQ==;_hp2_id.547804831=%7B%22userId%22%3A%228142445880749916%22%2C%22pageviewId%22%3A%227965140616895061%22%2C%22sessionId%22%3A%225757973531091847%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D;_hp2_ses_props.547804831=%7B%22r%22%3A%22https%3A%2F%2Fwww.hackerrank.com%2Fadministration%2Fcontests%22%2C%22ts%22%3A1684433382125%2C%22d%22%3A%22www.hackerrank.com%22%2C%22h%22%3A%22%2F%22%7D;_mkto_trk=id:487-WAY-049&token:_mch-hackerrank.com-1633190595381-13383;_uetsid=28d9a0b0f5a711eda1b0cfe68cd9b87d;_uetvid=394c9d80239a11ec9c13f99962650c06;cebs=1;cebsp_=2;h_l=in_app;h_r=auth_dialog;h_v=_default;hackerrank_mixpanel_token=f71ca374-d04c-43b0-8e43-4a0a1acee9f0;mp_bcb75af88bccc92724ac5fd79271e1ff_mixpanel=%7B%22distinct_id%22%3A%20%22eecfd32c-8cab-4d2c-a389-9c3bbebda660%22%2C%22%24device_id%22%3A%20%2217c41be9a9b201-093786995c80da-b7a1a38-e1000-17c41be9a9c38c%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%22eecfd32c-8cab-4d2c-a389-9c3bbebda660%22%7D;optimizelyBuckets=%7B%7D;optimizelyEndUserId=oeu1634468993243r0.34553903057348934;optimizelySegments=%7B%221709580323%22%3A%22false%22%2C%221717251348%22%3A%22gc%22%2C%221719390155%22%3A%22referral%22%2C%222308790558%22%3A%22none%22%7D;user_theme=dark;user_type=hacker;_gd_session=f1d702e9-5f35-4eb1-8a67-32da75741993;_gd_svisitor=6b221102207300008e98f9600c0000001b570100;_gd_visitor=af132a60-02d8-418a-885f-a3d4b6ba4417;_hrank_session=dc12584eff35d7affd6115cf093009db;_pk_id.5.fe0a=3c3d0f71929940d4.1670576582.;_pk_ses.5.fe0a=1;_wchtbl_sid=4f38a46d-5e13-459d-ab1e-2c66a45911d6;_wchtbl_uid=c4cdca5d-10a1-4048-8fe6-ec034aa89e0e;assignment-3-semester_crp=*nil*;assignment-one-semester_crp=*nil*;assignment-two_crp=*nil*;boss-liar-trial_crp=*nil*;cccmpn102-labexam-47777-s23_crp=*nil*;cmp-assignment_crp=*nil*;cmp1040-ass-s2022_crp=*nil*;cmp2030-fall2020-lab5-semester_crp=*nil*;cmp2030-fall2021-hw1_crp=*nil*;cmp2030-fall2021-hw3_crp=*nil*;cmp2030-fall2021-hw4_crp=*nil*;cmp2030-fall2021-hw5_crp=*nil*;cmp2030-fall2021-lab0_crp=*nil*;cmp2030-fall2021-lab4_crp=*nil*;cmp2030-fall2021-lab5-new_crp=*nil*;cmp2030-fall2021-lab5-semester_crp=*nil*;cmp2030-fall2021-lab5-updated_crp=*nil*;cmp2030-fall2022-hw4_crp=*nil*;cmp302-fall2020-lab1_crp=*nil*;cmpn103-fall2021-hw5-sunday_crp=*nil*;cmpn1040-labexam-morning_crp=*nil*;cmpn302-f2022-lab5-sunday_crp=*nil*;cmpn302-f22-llabexam4-tuuuesss_crp=*nil*;cmpn302-fall2021-lab6-sund_crp=*nil*;cmpn302-fall2022-hw1_crp=*nil*;cmpn302-fall2022-hw4_crp=*nil*;cmpn302-s2022-hw1_crp=*nil*;cmpn302-s2022-hw3_crp=*nil*;cmpn302-s2022-lab1_crp=*nil*;cmpn302-s2022-lab5_crp=*nil*;cmpn302-s2023-hw1_crp=*nil*;cmpn302-s2023-labexammm_crp=*nil*;dp-bonus-question_crp=*nil*;enableIntellisenseUserPref=true;f21-lab1-trial_crp=*nil*;hacker_editor_theme=light;homepage_variant=https://www.hackerrank.com/;hrc_l_i=T;labexam-sem-ssection2_crp=*nil*;ln_or=eyI0Nzc3MCI6ImQifQ%3D%3D;metrics_user_identifier=10063dc-e9da0c6918475d82666575ada5be02edec06daba;react_var=true__trm6;react_var2=true__trm6;referrer=direct;session_id=6z216wd7-1684433356393;show_cookie_banner=false;'


def get_page(driver, url):
    while True:
        try:
            driver.get(url)
            break
        except Exception as e:
            print("Failed to get page : " + url + "\n")
            print(e)

def initiate():

    WEB_URL = "https://www.hackerrank.com/login"
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10) # give time for slow connections
    get_page(driver,WEB_URL) # gets hacker rank main page
    username = "cmpn1040@gmail.com"#input("Please enter your username/email: \n")
    password = "#CMPN$1040!"#input("Please enter your password : \n")

    driver.find_element(By.ID, 'input-1').send_keys(username) # enter username
    driver.find_element(By.ID, 'input-2').send_keys(password) # enter password
    driver.find_element(By.XPATH, '//*[@id="tab-1-content-1"]/div[1]/form/div[4]/button').click() # submit form
    return driver

def get_contests(driver):
    contests = {}
    time.sleep(2)
    for i in range(2,4):
        get_page(driver, str.format("https://www.hackerrank.com/administration/contests/page/{}", i))
        time.sleep(2)
        contest_table = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/section/div[2]')
        contest_links = contest_table.find_elements(By.TAG_NAME, 'a')
        for link in contest_links:
            div = link.find_element(By.CLASS_NAME, 'alignL')
            p = div.find_element(By.TAG_NAME, "p")
            contests[p.text] = link.get_attribute('href')
    return contests

def choose_contest(contests):
    c = 1
    print("\nPlease enter the number of the contest to downlaod the grades for :")
    ncontests = {}
    names = {}
    for contest in contests:
        print(str(c) + ") " + contest + "\n")
        ncontests[str(c)] = contests[contest]
        names[str(c)] = contest
        c+=1
    cid = input('')
    return ncontests[cid]+"/details",names[cid]

def fetchCode(contest, id, username):
    code_url = f"https://www.hackerrank.com/rest/contests/{contest}/submissions/{id}?&_=1666788904258"
    response = requests.get(code_url, headers={"cookie": cookies, "User-Agent": "PostmanRuntime/7.29.2"})
    while response.status_code == 429:
        time.sleep(2)
        response = requests.get(code_url, headers={"cookie": cookies, "User-Agent": "PostmanRuntime/7.29.2"})
    if response.status_code == 200:
        print(f"Done Fetching {username} code")
        return response.json()["model"]["code"]
    else:
        print(response.status_code)
        print(f"Error Fetching {username} code")
        return ""

def get_all_submissions_grades(driver, contest_link, contest_name):
    get_page(driver, contest_link)
    contest_name = driver.find_elements(By.CLASS_NAME, 'model-slug')[0].get_attribute('href')[27:]
    get_page(driver, driver.find_element(By.PARTIAL_LINK_TEXT, 'all contest submissions').get_attribute('href'))
    submissions_dictionary = {}
    challenges = []
    while True:
        try:
            submissions = driver.find_elements(By.CLASS_NAME, 'judge-submissions-list-view')

            for submission in submissions:
                submission_challenge = submission.find_elements(By.TAG_NAME, 'a')[0].text
                submission_ps = submission.find_elements(By.CSS_SELECTOR, 'p[class="small"]')
                during_contest = submission_ps[3].text == "Yes"
                if(not during_contest):
                    continue
                submission_grade = float(submission_ps[2].text)
                submission_link = submission.find_elements(By.TAG_NAME, 'a')[2].get_attribute('href')
                submission_user = submission.find_elements(By.TAG_NAME, 'a')[1].text
                submission_ID = submission.find_elements(By.TAG_NAME, 'p')[2].text

                if(not (submission_user in submissions_dictionary)):
                    submissions_dictionary[submission_user] = {}
                if (not submission_challenge in challenges):
                    challenges.append(submission_challenge)
                if(not (submission_challenge in submissions_dictionary[submission_user])):
                    submissions_dictionary[submission_user][submission_challenge] = {}
                    submissions_dictionary[submission_user][submission_challenge]["grade"] = -1.0
                    submissions_dictionary[submission_user][submission_challenge]["code"] = ""
                if submissions_dictionary[submission_user][submission_challenge]["grade"] <  submission_grade:
                    submissions_dictionary[submission_user][submission_challenge]["grade"] = submission_grade
                    submissions_dictionary[submission_user][submission_challenge]["code"] = fetchCode(contest_name, submission_ID, submission_user)


            time.sleep(2)
            pagination = driver.find_element(By.CSS_SELECTOR, 'div[class="pagination"]')
            next_page = pagination.find_elements(By.TAG_NAME, 'li')[-2]
            if next_page.get_attribute('class') == "disabled":
                break
            else:
                next_page.find_element(By.TAG_NAME, 'a').click()
        except Exception as e:
            print(e)
    return submissions_dictionary,challenges

def save_grades(grades,challenges,name):
        now = datetime.now()
        f = open(name+"_grades.txt","w")
        f.write("username\t")
        for challenge in challenges:
            f.write(challenge + "\t")
        f.write("\n")
        for user in grades:
            f.write(user+"\t")
            for challenge in challenges:
                if(challenge in grades[user]):
                    f.write(str(grades[user][challenge]) + "\t")
                else:
                    f.write("0.0" + "\t")
            f.write("\n")
        f.close()

def save_grades_csv(grades,challenges,name):
        now = datetime.now()
        try:
            os.mkdir(name)
        except:
            pass
        f = open(name+'/'+name+"_grades.csv","w")
        f.write("username,")
        for challenge in challenges:
            f.write(challenge + ",")
            try:
                os.mkdir(name+'/'+challenge)
            except:
                pass
        f.write("\n")
        for user in grades:
            f.write(user+",")
            for challenge in challenges:
                if(challenge in grades[user]):
                    f.write(str(grades[user][challenge]["grade"]) + ",")
                    with open(name + '/' + challenge + '/' + user + '.cpp', 'w') as fi:
                        fi.write(grades[user][challenge]["code"])
                else:
                    f.write("0.0" + ",")
            f.write("\n")
        f.close()

def main():
    driver = initiate()
    contests = get_contests(driver)
    contest_link,name = choose_contest(contests)
    grades,challenges = get_all_submissions_grades(driver, contest_link, name)
    save_grades_csv(grades,challenges,name)
    time.sleep(5)

if __name__ == "__main__":
    main()