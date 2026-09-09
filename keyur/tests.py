from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from keyur.cart_utils import normalize_cart_quantity
from keyur.models import Product
from keyur.views import get_related_products


class CartQuantityValidationTests(SimpleTestCase):
    def test_quantity_cannot_exceed_available_stock(self):
        self.assertEqual(normalize_cart_quantity(2, 4, 5), 5)
        self.assertEqual(normalize_cart_quantity(5, 4, 5), 5)
        self.assertEqual(normalize_cart_quantity(1, 3, 5), 4)
        self.assertEqual(normalize_cart_quantity(0, 2, 5), 2)


class ManualRecommendationTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Main product', price='100.00', stock=5, image='products/main.jpg'
        )
        self.first_recommendation = Product.objects.create(
            name='First recommendation', price='20.00', stock=5, image='products/first.jpg'
        )
        self.second_recommendation = Product.objects.create(
            name='Second recommendation', price='30.00', stock=5, image='products/second.jpg'
        )
        self.product.recommended_products.set([
            self.first_recommendation,
            self.second_recommendation,
        ])

    def test_only_selected_products_are_returned(self):
        self.assertEqual(
            get_related_products(self.product),
            [self.first_recommendation, self.second_recommendation],
        )

    def test_shop_shows_recommendations_selected_for_any_product(self):
        other_product = Product.objects.create(
            name='Other product', price='200.00', stock=5, image='products/other.jpg'
        )
        other_product.recommended_products.add(self.second_recommendation)
        uploaded_image_product = Product.objects.create(
            name='Uploaded recommendation',
            price='250.00',
            stock=5,
            image='products/uploaded.jpg',
        )

        response = self.client.get(reverse('shop'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.second_recommendation, response.context['products'])
        self.assertNotIn('recommendations', response.context)

    def test_recommended_product_page_hides_recommendations(self):
        response = self.client.get(
            reverse('product_detail', args=[self.first_recommendation.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['show_recommendations'])
        self.assertEqual(response.context['related_products'], [])
