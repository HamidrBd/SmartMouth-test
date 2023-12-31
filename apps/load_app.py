import streamlit as st
import hydralit_components as hc
import time
from hydralit import HydraHeadApp
import cv2 as cv

class Education(HydraHeadApp):

    def __init__(self, title = 'Loader Playground', delay=0, **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        self.delay = delay

    def run(self):

        col1, col2, col3 = st.columns(3)

        with col2:

            st.text_input(
            "Search Box",
            "Please enter your clinic, doctor, damage or prodocts name.",
            key="placeholder",
            )
        
        st.write('')
        st.write('')
        st.write('')

        col1, col2, col3 = st.columns(3)

        with col1:
            # st.header("A cat")
            st.image("https://sabkadentist.com/wp-content/uploads/2020/07/anatomy-of-tooth.png.webp", use_column_width=True, width=700)

        with col2:
            # st.header("A dog")
            st.image("https://azlaserdentistry.com/wp-content/uploads/2019/03/Permanent-Crown111.jpg", use_column_width=True, width=600)

        with col3:
            # st.header("An owl")
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiMxMlXq7y_fxY65T6w14hVWnMDJ5N45nn2g&usqp=CAU", use_column_width=True, width=600)


        col1, col2, col3 = st.columns(3)

        with col1:
            # st.header("A cat")
            st.image("https://cdn.3d4medical.com/website/blog/teeth-2.jpg", use_column_width=True)

        with col2:
            # st.header("A dog")
            st.image("https://www.rutgers.edu/sites/default/files/tooth_xray.jpg", use_column_width=True)

        with col3:
            # st.header("An owl")
            st.image("https://www.deltadental.com/content/dam/ddpa/us/en/articles/when-do-you-need-a-root-canal/human%20tooth%20anatomy%201024x843.jpg", use_column_width=True)


        col1, col2, col3 = st.columns(3)

        with col1:
            # st.header("A cat")
            st.image("https://www.smiledesignersandiego.com/wp-content/uploads/2021/12/cavity-process.jpg", use_column_width=True)

        with col2:
            # st.header("A dog")
            st.image("https://images.squarespace-cdn.com/content/v1/56801fced82d5e87366f5448/1619797434866-07YMNU8CROQW9TZLBGNA/Brush_Teeth_Steps.jpg", use_column_width=True)

        with col3:
            # st.header("An owl")
            st.image("https://jdh.adha.org/content/jdenthyg/87/3/118/F2.large.jpg", use_column_width=True)





#         single_loader_list={
#                     'pacman':{'loader': hc.Loaders.pacman,'length': 0},
#                     'points_line':{'loader': hc.Loaders.points_line,'length': 0},
#                     'grid_points':{'loader': hc.Loaders.grid_points,'length': 0},
#                     'pulse_bars':{'loader': hc.Loaders.pulse_bars,'length': 0},
#                     'showcase_pretty':{'loader': hc.Loaders.showcase_pretty,'length': 0}
#         }
        

#         multi_loader_list={
#                     'standard_loaders': {'loader': hc.Loaders.standard_loaders,'length': 8},
#                     'pretty_loaders': {'loader': hc.Loaders.pretty_loaders,'length': 15}
#         }

#         s,c1,c2,c3 = st.columns([2,4,4,4])
#         loader_delay = st.slider('Loader Display Time (sec)', 2, 20, 5)
#         loader_mixer = s.checkbox('Multi-select Loaders')
        
        
#         if loader_mixer:
#             loader_list = multi_loader_list
#             loader_replicat = s.checkbox('Enable Loader Replication')
#             selected_loader = c1.selectbox('Select Loader',loader_list.keys())

#             if loader_replicat:
#                 loader_index = c2.selectbox('Loader index',list(range(loader_list[selected_loader]['length'])))
#                 loader_rep = c3.selectbox('Loader Replication',[1,2,3,4,5,6,7,8,9,10])
#                 loader_index=[loader_index]*loader_rep
#             else:
#                 loader_index = c2.multiselect('Loader indexes',list(range(loader_list[selected_loader]['length'])))

#         else:
#             loader_list = single_loader_list
#             loader_index = 0
#             selected_loader = c1.selectbox('Select Loader',loader_list.keys())


#         b,c, = st.columns([3,7])

#         if b.button('Unleash the Loader!'):
#             with hc.HyLoader('Now doing loading',loader_list[selected_loader]['loader'],index=loader_index):
#                 time.sleep(loader_delay)
  
#         cex = c.expander('Show Code')

#         cex.code(
# """
# import hydralit_components as hc

# single_loader_list={
#             'pacman': hc.Loaders.pacman
#             'points_line': hc.Loaders.points_line
#             'grid_points': hc.Loaders.grid_points
#             'pulse_bars': hc.Loaders.pulse_bars
#             'showcase_pretty': hc.Loaders.showcase_pretty
# }

# multi_loader_list={
#             'standard_loaders': hc.Loaders.standard_loaders,
#             'pretty_loaders': hc.Loaders.pretty_loaders
# }

# # a dedicated single loader 
# with hc.HyLoader('Now doing loading',single_loader_list['pacman'],):
#     time.sleep(loader_delay)

# # for 3 loaders from the standard loader group
# with hc.HyLoader('Now doing loading',multi_loader_list['standard_loaders'],index=[3,0,5]):
#     time.sleep(loader_delay)

# # for 1 (index=5) from the standard loader group
# with hc.HyLoader('Now doing loading',multi_loader_list['standard_loaders'],index=5):
#     time.sleep(loader_delay)

# # for 4 replications of the same loader (index=2) from the standard loader group
# with hc.HyLoader('Now doing loading',multi_loader_list['standard_loaders'],index=[2,2,2,2]):
#     time.sleep(loader_delay)
# """
#         )