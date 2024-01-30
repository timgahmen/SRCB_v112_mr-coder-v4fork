echo -e "\e[1;34m$(pyfiglet -f slant "starting Bot")\n$(pyfiglet -f slant "radhe radhe")\e[0m"
LANG=en_US.UTF-8
export PYTHONIOENCODING=utf-8
git clean -xdf
nohup python -m main &
