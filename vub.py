from random import choice

capital = "Brussels"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the Range"


def randomfunfact():
    funfacts = [
        "Brusssels is considered the most fun city to live in, but it does have some bad neighbourhood.",
        "Antwerp is the largest city in Flanders, but many would guess that it is Ghent.",
        "A considerable portion of Brussels is actually in Flanders.",

    ]

    index = choice("0123")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
