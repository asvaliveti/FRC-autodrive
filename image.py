import wx

class ImagePanel(wx.Panel):
    def __init__(self, parent=None, id=-1,pos=wx.DefaultPosition, title='wxPython'):
        length = 1000
        width = length * 0.51376721
        imagePath = 'infinite-recharge-field.jpg'
        wx.Frame.__init__(self, parent, id, size=(length, width))
        image_file = 'infinite-recharge-field.jpg'
        bmp = wx.Image(
            image_file, 
            wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        bmp1 = self.scale_bitmap(bmp, length, width)
        self.bitmap1 = wx.StaticBitmap(
            self, -1, bmp1, (0, 0))

    def scale_bitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result
        