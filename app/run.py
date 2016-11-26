from app import app
from app.models.meta import metadata

if __name__ == '__main__':
    metadata.create_all()
    app.run(debug=True)
