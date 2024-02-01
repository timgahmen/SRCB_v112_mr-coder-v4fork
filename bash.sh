#!/bin/bash

function check_requirements() {
    if ! command -v pip &> /dev/null; then
        echo "Error: pip is not installed. Please install pip to manage Python packages."
        exit 1
    fi

    # Check if all packages listed in requirements.txt are installed
    if ! pip install -r requirements.txt &> /dev/null; then
        echo "Installing necessary packages using pip..."
        pip install -U -r requirements.txt
    else
        echo "All pip dependencies are already installed."
    fi
}

check_requirements  # Call the check_requirements function to install necessary packages if needed

echo -e "\e[1;31m$(pyfiglet -f slant "starting")\n$(pyfiglet -f slant "bot")\e[0m\n\e[1;36m$(pyfiglet -f slant "hare")\n\e[1;36m$(pyfiglet -f slant "krishna")\e[0m"

export LANG=en_US.UTF-8
export PYTHONIOENCODING=utf-8

git clean -xdfq  # Clean the git directory

nohup python -m main > /dev/null 2>&1 &  # Run the Python main script in the background
