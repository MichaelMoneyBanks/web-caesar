import webapp2


page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>FlickList</title>
</head>
<body>
    <h1>FlickList</h1>
"""

page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):


    def get(self):

        edit_header = "<h3>Edit My Watchlist</h3>"

        # a form for adding new movies
        add_form = """
        <form action="/add" method="post">
            <label>
                I want to add
                <input type="text" name="new-movie"/>
                to my watchlist.
            </label>
            <input type="submit" value="Add It"/>
        </form>
        """

        edit_header = "<h3>Edit My Watchlist</h3>"

    # a form for adding new movies
        add_form = """
        <form action="/remove" method="post">
            <label>
                I want to remove
                <input type="text" name="watched-movie"/>
                from my watchlist.
            </label>
            <input type="submit" value="Remove It"/>
        </form>
        """


        content = page_header + edit_header + add_form + page_footer
        self.response.write(content)


class AddMovie(webapp2.RequestHandler):
    """ Handles requests coming in to '/add'
        e.g. www.flicklist.com/add
    """

    def post(self):
        self.response.write(content)


class RemoveMovie(webapp2.RequestHandler):

    def post(self):

        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddMovie),
    ('/remove', RemoveMovie)
], debug=True)
