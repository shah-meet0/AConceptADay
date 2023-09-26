import streamlit as st
import os
from utilities import parse_post
st.set_page_config(page_title="A Concept a Day")


@st.cache_data
def parse_all_posts():
    categories = {'All': {}}  # Dictionary: String, Dictionary
    posts = os.listdir('./posts')
    for post in posts:
        temp_post = parse_post('./posts/' + post)
        if temp_post.category.title() in categories.keys():
            post_dict = categories.get(temp_post.category.title())
            post_dict[temp_post.title.title()] = temp_post
            categories['All'][temp_post.title.title()] = temp_post
        else:
            categories[temp_post.category.title()] = {temp_post.title.title(): temp_post}
            categories['All'][temp_post.title.title()] = temp_post
    return categories

# ******************************************START OF APP******************************************************


# Post Import Space
category_selection = parse_all_posts()


# Sidebar
category_selected = st.sidebar.selectbox(label='Topic', options=category_selection.keys())
post_selected = st.sidebar.selectbox(label='Posts', options=category_selection[category_selected])

show_title = st.sidebar.checkbox('Show Title', value=True)

# Main Page

# Title Space
if show_title:
    st.title('A Concept a Day')
    st.write('By Meet Shah')


st.write(category_selection[category_selected][post_selected].__str__())

