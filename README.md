# Romania Map Search

This project implements a search algorithm to find the shortest path between two cities on the Romania map. The algorithm uses a graph search approach and visualizes the search process on a graphical user interface (GUI).

## Dependencies

The following dependencies are required to run the program:

- `tkinter`: Python library for creating GUI applications
- `implementation`: Module containing search algorithm implementation
- `utils`: Module containing utility functions
- `copy`: Module for deep copying objects

## How to Run

1. Make sure you have installed the necessary dependencies.
2. Clone the repository and navigate to the project directory.
3. Run the `main.py` file using Python: `python main.py`.
4. The GUI window will open, displaying the Romania map.
5. Select the start and goal cities from the drop-down menus.
6. Click the "Find Path" button to start the search algorithm.
7. The search process will be visualized on the map, and the shortest path will be displayed when found.

## Algorithm

The search algorithm used in this project is a graph search algorithm. It explores the search space by expanding nodes and adding them to the frontier, which is a priority queue based on the path cost. The algorithm keeps track of explored nodes and avoids revisiting them.

The search algorithm proceeds in three steps:

1. Selection: The algorithm selects the next node to expand from the frontier based on the lowest path cost.
2. Expansion: The selected node is expanded by generating its child nodes. Child nodes are added to the frontier if they have not been explored or added to the frontier before.
3. Visualization: The GUI visualizes the current state of the frontier and explored nodes on the map.

## GUI Features

The GUI provides the following features:

- Visualization of the Romania map with cities and connections.
- Drop-down menus to select the start and goal cities.
- "Find Path" button to initiate the search algorithm.
- Visual representation of the search process on the map.
- Different node types displayed with different colors:
  - Unexplored Node: White
  - Frontier Node: Yellow
  - Current Node: Red
  - Explored Node: Blue
  - Solution Node: Purple

## File Structure

The project files are organized as follows:

- `main.py`: The main script to run the program and create the GUI window.
- `implementation.py`: Module containing the search algorithm implementation.
- `utils.py`: Module containing utility functions.
- `romania_map.py`: Module containing the map of Romania and its connections.
- `README.md`: This file, providing an overview of the project.

## Conclusion

The Romania Map Search project demonstrates the use of a graph search algorithm to find the shortest path between cities. The GUI provides an interactive way to visualize the search process and observe the exploration of nodes. This project can be extended to incorporate other search algorithms or different maps for pathfinding applications.
