from graphics import *

x = 400
y = 400

# Start the code and asks user if they would like to proceed.


def start():
    print("Lets Play Othello!")
    print("Are you ready to begin?")

    while True:
        answer = input("[Y/N] ")

        if "y" in answer.lower():
            print("go")
            break

        else:
            print("Whenever your ready..")


# Prints the board.4x4 layout.


def board():
    win = GraphWin("Final Project", x * 2, y * 2)
    win.setCoords(0, 0, x, y)
    win.setBackground("Green")

    i = 0

    while i < x:
        l = Line(Point(i, 0), Point(i, y))
        l.draw(win)
        l = Line(Point(0, i), Point(x, i))
        l.draw(win)
        i = i + (x / 4)

    return win


# the points on the board x-axis, y-axis coordinates on 400x400 console screen.


def boardkey():
    bank = [
        (50, 50),
        (150, 50),
        (250, 50),
        (350, 50),
        (50, 150),
        (350, 150),
        (50, 250),
        (350, 250),
        (50, 350),
        (150, 350),
        (250, 350),
        (350, 350),
    ]

    return bank


# Gets the X and Y points of the user and centers it so the pieces are more
# centered on the board within the squares.


def getPoint(win):
    mouse = win.getMouse()
    mX = mouse.getX()
    mY = mouse.getY()

    if mX >= 0 and mX < 100:
        nmX = 50
    elif mX >= 100 and mX < 200:
        nmX = 150
    elif mX >= 200 and mX < 300:
        nmX = 250
    else:
        nmX = 350
    if mY >= 0 and mY < 100:
        nmY = 50
    elif mY >= 100 and mY < 200:
        nmY = 150
    elif mY >= 200 and mY < 300:
        nmY = 250
    else:
        nmY = 350

    return nmX, nmY


# The point at which Player 1 (Black) appends points from the main bank into
# its own list to be colored later on in the program.


def blackmoves(nmX, nmY, black, white, bank):
    bp = nmX, nmY

    if bp in bank:
        black.append(bp)
        bank.remove(bp)

    return bp


# The point at which Player 2 (White) appends points from the main bank into
# its own list to be colored later on in the program.


def whitemoves(nmX, nmY, black, white, bank):
    wp = nmX, nmY

    if wp in bank:
        white.append(wp)
        bank.remove(wp)

    return wp


# The brain.. Checks the pieces and appends to the correct list for coloring.
# The logic behind whether it takes pieces or not.


def checkpieces(wp, bp, white, black, bank):
    if len(bank) % 2 != 0:
        loop = 0
        # Loops twice to check through list
        while loop < 2:
            # COMMENT: Confusing loop!  Make it clearer by breaking parts
            #   into functions, making variable names more explanatory, etc.
            # Black evaluating whether it should take white.
            for p in black:
                if bp[0] == p[0] or bp[1] == p[1]:
                    for i in white:
                        if bp[0] == i[0] and (p[1] == i[1] - 100 or p[1] == i[1] + 100):
                            if (
                                bp[1] < i[1]
                                and p[1] > i[1]
                                or bp[1] > i[1]
                                and p[1] < i[1]
                            ):
                                white.remove(i)
                                black.append(i)

                        if bp[1] == i[1] and (p[0] == i[0] - 100 or p[0] == i[0] + 100):
                            if (
                                bp[0] <= i[0]
                                and p[0] >= i[0]
                                or bp[0] >= i[0]
                                and p[0] <= i[0]
                            ):
                                white.remove(i)
                                black.append(i)

            loop += 1

    else:
        loop2 = 0
        # Loops twice to check through list for the white side.
        while loop2 < 2:
            # COMMENT: This loop is rather similar to above loop.  Avoid
            #  repetition, by making key parts that are repeated into one
            #  function.
            # White evaluating whether it should take black.
            for a in white:
                if wp[0] == a[0] or wp[1] == a[1]:
                    for b in black:
                        if wp[0] == b[0] and (a[1] == b[1] - 100 or a[1] == b[1] + 100):
                            if (
                                wp[1] < b[1]
                                and a[1] > b[1]
                                or wp[1] > b[1]
                                and a[1] < b[1]
                            ):
                                black.remove(b)
                                white.append(b)

                        if wp[1] == b[1] and (a[0] == b[0] - 100 or a[0] == b[0] + 100):
                            if (wp[0] < b[0] and a[0] > b[0]) or (
                                wp[0] > b[0] and a[0] < b[0]
                            ):
                                black.remove(b)
                                white.append(b)
            loop2 += 1


# Check both lists or set and colors it based on its algorithm.


def draw_color(black, white, win):
    for i in black:
        dbP = Circle(Point(i[0], i[1]), 20)
        dbP.setFill("Black")
        dbP.draw(win)

    for p in white:
        dwP = Circle(Point(p[0], p[1]), 20)
        dwP.setFill("White")
        dwP.draw(win)


# Prints the score to the console.


def scorekeep(black, white, win, bank):
    resetscore1 = Rectangle(Point(160, 387), Point(198, 399))
    resetscore1.setFill("Grey")

    resetscore2 = Rectangle(Point(240, 387), Point(202, 399))
    resetscore2.setFill("Grey")

    resetscore3 = Rectangle(Point(327, 387), Point(373, 399))
    resetscore3.setFill("Grey")

    p1 = Text(Point(175, 393), "Black: ")
    p1.setSize(15)
    p1s = Text(Point(188, 393), str(len(black)))
    p1s.setSize(15)
    p2 = Text(Point(218, 393), "White: ")
    p2.setSize(15)
    p2s = Text(Point(232, 393), str(len(white)))
    p2s.setSize(15)

    if len(bank) % 2 == 0:
        p3 = Text(Point(350, 393), "Black's Turn")
        p3.setSize(15)

    else:
        p3 = Text(Point(350, 393), "White's Turn")
        p3.setSize(15)

    return (
        resetscore1.draw(win),
        resetscore2.draw(win),
        resetscore3.draw(win),
        p1.draw(win),
        p1s.draw(win),
        p2.draw(win),
        p2s.draw(win),
        p3.draw(win),
    )


# Ending of the program and prints the winner.


def end(black, white, win, bank):
    if len(bank) == 0:
        if len(black) > len(white):
            resetscore4 = Rectangle(Point(327, 387), Point(373, 399))
            resetscore4.setFill("Grey")
            p4 = Text(Point(350, 393), "Black Wins!")
            p4.setSize(15)
            resetscore4.draw(win)
            p4.draw(win)

        elif len(white) > len(black):
            resetscore4 = Rectangle(Point(327, 387), Point(373, 399))
            resetscore4.setFill("Grey")
            p4 = Text(Point(350, 393), "White Wins!")
            p4.setSize(15)
            resetscore4.draw(win)
            p4.draw(win)

        else:
            resetscore4 = Rectangle(Point(327, 387), Point(373, 399))
            resetscore4.setFill("Grey")
            p4 = Text(Point(350, 393), "Draw!")
            p4.setSize(15)
            resetscore4.draw(win)
            p4.draw(win)


# Main!!


# COMMENT: Nice main which is broken into functions with easy to follow logic
def main():
    start()
    wp, bp = 0, 0
    bank = boardkey()
    win = board()

    black = [(250, 150), (150, 250)]
    white = [(150, 150), (250, 250)]

    draw_color(black, white, win)

    while len(bank) != 0:
        scorekeep(black, white, win, bank)
        nmX, nmY = getPoint(win)

        if len(bank) % 2 == 0:
            bp = blackmoves(nmX, nmY, black, white, bank)
        else:
            wp = whitemoves(nmX, nmY, black, white, bank)
        checkpieces(wp, bp, white, black, bank)

        draw_color(black, white, win)
        end(black, white, win, bank)

    print("play again?")
    i = input("[Y/N]")

    if "y" in i.lower():
        return main()


if __name__ == "__main__":
    main()
