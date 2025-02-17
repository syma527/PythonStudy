import unittest
import os
import logging
from http.client import responses



class TestMyFeature(unittest.TestCase):
    def setUp(self):
        self.test_data = {
            "user": os.getenv("TEST_USER", "test_user"),
            "password": os.getenv("TEST_PASSWORD", "test_password")
        }

    def test_login_success(self):
        try:
            response = login(self.test_data["user"], self.test_data["password"])
            self.assertTrue(response["success"], "Login should be successful")
            self.assertIn("message", response, "Response should contain a message field")
        except KeyError as e:
            logging.error(f"KeyError in response: {e}")
            self.fail(f"Login failed with KeyError: {e}")
        except Exception as e:
            logging.error(f"Unexpected exception: {e}")
            self.fail(f"Login failed with unexpected exception: {e}")

    def test_login_failure(self):
        invalid_user = os.getenv("INVALID_TEST_USER", "invalid_user")
        invalid_password = os.getenv("INVALID_TEST_PASSWORD", "invalid_password")
        try:
            response = login(invalid_user, invalid_password)
            self.assertFalse(response["success"], "Login should fail with invalid credentials")
            self.assertIn("message", response, "Response should contain a message field")
        except KeyError as e:
            logging.error(f"KeyError in response: {e}")
            self.fail(f"Login failed with KeyError: {e}")
        except Exception as e:
            logging.error(f"Unexpected exception: {e}")
            self.fail(f"Login failed with unexpected exception: {e}")

    def test_empty_credentials(self):
        try:
            response = login("", "")
            self.assertFalse(response["success"], "Login should fail with empty credentials")
            self.assertIn("message", response, "Response should contain a message field")
        except KeyError as e:
            logging.error(f"KeyError in response: {e}")
            self.fail(f"Login failed with KeyError: {e}")
        except Exception as e:
            logging.error(f"Unexpected exception: {e}")
            self.fail(f"Login failed with unexpected exception: {e}")


if __name__ == '__main__':
    unittest.main()
