
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
    
    
    def succ(self, action):
        
        """
        Rellenar con el codigo necesario para generar un nuevo estado a partir del actual
        y una accion proporcionada como parametro. La accion tiene el formato '<MC' o '>MC',
        donde M es el numero de misioneros y C el numero de canibales que pasan al otro lado
        del rio. La funcion debe devolver None si el estado generado es invalido segun
        las especificaciones del problema
        """
        return None
        
        
    def next_states(self):
        new_states = []

        """
        Rellenar con el codigo necesario para generar la lista de nuevos estados accesibles
        desde el estado actual, aplicando las diferentes acciones posibles. Los estados deben 
        ser validos segun las especificaciones del problema. La lista debe estar formada por 
        pares (nuevo_estado, accion)
        """
        return new_states
            
        
        