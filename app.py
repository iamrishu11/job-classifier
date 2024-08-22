import numpy as np
import streamlit as st
import pickle

#Load the model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

#Function for classifier
