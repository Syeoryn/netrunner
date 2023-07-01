# Netrunner
This project is a [Streamlit](https://streamlit.io/) app built to visualize and share netrunner cards, trends, and statistics.

## Getting Started
To start developing on this project, run:
```shell
pip3 install -r requirements.txt  # install project dependencies.
```

To run the project run
```shell
streamlit run netrunner/app.py  # run the netrunner server locally
```
And then navigate in your browser to [http://localhost:8501](http://localhost:8501) (or the url indicated in the output of the above command).
While the server is running, all changes will be auto-updated on save, just refresh the browser.  You can also toggle on "auto-reload" in the menu in the upper right corner of the browser.

To run tests, run:
```shell
pytest
```


## Streamlit Concepts
Streamlit embraces scripting, and [magically](https://docs.streamlit.io/library/api-reference/write-magic/magic) renders any data you give it.
Anytime anything needs to be updated on the page (perhaps after user input), streamlit reruns the entire python script from top to bottom.  For this reason, code needs to be written in a way that can be rerun, and should rely on [session state](https://docs.streamlit.io/library/api-reference/session-state#use-callbacks-to-update-session-state) to persist data in a user session between runs.  Session state is not shared across user sessions.

You can read more [here](https://docs.streamlit.io/library/get-started/main-concepts).