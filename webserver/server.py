
"""
@author Mahir Oberai mo2654
@author Greg Sansolo gds2127

Columbia's COMS W4111.001 Introduction to Databases
Example Webserver
To run locally:
    python server.py
Go to http://localhost:8111 in your browser.
A debugger such as "pdb" may be helpful for debugging.
Read about it online.
"""
import os
  # accessible as a variable in index.html:
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


#
# The following is a dummy URI that does not connect to a valid database. You will need to modify it to connect to your Part 2 database in order to use the data.
#
# XXX: The URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@35.243.220.243/proj1part2
#
# For example, if you had username gravano and password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://gravano:foobar@35.243.220.243/proj1part2"

"""
I have commented out the database connection part so that I can work on the html pages in the mean time - Mahir


Database connect part starts here

DATABASEURI = "postgresql://user:password@35.243.220.243/proj1part2"


#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

#
# Example of running queries in your database
# Note that this will probably not work if you already have a table named 'test' in your database, containing meaningful data. This is only an example showing you how to run queries in your database using SQLAlchemy.

#add back the quotes 

engine.execute(CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);)
engine.execute(INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');)


@app.before_request
def before_request():
  #add back the quotes
  
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  
  try:
    g.conn = engine.connect()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  #add back the quotes
  
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  
  try:
    g.conn.close()
  except Exception as e:
    pass


Database connect part ends here
"""

#
# @app.route is a decorator around index() that means:
#   run index() whenever the user tries to access the "/" path using a GET request
#
# If you wanted the user to go to, for example, localhost:8111/foobar/ with POST or GET then you could use:
#
#       @app.route("/foobar/", methods=["POST", "GET"])
#
# PROTIP: (the trailing / in the path is important)
# 
# see for routing: http://flask.pocoo.org/docs/0.10/quickstart/#routing
# see for decorators: http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
#
@app.route('/')
def index():
  """
  request is a special object that Flask provides to access web request information:

  request.method:   "GET" or "POST"
  request.form:     if the browser submitted a form, this contains the data in the form
  request.args:     dictionary of URL arguments, e.g., {a:1, b:2} for http://localhost?a=1&b=2

  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
  """

  # DEBUG: this is debugging code to see what request looks like
  print(request.args)


  #
  # example of a database query
  #
  #uncomment this below
  """
  cursor = g.conn.execute("SELECT name FROM test")
  names = []
  for result in cursor:
    names.append(result['name'])  # can also be accessed using result[0]
  cursor.close()




  Part 1 Queries that we outlines:
  1. Query that returns venues along with their artists, setlists, and seat occupancy
  2. Query that returns total duration of setlists in a venue
    To do this, need to sum up song durations of each setlist and then sum up setlist durations
  
  3. Query that returns all artists with a specific genre #maybe make a new genre page

  2.

  cursor = g.conn.execute("
  SELECT V.Name, a.Name, sl.Name, count(s.Seat_ID)  FROM Venues v
  JOIN Artists a on a.Venue_ID = v.Venue_ID
  JOIN Setlists sl ON sl.Venue_ID = v.Venue_ID
  JOIN Seats s ON s.Venue_ID = v.Venue_ID
  GROUP BY v.Name
  ")
  venues_info = []
  for result in cursor:
    venues_info.append(result[0])
  cursor.close()


  """

  #
  # Flask uses Jinja templates, which is an extension to HTML where you can
  # pass data to a template and dynamically generate HTML based on the data
  # (you can think of it as simple PHP)
  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
  #
  # You can see an example template in templates/index.html
  #
  # context are the variables that are passed to the template.
  # for example, "data" key in the context variable defined below will be 
  # accessible as a variable in index.html:
  #
  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
  #     <div>{{data}}</div>
  #     
  #     # creates a <div> tag for each element in data
  #     # will print: 
  #     #
  #     #   <div>grace hopper</div>
  #     #   <div>alan turing</div>
  #     #   <div>ada lovelace</div>
  #     #
  #     {% for n in data %}
  #     <div>{{n}}</div>
  #     {% endfor %}
  #

  #uncomment this below
  #context = dict(data = names)


  #
  # render_template looks in the templates/ folder for files.
  # for example, the below file reads template/index.html
  #
  return render_template("index.html") #, **context) 

#
# This is an example of a different path.  You can see it at:
# 
#     localhost:8111/another
#
# Notice that the function name is another() rather than index()
# The functions for each app.route need to have different names
#
@app.route('/manager')
def manager():
  """
  cursor = g.conn.execute("SELECT Managers.Name FROM Managers")
  managers = []
  for result in cursor:
    names.append(result[0])  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = managers)

  """



  return render_template("manager.html") #, **context)

@app.route('/artist')
def artist():
  """
  #Query that matches the one from part 2

  cursor = g.conn.execute("SELECT * FROM Artists JOIN")
  artists_info = []
  for result in cursor:
    artists_info.append(result[0])
  cursor.close()

  context = dict(data = artists_info)

  """

  return render_template("artist.html") #, **context)

@app.route('/setlist')
def setlist():
  """
  cursor = g.conn.execute("SELECT Setlists.Name FROM Setlists")
  setlists = []
  for result in cursor:
    names.append(result[0])  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = setlists)

  """
  return render_template("setlist.html") #, **context)

@app.route('/song')
def song():
  return render_template("song.html") #, **context)    

@app.route('/venue')
def venue():
  
  """
  1.
  This was according to what was written in our iniital part 1 write up
  I wasn't sure how the database relationships were set up so this may not be possibe


  cursor = g.conn.execute("
  SELECT V.Name, a.Name, sl.Name, count(s.Seat_ID)  FROM Venues v
  JOIN Artists a on a.Venue_ID = v.Venue_ID
  JOIN Setlists sl ON sl.Venue_ID = v.Venue_ID
  JOIN Seats s ON s.Venue_ID = v.Venue_ID
  GROUP BY v.Name
  ")
  venues_info = []
  for result in cursor:
    venues_info.append(result[0])
  cursor.close()  
  
  context = dict(data = venues_info)
  """


  return render_template("venue.html") #, **context)

@app.route('/seat')
def seat():
  """
  cursor = g.conn.execute("SELECT * FROM Seats")
  seats_info = []
  for result in cursor:
    names.append(result[0])  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = seats_info)

  """
  return render_template("seat.html") #, **context)

@app.route('/ticket_holder')
def ticket_holder():
  """
  cursor = g.conn.execute("SELECT Ticket_Holders.Name FROM Ticket_Holders") #not sure how ticket holders table was named
  ticket_holders = []
  for result in cursor:
    names.append(result[0])  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = ticket_holders)

  """
  return render_template("ticket_holder.html") #, **context) 


# Example of adding new data to the database
@app.route('/add', methods=['POST'])
def add():
  name = request.form['name']
  g.conn.execute('INSERT INTO test(name) VALUES (%s)', name)
  return redirect('/')


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using:

        python server.py

    Show the help text using:

        python server.py --help

    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

  run()
