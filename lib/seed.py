

from models import Company, Dev, Freebie, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#  database engine created
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)  


Session = sessionmaker(bind=engine)
session = Session()

#  instances of Company created
CompanyMicrosoft = Company(name="Company Microsoft", founding_year=1976)
CompanyOracle = Company(name="Company Oracle", founding_year=2017)

#  instances of Dev created
Newton = Dev(name="Newton")
Sirima = Dev(name="Sirima")

# all the sessions together committed tot the database
session.add_all([Newton, Sirima])
session.commit()

# Creating  instances of Freebie
freebie1 = Freebie(item_name="Laptop", value=1000, dev=Newton, company=CompanyMicrosoft)
freebie2 = Freebie(item_name="Database software", value=20, dev=Sirima, company=CompanyOracle)

# Add freebies to the session
session.add_all([freebie1, freebie2])
session.commit()

print("Database seeded successfully!")


