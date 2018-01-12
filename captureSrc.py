#! Python 3

import wx
import time
import sys

time_delay = 0
ts = time.time()
file_name = "screenshot_" + str(ts)

if __name__ == "__main__":
    app = wx.App()

    # check for args being passed
    if len(sys.argv) > 1:
        # delay in seconds
        if len(sys.argv) >= 2:
            time_delay = sys.argv[1]

            # filename
            if len(sys.argv) >= 3:
                file_name = sys.argv[2]

    if time_delay > 0:
        time.sleep(float(time_delay))

    # capture screen and save it to file
    screen = wx.ScreenDC()
    size = screen.GetSize()
    bmp = wx.EmptyBitmap(size[0], size[1])
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
    del mem
    bmp.SaveFile(file_name + ".png", wx.BITMAP_TYPE_PNG)

    # show alert message
    dlg = wx.MessageDialog(None, "Screenshot was saved as " + file_name + ".png", "Alert",
                           wx.OK | wx.ICON_INFORMATION | wx.STAY_ON_TOP)
    dlg.ShowModal()
    dlg.Destroy()

