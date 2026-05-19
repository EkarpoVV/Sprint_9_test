from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 5
        self.wait = WebDriverWait(self.driver,self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def wait_text_absense(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator).text

    def wait_text(self, locator, text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator, text)) and self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator, text))
        return self.driver.find_element(*locator).text
    
    def invisibility_of_element(self, locator):
        element = self.wait.until(
            expected_conditions.invisibility_of_element_located(locator))
        return element

    def find_element_clickable_with_wait(self, locator):
        self.wait.until(
            expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)
    
    def find_element_presence_with_wait(self, locator):
        self.wait.until(
            expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def click_to_element(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    
    def swith_to_another_window(self, driver):
        windows_list = self.driver.window_handles
        driver.switch_to.winow(windows_list[-1])

    def my_drag_and_drop(self, locator_from, locator_to):
        elem_from = self.find_element_with_wait(locator_from)
        elem_to = self.find_element_with_wait(locator_to)
        ActionChains(self.driver).drag_and_drop(elem_from, elem_to).perform()
                               
    def click_element_via_js(self, some):
        self.wait.until(expected_conditions.element_to_be_clickable(some))
        element = self.driver.find_element(*some)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_enable(self, locator):
        self.wait.until(
    lambda d: d.find_element(*locator).is_enabled())
        
    def element_is_displayed(self, locator):
        return self.find_element_with_wait(locator).is_displayed()
    
    def wait_for_modal_closed(self, driver, locator):
        wait = WebDriverWait(driver, 2)
        try:
            element = wait.until(expected_conditions.invisibility_of_element_located(locator))
            return element
        except TimeoutException:
            print("Modal did not close within the expected time")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def drag_and_drop_element_ff(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

        script = """
        function simulateDragDrop(sourceNode, destinationNode) {
            var EVENT_TYPES = {
                DRAG_END: 'dragend',
                DRAG_START: 'dragstart',
                DROP: 'drop'
            }

            function createCustomEvent(type) {
                var event = new CustomEvent("CustomEvent")
                event.initCustomEvent(type, true, true, null)
                event.dataTransfer = {
                    data: {
                    },
                    setData: function(type, val) {
                        this.data[type] = val
                    },
                    getData: function(type) {
                        return this.data[type]
                    }
                }
                return event
            }

            function dispatchEvent(node, type, event) {
                if (node.dispatchEvent) {
                    return node.dispatchEvent(event)
                }
                if (node.fireEvent) {
                    return node.fireEvent("on" + type, event)
                }
            }

            var event = createCustomEvent(EVENT_TYPES.DRAG_START)
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event)

            var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
            dropEvent.dataTransfer = event.dataTransfer
            dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent)

            var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
            dragEndEvent.dataTransfer = event.dataTransfer
            dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source_element, target_element)