import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    print("installing pip pckage")
    
upgrade = "--upgrade pip setuptools wheel"
wget = "wget"
selenium = "selenium"
bs = "beautifulsoup4"
requests = "requests"
pandas = "pandas"
#install(upgrade)
install(wget)
install(requests)
install(bs)
install(pandas)





import wget

url = 'https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_win32.zip'
chromedriver = wget.download(url)