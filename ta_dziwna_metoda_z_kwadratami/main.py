from typing import List
from zdominowane import zdominowane

def RSM(A : List[List[float]], C :  List[List[float]]):
    """
    RSM metoda zbiorów odniesienia

    args:
        A - zbiór punktów odniesienia
        B - zbiór punktów dopószczalnych

    return
        punkty skoringowe zbioru B
    """
    A0,rest = zdominowane()