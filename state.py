
class MissionariesState:
    """
    This class is used to represent a state of the missionaries
    and cannibals problem. Each state contains the number of
    missionaries and cannibals in each shore, the position
    of the boat, and the capacity of the boat to determine
    whether a state is valid or not.
    """
    
    def __init__(self, left_miss, left_cann, right_miss, right_cann, boat_position, capacity=2):
        self.miss = (left_miss, right_miss)  # missionaries in left and right shores
        self.cann = (left_cann, right_cann)  # cannibals in left and right shores
        self.boat_position = boat_position   # boat position ('left', 'right')
        self.capacity = capacity             # boat capacity (missionaries+cannibals)
        
    def __str__(self):
        to_str = "(%d, %d)" % (self.miss[0], self.cann[0])
        if self.boat_position == "left":
            to_str += " (||)      "
        else:
            to_str += "      (||) "
        to_str += "(%d, %d)" % (self.miss[1], self.cann[1])
        return to_str
        
    def __eq__(self, other):
        return self.miss == other.miss and self.cann == other.cann and self.boat_position == other.boat_position
    
    def __hash__(self):
        # Crea una tupla de todos los atributos relevantes para el hash
        return hash((self.miss, self.cann, self.boat_position))

    def succ(self, action):
        """
        Genera un nuevo estado a partir de la acción dada, validando el resultado.
        Las acciones son en el formato '<MC' o '>MC', donde M es el número de
        misioneros y C es el número de caníbales que pasan al otro lado del río.
        """
        if action[0] not in ['<', '>']:
            raise ValueError(f"Incorrect direction '{action[0]}'")  # Validación de la dirección

        M = int(action[1])  # Número de misioneros que se mueven
        C = int(action[2])  # Número de caníbales que se mueven
        
        # Determina el nuevo estado basado en la posición actual del bote
        if self.boat_position == "left" and action[0] == '>':
            new_miss = (self.miss[0] - M, self.miss[1] + M)
            new_cann = (self.cann[0] - C, self.cann[1] + C)
            new_boat_position = "right"
        elif self.boat_position == "right" and action[0] == '<':
            new_miss = (self.miss[0] + M, self.miss[1] - M)
            new_cann = (self.cann[0] + C, self.cann[1] - C)
            new_boat_position = "left"
        else:
            return None  # Movimiento inválido si el bote está en el lado equivocado
        
        # Verifica que no hay numero negativo de canibales ni misioneros en las orillas
        for miss in new_miss:
            if miss < 0:
                return None

        for cann in new_cann:
            if cann < 0:
                return None

        if (new_miss[0] < new_cann[0] and new_miss[0] > 0) or (new_miss[1] < new_cann[1] and new_miss[1] > 0):
            return None  # Estado inválido (más caníbales que misioneros en alguna orilla)
        
        return MissionariesState(new_miss[0], new_cann[0], new_miss[1], new_cann[1], new_boat_position, self.capacity)

        
        
    def next_states(self):
        new_states = []
        actions = ['<00', '<01', '<10', '<11', '>00', '>01', '>10', '>11']  # Posibles acciones
        
        for action in actions:
            new_state = self.succ(action)
            if new_state is not None:  # Solo añade estados válidos
                new_states.append((new_state, action))
    
        return new_states

        
        