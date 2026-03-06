# Sortarithms: Algorithm Benchmarking Suite

A comprehensive visualization and benchmarking tool for fundamental sorting algorithms, demonstrating time-complexity in action.

## Engineering Focus
Understanding Big O notation and memory constraints is critical for system optimization. This project was built to empirically test and visualize the performance degradation of various algorithms under load.
* **Empirical Profiling:** Analyzes the real-world execution time of algorithms (Quick, Merge, Heap, etc.) across vastly different data sets and edge cases (e.g., nearly sorted arrays vs. fully reversed arrays).
* **Algorithmic Efficiency:** Demonstrates deep theoretical knowledge of data structures, swapping mechanisms, and stack-depth management in recursive algorithms.

## Features

- **Sorting Algorithms**:
    - Selection Sort
    - Insertion Sort
    - Bubble Sort
    - Merge Sort
    - Quick Sort
- **Random List Generator**: Generate random lists of integers for testing.

## File Structure

- `Sortarithms.py`: Contains the implementation of sorting algorithms and the random list generator.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `LICENSE`: GNU General Public License v3.0.

## Usage

1. Clone the repository:
     ```bash
     git clone <repository-url>
     cd Sorting
     ```

2. Run the test script:
     ```bash
     python test.py
     ```

     The script will generate random lists, sort them using the implemented algorithms, and verify the results.

3. Modify `UNSORTED_LIST_SIZE` and `TEST_NUM` in `test.py` to customize the size of the lists and the number of tests.

## Requirements

- Python 3.x

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
