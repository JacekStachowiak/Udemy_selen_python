from selenium.webdriver.common.by import By
class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        
        loginLink = self.driver.find_element(By.XPATH, '//a[text()="Sign In"]')
        loginLink.click()
                
        emailField = self.driver.find_element(By.ID, 'email')
        emailField.send_keys(username)
        
        passwordField = self.driver.find_element(By.ID, 'password')
        passwordField.send_keys(password)
        
        loginButton = self.driver.find_element(By.XPATH, '//input[@class="btn btn-default btn-block btn-md dynamic-button"]')
        loginButton.click()
        
        allCourse = self.driver.find_element(By.XPATH, '//a[text()="ALL COURSES"]')
        allCourse.click()
        
    