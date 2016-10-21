import player_obj as po
import interface_obj as io

p1 = po.Player(1)
p2 = po.Player(2)

interface = io.Interface(p1, p2)

interface.game()