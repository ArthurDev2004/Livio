from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Category, Product

class MarketSmokeTests(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(name="General", slug="general")
        Product.objects.create(title="Sample Product", slug="sample-product", category=self.cat)

    def test_health(self):
        resp = self.client.get("/api/market/health/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("ok", resp.json())

    def test_products(self):
        resp = self.client.get("/api/market/products/")
        self.assertEqual(resp.status_code, 200)
        self.assertGreaterEqual(len(resp.json().get("results", [])), 1)
