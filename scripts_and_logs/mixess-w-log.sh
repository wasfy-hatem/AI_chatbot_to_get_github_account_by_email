#!/bin/bash
/usr/bin/python3.6 /home/centos/python_progs/webhook_github_slack/app.py 2>&1 | tee /home/centos/python_progs/webhook_github_slack/scripts_and_logs/log.log

