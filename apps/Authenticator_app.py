# Import the required library
import psycopg2
import re
import pandas as pd
import os
from trycourier import Courier
import secrets
from argon2 import PasswordHasher
import requests



ph = PasswordHasher() 

# Method to create a connection object
# It creates a pointer cursor to the dataframe
# and returns it along with Connection object
def create_connection(path):
    '''Create connection to database.'''
    # read the dataFrame
    userDataFrame = pd.read_csv(path)

    return userDataFrame


def generate_id(id):
    return id + 1


def creat_data_frame(path) -> None:
    '''Creat dataframe for each user in folder.'''

    userDict = {'id':1,

       }
    
    df = pd.DataFrame(userDict)

    # path of user data file
    newPath = os.join(path, 'userData.csv')

    # saving the dataframe
    df.to_csv(newPath)


def update_data_frame(id, first_name, last_name, e_mail, phone_number, birthDay, screeining_day, gender, city, register_date, pass_word, image_location):
    '''Update the user's information dataframe.'''

    userDict = {'id':id,
            'FirstName':first_name,
            'LastName':last_name,
            'Email':e_mail,
            'PhoneNumber': phone_number,
            'Gender':gender,
            'City':city,
            'Birthday':birthDay,
            'ScreeiningDay':screeining_day,
            'Password': pass_word,
            'RegisterDate':register_date,
            'ImageLocation':image_location,
       }
    
    df = create_connection(path="./data/usersData.csv")
    df = df.append(userDict, ignore_index = True)

    # saving the dataframe
    df.to_csv("./data/usersData.csv")
 

def create_folder():
    '''Create folder for new user.'''

    try:


        df = create_connection("./data/usersData.csv")
        # df = pd.read_csv("./data/usersData.csv")
        
        

        if df['id'] is not None:
            id = int(df['id'].tail(1))
            newId = generate_id(id)

        else:
            newId = 0


        try:
            # Directory
            directory = str(newId)
            
            # Parent Directory path
            parent_dir = r"C:\Users\hamidr.bd\Documents\Programming\Python\Jupyter\Libraries\web\Streamlit\project\Authenticator\streamlit_login_auth_ui-main\pandas\data\Users"

            # Path
            path = os.path.join(parent_dir, directory)

            # Create the directory
            os.mkdir(path)
            print("Directory '% s' created" % directory)

        except OSError as error: 
            print(error) 

        finally:
            pass

    except:
        print("can't connect to dataframe")

    finally:
        pass


    return path, newId


def show_user_info(user_id):
    try:
        # Get the cursor object from the connection object
        userDataFrame = create_connection()

        return userDataFrame
            
    except OSError as error: 
        print(error)
        print("falseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

# need True
def check_usr_pass(Email: str, password: str) -> bool:
    """
    Authenticates the Email and password.
    """

    try:
        df = create_connection("./data/usersData.csv")

        try:

            # row's number
            emailIndex = df[df['Email'] == Email].index[0]

            if emailIndex is not None:
                # if df.iloc[emailIndex]['Email'] == Email:
                if str(df.iloc[emailIndex]['Password']) == password:
                    return True, "Login do."
                

                else:
                    return False, "Please enter correct password."


            else:
                return False, "Can't find Email address. please check the Email."
            
        except:
            return False, "Can't find Email address. please check the Email."

        
        # try:
        #     passwd_verification_bool = ph.verify(stored_password, password)
        #     if passwd_verification_bool == True:
        #         print("hamid")
        #         return True
        # except:
        #     return False

    except:
        return False, "Cant't connect to database for check user and pass."
    
    finally:
        pass


def load_lottieurl(url: str) -> str:
    """
    Fetches the lottie animation using the URL.
    """
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        pass


def check_valid_name(name_sign_up: str) -> bool:
    """
    Checks if the user entered a valid name while creating the account.
    """
    name_regex = (r'^[A-Za-z_][A-Za-z0-9_]*')

    if re.search(name_regex, name_sign_up):
        return True
    return False


def check_valid_email(email_sign_up: str) -> bool:
    """
    Checks if the user entered a valid email while creating the account.
    """
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, email_sign_up):
        return True
    
    return False

# need
def check_unique_email(email_sign_up: str) -> bool:
    """
    Checks if the email already exists (since email needs to be unique).
    """

    try:
        # curr = create_connection()

        # # Execute a query to check if the email is unique in the dataframe
        # query = "SELECT COUNT(*) FROM mazidy WHERE email = %s"
        # curr.execute(query, (email_sign_up,)) # email_to_check

        # # Fetch the count result
        # count = curr.fetchone()[0]

        # # If count is 0, the email is unique; otherwise, it's not unique
        # return count == 0
        pass



    except psycopg2.Error as e:
        return f"Error: {e}"
    
    finally:
        pass


def check_valid_phone_number(phone_number_sign_up: str) -> bool:
    pass

def check_unique_phone_number(phone_number_sign_up: str) -> bool:
    pass


def non_empty_str_check(username_sign_up: str) -> bool:
    """
    Checks for non-empty strings.
    """
    empty_count = 0
    for i in username_sign_up:
        if i == ' ':
            empty_count = empty_count + 1
            if empty_count == len(username_sign_up):
                return False

    if not username_sign_up:
        return False
    return True

# need
def check_unique_usr(username_sign_up: str):
    """
    Checks if the username already exists (since username needs to be unique),
    also checks for non - empty username.
    """
    # authorized_user_data_master = list()
    # with open("_secret_auth_.json", "r") as auth_json:
    #     authorized_users_data = json.load(auth_json)

    #     for user in authorized_users_data:
    #         authorized_user_data_master.append(user['username'])

    # if username_sign_up in authorized_user_data_master:
    #     return False
    
    # non_empty_check = non_empty_str_check(username_sign_up)

    # if non_empty_check == False:
    #     return None
    # return True

    try:
        conn, curr = create_connection()

        # Execute a query to check if the email is unique in the dataframe
        query = "SELECT COUNT(*) FROM mazidy WHERE username = %s"
        curr.execute(query, (username_sign_up,)) # email_to_check

        # Fetch the count result
        count = curr.fetchone()[0]

        # If count is 0, the email is unique; otherwise, it's not unique
        return count == 0


    except psycopg2.Error as e:
        return f"Error: {e}"
    
    finally:
        if conn:
            curr.close()
            conn.close()

# need True
def register_new_usr(first_name_sign_up: str, last_name_sign_up: str, email_sign_up: str, phone_number_sign_up: int, city_sign_up, birth_day_sign_up, screeining_day_sign_up, gender_sign_up, password_sign_up: str, register_date_sign_up) -> None:
    """
        Saves the information of the new user in the _secret_auth.json file.
    """

    try:	
        # The path of each user
        print(1111111111111111111111111111111111111)
        userFolderPath, id = create_folder()
        print(userFolderPath)

        update_data_frame(id=id,
                          first_name=first_name_sign_up,
                          last_name=last_name_sign_up,
                          e_mail=email_sign_up,
                          phone_number=phone_number_sign_up,
                          gender=gender_sign_up,
                          city=city_sign_up,
                          birthDay=birth_day_sign_up,
                          screeining_day=screeining_day_sign_up,
                          pass_word=password_sign_up,
                          register_date=register_date_sign_up,
                          image_location=userFolderPath
                          )

    except:
        print("Error while register new user.")

    finally:
        pass

# need
def check_username_exists(user_name: str) -> bool:
    """
    Checks if the username exists in the _secret_auth.json file.
    """
    authorized_user_data_master = list()
    with open("_secret_auth_.json", "r") as auth_json:
        authorized_users_data = json.load(auth_json)

        for user in authorized_users_data:
            authorized_user_data_master.append(user['username'])
        
    if user_name in authorized_user_data_master:
        return True
    return False
        
# need
def check_email_exists(email_forgot_passwd: str):
    """
    Checks if the email entered is present in the _secret_auth.json file.
    """

    try:
        df = create_connection("./data/usersData.csv")

        try:

            # row's number
            emailIndex = df[df['Email'] == email_forgot_passwd].index[0]

            if emailIndex is not None:
                    return True, emailIndex, "New password send to your email."
                

            else:
                return False, None, "Email ID not registered with us!"
            
        except:
            return False, None, "Can't find Email address. please check the Email."


    except:
        return False, "Cant't connect to database for check user and pass."
    
    finally:
        pass


def generate_random_passwd() -> str:
    """
    Generates a random password to be sent in email.
    """
    password_length = 10
    return secrets.token_urlsafe(password_length)


def send_passwd_in_email(auth_token: str, username_forgot_passwd: str, email_forgot_passwd: str, company_name: str, random_password: str) -> None:
    """
    Triggers an email to the user containing the randomly generated password.
    """
    client = Courier(auth_token = auth_token)

    resp = client.send_message(
    message={
        "to": {
        "email": email_forgot_passwd
        },
        "content": {
        "title": company_name + ": Login Password!",
        "body": "Hi! " + username_forgot_passwd + "," + "\n" + "\n" + "Your temporary login password is: " + random_password  + "\n" + "\n" + "{{info}}"
        },
        "data":{
        "info": "Please reset your password at the earliest for security reasons."
        }
    }
    )

# need
def change_passwd(email_: str, random_password: str) -> None:
    """
    Replaces the old password with the newly generated password.
    """
    df = create_connection()

    

    with open("_secret_auth_.json", "w") as auth_json_:
        for user in authorized_users_data:
            if user['email'] == email_:
                user['password'] = ph.hash(random_password)
        json.dump(authorized_users_data, auth_json_)
    
# need
def check_current_passwd(email_reset_passwd: str, current_passwd: str) -> bool:
    """
    Authenticates the password entered against the username when 
    resetting the password.
    """
    with open("_secret_auth_.json", "r") as auth_json:
        authorized_users_data = json.load(auth_json)

        for user in authorized_users_data:
            if user['email'] == email_reset_passwd:
                try:
                    if ph.verify(user['password'], current_passwd) == True:
                        return True
                except:
                    pass
    return False

# Author: Hamidreza Badr
# GitHub: 

