class Hero:
    """Добавлен базовый класс Hero"""
    __mage_skills = ["огненный шар", "ледяная стрела", "удар молнии"]
    __warrior_skills = ["удар в прыжке", "вой", "берсерк"]
    __ranger_skills = ["быстрая стрельба", "двойной выстрел", "скрытность"]

    def __init__(self, name):
        """Написан конструктор для класса"""
        self.__name = name
        self.my_hero_skills = []
        self.__level = 0
        self.__exp = 0

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_exp(self):
        return self.__exp

    def get_skills(self, character_class):
        """Добавлен геттер для навыков, результат зависит от выбранного класса"""
        if character_class == 'воин':
            return self.__warrior_skills
        elif character_class == 'маг':
            return self.__mage_skills
        elif character_class == 'рейнджер':
            return self.__ranger_skills
        else:
            exit("Ошибка перезапустите программу!")

    def get_new_level(self):
        if self.get_exp() >= 1000:
            self.__level = 3
        elif self.get_exp() >= 500:
            self.__level = 2
        elif self.get_exp() >= 200:
            self.__level = 1
        else:
            self.level = 0
        return f"Герой {self.get_name()}, теперь {self.get_level()} уровня, навыки: {', '.join(self.my_hero_skills)}"

    def add_exp(self, exp):
        self.__exp += exp
        new_level = self.get_new_level()
        return new_level

class MyHero(Hero):

    def __init__(self, name, character_class):
        super().__init__(name)
        self.__skill_list = super().get_skills(character_class)

    def get_skill_list(self):
        return self.__skill_list


