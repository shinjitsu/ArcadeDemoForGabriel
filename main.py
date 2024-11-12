import arcade

import Comp151Window

def main():
    our_window = Comp151Window.Comp151Window(
        2000, 2000, "Arcade with a Window Class")
    our_window.setup()
    arcade.run()

main()