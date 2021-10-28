from .test_setup import TestSetup
from ..models import Points

class TestViews(TestSetup):

    def test_user_can_get_cohort_students(self):
        res = self.client.get(self.data_url)
        
        self.assertContains(res,'Anas Abusaif')
        self.assertContains(res,'Dario Thornhill')
        self.assertEqual(res.status_code, 200)


    def test_user_can_create_point(self):
        res = self.client.post(self.points_url, self.point_data, format="json")
 
        self.assertEqual(res.data['owner'], self.point_data['owner'])
        self.assertEqual(res.data['reward'], self.point_data['reward'])
        self.assertEqual(res.status_code, 201)


    def test_user_can_get_points(self):
        self.client.post(self.points_url, self.point_data, format="json")
        res = self.client.get(self.points_url)

        self.assertContains(res,"+1 mark on any submission")
        self.assertEqual(res.data[0]['owner'], self.point_data['owner'])
        self.assertEqual(res.status_code, 200)


    def test_user_can_confirm_point(self):
        point = self.client.post(self.points_url, self.point_data, format="json")
        res = self.client.put(self.done_claim_url, self.confirm, format="json")
        
        expetcted = Points.objects.get(id=point.data['id'])
        
        self.assertEqual(res.data['owner'], expetcted.owner)
        self.assertEqual(res.data['is_confirmed'], expetcted.is_confirmed)
        self.assertEqual(res.status_code, 200)

