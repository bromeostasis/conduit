# Conduit take-home assignment
This repository houses the take-home assignment for Conduit Tech. Included is all code needed to solve the problem as well as backend tests and an explanation document (this README!).

The solution relies on a React app on the frontend that is connected to a flask server on the backend. The flask server largely uses `pandas` to filter and query the csv in order to find the next material category and values!

## Running the solution locally

*Note: this solution was built with the following libraries/version:*

* Mac: OS 12.5
* Python: 3.7.3
* node: v16.18.0
* npm: 8.19.2

1. Clone the repository: `git clone git@github.com:bromeostasis/conduit.git`
1. Go to the backend : `cd backend`
1. Create a virtual env: `python3 -m venv conduit`
1. Activate it: `source conduit/bin/activate`
1. Install requirements: `pip install -r requirements.txt`
1. Run tests (optional!): `pytest`. All tests should pass!
1. Start the server: `python server.py`. You can confirm this is working by heading to [http://localhost:5000/](http://localhost:5000/). You will see a greeting response.
1. Open a second terminal/tab. You will need one for the frontend and one for the backend
1. `cd` to where you've cloned the repository. Then, `cd frontend`
1. Run `npm i` to install dependencies
1. Run `npm start` to start the frontend. If the backend is running, you should see the working application! Create react app usually opens this for you, but if not, you can manually head to this link: [http://localhost:3000/](http://localhost:3000/)

## Next steps

As with any timed assignment (or real feature!), there was not enough time to complete everything I wanted to do. Below is a list of tasks I wanted to do, but did not complete (in rough priority order):


* Add typescript to frontend
* Backend input validation\*
* More error handling in `reader.py`\*
* Frontend tests
* Switch from endpoint returning an array to a single value. Initially, I was thinking I'd return multiple results (to, for example, pre-select a field with only one value), but ultimately decided not to go in that direction.

\*I decided not to implement these since we have a fairly "closed system". If any piece of this was opened up to interface with external libraries or pieces of software, this would become much more imperative.

## Tradeoffs

One important tradeoff I made was to read directly from the csv. Given the scope of the assignment, I felt this would allow me to scale the solution up quickly. However, in a production-like environment, the first change I would make would likely be to store this data in the database. This allows the data to change much more easily and scales better if there are thousands or hundreds of thousands of options.


Another consequential decision was to store the list of selections in an array instead of a dictionary. I personally liked the benefits that the ordered index of the array provided. Alternatively, I could have stored the selections in a dictionary, which would have made getting the category easier (I had to do a lot of selecting the first key of the dictionary), but determining which category was next would have been more cumbersome.