from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application

from support.logger import logger

#  Run Behave tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_app_tests.feature
# To export the allure JSON files created: allure serve ./(file name)/


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # HEADLESS MODE
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(options = options, service = service)

    # FIREFOX BROWSER
    # service = Service(executable_path='A:/Python_Automation_Course_QA/python-selenium-automation/geckodriver.exe')
    # context.driver = webdriver.Firefox(service=service)

    # BROWSERSTACK CODE #
    # bs_user = 'kaitlynfriden_y2mXKl'
    # bs_key = 'eQHRTGhV6JqHDHTJNyFm'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    #
    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    # print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed: {step}')
        # print('\nStep failed: ', step)
        context.app.base_page.save_screenshot(step)


def after_scenario(context):
    context.driver.quit()
