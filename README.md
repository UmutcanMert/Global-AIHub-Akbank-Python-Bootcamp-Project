##### Bu proje Global AI Hub Akbank Python Bootcamp kapsamında hazırlanmıştır. İstenilen temel özellikler aşağı belirtilmiştir.
##### Ek olarak;
##### GUI kullananarak ,kivy ile bir arayüz tasarlanmıştır. 
##### Validation kontrolleri yapılmıştır.   
##### Quantity özelliği eklenmiştir.
##### Proje ile ilgili resimler aşağıda belirtilmiştir.

<br>

#### Library Management System
In this project you will be building “Library Management System” using object-oriented 
programming techniques. This program will use books.txt file that you will create as a database 
where each line will represent a single book. At each line, book name, author, release date 
and number of pages will be kept and separated with a comma.
1. Create a class named “Library”:
a. Create the constructer method to open the books.txt file, and destructor 
method to close the file.
Tip: If you open books.txt with “a+” mode, you can both read and append lines 
to the file. And also, if books.txt is not created previously, this mode will create 
the file.
2. Add the following methods to library:
a. List Books
This method will list all the books in the books.txt file.
i. Read the contents of the file.
ii. Add each line to a list using splitlines() method of the string object.
iii. Now each element of the list holds information about a single book. 
Print book names and authors using this information.
b. Add Book
This method will add a book to a books.txt file.
i. Ask user input for book title, book author, first release year and number 
of pages
ii. Create a string with this information. Add book title then comma then 
author then comma etc.
iii. Append this line to the file.
c. Remove Book
This method will delete the book with the given title from the books.txt.
i. Ask the user input for book title.
ii. Read the file contents and add book to a list (just like you did while 
creating a list books method).
iii. Find the index of the book to be deleted in the list.
iv. Remove the book from the list.
v. Remove the contents of the books.txt.
vi. Add all elements of the list to the books.txt.
2
* With this method you remove contents of the books.txt and rewrite 
the new list. If you don’t remove the contents, it will add the same 
books again to the file.
3. Create an object named “lib” with “Library” class.
4. Create a menu to interact with the “lib” object.
a. Print the following to the screen
*** MENU***
1) List Books
2) Add Book
3) Remove Book
b. Ask user input for menu item and assign the input to a variable.
c. Using if-elif-else statement check the user input.
d. According to the user input, run the relevant method of the “lib” object
