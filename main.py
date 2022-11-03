from app import create_app, db
import app.models

if __name__=='__main__':
    # Creates application environment
    app=create_app()
    app.run(debug=True)


    # Initialises DB with structure
    ctx=app.app_context()
    ctx.push()
    db.create_all()
