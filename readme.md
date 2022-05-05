Once the folder is extracted, open a terminal in the extracted location. 
- Run `python manage.py runserver`

To populate the database with new datapoints: 
- `python manage.py flush`
- `python manage.py populate`

The program will read files from the `checkPoint2/static/Data` folder when populating the `sqlite3` database

Currently, the program only reads from one file, `lax_terminal1_predictions.csv`, but this can be changed in `checkPoint2/management/commands/populate.py`

My contribution to this project are in the files `checkPointMng/views.py`, `checkPointMng/models.py`, `checkPoint2/templates/base.html`, `checkPoint2/management/commands/populate.py`

The index function in `views.py` is responsible for displaying the main page. It reads in datapoints from the database based on the request from the form, and then sends the information to `base.html`.

In `base.html`, we read the data sent from the index function and display it in the graph.js graph. 