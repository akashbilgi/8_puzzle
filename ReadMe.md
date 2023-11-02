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

## License

This project is licensed under the MIT License 
## Acknowledgments

- Special thanks to Dr. Eamonn Keogh for providing the default test cases and guidance during this project.
- We acknowledge the contributions of open-source libraries and resources that have been instrumental in the development of this solver.

## Contributing

Contributions are welcome and encouraged! If you would like to improve the code, fix issues, or add new features, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or fix: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add your feature'`
4. Push your changes to your fork: `git push origin feature/your-feature-name`
5. Create a pull request to the `main` branch of this repository.

We appreciate your contributions to make this solver even better!


