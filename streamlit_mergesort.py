# streamlit_merge_sort.py

import streamlit as st
from mergesort import merge_sort

# Set up the Streamlit app
st.title('Merge Sort Visualization')

# Input field for user to input numbers
input_numbers = st.text_input('Enter numbers separated by commas (e.g., 5, 2, 9, 1, 5, 6)')

if st.button('Sort'):
    # Convert the input string to a list of integers
    try:
        number_list = list(map(int, input_numbers.split(',')))

        # Call the merge sort function
        sorted_list = merge_sort(number_list)

        # Display the sorted list
        st.write(f'Sorted List: {sorted_list}')
    except ValueError:
        st.error('Please enter a valid list of integers separated by commas.')