from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

class ThingTests(TestCase) :
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = "tester", email = "tester@email.com", password = "pass"
        )

        self.snack = Snack.objects.create(
            name="banana", description = "Healthy Fruits" , purchaser = self.user,
        )
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "banana")

    def test_thing_content(self):
        self.assertEqual(f"{self.snack.name}", "banana")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(self.snack.description, "Healthy Fruits")

    def test_thing_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "banana")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_thing_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_thing_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "name": "Apple slices with peanut butter",
                "description": "Apples and peanut butter are a match made in heaven — both nutritionally and flavor-wise.On one hand, apples are a fiber-rich fruit. On the other hand, peanuts provide healthy fats, plant-based protein, and fiber — pretty much all of the filling nutrients you should look for in a snack",
                "purchaser": self.user.id,
            }, follow=True
        )
        self.assertRedirects(response, reverse("snack_detail", args="2"))

    def test_thing_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name" : "Updated name", "description" : "Any Thing", "purchaser" : self.user.id}
        )
        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_thing_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)