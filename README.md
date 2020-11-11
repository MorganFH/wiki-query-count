# wiki-query-count

Basic web app that counts number of occurences of a `topic` word in the Wikipedia article text for that `topic`. Can optionally specify a `section` within the article to count occurences for. This defaults to counting all sections.

![Image of project](https://i.imgur.com/DcE0epH.png)


See `backend_script.py`for the script that counts the occurences.

## Setup
Run the following commands to setup and run the project:

- Clone the project using `git clone`
- Run`cd wiki-query-count` to enter the project directory
- Create a virtual environment using `python3 -m venv venv`
- Activate the virtual environment with `source venv/bin/activate`
- Install required python packages with `pip install -r requirements.txt`
- Install required packages for frontend `cd frontend && npm install`
- Compile frontend with `npm run dev`
- Start the django server with `cd .. && python manage.py runserver`
- If necessary, migrate database with `python manage.py migrate`
