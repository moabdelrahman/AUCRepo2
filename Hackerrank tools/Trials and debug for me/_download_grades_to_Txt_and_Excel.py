#How to use this script to downlaod hackerrank scores for certain contest
#NOTICE that This script donwloads BEST score for each challenge in the contest
#   1- first install the required modules as follows:
#       python -m pip install selenium
#       python -m pip install webdriver-manager
#       python -m pip install xlwt
#   2- You will be prompted to enter
#       username & password
#       contest name
#       File to save scores in (text and Excel)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
from xlwt import Workbook



def get_page(driver, url):
    while True:
        try:
            driver.get(url)
            break
        except Exception as e:
            print("Failed to get page : " + url + "\n")
            print(e)

def initiate(username, password):

    WEB_URL = "https://www.hackerrank.com/login"
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10) # give time for slow connections
    get_page(driver,WEB_URL) # gets hacker rank main page

    driver.find_element(By.ID, 'input-1').send_keys(username) # enter username
    driver.find_element(By.ID, 'input-2').send_keys(password) # enter password
    driver.find_element(By.XPATH, '//*[@id="tab-1-content-1"]/div[1]/form/div[4]/button').click() # submit form
    return driver

def get_contests(driver):
    time.sleep(5)
    get_page(driver, "https://www.hackerrank.com/administration/contests")
    contests = {}
    
    while True:
        try:
            contest_table = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/section/div[2]')
            contest_links = contest_table.find_elements(By.TAG_NAME, 'a')
            for link in contest_links:
                div = link.find_element(By.CLASS_NAME, 'alignL')
                p = div.find_element(By.TAG_NAME, "p")
                contests[p.text] = link.get_attribute('href')
                
                
            pagination = driver.find_element(By.CSS_SELECTOR, 'div[class="pagination"]')
            next_page = pagination.find_elements(By.TAG_NAME, 'li')[-2]
            if next_page.get_attribute('class') == "disabled":
                break
            else:
                next_page.find_element(By.TAG_NAME, 'a').click()
        except Exception as e:
            print(e)
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
    
    

def get_all_submissions_grades(driver, contest_link):
    get_page(driver, contest_link)
   # get_page(driver,"https://www.hackerrank.com/contests/labexam-sem-ssection2/judge/submissions")
    submissions_dictionary = {}
    challenges = []
    while True:
        try:
            submissions = driver.find_elements(By.CLASS_NAME, 'judge-submissions-list-view')
            ##
            print (submissions)
            ##
            for submission in submissions:
                submission_challenge = submission.find_elements(By.TAG_NAME, 'a')[0].text
                submission_ps = submission.find_elements(By.CSS_SELECTOR, 'p[class="small"]')
                during_contest = submission_ps[3].text == "Yes"
                if(not during_contest):
                    continue
                submission_grade = float(submission_ps[2].text)
                submission_link = submission.find_elements(By.TAG_NAME, 'a')[2].get_attribute('href')
                submission_user = submission.find_elements(By.TAG_NAME, 'a')[1].text

                if(not (submission_user in submissions_dictionary)):
                    submissions_dictionary[submission_user] = {}
                if (not submission_challenge in challenges):
                    challenges.append(submission_challenge)
                if(not (submission_challenge in submissions_dictionary[submission_user])):
                    submissions_dictionary[submission_user][submission_challenge] = 0.0
                if submissions_dictionary[submission_user][submission_challenge] <  submission_grade:
                    submissions_dictionary[submission_user][submission_challenge] = submission_grade

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

def SaveGradesAsTxtFile(grades,challenges,name):
        now = datetime.now()
        #f = open(name+"_"+str(now)+"_grades.txt","w")

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
        
def SaveGradesAsExcelFile(grades,challenges,filename):
        wb = Workbook() # Create Workbook
        # add_sheet is used to create sheet.
        GradesSheet = wb.add_sheet('Grades Sheet')

        col = 1
        GradesSheet.write(0,0,"User Name")
        for challenge in challenges:
            GradesSheet.write(0,col,challenge)  # write challenges header row
            col = col + 1
        row = 1
        for user in grades:
            GradesSheet.write(row,0,user) #write user at 1st col
            col = 1
            for challenge in challenges:
                if(challenge in grades[user]):
                    GradesSheet.write(row,col,grades[user][challenge])
                else:
                    GradesSheet.write(row,col,0)
                col = col + 1
            row = row +1
        wb.save(filename + '.xls')


def main():
    username = input("Please enter your username/email: \n")
    password = input("Please enter your password : \n")
    print("Connecting to Hackerrank, please wait...")
    driver = initiate(username, password)
    # contests = get_contests(driver)
    # contest_link,name = choose_contest(contests)
    contest_name = input("please enter contest name:")
    SaveFile = input("please enter txt file name to save grades:")
    excl = input("Save to excel file too (y/n)?")
    if str(excl).capitalize() == 'Y':
        excelFileName = input("Enter excel file name:")
    grades,challenges = get_all_submissions_grades(driver, "https://www.hackerrank.com/contests/"+contest_name+"/judge/submissions")
    SaveGradesAsTxtFile(grades,challenges,SaveFile)
    if str(excl).capitalize() == 'Y':
        SaveGradesAsExcelFile(grades,challenges,excelFileName)
    time.sleep(5)

if __name__ == "__main__":
    main()
