Step 1: To create virtual Environment(Only once it need to be exected)
    For window:- py -3 -m venv venv
    for linux:- sudo apt install python3.11-venv

Step 2: Installing packages from requirements file 
        ## Windows 
        1. py -3 -m venv .venv

        ## Linux
        python3 -m venv .venv 

 

Step 3: Activate virual Enviroment (everytime when opening new project)
        ## Windows 
        1. .venv\Scripts\activate 

        ## Linux
        . .venv/bin/activate

step 4: Is to install dependencies
        pip install -r requirement.txt

Step 5: Run flask app
        ## Linux
        export FLASK_APP=run

        ## Windows 
        set FLASK_APP=run

step 6: Run flask app
        ### common
        * flask run --debug
