#!/bin/bash
echo "Extracting SSH login attempts..."
grep "sshd" /var/log/auth.log | grep "Accepted" > ssh_logins.txt
echo "Extracted logins saved to ssh_logins.txt"
