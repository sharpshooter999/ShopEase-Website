from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from keyur.cart_utils import normalize_cart_quantity
from keyur.models import Product
from keyur.views import get_related_products, validate_payment_details


class CartQuantityValidationTests(SimpleTestCase):
    def test_quantity_cannot_exceed_available_stock(self):
        self.assertEqual(normalize_cart_quantity(2, 4, 5), 5)
        self.assertEqual(normalize_cart_quantity(5, 4, 5), 5)
        self.assertEqual(normalize_cart_quantity(1, 3, 5), 4)
        self.assertEqual(normalize_cart_quantity(0, 2, 5), 2)


class PaymentValidationTests(SimpleTestCase):
    def test_card_details_require_bounded_values(self):
        self.assertEqual(
            validate_payment_details("card", {
                "card_number": "123456789012",
                "expiry": "12/2030",
                "cvv": "123",
            }),
            "",
        )
        self.assertIn("card number", validate_payment_details("card", {
            "card_number": "123",
            "expiry": "12/2030",
            "cvv": "123",
        }))

    def test_other_payment_methods_require_their_details(self):
        self.assertIn("UPI", validate_payment_details("upi", {"upi_id": "invalid"}))
        self.assertEqual(validate_payment_details("upi", {"upi_id": "9876543210@bank"}), "")
        self.assertIn("bank", validate_payment_details("net_banking", {"bank": ""}))
        self.assertEqual(validate_payment_details("cod", {}), "")

    def test_expiry_date_cannot_be_in_the_past(self):
        self.assertIn("not passed", validate_payment_details("card", {
            "card_number": "4111111111111111",
            "expiry": "01/2020",
            "cvv": "123",
        }))

    def test_cvv_must_be_exactly_three_digits(self):
        self.assertEqual(validate_payment_details("card", {
            "card_number": "123456789012",
            "expiry": "12/2030",
            "cvv": "123",
        }), "")
        self.assertIn("3 digit", validate_payment_details("card", {
            "card_number": "123456789012",
            "expiry": "12/2030",
            "cvv": "1234",
        }))


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
