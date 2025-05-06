from classes import Candidate
from colors import bcolors
import functions
def entrance():
    """
    log in or sign op to the system
    :return: type of user
    """
    while True:
        choice = int(input(bcolors.OKBLUE + 'choose an option: \n1. Log in \n2. Sign up\n'))
        x, username = functions.log_in()
        if choice == 1:
            if x is Candidate:
                print('Welcome ', username)
                return 'Candidate'
            else:
                print('Welcome ', username)
                return 'Employer'


        elif choice == 2:
            typ_ = functions.sign_up()
            print('sign up succeeded')
            return typ_
        print(bcolors.FAIL + 'Invalid input, Try again' + bcolors.ENDC)

#The system output:
print(bcolors.BLUEBG + 'Welcome To Search Job System' + bcolors.ENDC)
typ = entrance()


