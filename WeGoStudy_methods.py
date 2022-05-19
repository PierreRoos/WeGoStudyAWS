
from time import sleep
import datetime
import wegostudy_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)


s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Test starts at {datetime.datetime.now()}.')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.app_url)

    if driver.current_url == locators.app_url and locators.homepage_title in driver.title:
        print(f'{locators.app} website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch successfully, please check your code and launch again!')
        print(f'Current URL: {driver.current_url}, Current page title: {driver.title}.')
        driver.close()
        driver.quit()


def tearDown():
    if driver is not None:
        print(f'---------The test is passed.----------------')
        print(f'---------The test is completed on {datetime.datetime.now()}.-------------')
        sleep(0.5)
        driver.close()
        driver.quit()


def login():
    driver.find_element(By.XPATH, '//b[normalize-space()="LOGIN"]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'user_email').send_keys(locators.admin_email)
    sleep(0.25)
    driver.find_element(By.ID, 'user_password').send_keys(locators.admin_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@value="SIGN IN"]').click()
    sleep(0.5)
    driver.find_element(By.ID, 'authentication-popup').is_displayed()
    sleep(3)
    print('------------Signed up successfully!-----------------')


def logout():
    driver.find_element(By.CSS_SELECTOR, 'span[class="my-auto mr-2 pf-name"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[contains(., "Log out")]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'authentication').is_displayed()
    sleep(0.25)
    print('-----------------Signed out successfully.-----------------')


def create_new_student():
    if driver.current_url == locators.login_page_url:
        print(f'----------Current URL: {locators.login_page_url}--------')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(0.25)
    if driver.current_url == locators.student_page_url:
        print(f'-------------Create New Student----------------------')
    driver.find_element(By.XPATH, '//a[normalize-space()="Create New Student"]').click()
    sleep(0.25)

    # date of birth
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('1')
    sleep(1.5)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(10 * Keys.BACKSPACE)
    sleep(1.5)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(locators.birthday)
    sleep(0.5)

    # select citizenship
    driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
    sleep(1.25)
    driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(locators.country)
    sleep(1.25)
    driver.find_element(By.CLASS_NAME, 'select2-search__field').send_keys(Keys.RETURN)
    sleep(1.25)

    # select country
    driver.find_element(By.XPATH, '//span[text()="Country"]').click()
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'chosen-search-input').send_keys('Australia')
    sleep(0.25)
    driver.find_element(By.CLASS_NAME, 'chosen-search-input').send_keys(Keys.RETURN)
    sleep(0.25)
    # x = random.randint(1,20)
    # driver.find_element(By.XPATH, f'//li[@data-option-array-index="{x}"]').click()
    # sleep(0.5)

    # select province
    driver.find_element(By.XPATH, '//span[text()="Province/State"]').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//li[@data-option-array-index = "1"]').click()
    sleep(0.5)
    # y = random.randint(1,2)
    # driver.find_element(By.XPATH, f'(//li[@data-option-array-index = "{y}"])[2]').click()
    # sleep(0.5)
    # driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/div/input').send_keys(Keys.RETURN)
    # sleep(0.25)

    # select city
    driver.find_element(By.XPATH, '//span[text()="City"]').click()
    sleep(0.5)

    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/ul/li[2]').click()
    sleep(0.5)
    # driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/div/input').send_keys(Keys.RETURN)
    # sleep(0.25)

    # select Credentials
    driver.find_element(By.XPATH, '//span[contains(., "Credentials")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(
        'Degree')
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_credentials_chosen"]/div/div/input').send_keys(
        Keys.RETURN)
    sleep(0.25)

    # select GPA Scale
    driver.find_element(By.XPATH, '//span[contains(., "GPA Scale")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys(
        '100')
    sleep(0.25)
    driver.find_element(By.XPATH,
                        '//*[@id="user_student_detail_attributes_user_educations_attributes_0_gpa_scale_chosen"]/div/div/input').send_keys(
        Keys.RETURN)
    sleep(0.25)

    for i in range(len(locators.lst_column)):
        clm, fid, val = locators.lst_column[i], locators.lst_id[i], locators.lst_value[i]
        driver.find_element(By.ID, fid).send_keys(str(val))
        sleep(0.25)

    driver.find_element(By.XPATH, '//input[@value="Save"]').click()
    sleep(0.5)
    driver.find_element(By.CLASS_NAME, 'toast-message').is_displayed()
    sleep(5)
    print('-------------Student is created successfully.-----------')


def create_new_application():
    print(f'*****************Course Information******************')

    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    # driver.find_element(By.CSS_SELECTOR, 'a[aria-expanded="false"] span[class="my-auto mr-2"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(0.75)
    driver.find_element(By.LINK_TEXT, 'Create Application').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select School"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_institute_detail_id_chosen"]/div/ul/li[7]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select Course"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_institute_program_id_chosen"]/div/ul/li[2]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select Starting Semester"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_starting_semester_chosen"]/div/ul/li[3]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select Start Day"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_start_day_chosen"]/div/ul/li[3]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//span[normalize-space()="Select Year"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//*[@id="admission_start_year_chosen"]/div/ul/li[3]').click()
    sleep(0.75)
    driver.find_element(By.CSS_SELECTOR, '#admission_last_name').send_keys(locators.last_name)
    sleep(0.75)
    driver.find_element(By.XPATH, '//input[@id="admission_electronic_communication_true"]').click()
    sleep(0.75)
    driver.find_element(By.XPATH, '//input[@name="commit"]').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'toast-message').is_displayed()
    sleep(4)
    print('-------------application is created successfully.-----------')

def view_details():
    print(f'***************** View Details ******************')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    # driver.find_element(By.CSS_SELECTOR, 'a[aria-expanded="false"] span[class="my-auto mr-2"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(4)
    driver.find_element(By.XPATH, '//a[@href="/partners/student_details/christopher-knapp"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//body//form').click()
    sleep(6)

# setUp()
# login()
# create_new_student()
# create_new_application()
# view_details()
# logout()
# tearDown()