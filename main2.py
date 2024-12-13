from gui2 import *

def main():
    window = Tk()
    window.title('Grade Calculator')
    window.geometry('600x600')
    window.resizable(False, False) 

    Gui(window)
    window.mainloop()
    
if __name__ == '__main__':
    main()