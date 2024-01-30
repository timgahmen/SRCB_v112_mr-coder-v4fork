echo -e "\e[1;36m$(pyfiglet -f slant "hare")\n$(pyfiglet -f slant "krishna")\e[0m"
LANG=en_US.UTF-8
export PYTHONIOENCODING=utf-8
git clean -xdf
nohup python -m main &
