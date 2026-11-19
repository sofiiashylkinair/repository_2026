class RaceHorse:
    def __init__(self, name: str, age: int, speed: float):
        self.name = name
        self.age = age
        self.speed = speed
        self.place_in_race = 0

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed

    def __del__(self):
        print(f"Кінь {self.name} видалений з пам'яті.")

    def __str__(self):
        place = f"Місце: {self.place_in_race}" if self.place_in_race > 0 else "Місце: немає"
        return f"Кінь: {self.name} | Вік: {self.age} р. | Швидкість: {self.speed} км/год | {place}"


class Race:
    def __init__(self, race_name: str):
        self.race_name = race_name
        self.horses = []

    def __del__(self):
        print(f"Перегони '{self.race_name}' завершено.")

    def add_horse(self, horse: RaceHorse):
        if 3 <= horse.age <= 7:
            self.horses.append(horse)
            print(f"Кінь {horse.name} допущений до перегонів.")
        else:
            print(f"Кінь {horse.name} НЕ допущений (вік має бути від 3 до 7 років).")

    def remove_horse(self, horse_name: str):
        for horse in self.horses:
            if horse.name == horse_name:
                self.horses.remove(horse)
                print(f"Кінь {horse_name} покидає перегони.")
                return
        print(f"Коня {horse_name} немає серед учасників.")

    def sort_by_speed(self):
        self.horses.sort(key=lambda horse: horse.speed, reverse=True)
        print("Учасників посортовано за швидкістю.")

    def assign_places(self):
        self.sort_by_speed()
        for i, horse in enumerate(self.horses):
            if i < 3:
                horse.place_in_race = i + 1
            else:
                horse.place_in_race = 0

    def determine_winner(self):
        if not self.horses:
            print("Немає учасників для визначення переможця.")
            return None
        
        avg_age = sum(h.age for h in self.horses) / len(self.horses)
        print(f"Середній вік учасників: {avg_age:.1f} р.")

        winner = max(self.horses, key=lambda h: h.speed - abs(h.age - avg_age))
        return winner

    def display(self):
        print(f"\n--- Список учасників ({self.race_name}) ---")
        for horse in self.horses:
            print(horse)
        print("-" * 40)


if __name__ == "__main__":
    race = Race("Великі Забіги")

    h1 = RaceHorse("Блискавка", 4, 65.5)
    h2 = RaceHorse("Буря", 6, 69.0)
    h3 = RaceHorse("Тінь", 3, 61.0)
    h4 = RaceHorse("Старий", 9, 72.0)  
    h5 = RaceHorse("Вітер", 5, 67.0)

    print("--- Додавання учасників ---")
    race.add_horse(h1)
    race.add_horse(h2)
    race.add_horse(h3)
    race.add_horse(h4)
    race.add_horse(h5)

    race.display()

    print("--- Присвоєння місць за швидкістю ---")
    race.assign_places()
    race.display()

    print("--- Визначення переможця ---")
    winner = race.determine_winner()
    if winner:
        print(f"Переможець за розрахунком: {winner.name} (Вік: {winner.age}, Швидкість: {winner.speed})")

    print("\n--- Видалення учасника ---")
    race.remove_horse("Тінь")

    print("rase")
    for horse in race.horses:
        print(f"Ім'я: {horse.name}, Вік: {horse.age} р.")