Was unable to upload blockchain-env here...
**Activate the virtual environment**

```
source blockchain-env/bin/activate
```

**Install all packages**

```
pip3 install -r requirements.txt
```

**Run tests**

Make sure to activate virtual environment

```
python3 -m pytest backend/tests
```

**Run the application and API**

Make sure to activate virtual environment

```
python3 -m pytest backend.app
```

**Please install pubnub version 4.1.6**


**Run a peer instance**

Make sure to activate the virtual environment.

```
export PEER=True && python3 -m backend.app
```

