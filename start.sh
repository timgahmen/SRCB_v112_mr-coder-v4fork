LANG=en_US.UTF-8
export PYTHONIOENCODING=utf-8
pip install -U pip wheel pyaesni
pip install -U -r requirements.txt
nohup python -m main &
top
