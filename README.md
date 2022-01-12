[Contributors](https://img.shields.io/github/contributors/Gbolahan-Aziz/Covid_19-?logoColor=green&style=plastic)
# Covid_19 Detector

![alt text](https://media.premiumtimesng.com/wp-content/files/2021/11/Coronavirus-used-to-tell-the-story.jpg)

This project is inspired by the ongoing number of covid_19 cases worldwide. In Nigeria it has been reported that some patient were wrongly Quarantined because they inhabited covid sypmtoms,
whereas they had common cold or pnemonia. This prompt me to build a Computer Vision project that easily distinguishes between a patient with Covid and a patient with Pnemonia from a pateint with neither of the two.
This would help doctors be more efficient in treating their patients.
The project was developed as a webapp and deploy on [Heroku](https://covid19--detector.herokuapp.com/) , the webapp takes in web URL as input and returns the class of the image as well as downloading the image on that URL.

## How to Install and Run the Project
Steps to install this project include :
- Clone the github repository by running `git clone https://github.com/Gbolahan-Aziz/Covid_19-.git`
- Create and activate a virtual environment on your local machine
- Using your terminal and in your virtual environment, install all the dependencies in the requirement.txt file by running

  `pip install -r requirements.txt`
- After installing all requirements, you should be able to run `streamlit run app.py`, successfully.
- This should automatically redirect you to your default browser. If it doesn't, simply copy and open the Local URL on your terminal to your browser.

## Built With
- [Tensorflow](https://www.tensorflow.org/)
- [Numpy](https://numpy.org)
- [Pillow](https://pillow.readthedocs.io/)
- [Requests](https://docs.python-requests.org/)
- [IO](https://docs.python.org/3/library/io.html)
- [Streamlit](https://streamlit.io/)
