
# use __init__. if __init__ is not exist in directory, this will not work.
# __init__ means certain directory is included.
import game.sound.echo
game.sound.echo.echo_test() # echo

# use __all__
from game.sound import *
echo.echo_test()    # echo

