# basic GUI test; MK1

# Need to import wx, for wxPython access
import wx


# Creating instance of the application object, only 1 can exist per application
app = wx.App(False)
# title  = appears at the top of window; parent = close
frame = wx.Frame(parent = None, title = 'Hello World')
frame.Show()  # Make visible to the user
app.MainLoop()  # Starts the event loop

