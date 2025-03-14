from input_data import add_officer,add_badge,add_case,add_suspect,add_motorbike
from list_data import list_officers,list_badges,list_cases,list_suspects,list_motorbikes

def show_menu():
    
    print("\nPolice Station Database CLI")
    print("1. Add Officer")
    print("2. Add Badge")
    print("3. Add Case")
    print("4. Add Suspect")
    print("5. Add Motorbike")
    print("6. List Officers")
    print("7. List Cases")
    print("8. List Suspects")
    print("9. List Motorbikes")
    print("10. List Badges")
    print("11. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_officer()
        elif choice == "2":
            add_badge()
        elif choice == "3":
            add_case()
        elif choice == "4":
            add_suspect()
        elif choice == "5":
            add_motorbike()
        elif choice == "6":
            list_officers()
        elif choice == "7":
            list_cases()
        elif choice == "8":
            list_suspects()
        elif choice == "9":
            list_motorbikes()
        elif choice == "10":
            list_badges()
        elif choice == "11":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()