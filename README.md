# SMS Notifications Web Application with Twilio and Python | Flask

## Local Development

1. You will need to configure Twilio account to send SMS and receive HTTP POST to the application.

   You will need Account SID, AUTH Token, and Messaging SID to send SMS.

   [Please see twilio documentation here](https://www.twilio.com/docs/sms).

1. Clone this repository and `cd` into it.

1. Create a new virtual environment.

   - If using [venv](https://docs.python.org/3/library/venv.html):

     ```
     python3 -m venv <env name>
     source <env name>/bin/activate
     ```

1. Install the requirements using [pip](https://pip.pypa.io/en/stable/installing/).

   ```
   pip install -r requirements.txt
   ```

1. Project is using python-dotenv package to register environment variables automatically imported when you run flask command so you can avoid to set FLASK_APP environment variable to the entry point every time.

1. Run the migrations.

   ```
   flask db upgrade
   ```

1. Start the development server.

   ```
   flask run
   ```

1. To test your webhook use [ngrok](https://ngrok.com)

   To start using `ngrok` in our project you'll have execute to the following
   line in the _command prompt_.

   ```
   ngrok http 5000 -host-header="localhost:5000"
   ```

   Keep in mind that our endpoint is:

   ```
   http://<your-ngrok-subdomain>.ngrok.io/message
   ```

## Run the tests

You can run the tests locally through [coverage](http://coverage.readthedocs.org/):

1. Run the tests.

   ```
   $ coverage run test.py
   ```

You can then view the results with `coverage report` or build an HTML report with `coverage html`.
