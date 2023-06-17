from implementation import *
from utils import PriorityQueue
from copy import deepcopy
from tkinter import *

window = None
romaniaMap = None
romania_problem = None
counter = -1
frontier = None
node = None
explored = None
city_coord = {}


def drawline(map, x0, y0, x1, y1, distance):

    map.create_line(x0, y0, x1, y1, fill='#88324f')
    map.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=distance)

def drawrectangle(map, x0, y0, margin, city_name):

    global city_coord
    rect = map.create_rectangle(
        x0 - margin,
        y0 - margin,
        x0 + margin,
        y0 + margin,
        fill="white")
    if "Bucharest" in city_name or "Pitesti" in city_name or "Lugoj" in city_name \
            or "Mehadia" in city_name or "Drobeta" in city_name:
        map.create_text(
            x0 - 2 * margin,
            y0 - 2 * margin,
            text=city_name,
            anchor=E)
    else:
        map.create_text(
            x0 - 2 * margin,
            y0 - 2 * margin,
            text=city_name,
            anchor=SE)
    city_coord.update({city_name: rect})



def createMap(window):

    global romaniaMap, start, goal
    romania_locations = romania_map.locations
    width = 1000
    height = 640
    margin = 8.5
    romaniaMap = Canvas(window, width=width, height=height)
    romaniaMap.pack()

    drawline(
        romaniaMap,
        romania_locations['Arad'][0],
        height -
        romania_locations['Arad'][1],
        romania_locations['Sibiu'][0],
        height -
        romania_locations['Sibiu'][1],
        romania_map.get('Arad', 'Sibiu'))
    drawline(
        romaniaMap,
        romania_locations['Arad'][0],
        height -
        romania_locations['Arad'][1],
        romania_locations['Zerind'][0],
        height -
        romania_locations['Zerind'][1],
        romania_map.get('Arad', 'Zerind'))
    drawline(
        romaniaMap,
        romania_locations['Arad'][0],
        height -
        romania_locations['Arad'][1],
        romania_locations['Timisoara'][0],
        height -
        romania_locations['Timisoara'][1],
        romania_map.get('Arad', 'Timisoara'))
    drawline(
        romaniaMap,
        romania_locations['Oradea'][0],
        height -
        romania_locations['Oradea'][1],
        romania_locations['Zerind'][0],
        height -
        romania_locations['Zerind'][1],
        romania_map.get('Oradea', 'Zerind'))
    drawline(
        romaniaMap,
        romania_locations['Oradea'][0],
        height -
        romania_locations['Oradea'][1],
        romania_locations['Sibiu'][0],
        height -
        romania_locations['Sibiu'][1],
        romania_map.get('Oradea', 'Sibiu'))
    drawline(
        romaniaMap,
        romania_locations['Lugoj'][0],
        height -
        romania_locations['Lugoj'][1],
        romania_locations['Timisoara'][0],
        height -
        romania_locations['Timisoara'][1],
        romania_map.get('Lugoj', 'Timisoara'))
    drawline(
        romaniaMap,
        romania_locations['Lugoj'][0],
        height -
        romania_locations['Lugoj'][1],
        romania_locations['Mehadia'][0],
        height -
        romania_locations['Mehadia'][1],
        romania_map.get('Lugoj', 'Mehadia'))
    drawline(
        romaniaMap,
        romania_locations['Drobeta'][0],
        height -
        romania_locations['Drobeta'][1],
        romania_locations['Mehadia'][0],
        height -
        romania_locations['Mehadia'][1],
        romania_map.get('Drobeta', 'Mehadia'))
    drawline(
        romaniaMap,
        romania_locations['Drobeta'][0],
        height -
        romania_locations['Drobeta'][1],
        romania_locations['Craiova'][0],
        height -
        romania_locations['Craiova'][1],
        romania_map.get('Drobeta', 'Craiova'))
    drawline(
        romaniaMap,
        romania_locations['Pitesti'][0],
        height -
        romania_locations['Pitesti'][1],
        romania_locations['Craiova'][0],
        height -
        romania_locations['Craiova'][1],
        romania_map.get('Pitesti', 'Craiova'))
    drawline(
        romaniaMap,
        romania_locations['Rimnicu'][0],
        height -
        romania_locations['Rimnicu'][1],
        romania_locations['Craiova'][0],
        height -
        romania_locations['Craiova'][1],
        romania_map.get('Rimnicu', 'Craiova'))
    drawline(
        romaniaMap,
        romania_locations['Rimnicu'][0],
        height -
        romania_locations['Rimnicu'][1],
        romania_locations['Sibiu'][0],
        height -
        romania_locations['Sibiu'][1],
        romania_map.get('Rimnicu', 'Sibiu'))
    drawline(
        romaniaMap,
        romania_locations['Rimnicu'][0],
        height -
        romania_locations['Rimnicu'][1],
        romania_locations['Pitesti'][0],
        height -
        romania_locations['Pitesti'][1],
        romania_map.get('Rimnicu', 'Pitesti'))
    drawline(
        romaniaMap,
        romania_locations['Bucharest'][0],
        height -
        romania_locations['Bucharest'][1],
        romania_locations['Pitesti'][0],
        height -
        romania_locations['Pitesti'][1],
        romania_map.get('Bucharest', 'Pitesti'))
    drawline(
        romaniaMap,
        romania_locations['Fagaras'][0],
        height -
        romania_locations['Fagaras'][1],
        romania_locations['Sibiu'][0],
        height -
        romania_locations['Sibiu'][1],
        romania_map.get('Fagaras', 'Sibiu'))
    drawline(
        romaniaMap,
        romania_locations['Fagaras'][0],
        height -
        romania_locations['Fagaras'][1],
        romania_locations['Bucharest'][0],
        height -
        romania_locations['Bucharest'][1],
        romania_map.get('Fagaras', 'Bucharest'))
    drawline(
        romaniaMap,
        romania_locations['Giurgiu'][0],
        height -
        romania_locations['Giurgiu'][1],
        romania_locations['Bucharest'][0],
        height -
        romania_locations['Bucharest'][1],
        romania_map.get('Giurgiu', 'Bucharest'))
    drawline(
        romaniaMap,
        romania_locations['Urziceni'][0],
        height -
        romania_locations['Urziceni'][1],
        romania_locations['Bucharest'][0],
        height -
        romania_locations['Bucharest'][1],
        romania_map.get('Urziceni', 'Bucharest'))
    drawline(
        romaniaMap,
        romania_locations['Urziceni'][0],
        height -
        romania_locations['Urziceni'][1],
        romania_locations['Hirsova'][0],
        height -
        romania_locations['Hirsova'][1],
        romania_map.get('Urziceni', 'Hirsova'))
    drawline(
        romaniaMap,
        romania_locations['Eforie'][0],
        height -
        romania_locations['Eforie'][1],
        romania_locations['Hirsova'][0],
        height -
        romania_locations['Hirsova'][1],
        romania_map.get('Eforie', 'Hirsova'))
    drawline(
        romaniaMap,
        romania_locations['Urziceni'][0],
        height -
        romania_locations['Urziceni'][1],
        romania_locations['Vaslui'][0],
        height -
        romania_locations['Vaslui'][1],
        romania_map.get('Urziceni', 'Vaslui'))
    drawline(
        romaniaMap,
        romania_locations['Iasi'][0],
        height -
        romania_locations['Iasi'][1],
        romania_locations['Vaslui'][0],
        height -
        romania_locations['Vaslui'][1],
        romania_map.get('Iasi', 'Vaslui'))
    drawline(
        romaniaMap,
        romania_locations['Iasi'][0],
        height -
        romania_locations['Iasi'][1],
        romania_locations['Neamt'][0],
        height -
        romania_locations['Neamt'][1],
        romania_map.get('Iasi', 'Neamt'))

    for city in romania_locations.keys():
        drawrectangle(
            romaniaMap,
            romania_locations[city][0],
            height -
            romania_locations[city][1],
            margin,
            city)

    setType(romaniaMap)


def setType(map):
    rect1 = map.create_rectangle(300, 500, 310, 510, fill="white")
    text1 = map.create_text(315, 505, anchor=W, text="Unexplored Node")

    rect2 = map.create_rectangle(300, 515, 310, 525, fill="yellow")
    text2 = map.create_text(315, 520, anchor=W, text="Frontier Node")

    rect3 = map.create_rectangle(300, 530, 310, 540, fill="red")
    text3 = map.create_text(315, 535, anchor=W, text="Current")

    rect4 = map.create_rectangle(300, 545, 310, 555, fill="blue")
    text4 = map.create_text(315, 550, anchor=W, text="Explored Node")

    rect5 = map.create_rectangle(300, 560, 310, 570, fill="#88324f")
    text5 = map.create_text(315, 565, anchor=W, text="Solution Node")
    
    text5 = map.create_text(750, 80, anchor=W, text="Straight Line distance to Bucharest", fill="#88324f")

    text5 = map.create_text(800, 110, anchor=W, text="Arad:              366", fill="#88324f")
    
    text5 = map.create_text(800, 125, anchor=W, text="Bucharest:       0", fill="#88324f")
    text5 = map.create_text(800, 140, anchor=W, text="Craiova:         160", fill="#88324f")
    text5 = map.create_text(800, 155, anchor=W, text="Dobreta:         242", fill="#88324f")
    text5 = map.create_text(800, 170, anchor=W, text="Eforie:            161", fill="#88324f")
    text5 = map.create_text(800, 185, anchor=W, text="Fagaras:         178", fill="#88324f")
    text5 = map.create_text(800, 200, anchor=W, text="Giurgiu:          77", fill="#88324f")
    text5 = map.create_text(800, 215, anchor=W, text="Hirsova:          151", fill="#88324f")
    text5 = map.create_text(800, 230, anchor=W, text="Iasi:                  226", fill="#88324f")
    text5 = map.create_text(800, 245, anchor=W, text="Lugoj:              244", fill="#88324f")
    text5 = map.create_text(800, 260, anchor=W, text="Mehadia:         241", fill="#88324f")
    text5 = map.create_text(800, 275, anchor=W, text="Neamt:            234", fill="#88324f")
    text5 = map.create_text(800, 290, anchor=W, text="Oradea:            380", fill="#88324f")
    text5 = map.create_text(800, 305, anchor=W, text="Piteshi:             98", fill="#88324f")
    text5 = map.create_text(800, 320, anchor=W, text="Rimnicu Vilcea:  193", fill="#88324f")
    text5 = map.create_text(800, 335, anchor=W, text="Sibiu:                253", fill="#88324f")
    text5 = map.create_text(800, 350, anchor=W, text="Timisoara:        329", fill="#88324f")
    text5 = map.create_text(800, 365, anchor=W, text="Urziceni:           80", fill="#88324f")
    text5 = map.create_text(800, 380, anchor=W, text="Vaslui:             199", fill="#88324f")
    text5 = map.create_text(800, 395, anchor=W, text="Zerind:            374", fill="#88324f")

def graph_search(problem):

    global counter, frontier, node, explored
    if counter == -1:
        frontier.append(Node(problem.initial))
        explored = set()

        display_frontier(frontier)
    if counter % 3 == 0 and counter >= 0:
        node = frontier.pop()

        curr(node)
    if counter % 3 == 1 and counter >= 0:
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        frontier.extend(child for child in node.expand(problem)
                        if child.state not in explored and
                        child not in frontier)

        display_frontier(frontier)
    if counter % 3 == 2 and counter >= 0:
        display_explored(node)
    return None


def display_frontier(queue):

    global romaniaMap, city_coord
    qu = deepcopy(queue)
    while qu:
        node = qu.pop()
        for city in city_coord.keys():
            if node.state == city:
                romaniaMap.itemconfig(city_coord[city], fill="yellow")

def curr(node):
    global romaniaMap, city_coord
    city = node.state
    romaniaMap.itemconfig(city_coord[city], fill="red")

def display_explored(node):

    global romaniaMap, city_coord
    city = node.state
    romaniaMap.itemconfig(city_coord[city], fill="blue")

def display_final(cities):

    global romaniaMap, city_coord
    for city in cities:
        romaniaMap.itemconfig(city_coord[city], fill="#88324f")

def bestfs(problem, f):

    global frontier, node, explored, counter

    if counter == -1:
        f = memoize(f, 'f')
        node = Node(problem.initial)
        curr(node)
    
        frontier = PriorityQueue('min', f)
        frontier.append(node)
        display_frontier(frontier)
        explored = set()
    if problem.goal_test(node.state):
        return node
    if counter % 3 == 0 and counter >= 0:
        node = frontier.pop()
        curr(node)
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
       # cost+=node.path_cost
      
    if counter % 3 == 1 and counter >= 0:
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
        display_frontier(frontier)
    if counter % 3 == 2 and counter >= 0:
        display_explored(node)
    return None


def g_bfs(problem,h=None):

    h = memoize(h or problem.h, 'h')
    return bestfs(problem, lambda n: h(n))

def on_click():
    global algo, counter, next_button, romania_problem, start, goal
    romania_problem = GraphProblem(start.get(), goal.get(), romania_map)
    node = g_bfs(romania_problem)
    if node is not None:
        final_path = g_bfs(romania_problem).solution()
        final_path.append(start.get())
        display_final(final_path)
        next_button.config(state="disabled")
    counter += 1

def exit_window():
    window.destroy()
    exit()


if __name__ == "__main__":
    global aldo,start,goal,next_button
    window=Tk()
    window.title("AI Assignment")
    window.geometry("1920x1080")
    window.configure(bg='#88324f')
    Label(window,text="Gready BFS",fg = "Black",
		 bg = "White",
		 font = "Arial").pack()
    start = StringVar(window)
    goal = StringVar(window)
    start.set(None)
    goal.set(None)
    cities = sorted(romania_map.locations.keys())
    frame1 = Frame(window)
    Label(frame1, text="Source", font=("Helvetica", 13), fg="#88324f").grid(row=0,column=0)
    start_menu = OptionMenu(frame1, start, *cities)
    start_menu.grid(row=0 ,column=1)
    Label(frame1, text="Destination", font=("Helvetica", 13), fg="#88324f").grid(row=1, column=0)
    goal_menu = OptionMenu(frame1, goal, *cities)
    
    goal_menu.grid(row=1 ,column=1)
    frame1.pack()
    
    createMap(window)
    frame2 = Frame(window)
    next_button = Button(
        frame2,
        width=20,
        height=2,
        text="Next",
        command=on_click,
        padx=2,
        pady=2,
        relief=RAISED)
    next_button.grid(row=0 ,column=0)
    reset_button = Button(
        frame2,
        width=20,
        height=2,
        text="Exit",
        command=exit_window,
        padx=2,
        pady=2,
        relief=RAISED)
    reset_button.grid(row=0 ,column=1)
    frame2.pack()
    
    window.mainloop()

