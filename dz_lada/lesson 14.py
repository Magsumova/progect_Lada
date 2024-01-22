# Задания № 1

""" Вам нужно создать класс
Calendar, который будет представлять календарь. 
Класс должен иметь методы для добавления событий (например. встреч или задач), 
отображения событий на конкретную дату и удаления событий. 
Каждое событие должно иметь название и дату. Добавьте функцию, которая будет выводить все события на ближайшие N дней."""

"""from datetime import datetime, timedelta

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, name, date):
        event = Event(name, date)
        self.events.append(event)
        print(f"Событие '{event.name}' добавлено на {event.date}.")

    def display_events_on_date(self, date):
        events_on_date = [event.name for event in self.events if event.date.date() == date]
        if events_on_date:
            print(f"События на {date}: {', '.join(events_on_date)}")
        else:
            print(f"На {date} событий нет.")

    def remove_event(self, name):
        self.events = [event for event in self.events if event.name != name]
        print(f"Событие '{name}' удалено.")

    def display_events_next_n_days(self, n):
        today = datetime.now().date()
        end_date = today + timedelta(days=n)
        upcoming_events = [event for event in self.events if today <= event.date.date() <= end_date]

        if upcoming_events:
            print(f"Ближайшие события на {n} дней:")
            for event in upcoming_events:
                print(f"{event.name} - {event.date}")
        else:
            print("Ближайших событий нет.")


my_calendar = Calendar()


my_calendar.add_event("Встреча", datetime(2024, 1, 30, 14, 0))
my_calendar.add_event("Задача", datetime(2024, 1, 31, 10, 30))
my_calendar.add_event("Другое событие", datetime(2024, 2, 5, 18, 0))


my_calendar.display_events_on_date(datetime(2024, 1, 31).date())


my_calendar.remove_event("Задача")


my_calendar.display_events_next_n_days(7)"""

# Задания № 2

"""class Inventoryltem():
    def __init__(self, name, quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price
        
    def display_info(self):
        print(f"Название товара {self.name}; Количество товара {self.quantity} мешков; Цена товара {self.price} тенге")

    def uvl(self):
        u = self.quantity+80
        print(f"Завтра придет новая партия {self.name} и общее количество будет {u}")
    
    def umen(self):
        um = self.quantity-30
        print(f"Сегодня продали {um} мешков {self.name}")

    def obsh_st(self):
        st = self.quantity*self.price
        print(f"Общая стоимость товара {st}")

tovar = Inventoryltem("Мука", 50, 7000)
tovar.display_info()
tovar.uvl()
tovar.umen()
tovar.obsh_st()"""

# Задания № 3

"""class Student():
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades

    def print_info(self):
        print(f" Студент: {self.name} Оценки {self.grades}")
    
    def average(self):
        aver = sum(self.grades)/len(self.grades)
        print(f"Успеваемость {aver} студента {self.name}")

student1=Student("Иван", [4,5,4,3,5,2,2,2,3])
student1.print_info()
student1.average()"""
