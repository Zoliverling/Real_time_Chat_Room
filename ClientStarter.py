from ChatClient import chatUI

import singleChatClient
import socket, threading
import tkinter as tk


class UIFooter(tk.Frame):
    def __init__(self,root,chat_callback=None, single_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._chat_callback = chat_callback
        self._single_callback = single_callback
        self._draw()

    def groupChatClick(self):
        if self._chat_callback is not None:
            self._chat_callback()

    def singleChatClick(self):
        if self._single_callback is not None:
            self._single_callback()


    def _draw(self):
        self.singleButton = tk.Button(master = self, text="1v1 Chat", width=20)
        self.singleButton.configure(command=self.singleChatClick)
        self.singleButton.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.groupButton = tk.Button(master=self, text="Group Chat", width=20)
        self.groupButton.configure(command=self.groupChatClick)
        self.groupButton.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)


class Starter(tk.Frame):
    def __init__(self, root):
        self.host = '127.0.0.1'
        self.port = 8000
        tk.Frame.__init__(self, root)
        self.root = root
        self._draw()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    def connect(self, msg:str):
        try:
            self.client.connect((self.host, self.port))
        except socket.error as e:
            print(str(e))
        self.client.send(msg.encode('utf-8'))
        self.client.close()

    def SingleChatClick(self):
        if getattr(self.client, '_closed') is not False:
            self.connect("single")
        self.root.destroy()
        self.window = tk.Tk()
        singleChatClient.chatUI(self.window)

    def ChatClick(self):
        if getattr(self.client, '_closed') is not False:
            self.connect("group")
        self.root.destroy()
        self.window = tk.Tk()
        chatUI(self.window)

    def _draw(self):
        self.footer = UIFooter(self.root, self.ChatClick, self.SingleChatClick)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)


if __name__ == "__main__":
    main = tk.Tk()
    # main.geometry("1920x1080")
    Starter(main)
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    main.mainloop()