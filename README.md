Recommended to use python3 and venv
```bash
python3 -m venv .
source bin/activate
pip install -r requirements.txt
```

Create exabgp.env and named pipe files
```bash
exabgp --fi > etc/exabgp/exabgp.env
mkfifo run/exabgp.{in,out}
chmod 600 run/exabgp.{in,out}
chown $USER:$USER run/exabgp.{in,out}
```
Copy exabgp.conf.dist to exabgp.conf and edit  
Run
```bash
exabgp exabgp.conf
```
