class Hero:
    """Добавлен базовый класс Hero"""
    __mage_skills = ["огненный шар", "ледяная стрела", "удар молнии"]
    __warrior_skills = ["удар в прыжке", "вой", "берсерк"]
    __ranger_skills = ["быстрая стрельба", "двойной выстрел", "скрытность"]

    def __init__(self, name):
        """Написан конструктор для класса"""
        self.__name = name
        self.__my_hero_skills = []
        self.__level = 0
        self.__exp = 0

    def get_name(self):
        """Написан геттер для поля name"""
        return self.__name

    def get_level(self):
        """Написан геттер для поля level"""
        return self.__level

    def get_my_hero_skills(self):
        """Написан геттер для поля my_hero_skills"""
        return self.__my_hero_skills

    def get_exp(self):
        """Написан геттер для поля exp"""
        return self.__exp

    def set_my_hero_skills(self, my_hero_skills):
        """Написан сеттер для поля my_hero_skills"""
        self.__my_hero_skills = my_hero_skills

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
        """Написан метод для нового уровня. Он определяет уровень и если нужно вызывает метод add_skill()"""
        if self.get_exp() >= 1000:
            self.__level = 3
            self.add_skill()
        elif self.get_exp() >= 500:
            self.__level = 2
            self.add_skill()
        elif self.get_exp() >= 200:
            self.__level = 1
            self.add_skill()
        else:
            self.__level = 0
        return f"Герой {self.get_name()}, теперь {self.get_level()} уровня, навыки: {', '.join(self.get_my_hero_skills())}"

    def add_exp(self, exp):
        """Написан метод опыта, она складывает опыт и вызывает метод get_new_level()"""
        self.__exp += exp
        new_level = self.get_new_level()
        return new_level

    def add_skill(self):
        """Написан метод"""
        pass


class MyHero(Hero):

    def __init__(self, name, character_class):
        """Написан конструктор для класса"""
        super().__init__(name)
        self.__character_class = character_class
        self.__skill_list = super().get_skills(character_class)

    def get_skill_list(self):
        """Написан геттер для поля skill_list"""
        return self.__skill_list

    def add_skill(self):
        """Написан метод, который запрашивает у пользователя навык и проверяет есть ли такой в допустимых навыках.
        Если такой навык присутствует, он помещает эту строку в список my_hero_skills и удаляет его из поля skill_list
        и делает проверку: если уровень героя равен длине списка my_hero_skills, то он прерывает цикл."""
        while True:
            skill = input(f'{super().get_name()}, выберете навык: {", ".join(self.get_skill_list())}\n')
            while skill not in self.get_skill_list():
                skill = input(f'НЕВЕРНЫЙ ВЫБОР!! Выберете навык: {", ".join(self.get_skill_list())}\n')
            my_hero_skills = super().get_my_hero_skills()
            my_hero_skills.append(skill)
            super().set_my_hero_skills(my_hero_skills)
            self.__skill_list.remove(skill)
            if len(my_hero_skills) == super().get_level():
                break
