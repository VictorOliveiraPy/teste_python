import heapq

from src.exceptions.exception import OpenContractsException


class Contract:
    def __init__(self, id, debt):
        self.id = id
        self.debt = debt

    def __str__(self):
        return 'id={}, debt={}'.format(self.id, self.debt)


class Contracts:

    def get_top_N_open_contracts(self, open_contracts: list, renegotiated_contracts: list[int], top_n: int):
        try:
            renegotiated_set = set(renegotiated_contracts)
            for contract in open_contracts:
                if contract.id not in renegotiated_set:
                    yield contract.debt
        except Exception as e:
            raise OpenContractsException("Erro ao processar contratos abertos") from e


contracts = [
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
]
renegotiated = [3]
top_n = 3
c = Contracts()

actual_open_contracts = heapq.nlargest(top_n, c.get_top_N_open_contracts(contracts, renegotiated, top_n))
