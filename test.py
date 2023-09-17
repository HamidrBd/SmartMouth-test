# import requests
# import streamlit as st
# from base64 import b64encode
# from streamlit_elements import elements, dashboard, html

# st.set_page_config(layout="wide")

# # Some random image URL.
# images_url = [
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
# ]

# # Download these images and get their bytes.
# images_bytes = [requests.get(url).content for url in images_url]

# # Encode these bytes to base 64.
# images_b64 = [b64encode(bytes).decode() for bytes in images_bytes]

# # Initialize a layout for our dashboard.
# # It's gonna be a 2x2 grid, with each element being of height 3 and width 6 out of 12.
# layout = [
#     dashboard.Item("image0", 0, 0, 6, 3),
#     dashboard.Item("image1", 6, 0, 6, 3),
#     dashboard.Item("image2", 0, 3, 6, 3),
#     dashboard.Item("image3", 6, 3, 6, 3),
# ]

# with elements("image_grid"):
#     with dashboard.Grid(layout):
#         # We iterate over our images encoded as base64.
#         # enumerate() will return the item's index i from 0 to 3, so I can generate
#         # dashboard layout keys from "image0" to "image3".
#         for i, b64 in enumerate(images_b64):
#             html.img(
#                 # We pass our base 64 to <img src=...></img> to display our image.
#                 # See: https://stackoverflow.com/a/8499716
#                 src=f"data:image/png;base64,{b64}",
#                 # A simple CSS style to avoid image distortion on resize.
#                 css={"object-fit": "cover"},
#                 # We set the key to bind our image to a dashboard item.
#                 key=f"image{i}",
#             )

# # =================================================================

# import streamlit as st
# from streamlit_elements import elements, mui, html, sync

# IMAGES = [
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
#     "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg",
# ]


# def slideshow_swipeable(images):
#     # Generate a session state key based on images.
#     key = f"slideshow_swipeable_{str(images).encode().hex()}"

#     # Initialize the default slideshow index.
#     if key not in st.session_state:
#         st.session_state[key] = 0

#     # Get the current slideshow index.
#     index = st.session_state[key]

#     # Create a new elements frame.
#     with elements(f"frame_{key}"):

#         # Use mui.Stack to vertically display the slideshow and the pagination centered.
#         # https://mui.com/material-ui/react-stack/#usage
#         with mui.Stack(spacing=2, alignItems="center"):

#             # Create a swipeable view that updates st.session_state[key] thanks to sync().
#             # It also sets the index so that changing the pagination (see below) will also
#             # update the swipeable view.
#             # https://mui.com/material-ui/react-tabs/#full-width
#             # https://react-swipeable-views.com/demos/demos/
#             with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
#                 for image in images:
#                     html.img(src=image, css={"width": "100%"})

#             # Create a handler for mui.Pagination.
#             # https://mui.com/material-ui/react-pagination/#controlled-pagination
#             def handle_change(event, value):
#                 # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
#                 st.session_state[key] = value-1

#             # Display the pagination.
#             # As the index value can also be updated by the swipeable view, we explicitely
#             # set the page value to index+1 (page value starts at 1).
#             # https://mui.com/material-ui/react-pagination/#controlled-pagination
#             mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


# def slideshow_transition(images, transition):
#     # Generate a session state key based on images.
#     key = f"slideshow_transition_{str(images).encode().hex()}"

#     # Initialize the default slideshow page.
#     if key not in st.session_state:
#         st.session_state[key] = 1

#     # Get the current slideshow index.
#     page = st.session_state[key]

#     # Create a new elements frame.
#     with elements(f"frame_{key}"):

#         # Use mui.Stack to vertically display the slideshow and the pagination centered.
#         # https://mui.com/material-ui/react-stack/#usage
#         with mui.Stack(spacing=2, alignItems="center"):

#             # Create a CSS grid.
#             # All slides will be displayed in the same column and row, they will overlap.
#             # https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout
#             with html.div(css={"display": "grid", "gridTemplateColumns": "1fr", "overflow": "hidden"}):

#                 # Iterate over images.
#                 # Generate an index/page that starts at 1 to check which image is selected.
#                 for page, image in enumerate(images, 1):
#                     selected = (st.session_state[key] == page)

#                     # Wrap the image in a transition.
#                     # mui.Grow and mui.Fade takes a 'in' property, however 'in' is also
#                     # a python keyword you cannot use as argument name. To bypass this
#                     # issue, you can just append an underscore.
#                     # https://mui.com/material-ui/transitions/
#                     with mui[transition](in_=selected):
#                         # Display the image in the first column and row.
#                         html.img(src=image, css={
#                             "gridRow": 1,
#                             "gridColumn": 1,
#                             "width": "100%",
#                         })

#             # Display the pagination.
#             # Synchronize onChange callback's second parameter with st.session_state[key].
#             # Ignore the first parameter by using None as first argument in sync().
#             # https://mui.com/material-ui/react-pagination/#controlled-pagination
#             # https://mui.com/material-ui/api/pagination/#props (onChange)
#             mui.Pagination(count=len(images), color="primary", onChange=sync(None, key))



# st.title("Streamlit Elements Slideshow")

# st.subheader("Swipeable slideshow")
# slideshow_swipeable(IMAGES)

# st.subheader("Slideshow with transitions")
# transition = st.radio("Select your transition", ["Collapse", "Fade", "Grow", "Slide", "Zoom"])
# slideshow_transition(IMAGES, transition)

# ==============================================================================



# ==============================================================================

# https://mp.weixin.qq.com/s?__biz=MzU0Mzc1MzcwNA==&mid=2247484660&idx=1&sn=243dacd9285e49dff289cc6901a23e2b&chksm=fb07d073cc705965beefd97f6a5a40a28e520eac3e51024b33f57bfc0f44c593e383101ffb6a#rd

import streamlit as st
from streamlit_elements import elements, dashboard, mui, nivo, html

st.set_page_config(page_title="Streamlit-elements-use case", layout="wide")
st.write('1')

layout = [
    dashboard.Item("area-map", 0, 0, 5, 3),
    dashboard.Item("Funnel-chart", 6, 0, 7, 3),

    dashboard.Item("Graph", 0, 2, 6, 3),
    dashboard.Item("histogram", 6, 2, 6, 3),

    dashboard.Item("radar-chart", 0, 4, 5, 4),
    dashboard.Item("pie-chart", 6, 4, 7, 4),
]

with elements("demo"):
    with mui.Paper:
        with mui.Typography:
            html.h1("Streamlit-elements-Use Cases",
                css={
                    "backgroundColor": "#00ccff",
                    "color":"white",
                    "borderRadius": "5px",
                    "zIndex": 'tooltip',
                    "height": "45px",   
                    "&:hover": {
                        "color": "lightgreen"
                    }
                })
    st.write('2')


    # with dashboard.Grid(layout, draggableHandle=".draggable"):
    #     with mui.Card(key="Graph", sx={"color": 'white', 'bgcolor': 'success.main', "display": "flex", 'borderRadius': 2,  "flexDirection": "column"}):
    #             mui.CardHeader(title="Graph", className="draggable")
    #             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
    #                  with mui.Paper:
    #                     with mui.Typography:
    #                         html.h1("Streamlit-elements-Use Cases",
    #                             css={
    #                                 "backgroundColor": "#00ccff",
    #                                 "color":"white",
    #                                 "borderRadius": "5px",
    #                                 "zIndex": 'tooltip',
    #                                 "height": "45px",
    #                                 "&:hover": {
    #                     "color": "lightgreen"
    #                 }
    #                                 })
                            
    #                         html.p('hamidreza badr')



                 

    # with dashboard.Grid(layout, draggableHandle=".draggable"):
    #     with mui.Card(key="Graph", sx={"color": 'white', 'bgcolor': 'success.main', "display": "flex", 'borderRadius': 2,  "flexDirection": "column"}):
    #             mui.CardHeader(title="Graph", className="draggable")
    #             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
    #                 with elements("nivo_charts"):
    #                     with mui.Box(sx={"height": 500}):
    #                          nivo.Calender(data=calendar_chart["data"], layout=calendar_chart["layout"], key="calendar_chart")
    #                          nc.nivo_chart(data=calendar_chart["data"], layout=calendar_chart["layout"], key="calendar_chart")


                                                























                         
                #         data_quxian = "see-code-below" 
                #         with mui.Box(sx={"height": 500}):
                #             nivo.Bump(
                #                 data=data_quxian,
                #                 margin={'top': 50, 'right': 110, 'bottom': 50, 'left': 60},
                #                 xScale = {'type': 'point'},
                #                 yScale = {
                #                     'type': 'linear',
                #                     'min': 'auto',
                #                     'max': 'auto',
                #                     'stacked': 'true',
                #                     'reverse': 'false'
                #                 },
                #                 yFormat = " >-.2f",
                #                 axisTop = {'null'},
                #                 axisBottom = {
                #                     'orient': 'bottom',
                #                     'tickSize': 5,
                #                     'tickPadding': 5,
                #                     'tickRotation': 0,
                #                     'legend': 'transportation',
                #                     'legendOffset': 36,
                #                     'legendPosition': 'middle'
                #                 },
                #                 axisLeft = {
                #                     'orient': 'left',
                #                     'tickSize': 5,
                #                     'tickPadding': 5,
                #                     'tickRotation': 0,
                #                     'legend': 'count',
                #                     'legendOffset': -40,
                #                     'legendPosition': 'middle'
                #                 },
                #                 pointSize = {10},
                #                 pointColor = {'theme': 'background'},
                #                 pointBorderWidth = {2},
                #                 pointBorderColor = {
                #                 'from': 'serieColor'},
                #                 pointLabelYOffset = {-12},
                #                 useMesh = {'true'},
                #                 legends = [
                #                     {
                #                         'anchor': 'bottom-right',
                #                         'direction': 'column',
                #                         'justify': 'false',
                #                         'translateX': 100,
                #                         'translateY': 0,
                #                         'itemsSpacing': 0,
                #                         'itemDirection': 'left-to-right',
                #                         'itemWidth': 80,
                #                         'itemHeight': 20,
                #                         'itemOpacity': 0.75,
                #                         'symbolSize': 12,
                #                         'symbolShape': 'circle',
                #                         'symbolBorderColor': 'rgba(0, 0, 0, .5)',
                #                         'effects': [
                #                             {
                #                                 'on': 'hover',
                #                                 'style': {
                #                                     'itemBackground': 'rgba(0, 0, 0, .03)',
                #                                     'itemOpacity': 1
                #                                 }
                #                             }
                #                         ]
                #                     }
                #                 ],
                #                 theme={
                #                     "background": "#00cccc",
                #                     "textColor": "white",
                #                     "tooltip": {
                #                         "container": {
                #                             "background": "#FFFFFF",
                #                             "color": "#31333F",
                #                         }
                #                     }
                #                 }
                #             )
                # st.write('3')

        # with mui.Card(key="histogram", sx={"color": 'white', 'bgcolor': 'success.main', "display": "flex", 'borderRadius': 2,  "flexDirection": "column"}):
    #             mui.CardHeader(title="histogram", className="draggable")
    #             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
    #                 data_zhuzhuangtu = "see-code-below"
    #                 nivo.Bar(
    #                     data=data_zhuzhuangtu,
    #                     layout="horizontal",
    #                     keys=[
    #                         'hot dog',
    #                         'burger',
    #                         'sandwich',
    #                         'kebab',
    #                         'fries',
    #                         'donut'
    #                     ],
    #                     indexBy="country",
    #                     margin={ "top": 20, "right": 130, "bottom": 50, "left": 60 },
    #                     padding={0.4},
    #                     valueScale={ "type": 'linear' },
    #                     indexScale={ "type": 'band', "round": "true" },
    #                     colors={ "scheme": 'nivo' },

    #                     borderColor={
    #                         "from": 'color',
    #                         "modifiers": [
    #                             [
    #                                 'darker',
    #                                 1.6
    #                             ]
    #                         ]
    #                     },
    #                     axisTop={"null"},
    #                     axisBottom={
    #                         "tickSize": 5,
    #                         "tickPadding": 5,
    #                         "tickRotation": 0,
    #                         "legend": 'country',
    #                         "legendPosition": 'middle',
    #                         "legendOffset": 32
    #                     },
    #                     axisLeft={
    #                         "tickSize": 5,
    #                         "tickPadding": 5,
    #                         "tickRotation": 0,
    #                         "legend": 'food',
    #                         "legendPosition": 'middle',
    #                         "legendOffset": -40
    #                     },
    #                     labelSkipWidth={12},
    #                     labelSkipHeight={12},
    #                     labelTextColor={
    #                         "from": 'color',
    #                         "modifiers": [
    #                             [
    #                                 'darker',
    #                                 1.6
    #                             ]
    #                         ]
    #                     },
    #                     legends=[
    #                         {
    #                             "dataFrom": 'keys',
    #                             "anchor": 'top-right',
    #                             "direction": 'column',
    #                             "margin": { "left": 10 },
    #                             "justify": "false",
    #                             "translateX": 120,
    #                             "translateY": 0,
    #                             "itemsSpacing": 2,
    #                             "itemWidth": 100,
    #                             "itemHeight": 20,
    #                             "itemDirection": 'left-to-right',
    #                             "itemOpacity": 0.85,
    #                             "symbolSize": 20,
    #                             "effects": [
    #                                 {
    #                                     "on": 'hover',
    #                                     "style": {
    #                                         "itemOpacity": 1
    #                                     }
    #                                 }
    #                             ]
    #                         }
    #                     ],
    #                     theme={
    #                         "background": "#00cccc",
    #                         "textColor": "white",
    #                         "tooltip": {
    #                             "container": {
    #                                 "background": "#FFFFFF",
    #                                 "color": "#31333F",
    #                             }
    #                         }
    #                     },
    #                     role="application",
    #                     ariaLabel="Nivo bar chart demo",
    #                 )
    #     st.write('4')

        # with mui.Card(key="radar-chart", sx={"color": 'white', 'bgcolor': 'success.main', "display": "flex", 'borderRadius': 2,  "flexDirection": "column"}):
        #         mui.CardHeader(title="radar-chart", className="draggable")
        #         with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
        #             data_leida = "见雷达下方"

        #             nivo.Radar(
        #                     data=data_leida,
        #                     keys=[ "chardonay", "carmenere", "syrah" ],
        #                     indexBy="taste",
        #                     valueFormat=">-.2f",
        #                     margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
        #                     borderColor={ "from": "color" },
        #                     gridLabelOffset=36,
        #                     dotSize=10,
        #                     dotColor={ "theme": "background" },
        #                     dotBorderWidth=2,
        #                     motionConfig="wobbly",
        #                     legends=[
        #                         {
        #                             "anchor": "top-left",
        #                             "direction": "column",
        #                             "translateX": -50,
        #                             "translateY": -40,
        #                             "itemWidth": 80,
        #                             "itemHeight": 20,
        #                             "itemTextColor": "#999",
        #                             "symbolSize": 12,
        #                             "symbolShape": "circle",
        #                             "effects": [
        #                                 {
        #                                     "on": "hover",
        #                                     "style": {
        #                                         "itemTextColor": "#000"
        #                                     }
        #                                 }
        #                             ]
        #                         }
        #                     ],
        #                     theme={
        #                         "background": "#00cccc",
        #                         "textColor": "white",
        #                         "tooltip": {
        #                             "container": {
        #                                 "background": "#FFFFFF",
        #                                 "color": "#31333F",
        #                             }
        #                         }
        #                     }
        #                 )

        # with mui.Card(key="pie-chart", sx={"color": 'white', 'bgcolor': 'success.main', "display": "flex", 'borderRadius': 2,  "flexDirection": "column"}):
        #         mui.CardHeader(title="pie-chart", className="draggable")
        #         with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
        #             data_bingtu = "see-code-below"

        #             nivo.Pie(
        #                     data=data_bingtu,
        #                     margin={"top": 40, "right": 80, "bottom": 80, "left": 80 },
        #                     innerRadius={0.5},
        #                     cornerRadius={6},
        #                     padAngle={0.7},
        #                     activeOuterRadiusOffset={8},
        #                     borderWidth={1},
        #                     borderColor={
        #                         "from": 'color',
        #                         "modifiers": [
        #                             [
        #                                 'darker',
        #                                 0.2
        #                             ]
        #                         ]
        #                     },
        #                     arcLinkLabelsSkipAngle={10},
        #                     arcLinkLabelsTextColor="#333333",
        #                     arcLinkLabelsThickness={2},
        #                     arcLinkLabelsColor={"from": 'color' },
        #                     arcLabelsSkipAngle={10},
        #                     arcLabelsTextColor={
        #                         "from": 'color',
        #                         "modifiers": [
        #                             [
        #                                 'darker',
        #                                 2
        #                             ]
        #                         ]
        #                     },
        #                     legends=[
        #                         {
        #                             "anchor": "top-left",
        #                             "direction": "column",
        #                             "translateX": -50,
        #                             "translateY": -40,
        #                             "itemWidth": 80,
        #                             "itemHeight": 20,
        #                             "itemTextColor": "#999",
        #                             "symbolSize": 12,
        #                             "symbolShape": "circle",
        #                             "effects": [
        #                                 {
        #                                     "on": "hover",
        #                                     "style": {
        #                                         "itemTextColor": "#000"
        #                                     }
        #                                 }
        #                             ]
        #                         }
        #                     ],
        #                     theme={
        #                         "background": "#00cccc",
        #                         "textColor": "white",
        #                         "tooltip": {
        #                             "container": {
        #                                 "background": "#FFFFFF",
        #                                 "color": "#31333F",
        #                             }
        #                         }
        #                     }
        #                 )

        # with mui.Card(key="area-map", sx={"color": 'white', 'bgcolor': 'success.main', "display": "flex", 'borderRadius': 2,  "flexDirection": "column"}):
        #         mui.CardHeader(title="area-map", className="draggable")
        #         with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
        #             data_area = "see-code-below"

        #             nivo.Stream(
        #                     data = data_area,
        #                     keys=[
        #                         'Raoul',
        #                         'Josiane',
        #                         'Marcel',
        #                         'René',
        #                         'Paul',
        #                         'Jacques'
        #                     ],
        #                     margin={ "top": 50, "right": 110, "bottom": 50, "left": 60 },
        #                     axisTop={"null"},
        #                     axisBottom={
        #                         "orient": 'bottom',
        #                         "tickSize": 5,
        #                         "tickPadding": 5,
        #                         "tickRotation": 0,
        #                         "legend": '',
        #                         "legendOffset": 36
        #                     },
        #                     axisLeft={
        #                         "orient": 'left',
        #                         "tickSize": 5,
        #                         "tickPadding": 5,
        #                         "tickRotation": 0,
        #                         "legend": '',
        #                         "legendOffset": -40
        #                     },
        #                     enableGridX={"true"},
        #                     enableGridY={"false"},
        #                     offsetType="silhouette",
        #                     colors={ "scheme": 'nivo' },
        #                     fillOpacity={0.85},
        #                     borderColor={ "theme": 'background' },
        #                     defs=[
        #                         {
        #                             "id": 'dots',
        #                             "type": 'patternDots',
        #                             "background": 'inherit',
        #                             "color": '#2c998f',
        #                             "size": 4,
        #                             "padding": 2,
        #                             "stagger": "true"
        #                         },
        #                         {
        #                             "id": 'squares',
        #                             "type": 'patternSquares',
        #                             "background": 'inherit',
        #                             "color": '#e4c912',
        #                             "size": 6,
        #                             "padding": 2,
        #                             "stagger": "true"
        #                         }
        #                     ],
        #                     fill=[
        #                         {
        #                             "match": {
        #                                 "id": 'Paul'
        #                             },
        #                             "id": 'dots'
        #                         },
        #                         {
        #                             "match": {
        #                                 "id": 'Marcel'
        #                             },
        #                             "id": 'squares'
        #                         }
        #                     ],
        #                     dotSize={8},
        #                     dotColor={ "from": 'color' },
        #                     dotBorderWidth={2},
        #                     dotBorderColor={
        #                         "from": 'color',
        #                         "modifiers": [
        #                             [
        #                                 'darker',
        #                                 0.7
        #                             ]
        #                         ]
        #                     },
        #                     legends=[
        #                         {
        #                             "anchor": 'bottom-right',
        #                             "direction": 'column',
        #                             "translateX": 100,
        #                             "itemWidth": 80,
        #                             "itemHeight": 20,
        #                             "itemTextColor": '#999999',
        #                             "symbolSize": 12,
        #                             "symbolShape": 'circle',
        #                             "effects": [
        #                                 {
        #                                     "on": 'hover',
        #                                     "style": {
        #                                         "itemTextColor": '#000000'
        #                                     }
        #                                 }
        #                             ]
        #                         }
        #                     ],
        #                     theme={
        #                         "background": "#00cccc",
        #                         "textColor": "white",
        #                         "tooltip": {
        #                             "container": {
        #                                 "background": "#FFFFFF",
        #                                 "color": "#31333F",
        #                             }
        #                         }
        #                     }
        #                 )

        # with mui.Card(key="Funnel-chart", sx={"color": 'white', 'bgcolor': 'success.main', 'borderRadius': 2, "display": "flex", "flexDirection": "column"}):
        #         mui.CardHeader(title="Funnel-chart", className="draggable")
        #         with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
        #             data_loudou = "see-code-below"
        #             nivo.Funnel(
        #                     data = data_loudou,
        #                     margin={"top": 20, "right": 20, "bottom": 20, "left": 20},
        #                     valueFormat = ">-.4s",
        #                     colors = {"scheme": 'spectral'},
        #                     borderWidth = {20},
        #                     labelColor = {
        #                     "from": 'color',
        #                           "modifiers": [
        #                         [
        #                             'darker',
        #                             3
        #                         ]
        #                     ]
        #                     },
        #                     theme={
        #                         "background": "#00cccc",
        #                         "textColor": "white",
        #                         "tooltip": {
        #                             "container": {
        #                                 "background": "#FFFFFF",
        #                                 "color": "#31333F",
        #                             }
        #                         }
        #                     }
        #                 )