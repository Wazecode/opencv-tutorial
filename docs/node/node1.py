"""Display nodes."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Node()
        Node()
        Node()

if __name__ == '__main__':
    Demo().run()