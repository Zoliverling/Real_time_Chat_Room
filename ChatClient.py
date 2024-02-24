import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import ttk, filedialog
from socket import *
import json
import socket
from _thread import *
import threading

class UIFooter(tk.Frame):
    def __init__(self,root,send_callback = None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._draw()

    def send_click(self):
        if self._send_callback is not None:
            self._send_callback()

    def quit_click(self):
        self.root.destroy()

    def _draw(self):
        self.send_button = tk.Button(master = self,text = "Send",width = 20)
        self.send_button.configure(command=self.send_click)
        self.send_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.quit_button = tk.Button(master = self,text = "Quit",width = 20)
        self.quit_button.configure(command=self.quit_click)
        self.quit_button.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)

        

class UIBody(tk.Frame):
    def __init__(self,root):
        tk.Frame.__init__(self,root)
        self.root = root
        self._draw()

    def get_text_entry(self) -> str:
        return self.entry_editor.get('1.0', 'end').rstrip()

    def set_text_entry(self, text:str):
        self.entry_editor.delete("1.0","end")
        self.entry_editor.insert(tk.END, text)
        
    def reset_text_entry(self):
        self.set_text_entry("")

    def set_text(self,mes):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END,mes)
        self.text_area.config(state='disabled')

    def _draw(self):
        text_Frame = tk.Frame(master = self,width = 400)
        text_Frame.pack(fill=tk.BOTH,side = tk.TOP)
        
        self.text_area = tk.Text(text_Frame,width = 0)
        self.text_area.pack(fill=tk.BOTH,side=tk.TOP,expand = True,padx = 0,pady = 0)
        self.text_area.config(state='disabled')

        text_scroll_frame = tk.Frame(master=text_Frame, bg="blue", width=10)
        text_scroll_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=False)

        text_editor_scrollbar = tk.Scrollbar(master=text_scroll_frame, command=self.text_area.yview)
        self.text_area['yscrollcommand'] = text_editor_scrollbar.set
        text_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT, expand=False, padx=0, pady=0)
    
        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        
        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        
        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
        
        self.entry_editor = tk.Text(editor_frame, width=0)
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame, command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.LEFT, expand=False, padx=0, pady=0)


class chatUI(tk.Frame):
    def __init__(self,root):
        self.host = '127.0.0.1'
        self.port = 8000
        tk.Frame.__init__(self, root)
        self.root = root
        self.connect()
        self._draw()
        

    def connect(self):
        self.ClientSocket = socket.socket()
        try:
            self.ClientSocket.connect((self.host, self.port))
        except socket.error as e:
            print(str(e))
        threading._start_new_thread(self.receive, (self.ClientSocket, "m"))

    def receive(self,sck,m):
        while True:
            data = sck.recv(4096)
            if not data:
                break
            self.body.set_text(data.decode('utf-8'))
        sck.close()
        self.root.destroy()

    def send_response(self):
        text = self.body.get_text_entry()
        self.body.reset_text_entry()
        self.body.set_text("You : "+text+'\n')
        self.ClientSocket.send(str.encode(text))
        
    
    def _draw(self):
        self.body = UIBody(self.root)
        self.body.pack(fill=tk.BOTH,side=tk.TOP,expand = True)
        self.footer = UIFooter(self.root,self.send_response)
        self.footer.pack(fill=tk.BOTH,side=tk.BOTTOM)

if __name__ == "__main__":
    main = tk.Tk()
    #main.geometry("1920x1080")
    chatUI(main)
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    main.mainloop()
    
        
        
