class Wizard:
    def __init__(self, name, health_points, mana_points):
        try:
            if len(name) < 3:
                raise ValueError("Имя  меньше 3 символов")

            if health_points <= 0:
                raise ValueError("Здоровье меньше 0")

            if mana_points < 0:
                raise ValueError("Мана меньше 0")
        except ValueError as e:
            print(e)
        else:
            print('всё ок')
        finally:
            print("удачи вам")

w = Wizard('kkkk', 1, -1)