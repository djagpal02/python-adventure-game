class Textui:
    """
    Class that allows priniting to console
    """

    def show_map(self,game):
        """
        Function that prints a map to console with location of the user
        ...

        Parameters
        ----------
        :param game: users current game
        :type game: game object
        """
        overall_matrix = []
        for i in game.user.current_location.map.matrix:
            inner_lists = []
            for j in i:
                inner_lists.append(j[1])
            overall_matrix.append(inner_lists)
            
        temp = overall_matrix
        y = game.user.current_location.row
        x = game.user.current_location.col
        temp_var = temp[y][x]
        temp[y][x] = "PLYER" 
        for i in temp:
            print(i)
        temp[y][x] = temp_var
