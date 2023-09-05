from app import db

class Graph(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')

    def __repr__(self):
        return f"Graph('{self.title}', '{self.image_file}')"

# >>> from app import app, db
# >>> app.app_context().push()
# >>> db.create_all()
# >>> from app imort Graph
# >>> from app import Graph
# >>> tcell_plot_per_sample = Graph(title='T Cell Plot Per Sample', image_file='figures/clonotype_count/clonotype_count_per_SAMPLE_ID.png')
# >>> db.session.add(tcell_plot_per_sample)
# >>> Graph.query.all() 
# >>> db.drop_all() # clears all data from db