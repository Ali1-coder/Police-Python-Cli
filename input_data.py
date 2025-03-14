from models import Officer, Badge, Case, Suspect, Motorbike, SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_officer():
    
    name = input("Enter officer's name: ")
    rank = input("Enter officer's rank: ")
    db = SessionLocal()
    officer = Officer(name=name, rank=rank)
    db.add(officer)
    db.commit()
    db.refresh(officer)
    db.close()
    print(f"Officer added with ID: {officer.id}")

def add_badge():
    
    badge_number = input("Enter badge number: ")
    officer_id = int(input("Enter officer ID: "))
    db = SessionLocal()
    badge = Badge(badge_number=badge_number, officer_id=officer_id)
    db.add(badge)
    db.commit()
    db.refresh(badge)
    db.close()
    print(f"Badge added with ID: {badge.id}")

def add_case():
    
    case_no = input("Enter case number: ")
    details = input("Enter case details: ")
    officer_id = int(input("Enter officer ID: "))
    db = SessionLocal()
    case = Case(case_no=case_no, details=details, officer_id=officer_id)
    db.add(case)
    db.commit()
    db.refresh(case)
    db.close()
    print(f"Case added with ID: {case.id}")

def add_suspect():
    
    name = input("Enter suspect's name: ")
    address = input("Enter suspect's address: ")
    db = SessionLocal()
    suspect = Suspect(name=name, address=address)
    db.add(suspect)
    db.commit()
    db.refresh(suspect)
    db.close()
    print(f"Suspect added with ID: {suspect.id}")

def add_motorbike():
    
    registration_number = input("Enter motorbike registration number: ")
    model = input("Enter motorbike model: ")
    officer_id = input("Enter officer ID (leave blank if unassigned): ")
    officer_id = int(officer_id) if officer_id else None
    db = SessionLocal()
    motorbike = Motorbike(registration_number=registration_number, model=model, officer_id=officer_id)
    db.add(motorbike)
    db.commit()
    db.refresh(motorbike)
    db.close()
    print(f"Motorbike added with ID: {motorbike.id}")

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