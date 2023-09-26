import streamlit as st
import os
from utilities import parse_post


@st.cache_data
def parse_posts():
    categories = {'All': {}}  # Dictionary: String, Dictionary
    posts = os.listdir('./posts')
    for post in posts:
        with open(f'./posts/{post}', 'rb') as f:
            temp_post = parse_post(f)
            if temp_post.category.title() in categories.keys():
                post_dict = categories.get(temp_post.category.title())
                post_dict[temp_post.title.title()] = temp_post
                categories['All'][temp_post.title.title()] = temp_post
            else:
                categories[temp_post.category.title()] = {temp_post.title.title(): temp_post}
                categories['All'][temp_post.title.title()] = temp_post
    return categories


# ******************************************START OF APP******************************************************

# Title Space

st.title('A Concept a Day')
st.subheader('By Meet Shah')

# Post Import Space
category_selection = parse_posts()


# Sidebar
category = st.sidebar.selectbox(label='Topic', options=category_selection.keys())
post_selection = st.sidebar.selectbox(label='Posts', options=category_selection[category])
