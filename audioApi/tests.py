from rest_framework.test import APIClient, APITestCase
from datetime import datetime


class test_group(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = ['/part/', '/song/', '/podcast/', '/audio/']

        self.individuals = {'name': 'collins'}
        self.song_post = {'songID': 1,
                          'songName': 'vibration',
                          'songUploaded': datetime.now(),
                          'songDuration': '240 seconds'}

        self.audio_post = {'audioBookID': 1,
                           'audioBookTitle': 'temi\'s_podcast',
                           'audioBookNarrator': 'eazi',
                           'audioBookAuthor': 'temi',
                           'audioBookDuration': '6000seconds',
                           'audioBookUploaded': datetime.now()}



    def test_list(self):

        #get uri
        self.client.get(self.uri[0])
        self.client.get(self.uri[1])
        self.client.get(self.uri[2])
        self.client.get(self.uri[3])

        #post to uri
        re = self.client.post((self.uri[0]), self.individuals)
        res = self.client.post(self.uri[1], self.song_post)
        resp = self.client.post(self.uri[3], self.audio_post)

        self.assertEqual(re.status_code, 201)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(resp.status_code, 201)
