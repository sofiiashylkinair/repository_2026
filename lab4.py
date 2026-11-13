class Student:
    course: int = 2
    university: str = "LNU"

    def __init__(
        self,
        name_surname: str = "Невідомо",
        rating: float = 0.0,
        height: float = 170.0,
        faculty: str = "ФПНК",
    ) -> None:
        self.__name_surname = name_surname
        self.__rating = rating
        self.__height = height
        self._faculty = faculty
        self.course = 8

    def get_name_surname(self) -> str:
        self.course = 5
        return self.__name_surname    

    def get_rating(self) -> float:
        return self.__rating

    def get_height(self) -> float:
        return self.__height

    def get_faculty(self) -> str:
        return self._faculty

    def __str__(self) -> str:
        return (
            f"Студент: {self.__name_surname}, Рейтинг: {self.__rating}, "
            f"Ріст: {self.__height}, Факультет: {self._faculty}"
        )

    def __repr__(self) -> str:
        return (
            f"Student('{self.__name_surname}', {self.__rating}, "
            f"{self.__height}, '{self._faculty}')"
        )

    def __del__(self) -> None:
        pass


def main() -> None:
    student1 = Student("Іван Петренко", 95.5, 182.0, "Прикладна математика")
    student2 = Student("Олена Коваль", 88.0, 165.0, "Кібербезпека")
    print(student2.course)
    student3 = Student()

    students = [student1, student2, student3]

    for s in students:
        print(f"Ім'я та прізвище: {s.get_name_surname()}")
        print(f"Рейтинг: {s.get_rating()}")
        print(f"Ріст: {s.get_height()}")
        print(f"Захищене поле (факультет): {s.get_faculty()}")
        print(f"Публічні поля: курс {s.course}, університет {s.university}")
        print(s)
        print("-" * 40)


main()