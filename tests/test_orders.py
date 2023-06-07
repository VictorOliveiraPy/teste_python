import pytest

from src.question2 import Orders


class TestOrders:
    def test_combine_orders_with_multiple_requests(self):
        orders = [70, 30, 10]
        n_max = 100
        expected_orders = 2

        how_many = Orders().combine_orders(orders, n_max)

        assert how_many == expected_orders

    @pytest.mark.parametrize("orders, n_max, expected_orders", [
        ([70, 30, 10], 100, 2),
        ([50], 50, 1),
        ([20, 30, 40], 60, 2),
        ([80, 50, 30, 20], 100, 3),
    ])
    def test_combine_orders_with_multiple_scenarios(self, orders, n_max, expected_orders):
        how_many = Orders().combine_orders(orders, n_max)
        assert how_many == expected_orders
