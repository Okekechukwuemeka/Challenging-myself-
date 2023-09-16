''' PROJECT FOR PYTHONIC REALITY.'''
#GUESS A WORD GAME. 
from random import choice as wordChoice 
from json import load
import wx 

class MyFrame(wx.Frame):

    def __init__(self):
        super().__init__(parent=None, title='Guess A Word Game.')

        #load the content from words.json
        self.file_opening = open('words.json', 'r')
        self.__read_file = load(self.file_opening)

        panel = wx.Panel(self)
        self.__label = wx.StaticText(panel, wx.ID_ANY, '')
        self.__update_random_word()    #initialise the random word

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel, wx.ID_ANY, value='')
        main_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        btn = wx.Button(panel, label='&Guess')
        btn.Bind(wx.EVT_BUTTON, self.on_guess)
        main_sizer.Add(btn, 0, wx.ALL | wx.CENTER, 5)

        label = wx.StaticText(panel, label='Welcome To The Game')
        button = wx.Button(panel, label='&Exit', id=wx.ID_EXIT)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(label, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        sizer.Add(button, 0, wx.ALIGN_CENTER | wx.ALL, 20)

        panel.SetSizer(main_sizer)
        panel.SetSizer(sizer)
        self.Bind(wx.EVT_BUTTON, lambda evt: self.Close(), button)
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(5000)
        self.Show()

    def on_timer(self, event):
        self.timer.Stop()
        self.Close() 
        print('Your time is up.')

    #method that update the random word
    def __update_random_word(self):
        self.__rand_word = wordChoice(self.__read_file)
        self.__rand_word_length = len(self.__rand_word)
        self.__first_letter = self.__rand_word[0]
        self.__last_letter = self.__rand_word[-1]
        label = f' Input a {self.__rand_word_length} letter word that begins with "{self.__first_letter}" and ends with "{self.__last_letter}" in your mind'
        self.__label.SetLabel(label)

    #method that confirms the result
    def __is_correct_word(self, word):
        is_first_letter = word.startswith(self.__first_letter)
        is_last_letter= word.endswith(self.__last_letter)
        is_same_length = self.__rand_word_length == len(word)
        word_exist = word in self.__read_file
        return (is_first_letter and is_last_letter and is_same_length and word_exist)


    def on_guess(self, event):
        #checks if the inputed word is either True or False and store it.
        is_true_value = self.__is_correct_word(self.text_ctrl.GetValue())

        title = 'Wow! Bravo!' if is_true_value else 'Oops!'
        msg = 'Congratulations! you are correct, you can now proceed to the next level.' if is_true_value else f'Oops! you are wrong.'

        dlg = wx.MessageDialog(None, msg, title)
        dlg.ShowModal()
        dlg.Destroy()
        #update the random word
        self.__update_random_word()
        self.text_ctrl.SetValue('')

if __name__ == '__main__':
    app = wx.App()
    message = wx.MessageBox('take note', 'Welcome to the Guess A Word Game! you have 5 seconds to complete this level')
    frame = MyFrame()
    app.MainLoop()