import unittest
import requests, json

URL = 'http://localhost:5000'
headers={'Content-Type': 'application/json'}

g = {"name": "lalit-lalit", "filter": { "netmask": "192.168.24.0/24"}}

class TestPolicyAPI(unittest.TestCase):

    def test1_create_group(self):
        global g
        requests.delete(URL + '/abc/' + g['name']) #ensure does not exist
        r = requests.post(URL + '/abc', headers = headers, data=json.dumps(g))
        self.assertEqual(r.status_code, 201)
        jd = json.loads(r.text)
        self.assertEqual(jd['groups']['name'], g['name'])

if __name__ == '__main__':
	unittest.main()