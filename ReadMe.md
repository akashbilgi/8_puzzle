# Python Solver for Sliding Puzzle

This Python script provides a solver for the classic 8-puzzle problem. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one empty tile. The objective is to arrange the tiles in a specific order by sliding them into the empty space.

The solver uses the A* search algorithm with two heuristic functions to find the optimal solution. You can choose between the Manhattan distance heuristic or the misplaced tiles heuristic to guide the search.

## Features

- Solves the 8-puzzle problem using A* search with two heuristic options.
- Provides clear and concise code for solving the problem.
- Supports user input for the initial state of the puzzle.
- Includes test cases for various solvable initial states.
- Measures and displays performance metrics, including runtime, nodes expanded, and max queue size.

## Getting Started

### Prerequisites

- Python 3.x

### Usage

1. Choose the input type: test cases or user input.
2. Select the search algorithm (A* with Manhattan distance, A* with misplaced tiles, or Uniform Cost Search).
3. Run the script and follow the prompts to enter the initial state or choose a test case.

## Examples

To run the solver with a test case:

```bash
python puzzle_solver.py
