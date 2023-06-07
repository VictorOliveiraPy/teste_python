import heapq

import pytest

from src.question1 import Contract, Contracts


class TestContracts:
    @pytest.mark.parametrize("top_n, expected_open_contracts", [
        (1, [5]),
        (2, [5, 4]),
        (3, [5, 4, 2]),
        (4, [5, 4, 2, 1])
    ])
    def test_get_top_N_open_contracts_returns_expected_contracts(self, top_n, expected_open_contracts):
        contracts = [
            Contract(1, 1),
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        renegotiated = [3]
        c = Contracts()
        actual_open_contracts = heapq.nlargest(top_n, c.get_top_N_open_contracts(contracts, renegotiated, top_n))

        assert expected_open_contracts == actual_open_contracts
