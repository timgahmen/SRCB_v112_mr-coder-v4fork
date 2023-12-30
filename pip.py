import subprocess

def install_dependencies():
    try:
        subprocess.check_call(['pip', 'install', '-U', '-r', 'requirements.txt'])
        print('All dependencies have been installed successfully.')
    except subprocess.CalledProcessError as e:
        print('An error occurred while installing the dependencies:', e)

if __name__ == "__main__":
    install_dependencies()
