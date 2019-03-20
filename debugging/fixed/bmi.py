from typing import Tuple
from typing import List


def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)


def get_bmis(patients: List[Tuple[float, float]]) -> List[float]:
    return [calculate_bmi(patient[0], patient[1]) for patient in patients]


if __name__ == "__main__":
    patient_list = [(70, 1.8), (80, 1.9), (150, 1.7)]
    print("\n".join(str(bmi) for bmi in get_bmis(patient_list)))
