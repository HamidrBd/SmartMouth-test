from hydralit import HydraApp
import hydralit_components as hc
import apps
import streamlit as st
from streamlit.components.v1 import html
from st_pages import Page, add_page_title, show_pages
from pathlib import Path
from streamlit_option_menu import option_menu


#Only need to set these here as we are add controls outside of Hydralit, to customise a run Hydralit!
st.set_page_config(page_title='Secure Hydralit Data Explorer',page_icon="🐙",layout='wide',initial_sidebar_state='auto',)

if __name__ == '__main__':

    #---ONLY HERE TO SHOW OPTIONS WITH HYDRALIT - NOT REQUIRED, use Hydralit constructor parameters.
    # st.write('Some options to change the way our Hydralit application looks and feels')
    c1,c2,c3,c4,_ = st.columns([2,2,2,2,8])
    # hydralit_navbar = c1.checkbox('Use Hydralit Navbar',True)
    # sticky_navbar = c2.checkbox('Use Sticky Navbar',False)
    # animate_navbar = c3.checkbox('Use Animated Navbar',True)
    # hide_st = c4.checkbox('Hide Streamlit Markers',True)

    hydralit_navbar = True
    sticky_navbar = False
    animate_navbar = True
    hide_st = True


    over_theme = {'txc_inactive': '#FFFFFF'}
    #this is the host application, we add children to it and that's it!

    
    app = HydraApp(
        title='Secure Hydralit Data Explorer', 
        favicon="🐙",
        hide_streamlit_markers=hide_st,
        #add a nice banner, this banner has been defined as 5 sections with spacing defined by the banner_spacing array below.
        use_banner_images=["./resources/Fartak.png", None, {'header':"<h1 style='text-align:center;padding: 0px 0px;color:grey;font-size:200%;'>Smart Mouth Project by Fartak co.</h1><br>"},None,"./resources/smartmouth logo.png"], 
        banner_spacing=[5,30,60,30,5],
        use_navbar=hydralit_navbar, 
        navbar_sticky=sticky_navbar,
        navbar_animation=animate_navbar,
        navbar_theme=over_theme,
        
    )

    

    

    # menu_data = [
    # {'icon': "far fa-copy", 'label':"Left End"},
    # {'id':'Copy','icon':"🐙",'label':"Copy"},
    # {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
    # {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
    # {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
    # {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
    # {'icon': "far fa-copy", 'label':"Right End"},
    # {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
    # ]


#     with st.sidebar:
#         menu_id = hc.nav_bar(
#         menu_definition=menu_data,
#         override_theme=over_theme,
#         home_name='Home',
#         login_name='Logout',
#         hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
#         sticky_nav=True, #at the top or not
#         sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
#         option_menu='True'
# )
    
    # 1. as sidebar menu
    # with st.sidebar:
    #     selected = option_menu("Main Menu", ["Home", 'Settings'], 
    #         icons=['house', 'gear'], menu_icon="cast", default_index=1)
    #     selected

    # # 2. horizontal menu
    # selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    #     icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #     menu_icon="cast", default_index=0, orientation="horizontal")
    # selected2

    # # 3. CSS style definitions
    # selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    #     icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #     menu_icon="cast", default_index=0, orientation="horizontal",
    #     styles={
    #         "container": {"padding": "0!important", "background-color": "#fafafa"},
    #         "icon": {"color": "orange", "font-size": "25px"}, 
    #         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    #         "nav-link-selected": {"background-color": "green"},
    #     }
    # )

    # # 4. Manual Item Selection
    # if st.session_state.get('switch_button', False):
    #     st.session_state['menu_option'] = (st.session_state.get('menu_option',0) + 1) % 4
    #     manual_select = st.session_state['menu_option']
    # else:
    #     manual_select = None
        
    # selected4 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    #     icons=['house', 'cloud-upload', "list-task", 'gear'], 
    #     orientation="horizontal", manual_select=manual_select, key='menu_4')
    # st.button(f"Move to Next {st.session_state.get('menu_option',1)}", key='switch_button')
    # selected4

    # # 5. Add on_change callback
    # def on_change(key):
    #     selection = st.session_state[key]
    #     st.write(f"Selection changed to {selection}")
        
    # selected5 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'],
    #                         icons=['house', 'cloud-upload', "list-task", 'gear'],
    #                         on_change=on_change, key='menu_5', orientation="horizontal")
    # selected5



    #Home button will be in the middle of the nav list now
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'), is_home=True)
    # app.add_app("Authenticator", icon="✅", app=apps.__login__())

    #add all your application classes here
    
    app.add_app("Education", icon="", app=apps.Education(title="Education"))
    app.add_app("AI predict", app=apps.AIPridect(title='ai'))
    app.add_app("Search", app=apps.Search(title='Search'))

    #we have added a sign-up app to demonstrate the ability to run an unsecure app
    #only 1 unsecure app is allowed
    app.add_app("Signup", icon="🛰️", app=apps.SignUpApp(title='Signup'), is_unsecure=True)

    #we want to have secure access for this HydraApp, so we provide a login application
    #optional logout label, can be blank for something nicer!
    app.add_app("Profile", app=apps.LoginApp(title='Profile'), is_login=True)  # 


    #specify a custom loading app for a custom transition between apps, this includes a nice custom spinner
    app.add_loader_app(apps.MyLoadingApp(delay=0))


    


    # Define your javascript
    my_js = """
    alert("your welcome");
    """

    # Wrapt the javascript as html code
    my_html = f"<script>{my_js}</script>"

    # Execute your app
    # st.title("Javascript example")
    # html(my_html)


    #we can inject a method to be called everytime a user logs out
    #---------------------------------------------------------------------
    # @app.logout_callback
    # def mylogout_cb():
    #     print('I was called from Hydralit at logout!')
    #---------------------------------------------------------------------

    #we can inject a method to be called everytime a user logs in
    #---------------------------------------------------------------------
    # @app.login_callback
    # def mylogin_cb():
    #     print('I was called from Hydralit at login!')
    #---------------------------------------------------------------------

    #if we want to auto login a guest but still have a secure app, we can assign a guest account and go straight in
    app.enable_guest_access()

    #check user access level to determine what should be shown on the menu
    user_access_level, username = app.check_access()
    # st.write('user_access_level: ' , user_access_level)
    # st.write('username: ' , username)

    # If the menu is cluttered, just rearrange it into sections!
    # completely optional, but if you have too many entries, you can make it nicer by using accordian menus
   
    # Doctor
    if user_access_level == 1:
        complex_nav = {
            'Home': ['Home'],
            'Education': ['Education'],
            'AI predict 🏆': ["AI predict"],
            'Search': ["Search"],
            # 'Authenticator': ["Authenticator"]
            # 'Profile': ['Profile']

        }

    # Patient
    elif user_access_level == 2:
        complex_nav = {
            'Home': ['Home'],
            'Education': ['Loader Playground'],
            'AI predict 🏆': ["AI predict"],
            'Search': ["Search"],
            # 'Authenticator': ["Authenticator"]
            # 'Profile': ['Profile']
        }
    else:
        complex_nav = {
            'Home': ['Home'],
            # 'Profile': ['Profile']
        }

  
    #and finally just the entire app and all the children.
    app.run(complex_nav)
    


    #print user movements and current login details used by Hydralit
    #---------------------------------------------------------------------
    # user_access_level, username = app.check_access()
    # prev_app, curr_app = app.get_nav_transition()
    # print(prev_app,'- >', curr_app)
    # print(int(user_access_level),'- >', username)
    # print('Other Nav after: ',app.session_state.other_nav_app)
    #---------------------------------------------------------------------

    # with st.echo("below"):
    
    #     "## Declaring the pages in your app:"

    #     show_pages(
    #         [
    #             Page("example_app/streamlit_app.py", "Home", "🏠"),
    #             # Can use :<icon-name>: or the actual icon
    #             Page("example_app/example_one.py", "Example One", "1️⃣"),
    #             # The pages appear in the order you pass them
    #             Page("example_app/example_four.py", "Example Four", "📖"),
    #             Page("example_app/example_two.py", "Example Two", "✏️"),
    #             # Will use the default icon and name based on the filename if you don't
    #             # pass them
    #             Page("example_app/example_three.py"),
    #             Page("example_app/example_five.py", "Example Five", "🧰"),
    #         ]
    #     )

    #     add_page_title()  # Optional method to add title and icon to current page


    #     with st.echo("below"):
    #         from st_pages import show_pages_from_config

    #         show_pages_from_config()

    #     "See more at https://github.com/blackary/st_pages"

    #     with st.expander("Show documentation"):
    #         st.help(show_pages)

    #         st.help(Page)

    #         st.help(add_page_title)

        