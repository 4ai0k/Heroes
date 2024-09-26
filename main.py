from heroClasses.heroesClasses import MyHero

if __name__ == '__main__':
    gimli = MyHero("Гимли", "воин")
    print(gimli.add_exp(200))
    print(gimli.add_exp(300))
    print(gimli.add_exp(500))

    print()

    legolas = MyHero("Леголас", "рейнджер")
    print(legolas.add_exp(500))
    print(legolas.add_exp(500))

    print()

    gendalf = MyHero("Гендальф", "маг")
    print(gendalf.add_exp(1000))
