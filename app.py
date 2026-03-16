import streamlit as st
st.title("Library")
if "books" not in st.session_state:
  st.session_state.books = []
title = st.text_input("book title")
author = st.text_input("book author")
price = st.number_input("book price", min_value = 0.0)
if st.button("Add the book"):
  book = {
    'title': title,
    "author": author,
    "price": price
  }
  st.session_state.books.append(book)
st.success("The book has been added!")
if st.button("Show all books"):
  if len(st.session_state.books) == 0:
    st.write("There aren't any added books")
  else:
    for book in st.session_state.books:
      st.write("title", book["title"])
      st.write("author", book["author"])
      st.write("price", book["price"])
      st.write("--------------------")
search_author = st.text_input("Enter the author's name")
if st.button("search author"):
  found = False
  for book in st.session_state.books:
    if book["author"] == search_author:
      st.write(book)
      found = True
    if found == False:
      st.write("The author isn't found")
search_title = st.text_input("Enter the book's title")
if st.button("search title"):
  found = False
  for book in st.session_state.books:
    if book["title"] == search_title:
      st.write(book)
      found = True
    if found == False:
      st.write("The title isn't found")
if st.button("Show the cheapest book"):
  if len(st.session_state.books) == 0:
    st.write("There isn't a book")
  else:
    cheapest = st.session_state.books[]
    for book in st.session_state.books:
      if book["price"]<cheapest["price"]:
        cheapest = book
        st.write("The cheapest book is")
        st.write(cheapest)
