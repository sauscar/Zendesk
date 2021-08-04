import unittest
from app import app
from app import handle_form, get_page
from unittest.mock import MagicMock
import pdb


class FlaskTest(unittest.TestCase):
    def testGetTickets(self):

        tester = app.test_client(self)
        response = tester.get("/get_tickets")
        # pdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def testRetrievePage(self):

        tester = app.test_client(self)
        response = tester.post("/retrieve_page")
        # pdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def testSingleTicket(self):

        tester = app.test_client(self)
        response = tester.post("/single_ticket")
        # pdb.set_trace()
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
