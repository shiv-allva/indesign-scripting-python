import win32com.client
app = win32com.client.Dispatch('InDesign.Application.2022')

print("adding document")
myDocument = app.Documents.Add()
myPage = myDocument.Pages.Item(1)
print("adding frame")
myTextFrame = myPage.TextFrames.Add()
myTextFrame.GeometricBounds = ["6p0", "6p0", "18p0", "18p0"]
myTextFrame.Contents = "Hello World!"
