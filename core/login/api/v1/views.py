from rest_framework.views import APIView
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from .serializers import LoginSerializer


class LoginAPIView(APIView):
    """
    This is a simple class to receive username & password and then send a message
    """

    serializer_class = LoginSerializer

    def post(self, request):
        # Get Username and Password from the user
        username = request.data.get('username')
        password = request.data.get('password')

        # Initialize Selenium webdriver
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 20)
        # Assuming you have Chrome driver installed
        driver.get('https://rosefakhri.com/fa')
        sleep(2)

        try:
            # Find and click on the login button
            show_login = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@show-login]")))
            show_login.click()
            sleep(2)

            # Find the username and password fields, and enter the login information
            username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='UserName']")))
            password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='Password']")))
            sleep(2)

            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)
            sleep(2)

            # Go to the new message page
            driver.get('https://rosefakhri.com/fa/profile#tab-Messages')
            sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="پیام جدید"]'))).click()
            sleep(2)

            # Fill out and submit the new message form
            title = wait.until(EC.presence_of_element_located((By.ID, "Title")))
            title.send_keys("Test Title")
            sleep(1)
            support = wait.until(EC.presence_of_element_located((By.ID, "SupportId")))
            support.send_keys("بخش مالی (فاکتور/پیش فاکتور/بازگشت وجه)")
            sleep(1)
            degree = wait.until(EC.presence_of_element_located((By.ID, "DegreeId")))
            degree.send_keys("کم")
            sleep(1)
            file_field = wait.until(EC.presence_of_element_located((By.ID, "File")))
            file_field.send_keys("test.txt")
            sleep(1)
            description = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='modal-body']//textarea[@id='Description']")))
            description.send_keys("Test Message ")
            sleep(1)
            submit = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="ارسال"]')))
            submit.click()
            sleep(5)

            # Find the table and extract the first number
            table = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "table")))
            number_element = table.find_element(By.XPATH, "//tbody/tr[1]/td[1]")
            number = number_element.text
            sleep(1)

        finally:
            # Close the browser
            driver.quit()

        return Response({"message": number})
