from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A is either a Knight or a Knave but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # If A is a Knight, then A is telling the truth
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is a Knave, then A is lying
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A and B are either Knights or Knaves but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # If A is a Knight, then A is telling the truth
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is a Knave, then A is lying
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A and B are either Knights or Knaves but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # If A is a Knight, then A is telling the truth about being the same kind
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    # If A is a Knave, then A is lying about being the same kind
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # If B is a Knight, then B is telling the truth about being of different kinds
    Implication(BKnight, Or(And(BKnight, AKnave), And(BKnave, BKnight))),
    # If B is a Knave, then B is lying about being of different kinds
    Implication(BKnave, Not(Or(And(BKnight, AKnave), And(BKnave, BKnight))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A, B, and C are either Knights or Knaves but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    # If B is a Knight, then B is telling the truth about C being a Knave
    Implication(BKnight, CKnave),
    # If B is a Knight, then B is telling the truth about A's statement
    Implication(BKnight, And(
        # If A is a Knight, then A is saying "I am a Knave"
        Implication(AKnight, AKnave),
        # If A is a Knave, then A is lying about being a Knave
        Implication(AKnave, Not(AKnave))
    )),
    # If B is a Knave, then B is lying about C being a Knave
    Implication(BKnave, Not(CKnave)),
    # If B is a Knave, then B is lying about A's statement
    Implication(BKnave, And(
        # If A is a Knight, then A is saying "I am a Knight"
        Implication(AKnight, AKnight),
        # If A is a Knave, then A is lying about being a Knight
        Implication(AKnave, Not(AKnight))
    )),
    # If C is a Knight, then C is telling the truth about A being a Knight
    Implication(CKnight, AKnight),
    # If C is a Knave, then C is lying about A being a Knight
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
