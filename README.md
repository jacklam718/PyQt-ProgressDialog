#About
This is a PyQt Progress Bar you can easily to use this library or inherit it

#Example
```python
from progressBar import DownloadProgressBar, UploadProgressBar, ProgressDialog

# create a ProgressDialog instance
progressDialog = ProgressDialog()

# create a DownloadProgressBar instance, you can pass an argument as the progress bar title
progressBar = DownloadProgressBar(text="Downloading")
# set max value
progressBar.setMax(100)
# set current value
progressBar.setValue(' ' * progress)
progressDialog.addProgressbar(progressbar)
# finally call show method
progressDialog.show()
```
> You can also directly execute the **progressBar.py** preview the effect

#Install
```bash
git clone https://github.com/jacklam718/PyQt-ProgressDialog
cd PyQt-ProgressDialog
python or python3 setup.py install
```

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
