from selenium import webdriver


def get_browser():
    # ua = UserAgent()
    # PROXY = proxy_generator()
    # userAgent = ua.random #get a random user agent
    options = webdriver.ChromeOptions()  # use headless version of chrome to avoid getting blocked
    options.add_argument('headless')
    # options.add_argument(f'user-agent={userAgent}')
    options.add_argument("incognito")#
    options.add_argument("start-maximized")# // open Browser in maximized mode
    options.add_argument("disable-infobars")# // disabling infobars
    options.add_argument("--disable-extensions")# // disabling extensions
    options.add_argument("--disable-gpu")# // applicable to windows os only
    options.add_argument("--disable-dev-shm-usage")# // overcome limited resource problems
    # options.add_argument('--proxy-server=%s' % PROXY)
    browser = webdriver.Chrome(chrome_options=options,  # give the path to selenium executable
                                   # executable_path='F://Armitage_lead_generation_project//chromedriver.exe'
                                   executable_path='//utilities//chromedriver.exe',
                               # service_args=["--verbose", "--log-path=D:\\qc1.log"]
                                   )
    return browser