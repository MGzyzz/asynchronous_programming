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
        self.speed_coefficient = 5 * self.speed_coefficient
        print(f"\n {'='*40} \nНачало пробежки {self.name} {datetime.now().strftime('%X')}. \nВозвраст {self.age} | Скорость {self.speed_coefficient} km/h\n {'='*40}")
        time_to_run = distance / self.speed_coefficient * 60
        await asyncio.sleep(time_to_run)
        print(f"\n {'='*40} \n{self.name} закончил пробежку в {datetime.now().strftime('%X')}\n {'='*40}")
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

    runner_times = list(zip(runners, results))
    runner_times.sort(key=lambda x: x[1])
    fastest_time = min(results)
    slowest_time = max(results)
    time_difference_minutes = (slowest_time - fastest_time)

    print(f'{"Имя":<15} | {"Возвраст":<15} | {"Скорость":<15} | Затраченное время')
    for i, (runner, result) in enumerate(runner_times, start=1):
        print(f"{runner.name:<15} | {runner.age:<15} | {runner.speed_coefficient:<15.2f} | {result:.2f}")

    print(f"\nВремя между быстрым и медленным бегуном: {time_difference_minutes:.2f} минут")

if __name__ == "__main__":
    asyncio.run(main())
