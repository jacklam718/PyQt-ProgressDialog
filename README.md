#About
This is a PyQt Progress Bar you can easily to use this library or inherit it

#Usage

```python
from progressBar import DownloadProgressBar, UploadProgressBar, ProgressDialog

# create a ProgressDialog instance
progressDialog = ProgressDialog()

# create a DownloadProgressBar instance, you can pass a argument as the progress bar title
progressBar = DownloadProgressBar(text="title")
# set max value
progressBar.set_max(100)
# set current value
progressBar.set_value(' ' * progressItem)

# finally call the addProgressbar method and show method
progressDialog.addProgressbar(progressbar)
progressDialog.show()
```
> You can also directly execute the **progressBar.py** preview the effect

#Tips
You can easily change the progress bar style
```python
class DownloadProgressBar(BaseProgressBar):
    def __init__(self, text='Downloading', parent=None):
        super(self.__class__, self).__init__(text, parent)
        style ="""
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: #37DA7E;
            width: 20px;
        }"""
        self.progressbar.setStyleSheet(style)
```

#Screenshots
<img src="https://raw.github.com/jacklam718/PyQt-ProgressBar/master/screenshots/progressbars.png" alt="progressbars">
