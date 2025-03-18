import streamlit as st
import pandas as pd

# Initialize session state for books if not already present
if 'books' not in st.session_state:
    st.session_state.books = []

# App title
st.title("📚 Library Manager")

# Sidebar for adding new books
st.sidebar.header("Add New Book")
title = st.sidebar.text_input("Title")
author = st.sidebar.text_input("Author")
genre = st.sidebar.text_input("Genre")
availability = st.sidebar.selectbox("Availability", ["Available", "Borrowed"])
status = st.sidebar.selectbox("Status", ["Read", "Unread"])

if st.sidebar.button("Add Book"):
    if title and author and genre:
        st.session_state.books.append({
            "Title": title,
            "Author": author,
            "Genre": genre,
            "Availability": availability,
            "Status": status
        })
        st.sidebar.success("Book added successfully!")
    else:
        st.sidebar.error("Please fill in all fields")

# Display books in a table
st.subheader("📖 Book List")
if st.session_state.books:
    df = pd.DataFrame(st.session_state.books)
    st.dataframe(df)
else:
    st.write("No books available. Add some!")

# Search functionality
st.subheader("🔍 Search Books")
search_query = st.text_input("Search by title, author, or genre")

if search_query:
    filtered_books = [book for book in st.session_state.books if search_query.lower() in book["Title"].lower() or search_query.lower() in book["Author"].lower() or search_query.lower() in book["Genre"].lower()]
    if filtered_books:
        st.dataframe(pd.DataFrame(filtered_books))
    else:
        st.warning("No matching books found.")

# Advanced Feature: Book Deletion
st.subheader("🗑️ Delete a Book")
delete_title = st.text_input("Enter book title to delete")
if st.button("Delete Book"):
    st.session_state.books = [book for book in st.session_state.books if book["Title"].lower() != delete_title.lower()]
    st.success("Book deleted successfully!")

# Advanced Feature: Update Book Status
st.subheader("📌 Update Book Status")
update_title = st.text_input("Enter book title to update status")
new_status = st.selectbox("Select new status", ["Read", "Unread"])
if st.button("Update Status"):
    for book in st.session_state.books:
        if book["Title"].lower() == update_title.lower():
            book["Status"] = new_status
    st.success("Book status updated successfully!")

