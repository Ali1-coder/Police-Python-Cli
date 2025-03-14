from models import Officer, Badge, Case, Suspect, Motorbike, SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def list_officers():
    
    db = SessionLocal()
    officers = db.query(Officer).all()
    for officer in officers:
        print(f"ID: {officer.id}, Name: {officer.name}, Rank: {officer.rank}")
    db.close()

def list_cases():
    
    db = SessionLocal()
    cases = db.query(Case).all()
    for case in cases:
        print(f"ID: {case.id}, Case No: {case.case_no}, Details: {case.details}, Officer ID: {case.officer_id}")
    db.close()

def list_suspects():
    
    db = SessionLocal()
    suspects = db.query(Suspect).all()
    for suspect in suspects:
        print(f"ID: {suspect.id}, Name: {suspect.name}, Address: {suspect.address}")
    db.close()

def list_motorbikes():
   
    db = SessionLocal()
    motorbikes = db.query(Motorbike).all()
    for motorbike in motorbikes:
        print(f"ID: {motorbike.id}, Registration: {motorbike.registration_number}, Model: {motorbike.model}, Officer ID: {motorbike.officer_id}")
    db.close()

def list_badges():
    
    db = SessionLocal()
    badges = db.query(Badge).all()
    for badge in badges:
        print(f"ID: {badge.id}, Badge Number: {badge.badge_number}, Officer ID: {badge.officer_id}")
    db.close()