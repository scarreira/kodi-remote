# kodi-remote
A kodi remote developed for rapsberri pi with TVHeadend running LibreELEC


# To run this app you will need to go trough the capacitor setup guide
Once that is done you can build it just like they state on their documentation

# Note mobile deploy
To deploy for mobile devices you need to run one of this commands

```
npm run build  OR npx cap sync
```

# The app will also run as a web app

### Because the kodi Json RPC does not have a Access-Control-Allow-Origin header and I wanted to develop this as a webapp, I made a simple python 2.7 server to run on the raspberry pi, the server should be set to start on boot

You will need pip, and it can be installed with get-pip

```
wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
```

Note that this was made this way, because my device is running LibreELEC and it does not allow installations outside of Kodi, but it does run python.


[a link](https://github.com/user/repo/blob/branch/other_file.md)
