class Cell:

    def __init__(self, is_alive):
        self.cell_status = is_alive

    def is_alive(self):
        return self.cell_status


    def calculate_next_generation(self, neighbours):
        alive_neighbours = 0
        for neighbour in neighbours:
            if neighbour.is_alive():
                alive_neighbours+=1
        if alive_neighbours < 2:
            return False