#!/bin/bash
python3.11 -m venv venv
source venv/bin/activate
python3.11 -m ensurepip
python3.11 -m pip install -r requirements.txt
