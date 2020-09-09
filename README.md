# findfib
In this project, one flask app is provided. 

With this app, out of all fibonaci numbers (with repetition), one can find out all possible combinations that sum up to a given target.

## Database
If there is not data base, One needs to create the database first as follows:
- > python
- > from app import db
- > db.create_all()


## Docker
To build the docker image 
- `docker build -t findfib .`

To run the docker image
- `docker run -p 5000:5000 findfib`
