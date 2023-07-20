# Knights and Knaves

This repository contains a Python program that solves various puzzles involving knights and knaves. Knights always tell the truth, and knaves always lie. The puzzles involve statements made by individuals, and the program uses logical reasoning to determine the identities of knights and knaves.

## How to Run

To run the Knights and Knaves Puzzle Solver, you will need to have Python installed on your system. Clone this repository and navigate to the project directory. Then, run the following command:

```
python puzzle.py
```

The program will solve four different puzzles and display the identities of knights and knaves based on the given logical statements.

## Files

- `puzzle.py`: This is the main Python file that contains the logical sentences and solves the puzzles. It uses the `logic.py` module to handle logical expressions and reasoning.

- `logic.py`: This file defines logical symbols (e.g., `Symbol`, `Not`, `And`, `Or`, `Implication`, `Biconditional`) and provides methods to evaluate and handle logical sentences.

## Dependencies

There are no external dependencies required to run this program.

## How the AI Works

The Knights and Knaves Puzzle Solver uses logical reasoning to determine the identities of knights and knaves based on their statements. It formulates logical sentences representing the statements made by different individuals and then evaluates these sentences using truth assignments for the symbols (knights and knaves).

The program defines the following symbols:

- AKnight: A represents "A is a Knight."
- AKnave: A represents "A is a Knave."
- BKnight: B represents "B is a Knight."
- BKnave: B represents "B is a Knave."
- CKnight: C represents "C is a Knight."
- CKnave: C represents "C is a Knave."

Each puzzle's knowledge base contains logical sentences representing the statements made by different individuals. The program then checks all possible truth assignments for these symbols to see which combinations satisfy the knowledge base.

1. Loading Knowledge: The program loads the knowledge base for each puzzle, which consists of logical sentences representing the statements made by individuals.

2. Evaluating Statements: For each puzzle, the program evaluates all possible truth assignments for the symbols to check if the knowledge base entails the query (the answer to the puzzle). It uses the `model_check` function from `logic.py` to check entailment.

3. Determining Identities: If a truth assignment satisfies the knowledge base, the program determines the identities of knights and knaves based on the truth values assigned to the symbols.

The program prints the results for each puzzle, displaying the identities of knights and knaves.
