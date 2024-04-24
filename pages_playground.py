class BasePage:
    def find_element(self):
        print('Finding element')

    def click(self):
        print('Clicking')

    def verify_text(self, expected_text):
        print(f'Checking {expected_text}')



class LoginPage(BasePage):

    def __init__(self):
        self.default_pw = 'Password'

    def login(self):
        print('Login...')

    def verify_terms_conditions(self):
        self.verify_text('TC text')

class RegistrationPage(BasePage):
    def register(self):
        print('Registering...')


login_page = LoginPage()
login_page.login()
login_page.click()
print(login_page.default_pw)