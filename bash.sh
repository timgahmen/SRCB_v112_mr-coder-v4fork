#!/bin/bash

# Add color to the starting message
echo -e "\e[1;31m$(pyfiglet -f slant "starting")\n$(pyfiglet -f slant "bot")\e[0m\n\e[1;36m$(pyfiglet -f slant "hare")\n\e[1;36m$(pyfiglet -f slant "krishna")\e[0m"

# Set the language and encoding
export LANG=en_US.UTF-8
export PYTHONIOENCODING=utf-8

# Clean git directory and run the Python main script in the background
git clean -xdfq
nohup python -m main > /dev/null 2>&1 &
