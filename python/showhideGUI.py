import os
import sys
import Tkinter
import pdb

def show():
    os.system("defaults write com.apple.finder AppleShowAllFiles TRUE") 
    os.system("killall Finder")

def hide():
    os.system("defaults write com.apple.finder AppleShowAllFiles FALSE") 
    os.system("killall Finder")
    
    
def main(): 
    pdb.set_trace()
    top = Tkinter.Tk()
    top.title("Show/hide")

    
    show_button = Tkinter.Button(top, text ="Show hidden files", command = show)
    hide_button = Tkinter.Button(top, text ="Hide hidden files", command = hide)
    
    show_button.pack()
    hide_button.pack()
    top.mainloop()





# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()