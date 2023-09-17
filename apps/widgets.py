import streamlit as st
import json
import os
import datetime

from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_cookies_manager import EncryptedCookieManager
from .Authenticator_app import check_usr_pass
from .Authenticator_app import load_lottieurl
from .Authenticator_app import check_valid_name
from .Authenticator_app import check_valid_email
from .Authenticator_app import check_unique_email
from .Authenticator_app import check_valid_phone_number
from .Authenticator_app import check_unique_phone_number
from .Authenticator_app import check_unique_usr
from .Authenticator_app import register_new_usr
from .Authenticator_app import check_email_exists
from .Authenticator_app import generate_random_passwd
from .Authenticator_app import send_passwd_in_email
from .Authenticator_app import change_passwd
from .Authenticator_app import check_current_passwd
from .Authenticator_app import create_connection
from .Authenticator_app import create_folder
from .Authenticator_app import show_user_info


class __login__:
    """
    Builds the UI for the Login/ Sign Up page.
    """

    def __init__(self, auth_token: str, company_name: str, width, height, logout_button_name: str = 'Logout', 
                 hide_menu_bool: bool = False, hide_footer_bool: bool = False, 
                 lottie_url: str = "https://assets8.lottiefiles.com/packages/lf20_ktwnwv5m.json" ):
        """
        Arguments:
        -----------
        1. self
        2. auth_token : The unique authorization token received from - https://www.courier.com/email-api/
        3. company_name : This is the name of the person/ organization which will send the password reset email.
        4. width : Width of the animation on the login page.
        5. height : Height of the animation on the login page.
        6. logout_button_name : The logout button name.
        7. hide_menu_bool : Pass True if the streamlit menu should be hidden.
        8. hide_footer_bool : Pass True if the 'made with streamlit' footer should be hidden.
        9. lottie_url : The lottie animation you would like to use on the login page. Explore animations at - https://lottiefiles.com/featured
        """
        self.auth_token = auth_token
        self.company_name = company_name
        self.width = width
        self.height = height
        self.logout_button_name = logout_button_name
        self.hide_menu_bool = hide_menu_bool
        self.hide_footer_bool = hide_footer_bool
        self.lottie_url = lottie_url

        # Call the create table method	
        # create_folder()

        self.cookies = EncryptedCookieManager(
        prefix="streamlit_login_ui_yummy_cookies",
        password='9d68d6f2-4258-45c9-96eb-2d6bc74ddbb5-d8f49cab-edbb-404a-94d0-b25b1d4a564b')

        if not self.cookies.ready():
            st.stop()   


    def check_auth_json_file_exists(self, auth_filename: str) -> bool:
        """
        Checks if the auth file (where the user info is stored) already exists.
        """
        file_names = []
        for path in os.listdir('./'):
            if os.path.isfile(os.path.join('./', path)):
                file_names.append(path)

        present_files = []
        for file_name in file_names:
            if auth_filename in file_name:
                present_files.append(file_name)
                    
            present_files = sorted(present_files)
            if len(present_files) > 0:
                return True
        return False


    def get_username(self):
        if st.session_state['LOGOUT_BUTTON_HIT'] == False:
            fetched_cookies = self.cookies
            if '__streamlit_login_signup_ui_username__' in fetched_cookies.keys():
                username=fetched_cookies['__streamlit_login_signup_ui_username__']
                return username
 

    def login_widget(self) -> None:
        """
        Creates the login widget, checks and sets cookies, authenticates the users.
        """

        pretty_btn = """
            <style>
            div[class="row-widget stButton"] > button {
                width: 100%;
            }
            </style>
            <br><br>
            """
        st.markdown(pretty_btn, unsafe_allow_html=True)

        # Checks if cookie exists.
        if st.session_state['LOGGED_IN'] == False:
            if st.session_state['LOGOUT_BUTTON_HIT'] == False:
                fetched_cookies = self.cookies
                if '__streamlit_login_signup_ui_username__' in fetched_cookies.keys():
                    if fetched_cookies['__streamlit_login_signup_ui_username__'] != '1c9a923f-fb21-4a91-b3f3-5f18e3f01182':
                        st.session_state['LOGGED_IN'] = True

        if st.session_state['LOGGED_IN'] == False:
            st.session_state['LOGOUT_BUTTON_HIT'] = False 

            del_login = st.empty()
            with del_login.form("Login Form"):
                Email = st.text_input("Email", placeholder = 'Please enter your Email')
                password = st.text_input("Password", placeholder = 'Your password', type = 'password')

                st.markdown("###")
                login_submit_button = st.form_submit_button(label = 'Login')

                if login_submit_button == True:
                    authenticate_user_check, errorNote = check_usr_pass(Email, password)

                    if authenticate_user_check == False:
                        st.error(errorNote)

                    else:
                        st.session_state['LOGGED_IN'] = True
                        self.cookies['__streamlit_login_signup_ui_username__'] = Email
                        self.cookies.save()
                        del_login.empty()
                        st.experimental_rerun()


    def animation(self) -> None:
        """
        Renders the lottie animation.
        """
        lottie_json = load_lottieurl(self.lottie_url)
        st_lottie(lottie_json, width = self.width, height = self.height)


    def sign_up_widget(self) -> None:
        """
        Creates the sign-up widget and stores the user info in a secure way in the _secret_auth_.json file.
        """


        with st.form("Sign Up Form"):

            leftColumn, rightColumn = st.columns(2)

            with leftColumn:
                firstName_sign_up = st.text_input("First name *", placeholder = 'Please enter your firstname')
                valid_first_name_check = check_valid_name(firstName_sign_up)


            with rightColumn:
                lastName_sign_up = st.text_input("Last name *", placeholder = 'Please enter your lastname')
                valid_last_name_check = check_valid_name(lastName_sign_up)


            with leftColumn:

                email_sign_up = st.text_input("Email *", placeholder = 'Please enter your email')
                valid_email_check = check_valid_email(email_sign_up)
                # unique_email_check = check_unique_email(email_sign_up)
                unique_email_check = True
                # st.write(unique_email_check)


            with rightColumn:

                # phone number
                phoneNumber_sign_up = st.text_input(label="Phone Number", placeholder="Please enter your phone number.")
                valid_PhoneNumber_check = check_valid_phone_number(phoneNumber_sign_up)
                unique_PhoneNumber_check = check_unique_phone_number(phoneNumber_sign_up)


                iranian_cities = ["",
                     "Tehran", 
                      "Mashhad", 
                      "Isfahan", 
                      "Karaj", 
                      "Shiraz", 
                      "Tabriz", 
                      "Qom", 
                      "Ahvaz", 
                      "Kermanshah", 
                      "Urmia", 
                      "Rasht", 
                      "Zahedan", 
                      "Hamadan", 
                      "Kerman", 
                      "Arak",
                      "Yazd",
                      "Ardabil", 
                      "Bandar Abbas", 
                      "Eslamshahr", 
                      "Qazvin"]
                city_sign_up = st.selectbox(label="City", options=iranian_cities)

                
                # Date of screening
                screeiningDay_sign_up = st.date_input(label="Screeining day", value=None, format="YYYY/MM/DD",)
                

            with leftColumn:
                genderList = ['', 'Male', 'Female']

                gender_sign_up = st.selectbox(label="Gender", placeholder="Please select your gender.", options=genderList, )

                # Date of birth
                birthDay_sign_up = st.date_input(label="Birthday", value=None, format="YYYY/MM/DD")

                

            
            with leftColumn:
                password_sign_up = st.text_input("Password *", placeholder = 'Create a strong password', type = 'password')

            with rightColumn:
                repeat_password_sign_up = st.text_input("Repeat Password *", placeholder = 'Please repeat your password', type = 'password')

            st.markdown("###")
            sign_up_submit_button = st.form_submit_button(label = 'Register')

            if sign_up_submit_button:
                if valid_first_name_check == False:
                    st.error("Please enter a valid name!")

                if valid_last_name_check == False:
                    st.error("Please enter a valid name!")

                elif valid_email_check == False:
                    st.error("Please enter a valid Email!")
                
                elif unique_email_check == False:
                    st.error("Email already exists!")
                


                if valid_first_name_check == True:
                    if valid_last_name_check == True:
                        if valid_email_check == True:
                            if unique_email_check == True:    
                                    st.write('hamidreza')           
                                    register_new_usr(first_name_sign_up=firstName_sign_up, 
                                                     last_name_sign_up=lastName_sign_up, 
                                                     email_sign_up=email_sign_up, 
                                                     phone_number_sign_up=phoneNumber_sign_up, 
                                                     birth_day_sign_up=birthDay_sign_up, 
                                                     screeining_day_sign_up=screeiningDay_sign_up, 
                                                     gender_sign_up=gender_sign_up, 
                                                     city_sign_up=city_sign_up,
                                                     password_sign_up=password_sign_up,
                                                     register_date_sign_up=datetime.date.today())
                                    
                                    st.success("Registration Successful!")


    def forgot_password(self) -> None:
        """
        Creates the forgot password widget and after user authentication (email), triggers an email to the user 
        containing a random password.
        """

        with st.form("Forgot Password Form"):
            email_forgot_passwd = st.text_input("Email", placeholder= 'Please enter your email')
            email_exists_check, index_forgot_passwd, errorNote = check_email_exists(email_forgot_passwd)

            st.markdown("###")
            forgot_passwd_submit_button = st.form_submit_button(label = 'Get Password')

            if forgot_passwd_submit_button:
                if email_exists_check == False:
                    st.error(errorNote)

                if email_exists_check == True:
                    random_password = generate_random_passwd()
                    send_passwd_in_email(self.auth_token, index_forgot_passwd, email_forgot_passwd, self.company_name, random_password)
                    change_passwd(email_forgot_passwd, random_password)
                    st.success("Secure Password Sent Successfully!")


    def reset_password(self) -> None:
        """
        Creates the reset password widget and after user authentication (email and the password shared over that email), 
        resets the password and updates the same in the _secret_auth_.json file.
        """
        with st.form("Reset Password Form"):
            email_reset_passwd = st.text_input("Email", placeholder= 'Please enter your email')
            email_exists_check, username_reset_passwd = check_email_exists(email_reset_passwd)

            current_passwd = st.text_input("Temporary Password", placeholder= 'Please enter the password you received in the email')
            current_passwd_check = check_current_passwd(email_reset_passwd, current_passwd)

            new_passwd = st.text_input("New Password", placeholder= 'Please enter a new, strong password', type = 'password')

            new_passwd_1 = st.text_input("Re - Enter New Password", placeholder= 'Please re- enter the new password', type = 'password')

            st.markdown("###")
            reset_passwd_submit_button = st.form_submit_button(label = 'Reset Password')

            if reset_passwd_submit_button:
                if email_exists_check == False:
                    st.error("Email does not exist!")

                elif current_passwd_check == False:
                    st.error("Incorrect temporary password!")

                elif new_passwd != new_passwd_1:
                    st.error("Passwords don't match!")
            
                if email_exists_check == True:
                    if current_passwd_check == True:
                        change_passwd(email_reset_passwd, new_passwd)
                        st.success("Password Reset Successfully!")
                

    def logout_widget(self) -> None:
        """
        Creates the logout widget in the sidebar only if the user is logged in.
        """
        if st.session_state['LOGGED_IN'] == True:
            del_logout = st.sidebar.empty()
            del_logout.markdown("#")
            logout_click_check = del_logout.button(self.logout_button_name)

            if logout_click_check == True:
                st.session_state['LOGOUT_BUTTON_HIT'] = True
                st.session_state['LOGGED_IN'] = False
                self.cookies['__streamlit_login_signup_ui_username__'] = '1c9a923f-fb21-4a91-b3f3-5f18e3f01182'
                del_logout.empty()
                st.experimental_rerun()
        

    def nav_sidebar(self):
        """
        Creates the side navigaton bar
        """
        main_page_sidebar = st.sidebar.empty()
        with main_page_sidebar:
            selected_option = option_menu(
                menu_title = 'Navigation',
                menu_icon = 'list-columns-reverse',
                icons = ['box-arrow-in-right', 'x-circle','arrow-counterclockwise'],
                options = ['Login', 'Forgot Password?', 'Reset Password'],
                styles = {
                    "container": {"padding": "5px"},
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px"}})
        return main_page_sidebar, selected_option
    

    def hide_menu(self) -> None:
        """
        Hides the streamlit menu situated in the top right.
        """
        st.markdown(""" <style>
        #MainMenu {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
    

    def hide_footer(self) -> None:
        """
        Hides the 'made with streamlit' footer.
        """
        st.markdown(""" <style>
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)


    def build_login_ui(self):
        """
        Brings everything together, calls important functions.
        """
        if 'LOGGED_IN' not in st.session_state:
            st.session_state['LOGGED_IN'] = False

        if 'LOGOUT_BUTTON_HIT' not in st.session_state:
            st.session_state['LOGOUT_BUTTON_HIT'] = False

        auth_json_exists_bool = self.check_auth_json_file_exists('_secret_auth_.json')

        # if auth_json_exists_bool == False:
        #     with open("_secret_auth_.json", "w") as auth_json:
        #         json.dump([], auth_json)

        tab1, tab2 = st.tabs(["Login", "Sign up"], )

        with tab1:
            
            c1, c2 = st.columns([7,3])
            with c1:
                self.login_widget()

                if st.button(label="Forgot Password?"):
                    self.forgot_password()


                # if st.button(label="Reset Password"):
                #     self.reset_password()



            with c2:
                if st.session_state['LOGGED_IN'] == False:
                    self.animation()

            


            # main_page_sidebar, selected_option = self.nav_sidebar()

            # if selected_option == 'Login':
            #     c1, c2 = st.columns([7,3])
            #     with c1:
            #         self.login_widget()
            #     with c2:
            #         if st.session_state['LOGGED_IN'] == False:
            #             self.animation()

            # if selected_option == 'Forgot Password?':
            #     self.forgot_password()

            # if selected_option == 'Reset Password':
            #     self.reset_password()

        with tab2:
            self.sign_up_widget()
              
        
        self.logout_widget()

        # if st.session_state['LOGGED_IN'] == True:
        #     main_page_sidebar.empty()
        
        if self.hide_menu_bool == True:
            self.hide_menu()
        
        if self.hide_footer_bool == True:
            self.hide_footer()
        
        return st.session_state['LOGGED_IN']


# Author: Hamidreza Badr
# GitHub: 


