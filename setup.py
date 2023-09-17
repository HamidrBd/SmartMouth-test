import setuptools

setuptools.setup(
    name="SmartMouth by Fartak",
    version="0.0.1",
    author="Hamidreza Badr",
    author_email="hamidrezabadr.w@gmail.com",
    description="",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63", "folium>=0.13",
    ],
)

