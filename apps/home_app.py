import os
import streamlit as st
from hydralit import HydraHeadApp
import numpy as np
import nivo_chart as nc
from streamlit.components.v1 import html
import plotly.graph_objects as go
from pathlib import Path
from hydralit import HydraApp
import apps





MENU_LAYOUT = [1,1,1,7,2]

class HomeApp(HydraHeadApp):


    def __init__(self, title = 'Hydralit Explorer', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):

        try:
            st.markdown("<h1 style='text-align:center;padding: 0px 0px;color:black;font-size:200%;'>Home</h1>",unsafe_allow_html=True)     

            col_header_logo_left_far, col_header_logo_left, col_header_text, col_header_logo_right, col_header_logo_right_far = st.columns([1,2,2,2,1])
            
            #col_header_logo_right_far.image(os.path.join(".","resources","hydra.png"),width=100,)

            if col_header_text.button('Creat new accont.'):  # , on_click=signup
                # self.do_redirect("https://hotstepper.readthedocs.io/index.html")
                # self.do_redirect('sign up')
                pass


            hydralit_navbar = True
            sticky_navbar = False
            animate_navbar = True
            hide_st = True

            over_theme = {'txc_inactive': '#FFFFFF'}
            
            


            # =============================================================================================================================
            
            # with st.sidebar:
            #     app1 = HydraApp(
            #         title='home app', 
            #         favicon="🏠",
            #         hide_streamlit_markers=hide_st,
            #         # banner_spacing=[5,30,60,30,5],
            #         use_navbar=hydralit_navbar, 
            #         navbar_sticky=sticky_navbar,
            #         navbar_animation=animate_navbar,
            #         navbar_theme=over_theme,
                    
                    
            #     )
            
            

            # app1.add_app("Spacy NLP", icon="⌨️", app=apps.SpacyNLP(title="Spacy NLP"))
            # app1.add_app("Uber Pickups", icon="🚖", app=apps.UberNYC(title="Uber Pickups"))




            # complex_nav = {

            # 'Clustering': ["Uber Pickups"],
            # 'NLP': ["Spacy NLP"],


            # }

            # app1.run(complex_nav)




            # =============================================================================================================================





            _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
            col_logo.image(os.path.join(".","resources","dental.png"),width=80,)
            col_text.subheader("This program is made with the help of artificial intelligence to identify and diagnose tooth damage and oral and gum diseases. Also, the possibility of buying dental equipment, searching for a doctor and training are also included in the program.")

            st.markdown('<br><br>',unsafe_allow_html=True)

            col_text.info("Teeth have the biggest and most important effect on human beauty.")


            _,_,col_logo, col_text, col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Cheat Sheet ➡️'):
            #     self.do_redirect('Cheat Sheet')
            col_logo.image(os.path.join(".","resources","home.png"),width=50,)
            col_text.info("After registration, different sections will be shown to you. The first page is home, that show your info.")

            #The sample content in a sub-section with jump to format.
            _,_,col_logo, col_text, col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Sequency Denoising ➡️'):
            #     self.do_redirect('Sequency Denoising')
                
            col_logo.image(os.path.join(".","resources","classroom.png"),width=50,)
            col_text.info("In this part of the program, there are trainings related to the basic principles of oral hygiene.")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Solar Mach ➡️'):
            #     self.do_redirect('Solar Mach')
            col_logo.image(os.path.join(".","resources","brain.png"),width=50,)
            col_text.info("The main part of the program that helps you using artificial intelligence. To use this section, upload a photo of your mouth or teeth so that the model can predict your oral health based on what it has already been taught.")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Spacy NLP ➡️'):
            #     self.do_redirect('Spacy NLP')
            col_logo.image(os.path.join(".","resources","dental 2.png"),width=50,)
            col_text.info("In this section, you can search for a doctor and clinic or specify an appointment and consultation.")

            _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
            # if col_text.button('Uber Pickups ➡️'):
            #     self.do_redirect('Uber Pickups')
            col_logo.image(os.path.join(".","resources","profile.png"),width=50,)
            col_text.info("On the profile page, there is information such as payments, login and exit page, support, etc.")

        
        except Exception as e:
            st.image(os.path.join(".","resources","failure.png"),width=100,)
            st.error('An error has occurred, someone will be punished for your inconvenience, we humbly request you try again.')
            st.error('Error details: {}'.format(e))

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")




# ====================================================================================================================
        
        col1, col2 = st.columns([1, 1])
        with col1:
        
            st.header("Tooth numbering system:")
            hemlPaht = r'apps/test - Copy.html'

            HtmlFile = open(hemlPaht, 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            html(source_code, height=700, width=500)

            st.write("")
            st.info("Understanding the teeth' numbers and names is essential to keeping track of your dental chart.")
            st.info("Dentists in the United States use the Universal System. In adults, each tooth is given a number. The third molar on the upper right side of our mouth is tooth number one. The third molar on our lower jaw is tooth number 32.")


        with col2:
            st.header("Condition of all teeth")
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')
            st.write('')

            fig =go.Figure(go.Sunburst(
                labels=["Teeth", "Healthy teeth", "Broken teeth", "Cavity", "Caries", "Pigmentation", "Restored teeth", "Amalgam(silver filing)", "Amalgam(white filing)"],
                parents=["", "Teeth", "Teeth", "Broken teeth", "Broken teeth", "Broken teeth", "Teeth", "Restored teeth", "Restored teeth"],
                values=[32, 13, 9, 3, 4, 2, 10, 3, 4],
            ))
            fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

            # Plot!
            st.plotly_chart(fig, use_container_width=True)

            st.write("")
            st.info("Adults erupt 32 teeth. Human teeth are the most rigid bones in your body. Calcium, protein, and collagen make teeth the natural tools your body has for eating. All your teeth are essential for a correct occlusion and to eat correctly; to grind and chew your food to obtain your body's nutrients. Teeth will not last forever if you do not take good care of them.")
        
# ====================================================================================================================

        calendar_chart = {
                    "data": [
                        {"value": 236, "day": "2016-11-21"},
                        {"value": 362, "day": "2017-05-02"},
                        {"value": 220, "day": "2017-07-12"},
                        {"value": 109, "day": "2017-01-08"},
                        {"value": 169, "day": "2016-05-30"},
                        {"value": 256, "day": "2016-01-10"},
                        {"value": 278, "day": "2016-08-01"},
                        {"value": 178, "day": "2017-04-14"},
                        {"value": 334, "day": "2017-01-15"},
                        {"value": 303, "day": "2017-12-09"},
                        {"value": 38, "day": "2017-08-10"},
                        {"value": 357, "day": "2016-06-02"},
                        {"value": 278, "day": "2017-02-23"},
                        {"value": 89, "day": "2015-04-30"},
                        {"value": 139, "day": "2016-05-01"},
                        {"value": 395, "day": "2017-01-14"},
                        {"value": 126, "day": "2015-04-21"},
                        {"value": 216, "day": "2018-08-11"},
                        {"value": 400, "day": "2018-03-15"},
                        {"value": 167, "day": "2018-06-28"},
                        {"value": 245, "day": "2015-05-20"},
                        {"value": 350, "day": "2017-07-28"},
                        {"value": 94, "day": "2018-04-03"},
                        {"value": 359, "day": "2016-12-31"},
                        {"value": 68, "day": "2015-05-19"},
                        {"value": 46, "day": "2017-07-25"},
                        {"value": 30, "day": "2016-01-26"},
                        {"value": 326, "day": "2015-06-09"},
                        {"value": 265, "day": "2015-08-27"},
                        {"value": 344, "day": "2017-01-30"},
                        {"value": 30, "day": "2016-10-31"},
                        {"value": 112, "day": "2017-05-08"},
                        {"value": 260, "day": "2015-08-09"},
                        {"value": 145, "day": "2015-12-02"},
                        {"value": 89, "day": "2015-06-10"},
                        {"value": 257, "day": "2016-01-31"},
                        {"value": 304, "day": "2016-08-20"},
                        {"value": 65, "day": "2015-07-29"},
                        {"value": 309, "day": "2016-06-06"},
                        {"value": 73, "day": "2016-01-19"},
                        {"value": 46, "day": "2016-07-16"},
                        {"value": 44, "day": "2017-09-27"},
                        {"value": 378, "day": "2017-10-18"},
                        {"value": 102, "day": "2015-05-31"},
                        {"value": 65, "day": "2015-09-12"},
                        {"value": 241, "day": "2017-06-08"},
                        {"value": 53, "day": "2017-01-27"},
                        {"value": 352, "day": "2016-03-20"},
                        {"value": 267, "day": "2018-02-12"},
                        {"value": 131, "day": "2017-09-09"},
                        {"value": 61, "day": "2015-11-02"},
                        {"value": 192, "day": "2017-04-24"},
                        {"value": 115, "day": "2016-11-06"},
                        {"value": 356, "day": "2016-10-24"},
                        {"value": 134, "day": "2016-02-12"},
                        {"value": 11, "day": "2018-01-15"},
                        {"value": 347, "day": "2017-12-04"},
                        {"value": 239, "day": "2015-11-01"},
                        {"value": 137, "day": "2017-05-19"},
                        {"value": 7, "day": "2017-03-04"},
                        {"value": 2, "day": "2016-12-25"},
                        {"value": 263, "day": "2017-07-20"},
                        {"value": 390, "day": "2018-03-18"},
                        {"value": 205, "day": "2016-08-11"},
                        {"value": 277, "day": "2017-04-27"},
                        {"value": 325, "day": "2015-04-01"},
                        {"value": 24, "day": "2016-05-10"},
                        {"value": 355, "day": "2017-12-25"},
                        {"value": 113, "day": "2018-04-14"},
                        {"value": 90, "day": "2017-12-17"},
                        {"value": 375, "day": "2018-01-18"},
                        {"value": 139, "day": "2017-12-03"},
                        {"value": 132, "day": "2016-11-10"},
                        {"value": 135, "day": "2015-05-28"},
                        {"value": 307, "day": "2018-03-26"},
                        {"value": 86, "day": "2015-07-13"},
                        {"value": 96, "day": "2016-06-12"},
                        {"value": 88, "day": "2015-12-14"},
                        {"value": 46, "day": "2017-10-15"},
                        {"value": 11, "day": "2018-02-26"},
                        {"value": 277, "day": "2018-05-05"},
                        {"value": 25, "day": "2018-02-05"},
                        {"value": 255, "day": "2015-06-17"},
                        {"value": 276, "day": "2017-08-22"},
                        {"value": 216, "day": "2015-12-31"},
                        {"value": 236, "day": "2018-03-05"},
                        {"value": 35, "day": "2015-12-30"},
                        {"value": 388, "day": "2016-09-25"},
                        {"value": 106, "day": "2016-05-08"},
                        {"value": 171, "day": "2016-11-07"},
                        {"value": 203, "day": "2015-09-05"},
                        {"value": 223, "day": "2016-09-05"},
                        {"value": 246, "day": "2015-11-06"},
                        {"value": 149, "day": "2015-10-18"},
                        {"value": 343, "day": "2015-10-19"},
                        {"value": 319, "day": "2017-07-22"},
                        {"value": 234, "day": "2016-06-11"},
                        {"value": 13, "day": "2017-12-15"},
                        {"value": 189, "day": "2018-02-14"},
                        {"value": 275, "day": "2017-09-15"},
                        {"value": 126, "day": "2018-03-13"},
                        {"value": 132, "day": "2015-08-14"},
                        {"value": 333, "day": "2017-04-09"},
                        {"value": 148, "day": "2017-02-03"},
                        {"value": 77, "day": "2015-04-24"},
                        {"value": 324, "day": "2017-03-02"},
                        {"value": 314, "day": "2015-06-06"},
                        {"value": 173, "day": "2016-07-12"},
                        {"value": 220, "day": "2016-12-11"},
                        {"value": 82, "day": "2018-05-09"},
                        {"value": 144, "day": "2017-08-15"},
                        {"value": 136, "day": "2016-10-29"},
                        {"value": 283, "day": "2016-01-28"},
                        {"value": 131, "day": "2016-03-13"},
                        {"value": 144, "day": "2015-11-26"},
                        {"value": 369, "day": "2016-05-20"},
                        {"value": 102, "day": "2018-08-08"},
                        {"value": 131, "day": "2017-10-31"},
                        {"value": 252, "day": "2017-06-17"},
                        {"value": 274, "day": "2016-04-17"},
                        {"value": 385, "day": "2017-09-16"},
                        {"value": 267, "day": "2017-10-25"},
                        {"value": 60, "day": "2015-08-12"},
                        {"value": 355, "day": "2016-10-14"},
                        {"value": 11, "day": "2017-10-28"},
                        {"value": 217, "day": "2016-10-06"},
                        {"value": 47, "day": "2018-03-21"},
                        {"value": 60, "day": "2016-12-22"},
                        {"value": 387, "day": "2018-01-25"},
                        {"value": 101, "day": "2017-04-01"},
                        {"value": 257, "day": "2017-09-11"},
                        {"value": 250, "day": "2015-10-20"},
                        {"value": 281, "day": "2018-08-04"},
                        {"value": 45, "day": "2015-05-10"},
                        {"value": 180, "day": "2017-08-28"},
                        {"value": 14, "day": "2015-11-13"},
                        {"value": 101, "day": "2015-08-10"},
                        {"value": 236, "day": "2017-09-22"},
                        {"value": 305, "day": "2016-02-04"},
                        {"value": 225, "day": "2015-06-13"},
                        {"value": 17, "day": "2017-09-28"},
                        {"value": 2, "day": "2016-11-11"},
                        {"value": 399, "day": "2015-09-30"},
                        {"value": 379, "day": "2016-04-29"},
                        {"value": 302, "day": "2015-08-15"},
                        {"value": 382, "day": "2017-12-23"},
                        {"value": 359, "day": "2015-11-11"},
                        {"value": 215, "day": "2015-08-21"},
                        {"value": 346, "day": "2017-12-05"},
                        {"value": 182, "day": "2017-04-18"},
                        {"value": 163, "day": "2016-02-21"},
                        {"value": 67, "day": "2018-01-07"},
                        {"value": 231, "day": "2016-10-01"},
                        {"value": 106, "day": "2018-05-26"},
                        {"value": 14, "day": "2015-09-03"},
                        {"value": 19, "day": "2015-07-09"},
                        {"value": 397, "day": "2017-07-30"},
                        {"value": 292, "day": "2017-01-21"},
                        {"value": 131, "day": "2016-06-05"},
                        {"value": 122, "day": "2018-04-28"},
                        {"value": 265, "day": "2016-04-11"},
                        {"value": 81, "day": "2018-01-22"},
                        {"value": 399, "day": "2016-03-30"},
                        {"value": 108, "day": "2016-03-14"},
                        {"value": 187, "day": "2017-07-13"},
                        {"value": 185, "day": "2015-06-12"},
                        {"value": 19, "day": "2016-07-05"},
                        {"value": 282, "day": "2017-07-01"},
                        {"value": 188, "day": "2017-03-26"},
                        {"value": 386, "day": "2016-02-05"},
                        {"value": 296, "day": "2015-12-17"},
                        {"value": 280, "day": "2017-02-13"},
                        {"value": 41, "day": "2017-05-11"},
                        {"value": 81, "day": "2016-03-04"},
                        {"value": 115, "day": "2017-05-28"},
                        {"value": 313, "day": "2017-02-04"},
                        {"value": 323, "day": "2017-08-21"},
                        {"value": 199, "day": "2018-03-07"},
                        {"value": 215, "day": "2017-08-14"},
                        {"value": 300, "day": "2018-03-03"},
                        {"value": 248, "day": "2016-05-21"},
                        {"value": 340, "day": "2017-09-30"},
                        {"value": 192, "day": "2015-09-14"},
                        {"value": 140, "day": "2018-08-03"},
                        {"value": 384, "day": "2016-04-18"},
                        {"value": 248, "day": "2017-02-28"},
                        {"value": 184, "day": "2017-06-19"},
                        {"value": 157, "day": "2016-12-04"},
                        {"value": 17, "day": "2015-11-05"},
                        {"value": 366, "day": "2016-12-08"},
                        {"value": 336, "day": "2016-09-24"},
                        {"value": 134, "day": "2017-12-01"},
                        {"value": 164, "day": "2017-05-18"},
                        {"value": 317, "day": "2017-08-01"},
                        {"value": 246, "day": "2016-10-13"},
                        {"value": 197, "day": "2016-03-26"},
                        {"value": 359, "day": "2017-04-26"},
                        {"value": 127, "day": "2017-11-12"},
                        {"value": 333, "day": "2018-04-08"},
                        {"value": 108, "day": "2017-06-10"},
                        {"value": 275, "day": "2017-11-01"},
                        {"value": 234, "day": "2018-01-30"},
                        {"value": 362, "day": "2016-01-08"},
                        {"value": 110, "day": "2018-05-23"},
                        {"value": 225, "day": "2015-10-02"},
                        {"value": 132, "day": "2016-06-27"},
                        {"value": 269, "day": "2018-05-14"},
                        {"value": 147, "day": "2017-10-24"},
                        {"value": 214, "day": "2018-01-27"},
                        {"value": 317, "day": "2016-01-05"},
                        {"value": 254, "day": "2018-03-11"},
                        {"value": 293, "day": "2015-07-18"},
                        {"value": 239, "day": "2017-01-23"},
                        {"value": 101, "day": "2018-06-20"},
                        {"value": 317, "day": "2017-07-11"},
                        {"value": 337, "day": "2016-11-20"},
                        {"value": 118, "day": "2018-06-01"},
                        {"value": 50, "day": "2016-12-18"},
                        {"value": 196, "day": "2018-04-30"},
                        {"value": 257, "day": "2016-12-05"},
                        {"value": 267, "day": "2018-01-09"},
                        {"value": 182, "day": "2016-01-16"},
                        {"value": 262, "day": "2016-11-24"},
                        {"value": 385, "day": "2015-10-29"},
                        {"value": 246, "day": "2017-10-26"},
                        {"value": 231, "day": "2018-01-12"},
                        {"value": 93, "day": "2017-03-12"},
                        {"value": 218, "day": "2016-05-19"},
                        {"value": 209, "day": "2016-07-26"},
                        {"value": 304, "day": "2016-02-10"},
                        {"value": 75, "day": "2017-11-14"},
                        {"value": 5, "day": "2018-04-04"},
                        {"value": 152, "day": "2017-10-29"},
                        {"value": 154, "day": "2015-12-13"},
                        {"value": 224, "day": "2015-12-26"},
                        {"value": 139, "day": "2017-09-07"},
                        {"value": 356, "day": "2015-10-03"},
                        {"value": 317, "day": "2016-05-31"},
                        {"value": 153, "day": "2015-10-06"},
                        {"value": 277, "day": "2017-09-03"},
                        {"value": 36, "day": "2017-09-21"},
                        {"value": 173, "day": "2015-05-15"},
                        {"value": 172, "day": "2018-07-14"},
                        {"value": 123, "day": "2016-12-20"},
                        {"value": 218, "day": "2016-08-04"},
                        {"value": 62, "day": "2015-06-29"},
                        {"value": 290, "day": "2016-03-01"},
                        {"value": 200, "day": "2017-09-05"},
                        {"value": 231, "day": "2016-04-09"},
                        {"value": 265, "day": "2017-04-23"},
                        {"value": 399, "day": "2016-07-18"},
                        {"value": 317, "day": "2017-10-01"},
                        {"value": 246, "day": "2017-08-18"},
                        {"value": 353, "day": "2017-11-21"},
                        {"value": 160, "day": "2016-11-27"},
                        {"value": 124, "day": "2015-10-25"},
                        {"value": 369, "day": "2017-02-17"},
                        {"value": 103, "day": "2017-10-17"},
                        {"value": 390, "day": "2017-08-05"},
                        {"value": 116, "day": "2016-10-28"},
                        {"value": 308, "day": "2018-02-16"},
                        {"value": 187, "day": "2015-08-25"},
                        {"value": 215, "day": "2016-10-18"},
                        {"value": 30, "day": "2016-02-28"},
                        {"value": 290, "day": "2016-11-14"},
                        {"value": 225, "day": "2017-12-29"},
                        {"value": 104, "day": "2016-08-17"},
                        {"value": 90, "day": "2016-10-22"},
                        {"value": 82, "day": "2017-06-02"},
                        {"value": 271, "day": "2015-07-04"},
                        {"value": 246, "day": "2015-12-08"},
                        {"value": 102, "day": "2017-04-13"},
                        {"value": 46, "day": "2016-11-22"},
                        {"value": 213, "day": "2016-03-19"},
                        {"value": 298, "day": "2015-07-10"},
                        {"value": 312, "day": "2017-05-13"},
                        {"value": 376, "day": "2018-03-29"},
                        {"value": 39, "day": "2018-05-21"},
                        {"value": 53, "day": "2017-02-15"},
                        {"value": 130, "day": "2015-04-16"},
                        {"value": 24, "day": "2018-04-02"},
                        {"value": 328, "day": "2018-07-08"},
                        {"value": 48, "day": "2015-04-13"},
                        {"value": 353, "day": "2016-12-02"},
                        {"value": 281, "day": "2016-04-13"},
                        {"value": 107, "day": "2016-06-13"},
                        {"value": 362, "day": "2018-01-28"},
                        {"value": 90, "day": "2015-05-06"},
                        {"value": 101, "day": "2017-11-11"},
                        {"value": 265, "day": "2017-11-18"},
                        {"value": 140, "day": "2017-11-02"},
                        {"value": 214, "day": "2016-12-21"},
                        {"value": 145, "day": "2017-09-01"},
                        {"value": 272, "day": "2016-05-04"},
                        {"value": 153, "day": "2018-06-17"},
                        {"value": 146, "day": "2018-05-10"},
                        {"value": 193, "day": "2018-05-12"},
                        {"value": 173, "day": "2017-10-20"},
                        {"value": 54, "day": "2017-11-06"},
                        {"value": 236, "day": "2015-04-25"},
                        {"value": 261, "day": "2015-06-16"},
                        {"value": 56, "day": "2017-11-30"},
                        {"value": 378, "day": "2015-05-30"},
                        {"value": 351, "day": "2017-08-16"},
                        {"value": 146, "day": "2017-01-20"},
                        {"value": 360, "day": "2018-07-18"},
                        {"value": 183, "day": "2016-04-21"},
                        {"value": 391, "day": "2016-02-07"},
                        {"value": 156, "day": "2017-08-09"},
                        {"value": 330, "day": "2015-06-01"},
                        {"value": 11, "day": "2017-02-25"},
                        {"value": 151, "day": "2018-01-01"},
                        {"value": 391, "day": "2016-04-03"},
                        {"value": 174, "day": "2015-06-08"},
                        {"value": 194, "day": "2016-12-26"},
                        {"value": 139, "day": "2015-08-30"},
                        {"value": 371, "day": "2016-01-12"},
                        {"value": 64, "day": "2016-11-18"},
                        {"value": 8, "day": "2016-09-13"},
                        {"value": 278, "day": "2016-09-01"},
                        {"value": 161, "day": "2018-07-12"},
                        {"value": 396, "day": "2015-11-12"},
                        {"value": 280, "day": "2015-10-15"},
                        {"value": 191, "day": "2017-07-18"},
                        {"value": 232, "day": "2017-03-28"},
                        {"value": 273, "day": "2016-07-04"},
                        {"value": 135, "day": "2018-02-11"},
                        {"value": 319, "day": "2017-06-30"},
                        {"value": 349, "day": "2016-11-26"},
                        {"value": 268, "day": "2016-07-08"},
                        {"value": 194, "day": "2017-04-19"},
                        {"value": 206, "day": "2015-08-01"},
                        {"value": 124, "day": "2016-05-11"},
                        {"value": 324, "day": "2016-12-06"},
                        {"value": 397, "day": "2017-11-05"},
                        {"value": 21, "day": "2018-08-01"},
                        {"value": 280, "day": "2015-05-09"},
                        {"value": 215, "day": "2016-01-11"},
                        {"value": 282, "day": "2016-01-14"},
                        {"value": 269, "day": "2015-10-17"},
                        {"value": 71, "day": "2015-10-01"},
                        {"value": 30, "day": "2017-11-09"},
                        {"value": 382, "day": "2016-04-14"},
                        {"value": 278, "day": "2017-12-07"},
                        {"value": 348, "day": "2015-11-25"},
                        {"value": 326, "day": "2015-11-15"},
                        {"value": 285, "day": "2015-11-07"},
                        {"value": 52, "day": "2018-06-04"},
                        {"value": 275, "day": "2018-08-05"},
                        {"value": 271, "day": "2016-06-01"},
                        {"value": 186, "day": "2018-05-28"},
                        {"value": 244, "day": "2017-12-13"},
                        {"value": 187, "day": "2017-02-21"},
                        {"value": 4, "day": "2015-06-11"},
                        {"value": 11, "day": "2015-09-07"},
                        {"value": 31, "day": "2016-08-06"},
                        {"value": 283, "day": "2015-06-02"},
                        {"value": 235, "day": "2016-03-18"},
                        {"value": 331, "day": "2017-03-03"},
                        {"value": 109, "day": "2017-05-16"},
                        {"value": 117, "day": "2017-05-24"},
                        {"value": 353, "day": "2015-04-19"},
                        {"value": 185, "day": "2017-04-16"},
                        {"value": 358, "day": "2018-05-02"},
                        {"value": 356, "day": "2015-08-06"},
                        {"value": 378, "day": "2015-04-12"},
                        {"value": 257, "day": "2016-03-08"},
                        {"value": 64, "day": "2017-11-26"},
                        {"value": 242, "day": "2015-11-28"},
                        {"value": 111, "day": "2015-09-18"},
                        {"value": 184, "day": "2015-11-24"},
                        {"value": 390, "day": "2016-10-03"},
                        {"value": 354, "day": "2018-04-26"},
                        {"value": 351, "day": "2016-03-29"},
                        {"value": 65, "day": "2016-05-14"},
                        {"value": 299, "day": "2015-10-23"},
                        {"value": 238, "day": "2016-07-24"},
                        {"value": 98, "day": "2017-08-11"},
                        {"value": 378, "day": "2017-11-03"},
                        {"value": 251, "day": "2017-07-14"},
                        {"value": 179, "day": "2015-10-27"},
                        {"value": 82, "day": "2015-08-19"},
                        {"value": 43, "day": "2017-09-10"},
                        {"value": 340, "day": "2018-02-20"},
                        {"value": 363, "day": "2018-04-01"},
                        {"value": 356, "day": "2018-07-30"},
                        {"value": 115, "day": "2015-05-08"},
                        {"value": 186, "day": "2016-01-20"},
                        {"value": 150, "day": "2016-07-09"},
                        {"value": 205, "day": "2017-12-14"},
                        {"value": 331, "day": "2018-02-22"},
                        {"value": 85, "day": "2017-01-25"},
                        {"value": 33, "day": "2016-09-04"},
                        {"value": 336, "day": "2016-04-27"},
                        {"value": 3, "day": "2016-04-06"},
                        {"value": 141, "day": "2016-06-21"},
                        {"value": 197, "day": "2016-11-08"},
                        {"value": 396, "day": "2017-04-17"},
                        {"value": 107, "day": "2017-11-20"},
                        {"value": 165, "day": "2016-04-24"},
                        {"value": 272, "day": "2018-04-19"},
                        {"value": 26, "day": "2018-01-06"},
                        {"value": 38, "day": "2016-04-04"},
                        {"value": 198, "day": "2016-10-30"},
                        {"value": 223, "day": "2018-01-11"},
                        {"value": 345, "day": "2015-07-05"},
                        {"value": 387, "day": "2017-01-12"},
                        {"value": 121, "day": "2016-07-10"},
                        {"value": 41, "day": "2015-10-04"},
                        {"value": 355, "day": "2017-03-27"},
                        {"value": 109, "day": "2015-04-18"},
                        {"value": 59, "day": "2015-09-09"},
                        {"value": 330, "day": "2015-09-10"},
                        {"value": 266, "day": "2017-07-03"},
                        {"value": 111, "day": "2016-02-19"},
                        {"value": 373, "day": "2015-04-28"},
                        {"value": 189, "day": "2017-11-19"},
                        {"value": 17, "day": "2016-04-22"},
                        {"value": 89, "day": "2017-07-17"},
                        {"value": 380, "day": "2016-12-28"},
                        {"value": 183, "day": "2017-07-04"},
                        {"value": 10, "day": "2018-05-08"},
                        {"value": 147, "day": "2017-01-07"},
                        {"value": 267, "day": "2017-04-30"},
                        {"value": 280, "day": "2015-12-27"},
                        {"value": 385, "day": "2015-09-17"},
                        {"value": 37, "day": "2015-10-16"},
                        {"value": 154, "day": "2016-04-12"},
                        {"value": 19, "day": "2016-02-06"},
                        {"value": 261, "day": "2017-12-26"},
                        {"value": 168, "day": "2016-09-19"},
                        {"value": 286, "day": "2017-02-12"},
                        {"value": 314, "day": "2018-02-23"},
                        {"value": 273, "day": "2015-09-27"},
                        {"value": 289, "day": "2015-12-04"},
                        {"value": 208, "day": "2016-06-23"},
                        {"value": 333, "day": "2018-04-18"},
                        {"value": 159, "day": "2016-11-05"},
                        {"value": 348, "day": "2016-10-08"},
                        {"value": 190, "day": "2017-09-20"},
                        {"value": 346, "day": "2015-10-05"},
                        {"value": 41, "day": "2015-10-07"},
                        {"value": 33, "day": "2018-08-07"},
                        {"value": 352, "day": "2015-05-22"},
                        {"value": 8, "day": "2016-07-22"},
                        {"value": 308, "day": "2016-04-19"},
                        {"value": 226, "day": "2016-10-26"},
                        {"value": 71, "day": "2017-05-03"},
                        {"value": 110, "day": "2015-04-11"},
                        {"value": 218, "day": "2016-08-16"},
                        {"value": 275, "day": "2017-11-23"},
                        {"value": 107, "day": "2018-06-07"},
                        {"value": 222, "day": "2016-03-07"},
                        {"value": 43, "day": "2017-12-08"},
                        {"value": 338, "day": "2017-04-15"},
                        {"value": 325, "day": "2017-11-13"},
                        {"value": 157, "day": "2016-08-10"},
                        {"value": 240, "day": "2017-06-06"},
                        {"value": 120, "day": "2015-04-15"},
                        {"value": 380, "day": "2017-10-02"},
                        {"value": 100, "day": "2016-11-03"},
                        {"value": 149, "day": "2015-11-21"},
                        {"value": 88, "day": "2017-03-30"},
                        {"value": 152, "day": "2018-05-01"},
                        {"value": 169, "day": "2018-05-25"},
                        {"value": 278, "day": "2018-01-16"},
                        {"value": 6, "day": "2016-01-22"},
                        {"value": 280, "day": "2017-04-22"},
                        {"value": 143, "day": "2015-06-25"},
                        {"value": 168, "day": "2015-06-23"},
                        {"value": 350, "day": "2018-02-28"},
                        {"value": 115, "day": "2017-03-22"},
                        {"value": 162, "day": "2015-12-03"},
                        {"value": 239, "day": "2016-05-29"},
                        {"value": 337, "day": "2016-10-19"},
                        {"value": 259, "day": "2018-06-26"},
                        {"value": 215, "day": "2017-06-09"},
                        {"value": 150, "day": "2018-08-06"},
                        {"value": 13, "day": "2015-10-13"},
                        {"value": 24, "day": "2015-09-21"},
                        {"value": 239, "day": "2016-09-09"},
                        {"value": 285, "day": "2015-08-07"},
                        {"value": 307, "day": "2018-04-27"},
                        {"value": 31, "day": "2017-05-15"},
                        {"value": 162, "day": "2017-07-06"},
                        {"value": 270, "day": "2015-04-03"},
                        {"value": 200, "day": "2016-01-03"},
                        {"value": 332, "day": "2016-12-19"},
                        {"value": 42, "day": "2015-07-01"},
                        {"value": 22, "day": "2017-06-04"},
                        {"value": 196, "day": "2017-08-24"},
                        {"value": 363, "day": "2018-01-19"},
                        {"value": 164, "day": "2015-07-12"},
                        {"value": 93, "day": "2016-11-30"},
                        {"value": 162, "day": "2016-05-16"},
                        {"value": 242, "day": "2015-07-25"},
                        {"value": 14, "day": "2017-12-19"},
                        {"value": 282, "day": "2017-09-08"},
                        {"value": 358, "day": "2015-04-05"},
                        {"value": 261, "day": "2016-10-05"},
                        {"value": 306, "day": "2018-06-18"},
                        {"value": 128, "day": "2017-03-11"},
                        {"value": 256, "day": "2015-07-23"},
                        {"value": 18, "day": "2018-01-26"},
                        {"value": 331, "day": "2017-09-24"},
                        {"value": 23, "day": "2017-01-01"},
                        {"value": 110, "day": "2018-03-04"},
                        {"value": 399, "day": "2018-05-24"},
                        {"value": 188, "day": "2017-03-24"},
                        {"value": 337, "day": "2018-06-22"},
                        {"value": 159, "day": "2015-04-23"},
                        {"value": 261, "day": "2016-07-01"},
                        {"value": 130, "day": "2015-12-29"},
                        {"value": 352, "day": "2015-06-05"},
                        {"value": 21, "day": "2015-11-30"},
                        {"value": 92, "day": "2015-10-21"},
                        {"value": 278, "day": "2017-04-03"},
                        {"value": 249, "day": "2015-05-04"},
                        {"value": 335, "day": "2017-08-29"},
                        {"value": 393, "day": "2016-09-02"},
                        {"value": 138, "day": "2018-06-06"},
                        {"value": 31, "day": "2016-09-16"},
                        {"value": 17, "day": "2016-09-30"},
                        {"value": 285, "day": "2018-06-30"},
                        {"value": 204, "day": "2016-08-08"},
                        {"value": 259, "day": "2018-01-31"},
                        {"value": 284, "day": "2017-06-24"},
                        {"value": 319, "day": "2016-04-16"},
                        {"value": 182, "day": "2015-11-20"},
                        {"value": 320, "day": "2016-06-26"},
                        {"value": 123, "day": "2017-06-12"},
                        {"value": 122, "day": "2016-03-12"},
                        {"value": 173, "day": "2017-01-06"},
                        {"value": 97, "day": "2018-04-07"},
                        {"value": 21, "day": "2015-12-11"},
                        {"value": 324, "day": "2015-09-16"},
                        {"value": 92, "day": "2018-03-06"},
                        {"value": 191, "day": "2016-03-23"},
                        {"value": 272, "day": "2016-03-09"},
                        {"value": 167, "day": "2015-11-23"},
                        {"value": 50, "day": "2016-02-24"},
                        {"value": 379, "day": "2015-10-30"},
                        {"value": 262, "day": "2016-11-28"},
                        {"value": 25, "day": "2018-07-04"},
                        {"value": 48, "day": "2015-07-08"},
                        {"value": 35, "day": "2017-10-14"},
                        {"value": 267, "day": "2017-04-29"},
                        {"value": 92, "day": "2015-12-24"},
                        {"value": 67, "day": "2018-03-20"},
                        {"value": 159, "day": "2017-06-03"},
                        {"value": 175, "day": "2016-06-18"},
                        {"value": 143, "day": "2016-09-26"},
                        {"value": 51, "day": "2017-06-23"},
                        {"value": 273, "day": "2015-04-20"},
                        {"value": 115, "day": "2018-03-30"},
                        {"value": 154, "day": "2015-04-09"},
                        {"value": 22, "day": "2018-01-03"},
                        {"value": 238, "day": "2018-04-12"},
                        {"value": 365, "day": "2016-07-27"},
                        {"value": 276, "day": "2018-02-27"},
                        {"value": 224, "day": "2015-05-26"},
                        {"value": 125, "day": "2016-12-13"},
                        {"value": 320, "day": "2016-11-16"},
                        {"value": 12, "day": "2016-10-15"},
                        {"value": 354, "day": "2017-08-26"},
                        {"value": 313, "day": "2016-07-17"},
                        {"value": 164, "day": "2015-08-17"},
                        {"value": 60, "day": "2016-03-21"},
                        {"value": 321, "day": "2015-04-08"},
                        {"value": 108, "day": "2018-05-06"},
                        {"value": 209, "day": "2018-06-13"},
                        {"value": 354, "day": "2016-12-12"},
                        {"value": 147, "day": "2016-06-04"},
                        {"value": 343, "day": "2017-10-08"},
                        {"value": 312, "day": "2015-12-16"},
                        {"value": 254, "day": "2017-10-04"},
                        {"value": 55, "day": "2017-03-05"},
                        {"value": 284, "day": "2017-02-01"},
                        {"value": 42, "day": "2018-01-05"},
                        {"value": 285, "day": "2016-07-07"},
                        {"value": 396, "day": "2016-07-29"},
                        {"value": 123, "day": "2015-07-22"},
                        {"value": 140, "day": "2016-02-27"},
                        {"value": 121, "day": "2017-05-22"},
                        {"value": 200, "day": "2017-08-17"},
                        {"value": 82, "day": "2016-06-30"},
                        {"value": 260, "day": "2016-11-15"},
                        {"value": 234, "day": "2016-01-24"},
                        {"value": 66, "day": "2016-03-06"},
                        {"value": 147, "day": "2015-04-07"},
                        {"value": 23, "day": "2016-06-17"},
                        {"value": 304, "day": "2016-05-27"},
                        {"value": 35, "day": "2018-06-08"},
                        {"value": 254, "day": "2015-08-16"},
                        {"value": 244, "day": "2017-03-21"},
                        {"value": 227, "day": "2017-02-09"},
                        {"value": 61, "day": "2016-01-23"},
                        {"value": 234, "day": "2018-05-27"},
                        {"value": 78, "day": "2015-04-04"},
                        {"value": 51, "day": "2015-09-02"},
                        {"value": 170, "day": "2016-01-09"},
                        {"value": 299, "day": "2017-07-15"},
                        {"value": 114, "day": "2017-01-31"},
                        {"value": 172, "day": "2018-07-13"},
                        {"value": 342, "day": "2017-08-20"},
                        {"value": 159, "day": "2016-08-29"},
                        {"value": 238, "day": "2016-05-02"},
                        {"value": 198, "day": "2017-12-11"},
                        {"value": 178, "day": "2016-02-25"},
                        {"value": 106, "day": "2016-09-27"},
                        {"value": 189, "day": "2015-12-07"},
                        {"value": 98, "day": "2016-06-03"},
                        {"value": 45, "day": "2016-05-17"},
                        {"value": 85, "day": "2016-04-30"},
                        {"value": 317, "day": "2017-11-25"},
                        {"value": 157, "day": "2016-09-10"},
                        {"value": 145, "day": "2015-07-07"},
                        {"value": 263, "day": "2016-12-15"},
                        {"value": 118, "day": "2015-07-20"},
                        {"value": 174, "day": "2017-07-26"},
                        {"value": 174, "day": "2018-07-03"},
                        {"value": 214, "day": "2016-09-08"},
                        {"value": 309, "day": "2017-10-30"},
                        {"value": 370, "day": "2016-05-22"},
                        {"value": 396, "day": "2016-05-06"},
                        {"value": 244, "day": "2018-06-11"},
                        {"value": 147, "day": "2016-06-29"},
                        {"value": 356, "day": "2017-05-07"},
                        {"value": 260, "day": "2017-08-27"},
                        {"value": 22, "day": "2016-07-13"},
                        {"value": 253, "day": "2017-05-17"},
                        {"value": 338, "day": "2016-07-31"},
                        {"value": 264, "day": "2017-06-18"},
                        {"value": 353, "day": "2017-12-22"},
                        {"value": 253, "day": "2018-01-29"},
                        {"value": 360, "day": "2016-10-11"},
                        {"value": 310, "day": "2017-06-16"},
                        {"value": 392, "day": "2018-07-21"},
                        {"value": 381, "day": "2018-07-11"},
                        {"value": 147, "day": "2016-01-02"},
                        {"value": 281, "day": "2018-04-15"},
                        {"value": 43, "day": "2015-05-07"},
                        {"value": 160, "day": "2018-02-06"},
                        {"value": 255, "day": "2018-03-23"},
                        {"value": 71, "day": "2015-10-28"},
                        {"value": 166, "day": "2018-05-03"},
                        {"value": 165, "day": "2017-05-01"},
                        {"value": 208, "day": "2016-08-19"},
                        {"value": 277, "day": "2017-06-15"},
                        {"value": 36, "day": "2016-11-09"},
                        {"value": 358, "day": "2017-08-25"},
                        {"value": 116, "day": "2016-06-20"},
                        {"value": 20, "day": "2017-11-17"},
                        {"value": 192, "day": "2017-12-10"},
                        {"value": 117, "day": "2018-06-25"},
                        {"value": 296, "day": "2018-02-04"},
                        {"value": 50, "day": "2018-05-29"},
                        {"value": 317, "day": "2017-08-06"},
                        {"value": 35, "day": "2018-07-10"},
                        {"value": 262, "day": "2017-03-14"},
                        {"value": 106, "day": "2018-07-25"},
                        {"value": 280, "day": "2017-07-23"},
                        {"value": 123, "day": "2016-09-07"},
                        {"value": 132, "day": "2017-07-21"},
                        {"value": 45, "day": "2018-02-07"},
                        {"value": 19, "day": "2015-09-29"},
                        {"value": 130, "day": "2015-07-24"},
                        {"value": 178, "day": "2015-06-30"},
                        {"value": 268, "day": "2016-06-15"},
                        {"value": 35, "day": "2018-06-02"},
                        {"value": 80, "day": "2016-11-17"},
                        {"value": 162, "day": "2017-07-10"},
                        {"value": 26, "day": "2017-03-16"},
                        {"value": 64, "day": "2017-05-06"},
                        {"value": 158, "day": "2015-05-21"},
                        {"value": 105, "day": "2016-03-24"},
                        {"value": 113, "day": "2017-03-08"},
                        {"value": 115, "day": "2017-03-06"},
                        {"value": 162, "day": "2017-12-21"},
                        {"value": 267, "day": "2016-07-19"},
                        {"value": 283, "day": "2016-10-20"},
                        {"value": 91, "day": "2017-10-11"},
                        {"value": 79, "day": "2015-11-29"},
                        {"value": 223, "day": "2016-09-06"},
                        {"value": 257, "day": "2016-05-18"},
                        {"value": 172, "day": "2015-12-25"},
                        {"value": 22, "day": "2017-01-10"},
                        {"value": 48, "day": "2016-02-01"},
                        {"value": 230, "day": "2018-01-08"},
                        {"value": 236, "day": "2015-04-27"},
                        {"value": 266, "day": "2015-06-24"},
                        {"value": 154, "day": "2018-04-20"},
                        {"value": 157, "day": "2015-07-27"},
                        {"value": 108, "day": "2017-11-24"},
                        {"value": 80, "day": "2017-01-26"},
                        {"value": 159, "day": "2018-03-02"},
                        {"value": 320, "day": "2017-12-02"},
                        {"value": 221, "day": "2017-12-27"},
                        {"value": 395, "day": "2015-05-27"},
                        {"value": 265, "day": "2016-05-09"},
                        {"value": 325, "day": "2017-04-07"},
                        {"value": 282, "day": "2016-06-22"},
                        {"value": 22, "day": "2015-07-28"},
                        {"value": 68, "day": "2018-04-11"},
                        {"value": 189, "day": "2016-04-25"},
                        {"value": 323, "day": "2017-01-09"},
                        {"value": 145, "day": "2017-11-10"},
                        {"value": 127, "day": "2018-06-03"},
                        {"value": 133, "day": "2016-09-20"},
                        {"value": 143, "day": "2017-08-08"},
                        {"value": 213, "day": "2016-04-28"},
                        {"value": 372, "day": "2016-03-15"},
                        {"value": 376, "day": "2017-01-29"},
                        {"value": 33, "day": "2015-07-31"},
                        {"value": 388, "day": "2017-03-18"},
                        {"value": 117, "day": "2017-12-31"},
                        {"value": 266, "day": "2015-11-19"},
                        {"value": 33, "day": "2015-11-27"},
                        {"value": 200, "day": "2017-09-12"},
                        {"value": 64, "day": "2016-05-03"},
                        {"value": 29, "day": "2016-03-17"},
                        {"value": 229, "day": "2017-06-29"},
                        {"value": 259, "day": "2016-11-29"},
                        {"value": 334, "day": "2016-09-11"},
                        {"value": 92, "day": "2018-03-27"},
                        {"value": 268, "day": "2016-07-28"},
                        {"value": 382, "day": "2018-04-09"},
                        {"value": 374, "day": "2015-12-01"},
                        {"value": 269, "day": "2016-09-12"},
                        {"value": 236, "day": "2015-09-06"},
                        {"value": 60, "day": "2018-04-22"},
                        {"value": 95, "day": "2016-08-15"},
                        {"value": 173, "day": "2017-02-22"},
                        {"value": 151, "day": "2016-11-23"},
                        {"value": 186, "day": "2017-10-06"},
                        {"value": 190, "day": "2017-09-06"},
                        {"value": 145, "day": "2016-11-13"},
                        {"value": 243, "day": "2015-12-23"},
                        {"value": 279, "day": "2015-10-08"},
                        {"value": 388, "day": "2015-10-22"},
                        {"value": 138, "day": "2018-01-23"},
                        {"value": 10, "day": "2016-08-05"},
                        {"value": 265, "day": "2016-03-27"},
                        {"value": 307, "day": "2017-05-27"},
                        {"value": 216, "day": "2018-07-26"},
                        {"value": 343, "day": "2015-04-14"},
                        {"value": 363, "day": "2018-07-01"},
                        {"value": 280, "day": "2018-03-14"},
                        {"value": 38, "day": "2017-11-22"},
                        {"value": 225, "day": "2015-04-10"},
                        {"value": 308, "day": "2017-04-02"},
                        {"value": 220, "day": "2016-08-21"},
                        {"value": 43, "day": "2018-07-24"},
                        {"value": 111, "day": "2018-03-12"},
                        {"value": 311, "day": "2017-09-29"},
                        {"value": 47, "day": "2017-03-13"},
                        {"value": 142, "day": "2016-09-03"},
                        {"value": 372, "day": "2018-01-02"},
                        {"value": 4, "day": "2015-11-10"},
                        {"value": 320, "day": "2018-06-29"},
                        {"value": 132, "day": "2016-06-19"},
                        {"value": 102, "day": "2017-08-12"},
                        {"value": 105, "day": "2016-09-18"},
                        {"value": 66, "day": "2016-05-07"},
                        {"value": 344, "day": "2016-10-12"},
                        {"value": 141, "day": "2018-07-09"},
                        {"value": 46, "day": "2017-05-26"},
                        {"value": 201, "day": "2018-04-05"},
                        {"value": 271, "day": "2016-10-07"},
                        {"value": 21, "day": "2018-06-15"},
                        {"value": 274, "day": "2016-07-21"},
                        {"value": 249, "day": "2017-08-31"},
                        {"value": 139, "day": "2018-06-23"},
                        {"value": 270, "day": "2018-04-25"},
                        {"value": 265, "day": "2017-04-12"},
                        {"value": 329, "day": "2016-07-02"},
                        {"value": 114, "day": "2015-09-26"},
                        {"value": 128, "day": "2018-02-17"},
                        {"value": 217, "day": "2016-01-30"},
                        {"value": 260, "day": "2015-11-17"},
                        {"value": 150, "day": "2017-05-25"},
                        {"value": 239, "day": "2016-07-06"},
                        {"value": 363, "day": "2015-12-28"},
                        {"value": 147, "day": "2015-09-22"},
                        {"value": 49, "day": "2015-07-21"},
                        {"value": 77, "day": "2017-06-11"},
                        {"value": 54, "day": "2016-07-30"},
                        {"value": 360, "day": "2015-08-22"},
                        {"value": 385, "day": "2018-05-13"},
                        {"value": 42, "day": "2015-08-31"},
                        {"value": 70, "day": "2016-08-09"},
                        {"value": 237, "day": "2017-01-04"},
                        {"value": 317, "day": "2018-03-31"},
                        {"value": 227, "day": "2016-04-23"},
                        {"value": 105, "day": "2015-08-11"},
                        {"value": 82, "day": "2017-04-05"},
                        {"value": 208, "day": "2018-01-20"},
                        {"value": 203, "day": "2017-03-01"},
                        {"value": 326, "day": "2016-08-30"},
                        {"value": 181, "day": "2016-08-24"},
                        {"value": 376, "day": "2015-08-29"},
                        {"value": 121, "day": "2016-02-26"},
                        {"value": 156, "day": "2015-10-14"},
                        {"value": 299, "day": "2015-08-18"},
                        {"value": 354, "day": "2017-05-29"},
                        {"value": 393, "day": "2018-06-05"},
                        {"value": 244, "day": "2018-06-16"},
                        {"value": 369, "day": "2018-03-24"},
                        {"value": 156, "day": "2016-08-12"},
                        {"value": 260, "day": "2017-10-05"},
                        {"value": 30, "day": "2015-07-19"},
                        {"value": 372, "day": "2016-06-10"},
                        {"value": 4, "day": "2017-11-16"},
                        {"value": 263, "day": "2016-10-17"},
                        {"value": 113, "day": "2016-03-22"},
                        {"value": 82, "day": "2017-04-08"},
                        {"value": 178, "day": "2017-09-19"},
                        {"value": 206, "day": "2018-03-08"},
                        {"value": 200, "day": "2016-04-26"},
                        {"value": 93, "day": "2016-08-31"},
                        {"value": 190, "day": "2016-09-14"},
                        {"value": 133, "day": "2017-11-04"},
                        {"value": 53, "day": "2018-01-04"},
                        {"value": 257, "day": "2018-05-30"},
                        {"value": 382, "day": "2016-03-11"},
                        {"value": 182, "day": "2017-12-18"},
                        {"value": 190, "day": "2017-08-30"},
                        {"value": 81, "day": "2016-08-28"},
                        {"value": 43, "day": "2016-08-14"},
                        {"value": 247, "day": "2017-10-16"},
                        {"value": 11, "day": "2018-03-17"},
                        {"value": 128, "day": "2017-07-27"},
                        {"value": 316, "day": "2017-04-06"},
                        {"value": 185, "day": "2018-01-10"},
                        {"value": 168, "day": "2018-03-16"},
                        {"value": 367, "day": "2015-12-21"},
                        {"value": 24, "day": "2018-05-11"},
                        {"value": 29, "day": "2015-11-14"},
                        {"value": 68, "day": "2015-06-14"},
                        {"value": 317, "day": "2015-12-18"},
                        {"value": 370, "day": "2017-07-08"},
                        {"value": 216, "day": "2015-09-19"},
                        {"value": 86, "day": "2018-02-18"},
                        {"value": 312, "day": "2015-08-02"},
                        {"value": 114, "day": "2018-03-09"},
                        {"value": 342, "day": "2017-08-13"},
                        {"value": 13, "day": "2017-10-12"},
                        {"value": 0, "day": "2017-02-06"},
                        {"value": 203, "day": "2018-06-10"},
                        {"value": 229, "day": "2015-09-24"},
                        {"value": 209, "day": "2016-03-16"},
                        {"value": 11, "day": "2015-08-20"},
                        {"value": 203, "day": "2017-03-31"},
                        {"value": 54, "day": "2018-01-21"},
                        {"value": 209, "day": "2018-07-07"},
                        {"value": 162, "day": "2015-05-12"},
                        {"value": 196, "day": "2018-02-25"},
                        {"value": 395, "day": "2016-05-12"},
                        {"value": 68, "day": "2016-08-26"},
                        {"value": 374, "day": "2016-05-05"},
                        {"value": 111, "day": "2016-07-03"},
                        {"value": 209, "day": "2015-11-16"},
                        {"value": 92, "day": "2016-03-25"},
                        {"value": 76, "day": "2016-10-27"},
                        {"value": 252, "day": "2018-05-17"},
                        {"value": 144, "day": "2016-02-15"},
                        {"value": 152, "day": "2017-02-07"},
                        {"value": 311, "day": "2018-05-18"},
                        {"value": 260, "day": "2015-05-03"},
                    ],
                    "layout": {
                        # "title": "Days you have screened",
                        "type": "calendar",
                        "height": 400,
                        "width": 1000,
                        "from": "2015-03-01",
                        "to": "2016-07-12",
                        "emptyColor": "#eeeeee",
                        "colors": ["#61cdbb", "#97e3d5", "#e8c1a0", "#f47560"],
                        "margin": {"top": 40, "right": 40, "bottom": 10, "left": 40},
                        "yearSpacing": 40,
                        "monthBorderColor": "#3f78e4",
                        "dayBorderWidth": 2,
                        "dayBorderColor": "#ffffff",
                        "legends": [
                            {
                                "anchor": "bottom-right",
                                "direction": "row",
                                "translateY": 36,
                                "itemCount": 4,
                                "itemWidth": 42,
                                "itemHeight": 36,
                                "itemsSpacing": 14,
                                "itemDirection": "right-to-left",
                            }
                        ],
                    },
                }
        chord_chart = {
            "data": [
                [473, 462, 189, 1102, 498],
                [28, 1782, 272, 127, 247],
                [1879, 307, 318, 222, 15],
                [437, 530, 134, 1683, 1238],
                [75, 127, 954, 274, 275],
            ],
            "layout": {
                "title": "Chord Diagram",
                "type": "chord",
                "height": 400,
                "width": 600,
                "keys": ["John", "Raoul", "Jane", "Marcel", "Ibrahim"],
                "margin": {"top": 60, "right": 60, "bottom": 90, "left": -400},
                "valueFormat": ".2f",
                "padAngle": 0.02,
                "innerRadiusRatio": 0.96,
                "innerRadiusOffset": 0.02,
                "inactiveArcOpacity": 0.25,
                "arcBorderColor": {"from": "color", "modifiers": [["darker", 0.6]]},
                "activeRibbonOpacity": 0.75,
                "inactiveRibbonOpacity": 0.25,
                "ribbonBorderColor": {"from": "color", "modifiers": [["darker", 0.6]]},
                "labelRotation": -90,
                "labelTextColor": {"from": "color", "modifiers": [["darker", 1]]},
                "colors": {"scheme": "nivo"},
                "motionConfig": "stiff",
                "legends": [
                    {
                        "anchor": "bottom",
                        "direction": "row",
                        "justify": False,
                        "translateX": 0,
                        "translateY": 70,
                        "itemWidth": 80,
                        "itemHeight": 14,
                        "itemsSpacing": 0,
                        "itemTextColor": "#999",
                        "itemDirection": "left-to-right",
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "effects": [{"on": "hover", "style": {"itemTextColor": "#000"}}],
                    }
                ],
            },
        }


        # col1, col2 = st.columns([2, 1])
        with col1:
           st.header("Days you have screened.")
           nc.nivo_chart(data=calendar_chart["data"], layout=calendar_chart["layout"], key="calendar_chart")
  

        # with col2:

        #     nc.nivo_chart(data=chord_chart["data"], layout=chord_chart["layout"], key="chord_chart")
            

        st.header("Understanding Teeth Names")
        st.info("The tooth names perform their function according to their shapes and morphology. Humans eat both meat and plants. This particular characteristic needs incisors, the cutting teeth, to cut foods into tiny pieces to facilitate inward movement into the mouth."+
                "What is the number of teeth in adults? Adults have 32 teeth known as secondary or permanent teeth.")                 
        
        st.info("Eight incisors (two central and two laterals))")
        st.info("Four canines, also named cuspids")
        st.info("Eight premolars, also known as bicuspid")
        st.info("12 molars that include four wisdom teeth")

        st.info("Children have 20 milk or primary teeth. They grow all teeth by age 3. Four incisors, Two canines and Four molars. When the child turns seven, they start replacing milk teeth with secondary ones.")


        st.header("The Meaning of Teeth Names")
        teethNames = ['Frontal Incisor', 'Lateral Incisor', 'Canines', 'Premolars', 'Molars', 'Wisdom Teeth']

        col1, col2 = st.columns([1, 1])
        with col1:
            teethName = st.selectbox("", teethNames)
            

        with col2:
            if teethName == 'Frontal Incisor':
                st.write("Incisor teeth are in the frontal area of your mouth, the front and face teeth. You have two in the lower jaw and two in the upper jaw. When you bite a fruit, you are using your incisors. Shaped as a chisel with sharp edges, they help you chew into your food. The incisors are the first to grow when the baby is between six and eight months old.")
            
            if teethName == 'Lateral Incisor':
                st.write("The four lateral incisors grow next to the middle incisors, one on each side, for the upper and lower jaw. These teeth tear food with their incisal edges.")

            if teethName == 'Canines':
                st.write("They are sharp, pointy teeth. A human body has two canines on the upper maxilla and two on the lower mandible. After 16 months of age, the baby will start growing canine teeth. Upper canine teeth grow before the lower ones. The canine teeth are called cuspids with incisors; they can bite and tear food.")
                
            if teethName == 'Premolars':
                st.write("The premolars are also called bicuspids. Premolars are a bit bigger than incisors and canines. Premolars are smaller than the molars and have two cusps on the biting location for crushing and tearing food. Premolars have ridges to crush down food and a flat surface for grinding food to make it easier to swallow. The premolars nearest to the incisors are the initial or first premolars, while the ones nearest to the molars are the second premolars. Humans have four premolars in the lower jaw and four in the upper maxilla.")

            if teethName == 'Molars':
                st.write("They are your most prominent and the most strong teeth; the large surface area of your molars helps grind up food. Molars are big teeth with four cusps in the mouth behind the premolars.When eating, the tongue passes the food to the back of the mouth to let the molars grind it into small pieces for easy swallowing. Molars have broad, flat surfaces for chewing, biting, and crumbling your food.The molars also include the four wisdom teeth, which are the last set of teeth to grow. Usually, they erupt between the ages of 17 and 25. Wisdom teeth are also called third molars.")

            if teethName == 'Wisdom Teeth':
                st.write("It is also known as Vestigial teeth, located at the back of the mouth, two in the upper jaw and two in the lower jaw. Wisdom teeth generally erupt during teenager but can grow at any time. Not all wisdom teeth need extraction. Not everyone has enough room in their mouth for this last group of teeth. Sometimes, the wisdom teeth grow impacted, meaning they are under the other molars; they don't have space to grow in. If you don't have room for your wisdom teeth, you'll likely have to have them removed surgically.")


        st.info("The tooth surfaces also have a name depending on their location inside the oral cavity. The area of the tooth nearest to the tongue is the lingual surface. For the face teeth, the area closest to the lip is the labial surface. For the back teeth (premolars and molars), the area that faces the checks is known as the buccal surface, and the chewing place is known as the occlusal surface.")
            
        
        # Labial: surface on the side of the lips of the anterior teeth (incisors and canines)
        # Buccal: surface on the side of the cheeks of the posterior teeth (premolars and molars)
        # Lingual: surface on the side of the tongue of every tooth (anterior and posterior)
        # Occlusal: masticating surface of the posterior teeth.
        # Incisive: the sharp edge of the incisors.
        # Mésial: interproximal surface (between the adjacent teeth) located nearest the midline.
        # Distal: interproximal surface (between the adjacent teeth) located farthest from the midline.

# ====================================================================

        # col1, col2 = st.columns([3, 1])
        # data = np.random.randn(10, 1)

        # col1.subheader("A wide column with a chart")
        # col1.line_chart(data)

        # col2.subheader("A narrow column with the data")
        # col2.write(data)

# ====================================================================

        # app1.run(complex_nav)
        
