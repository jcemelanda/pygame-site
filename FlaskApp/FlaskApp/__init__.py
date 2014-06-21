import os
from flask import Flask
from views import home_views, downloads_views
from views.mod_docs import docs_views
from views.mod_forum import forum_views
from views.mod_projects import projects_views

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=template_dir)

app.register_blueprint(home_views.view)
app.register_blueprint(downloads_views.view)
app.register_blueprint(docs_views.view)
app.register_blueprint(forum_views.view)
app.register_blueprint(projects_views.view)

if __name__ == "__main__":
	app.run(debug=True)


