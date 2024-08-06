## Firewall

File 100-port_forwarding is the replica of the configuration file /etc/ufw/before.rules on my server after updating it. I was tasked to configure my server so that its firewall redirects port 8080/TCP to port 80/TCP.
Line 11 to 15 are the updates made in the file.
After the update the below commands were run:
sudo ufw allow 8080
sudo ufw status
sudo service ufw restart
sudo ufw enable