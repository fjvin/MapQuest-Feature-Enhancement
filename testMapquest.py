import unittest
from flaskWebApp import app
from mapquestBackend import calculateDirection, convertMilestoKm

testCasesInputs = {
    ("Quezon City, Philippines", "Taguig City, Philippines", 1) : 0,
    ("Washington, DC", "Baltimore Md", 1) : 0,
    ("Wash", "Bal", 1) : 402,
    ("Washington, DC", "Bal", 1) : 402,
    ("Washington, DC", "", 1) : 611,
    ("", "", 1) : 611,
}

testMilesToKm = {
    1 : 1.61,
    2 : 3.22,
    3 : 4.83,
    69 : 111.04,
    420 : 675.92
}

class TestMapquest(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # Tests the Get Method if returns HTTP - 200 (Success Status)
    def testGetMethod(self):
        rv = self.app.get('/')
        statusCode = rv.status_code
        self.assertEqual(statusCode, 200)
    
    # Tests if the content type returned is text/html; charset=utf-8 (index.html)
    def testContentType(self):
        rv = self.app.get('/')
        statusCode = rv.status_code
        self.assertEqual(rv.content_type, "text/html; charset=utf-8")
    
    # Tests the Post Method if returns HTTP - 200 (Success Status)
    def testPostMethod(self):
        response = self.app.post("/", data={
            "start":"Quezon City, Philippines",
            "dest":"Taguig City, Philippines",
            "distanceUnit":1
        })
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)
    
    # Tests the calculateDirection helper function
    def testCalculateDirection(self):
        for k,v in testCasesInputs.items():
            tripDuration, distance, distanceUnit, directionList, json_status = calculateDirection(k[0], k[1], k[2])
            self.assertEqual(json_status, v)
    
    # Tests the convertMilesToKm function
    def testMilesToKm(self):
        for k,v in testMilesToKm.items():
            self.assertEqual(convertMilestoKm(k), v)
    

if __name__ == "__main__":
    unittest.main()