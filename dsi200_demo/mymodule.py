#mymodule.py
class Textbox(object):
    """
    This is my base class for simple textbox
    """
    top="^"
    bottom="."
    def __init__(self, text="empty"):
        self.text=text
        str_list=text.split("\n")
        longest_str=max(map(len,str_list))
        self.width=longest_str+5*2
        self.height=len(str_list)
        
    def __str__(self):
        buffer=""
        buffer+=self.top * self.width+"\n"
        str_list=self.text.split("\n")
        for i in str_list:
            margin=(self.width-len(i))//2
            buffer+=" " * margin + i +"\n"
            print
        buffer+=self.bottom * self.width
        return buffer
    
    def render(self):
        """
        To print the textbox on command line
        """
        print(self)

class TextboxA(Textbox):
    """
    Textbox with 'a' on top and bottom lines
    """
    def __init__(self,text="empty"):
        self.top='a'
        self.bottom='a'
        super().__init__(text)
        
class TextboxB(Textbox):
    """
    Textbox with UPPER case text
    """
    def __str__(self):
        return super().__str__().upper()