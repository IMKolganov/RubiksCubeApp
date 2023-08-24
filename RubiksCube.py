class RubiksCube:
    def __init__(self, size=3):
        self.size = size
        self.cube = self._initialize_cube()
        self.neighbours = self._define_neighbours()

    def _initialize_cube(self):
        faces = ['W', 'R', 'B', 'O', 'G', 'Y']
        return {face: [[face for _ in range(self.size)] for _ in range(self.size)] for face in faces}

    def _define_neighbours(self):
        return {
            'W': [('R', 'top'), ('B', 'top'), ('O', 'top'), ('G', 'top')],
            'R': [('W', 'right'), ('B', 'left'), ('Y', 'right'), ('G', 'right')],
            'B': [('W', 'bottom'), ('R', 'top'), ('Y', 'top'), ('O', 'bottom')],
            'O': [('W', 'left'), ('B', 'right'), ('Y', 'left'), ('G', 'left')],
            'G': [('W', 'top'), ('R', 'bottom'), ('Y', 'bottom'), ('O', 'top')],
            'Y': [('R', 'bottom'), ('B', 'bottom'), ('O', 'bottom'), ('G', 'bottom')],
        }

    def rotate(self, face='B'):
        # Вращаем грань
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]
        
        # Вращаем соседние грани
        for neighbour, position in self.neighbours[face]:
            # Логика для вращения соседних граней (тут можно добавить больше логики)
            pass

    def display(self):
        for face, data in self.cube.items():
            print(f"Face {face}:")
            for row in data:
                print(" ".join(row))
            print()