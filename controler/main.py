from model.human import Human
from model.analyst import Analyst
from util.creator import HumanCreator
from util.convector import Convector

def main():
    ls = HumanCreator.create(5)
    print(Convector.convert_to_string(ls))

    count_adults = Analyst.count_adult(ls)
    count_alive = Analyst.count_alive(ls)

    print(f"Count of adults: {count_adults}")
    print(f"Count of alive: {count_alive}")


if __name__ == "__main__":
    main()