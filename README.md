# JobApplicationBot

## Dependencies
- install python latest : https://www.python.org/downloads/
- check if pip installed, pip version should be latetst : pip -V

### start by installing the following manually:
- pip install selenium 
- pip install beautifulsoup4 requests
- pip install pandas
- download chromedriver from the web
### or run the install script:
~~~python
python install.py
~~~
[install.py](install.py)

## Demonstration of current state:

see the demo of current state below
![demonstration current state](demo.gif)
[recaptcha solver](https://drive.google.com/file/d/16Z0dYWyP3KWJGuRIdSHUOGWzUrN9iJJO/view?usp=sharing)

## Running jupyter notebook
~~~jupyter
install visual studio code
add jupyter notebook extension
open bot.ipynb
run all cells
~~~

## Imporvement TODO
- solve recaptcha v2 (matching images with words) maybe image recognition algorithm
- avoid being detected as a robot selenium
- slow down the speed of execution to mimic humans
- switch to parent indeed url while applying(could maybe avoid robot detection)
- integrate indeed and linkedin portals for quick apply
- go beyond and apply for non quick apply jobs


