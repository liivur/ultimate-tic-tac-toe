import player_obj as po
import bad_player_obj as bpo
import interface_obj as io

p1 = po.Player(1)
p2 = po.Player(2)
#p2 = bpo.BadPlayer(2)

interface = io.Interface(p1, p2)

interface.game()
