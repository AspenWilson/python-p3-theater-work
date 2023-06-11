from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Role, Audition

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///roles.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Role).delete()
    session.query(Audition).delete()

    fake = Faker()

    locations = ['Los Angeles', 'New York', 'Irvine', 'San Francisco', 'Hollywood', 'International']

    roles = []
    for i in range(50):
        role = Role(
            character_name = fake.name(),
        )

        session.add(role)
        session.commit()

        roles.append(role)
    
    auditions = []
    for role in roles:
        for i in range(random.randint(1,5)):
            audition = Audition(
                actor=fake.name(),
                location=random.choice(locations),
                phone=fake.phone_number(),
                hired= False,
                role_id=role.id
            )

            auditions.append(audition)

    session.bulk_save_objects(auditions)
    session.commit()
    session.close()