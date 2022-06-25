# ds4a-crimen Team-234

## Prerequisites (Do this only once)
- Create .env file with environment variables (ask a colleague for the values)
- Create virtual environment: python -m venv venv/
- Activate the virtual environment: (linux/mac) source venv/bin/activate (windows) .\venv\Scripts\activate.bat
- Install dependencies: pip install -r requirements.txt

## Steps to run the APP 
- Activate the virtual environment: (linux/mac) source venv/bin/activate (windows) .\venv\Scripts\activate.bat
- Run the app: python src/app.py
- Open the browser and visit: http://127.0.0.1:8050/


## How to install new dependencies
- Make sure the virtual environment is active see (Steps to run the APP), install the package with pip install package-name , Update the
requirements.txt file with: pip freeze > requirements.txt, commit your changes in git

## Deployment
- Buildfile: install dependencies required to comunicate with postgresql on the Ec2 instances
- Procfile: executes gunicorn as production server
- Every commit to master will trigger codepipeline and deploy the app to this url: http://ds4ateam234crimeapp-env.eba-8mmqfrr8.us-east-1.elasticbeanstalk.com/

