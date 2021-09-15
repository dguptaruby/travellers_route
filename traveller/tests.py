from django.urls import include, path, reverse

from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status


class AccountTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [path("api/", include("traveller.urls"))]

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse("route")
        response = self.client.get(
            url,
            format="json",
            kwargs={
                "list_cord": [
                    [75.85962616866853, 22.79614270933867],
                    [75.84514379758467, 22.797291799510006],
                    [75.88513552642058, 22.75784003109508],
                    [75.89375487666832, 22.744328470876017],
                ]
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
