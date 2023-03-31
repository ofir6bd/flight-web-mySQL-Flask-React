# """
# need to delete the migrations folder first, 
# this file will create the emapty table in the DB
# """

# def deploy():
# 	"""Run deployment tasks."""
# 	from models import create_app,db,UserRoles,Users,Administrators,Customers, Countries,AirlineCompanies,Flights,Tickets
# 	from flask_migrate import upgrade,migrate,init,stamp

	
# 	app = create_app()
# 	app.app_context().push()
# 	db.create_all()

# 	# migrate database to latest revision
# 	init()
# 	stamp()
# 	migrate()
# 	upgrade()
	
# deploy()