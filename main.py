from classes import Candidate
from colors import bcolors
import functions
def entrance():
    """
    log in or sign out to the system
    :return: type of user
    """
    while True:
        choice = int(input(bcolors.OKBLUE + 'choose an option: \n1. Log in \n2. Sign out\n'))
        if choice == 1:
            if functions.log_in() is Candidate:
                print('log in succeeded')
                return 'Candidate'
            else:
                return 'Employer'

        elif choice == 2:
            typ_ = functions.sign_up()
            print('sign out succeeded')
            return typ_
        print(bcolors.FAIL + 'Invalid input, Try again' + bcolors.ENDC)

#The system output:
print(bcolors.BLUEBG + 'Welcome To Search Job System' + bcolors.ENDC)
typ = entrance()


