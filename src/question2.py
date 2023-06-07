import numpy as np

from src.exceptions.exception import OrdersException


class Orders:
    def combine_orders(self, requests: [int], n_max: int):
        try:
            how_many: int = 0
            remaining_requests = len(requests)

            for i in range(remaining_requests):
                if requests[i] == n_max:
                    how_many += 1

                elif remaining_requests - i > 1:
                    combined_sum = np.sum(requests[i:i + 2])
                    if combined_sum <= n_max:
                        how_many += 1
                        i += 1
                    else:
                        how_many += 1

            return how_many
        except Exception as e:
            raise OrdersException("Erro ao combinar pedidos") from e
