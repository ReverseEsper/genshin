# To install service : 
1. Copy webhook.py to /lib/systemd/system/ folder
2. Change rights of file : sudo chmod 644 /lib/systemd/system/driverobot.service
3. Restart systemd : sudo systemctl daemon-reload
4. Enable servief : sudo systemctl enable driverobot.service