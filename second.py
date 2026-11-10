from typing import Callable

def generator_numbers(text:str):
    for num in text.split():

        try:
            yield float(num)

        except ValueError:
            continue

def sum_profit(text: str, func: Callable)->int:

    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")