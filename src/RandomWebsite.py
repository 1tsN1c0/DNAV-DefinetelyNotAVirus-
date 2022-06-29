# Documento creato il 26/06/2022

import random
import time
from selenium import webdriver

i = 1

def RandomWebsite():
    for i in range(1,51):

        n = random.randint(1, 3)

        # Rickroll
        if n == 1:
            url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            browser = webdriver.Chrome()
            browser.get(url)

        # Search: how to clean viruses from my pc
        elif n == 2:
            url = "https://www.google.com/search?q=how+do+i+clean+viruses+from+my+pc&source=hp&ei=BGW4YqfJFLKI9u8Pv5a_-AY&iflsig=AJiK0e8AAAAAYrhzFC5YEX3W8cjFFcpu8nktNA6444XY&ved=0ahUKEwin25Wbosv4AhUyhP0HHT_LD28Q4dUDCAk&uact=5&oq=how+do+i+clean+viruses+from+my+pc&gs_lcp=Cgdnd3Mtd2l6EANKBQhAEgExUABYAGAAaABwAHgAgAEAiAEAkgEAmAEAoAEC&sclient=gws-wiz"
            browser = webdriver.Chrome()
            browser.get(url)

        # Search: free music download
        elif n == 3:
            url = "https://www.google.com/search?q=free+music+download&ei=amW4YobPEcqS9u8P4eKy4AM&ved=0ahUKEwiGrOTLosv4AhVKif0HHWGxDDwQ4dUDCA4&uact=5&oq=free+music+download&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcILhDUAhBDOggILhCxAxCDAToECAAQQzoECC4QQzoLCC4QgAQQsQMQ1AI6DgguEIAEELEDEMcBEKMCOggIABCABBCxAzoHCAAQsQMQQzoLCC4QgAQQsQMQgwE6CAguEIAEELEDOgUILhCABDoGCAAQHhAWOgQIABAKOgsILhCABBDHARCvAToNCC4Q1AIQ6gIQtAIQQzoKCAAQ6gIQtAIQQzoUCAAQ6gIQtAIQigMQtwMQ1AMQ5QI6EQguEOoCELQCEIoDELcDEOUCOhQILhDqAhC0AhCKAxC3AxDUAxDlAjoRCC4QgAQQsQMQgwEQxwEQ0QM6DgguEIAEELEDEMcBENEDOg4ILhCABBCxAxCDARDUAjoRCC4QgAQQsQMQgwEQxwEQrwE6CAguEIAEENQCSgUIPBIBOUoECEEYAEoFCEASATFKBAhGGABQAFjUgwFg_oQBaApwAXgFgAHJBogBvDqSAQ4yLjI2LjEuMi4yLjIuMZgBAKABAbABCsABAQ&sclient=gws-wiz"
            browser = webdriver.Chrome()
            browser.get(url)

        # Aggiunge un delay di 30 secondi tra un'apertura di un sito e l'altra
        time.sleep(45)

        i = i + 1