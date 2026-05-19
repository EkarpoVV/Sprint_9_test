import os

SELENOID_URL = os.getenv("SELENOID_URL", "")
BROWSER_NAME = os.getenv("BROWSER_NAME", "chrome")
BROWSER_VERSION = os.getenv("BROWSER_VERSION", "128.0")