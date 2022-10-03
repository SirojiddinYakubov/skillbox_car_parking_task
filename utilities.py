class Car(object):
    def __init__(self, count, icon):
        self.count = count
        self.icon = icon

    def __str__(self):
        return self.icon

    def reduce_count(self, count):
        self.count = self.count - count


class Parking(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.get_variables()
        self.output_string = ""
        self.red_car = Car(count=self.x, icon="R")
        self.white_car = Car(count=self.y, icon='W')


    def get_variables(self):
        try:
            self.x = int(input("Введите количество красных автомобилей: "))
            self.y = int(input("Введите количество белых автомобилей: "))
        except ValueError:
            print("Количество красных и белых автомобилей должно быть заполнено правильно!")
            return self.get_variables()

    def start_placement(self):
        if (self.x != 0 and self.y != 0) and min(self.x, self.y) * 2 >= max(self.x, self.y):
            if self.x > self.y:
                self.output_string = self.red_car.icon
                self.red_car.reduce_count(1)
            elif self.x < self.y:
                self.output_string = self.white_car.icon
                self.white_car.reduce_count(1)
            else:
                self.output_string = "{}{}".format(self.red_car, self.white_car)
                self.red_car.reduce_count(1)
                self.white_car.reduce_count(1)

            while self.red_car.count and self.white_car.count:
                if self.red_car.count == self.white_car.count:
                    if self.output_string[-1] == self.white_car.icon:
                        self._placement_red_car(1)
                        self._placement_white_car(1)
                    else:
                        self._placement_white_car(1)
                        self._placement_red_car(1)
                else:
                    if self.red_car.count - self.white_car.count >= 2:
                        if self.output_string[-1] == self.red_car.icon:
                            self._placement_white_car(1)
                        else:
                            self._placement_red_car(2)
                    elif self.white_car.count - self.red_car.count >= 2:
                        if self.output_string[-1] == self.white_car.icon:
                            self._placement_red_car(1)
                        else:
                            self._placement_white_car(2)
                    else:
                        if self.output_string[-1] == self.white_car.icon:
                            self._placement_red_car(1)
                        else:
                            self._placement_white_car(1)
        elif (self.x == 0 and self.y) or (self.y == 0 and self.x):
            if self.x > self.y:
                self._placement_red_car(1)
            else:
                self._placement_white_car(1)
            return
        else:
            self.output_string = "Нет решения"
            return

    def __placement_car(self, count, obj):
        for _ in range(count):
            self.output_string += str(obj.icon)
            obj.reduce_count(1)

    def _placement_red_car(self, count):
        self.__placement_car(count, self.red_car)

    def _placement_white_car(self, count):
        self.__placement_car(count, self.white_car)

    def __str__(self):
        return self.output_string
