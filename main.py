import asyncio
import random
from datetime import  datetime


class Runner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.speed_coefficient = self.calculate_speed_coefficient()

    def calculate_speed_coefficient(self):
        if self.age < 10:
            return 0.7
        elif self.age < 20:
            return 2
        elif self.age < 40:
            return 2.5
        else:
            return 1.2

    async def run(self, distance):
        speed = 5 * self.speed_coefficient
        print(f"Начало пробежки {self.name} {datetime.now().strftime('%X')}. \nВозвраст {self.age} | Скорость {speed} km/h\n")
        time_to_run = distance / speed * 60
        print(time_to_run)
        await asyncio.sleep(time_to_run)
        print(f"{self.name} закончил пробежку в {datetime.now().strftime('%X')}")
        return time_to_run

    def __lt__(self, other):
        return self.age < other.age

async def main():
    runners = [
        Runner("Check_one", random.randint(5, 100)),
        Runner("Check_two", random.randint(5, 100)),
        Runner("Check_three", random.randint(5, 100)),
        Runner("Check_four", random.randint(5, 100)),
        Runner("Check_five", random.randint(5, 100)),
        Runner("Check_six", random.randint(5, 100)),
        Runner("Check_seven", random.randint(5, 100)),
        Runner("Check_eight", random.randint(5, 100)),
        Runner("Check_nine", random.randint(5, 100)),
    ]

    distance = 10
    tasks = [runner.run(distance) for runner in runners]
    results = await asyncio.gather(*tasks)

    sorted_runners = sorted(runners)
    fastest_time = results[0]
    slowest_time = results[-1]
    time_difference_minutes = (slowest_time - fastest_time) / 60

    print(f'{"Имя":<15} | {"Возвраст":<15} | {"Скорость":<15} | Затраченное время')
    for i, runner in enumerate(sorted_runners, start=1):
        print(f"{runner.name:<15} | {runner.age:<15} | {runner.speed_coefficient:<15.2f} | {results[i-1]:.2f}")

    print(f"\nВремя между быстрым и медленным бегуном: {time_difference_minutes:.2f} минут")

if __name__ == "__main__":
    asyncio.run(main())
