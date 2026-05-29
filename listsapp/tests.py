import json
from django.test import TestCase, Client
from django.urls import reverse
from .models import User, Product, List, PriceMkt

class ListsAppTests(TestCase):
    def setUp(self):
        # Criar usuários
        self.user = User.objects.create_user(username="cliente", password="123")
        self.market = User.objects.create_user(username="mercado1", password="123", is_supermarket=True)
        
        # Criar produto
        self.prod = Product.objects.create(name="Leite", unity="1L")
        
        # Criar lista para o usuário
        self.lista = List.objects.create(name="Minha Lista", user=self.user)

    def test_add_product_to_list_ajax(self):
        """Testa se a adição de produto na listpage via AJAX funciona"""
        self.client.login(username="cliente", password="123")
        
        response = self.client.post(
            reverse("listpage", args=[self.lista.id]),
            {"product_id": self.prod.id},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {
            "success": True,
            "id": self.prod.id,
            "name": "Leite",
            "unity": "1L"
        })
        self.assertTrue(self.prod in self.lista.products.all())

    def test_compare_prices_logic(self):
        """Testa se o cálculo de total por supermercado está correto"""
        # Criar outro mercado e outro produto
        market2 = User.objects.create_user(username="mercado2", password="123", is_supermarket=True)
        prod2 = Product.objects.create(name="Pão", unity="Kg")
        
        self.lista.products.add(self.prod, prod2)

        # Mercado 1: Leite $5, Pão $10 (Total 15)
        PriceMkt.objects.create(supermarket=self.market, product=self.prod, price=5.00)
        PriceMkt.objects.create(supermarket=self.market, product=prod2, price=10.00)

        # Mercado 2: Leite $4, Pão $12 (Total 16)
        PriceMkt.objects.create(supermarket=market2, product=self.prod, price=4.00)
        PriceMkt.objects.create(supermarket=market2, product=prod2, price=12.00)

        self.client.login(username="cliente", password="123")
        response = self.client.get(reverse("prices", args=[self.lista.id]))
        
        # O mercado 1 deve aparecer primeiro (Total 15 < 16)
        prices_list = response.context['price_per_market']
        self.assertEqual(prices_list[0]['supermarket'].username, "mercado1")
        self.assertEqual(prices_list[0]['total_price'], 15.00)

    def test_update_address_put_method(self):
        """Testa a atualização de endereço via método PUT (AJAX)"""
        self.client.login(username="mercado1", password="123")
        
        data = {"address": "Rua Nova, 123"}
        response = self.client.put(
            reverse("update_address", args=[self.market.id]),
            data=json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        self.assertEqual(response.status_code, 200)
        self.market.refresh_from_db()
        self.assertEqual(self.market.address, "Rua Nova, 123")