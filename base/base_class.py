

class Base():

    def __init__(self, driver):
        self.driver = driver


    """Метод для получения URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Метод assert word"""

    def assert_word(self, word, expected_result):
        value_word = word.text
        assert value_word == expected_result
        print("Good value")
