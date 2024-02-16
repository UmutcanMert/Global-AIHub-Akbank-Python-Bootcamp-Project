from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

class LibraryApp(App):
    def build(self):
        self.lib = Library()
        self.title = 'Library Management System'
        Window.clearcolor = (240/255, 240/255, 240/255, 0)
        self.layout = BoxLayout(orientation='vertical')
        self.show_login_popup()
        
        return self.layout

    def show_login_popup(self):
        layout = BoxLayout(orientation='vertical')
        self.username_input = TextInput(hint_text='Enter your username',multiline=False)
        layout.add_widget(self.username_input)
        
        self.password_input = TextInput(hint_text='Enter your password', password=True,multiline=False)
        layout.add_widget(self.password_input)
        
        login_btn = Button(text='Login', background_color=(0.5, 0.5, 0.5, 1))
        login_btn.bind(on_press=self.login)
        
        layout.add_widget(login_btn)
        popup = Popup(title='Login', content=layout, size_hint=(0.6, 0.6))
        popup.open()

    def login(self, instance):
        username = self.username_input.text.strip()
        password = self.password_input.text.strip()
        if username == 'admin' and password == 'admin123':
            self.layout.clear_widgets()
            self.add_menu_widgets(username)
        else:
            error_popup = Popup(title='Error', content=Label(text='Invalid username or password!'), size_hint=(None, None), size=(400, 200))
            error_popup.open()

    def add_menu_widgets(self, name):
        self.name_label = Label(text=f'Welcome, {name}!', color=(0, 0, 0, 1), font_size='20sp', bold=True, italic=True)
        self.layout.add_widget(self.name_label)
        list_books_btn = Button(text='List Books', background_color=(0.5, 0.5, 0.5, 1))
        list_books_btn.bind(on_press=self.list_books)
        self.layout.add_widget(list_books_btn)
        add_book_btn = Button(text='Add Book', background_color=(0.5, 0.5, 0.5, 1))
        add_book_btn.bind(on_press=self.add_book)
        self.layout.add_widget(add_book_btn)
        remove_book_btn = Button(text='Remove Book', background_color=(0.5, 0.5, 0.5, 1))
        remove_book_btn.bind(on_press=self.remove_book)
        self.layout.add_widget(remove_book_btn)
        exit_btn = Button(text='Exit', background_color=(0.5, 0.5, 0.5, 1))
        exit_btn.bind(on_press=self.stop)
        self.layout.add_widget(exit_btn)

    def list_books(self, instance):
        content = GridLayout(cols=5, spacing=10, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))

        books_info = self.lib.list_books_text()
        if books_info:
            for book_info in books_info.split('\n'):
                book_data = book_info.split(', ')
                for data in book_data:
                    label = Label(text=data, size_hint_y=None, height=40)
                    content.add_widget(label)

        popup = Popup(title='List of Books', content=content, size_hint=(0.9, 0.9))
        popup.open()


    def add_book(self, instance):
        layout = BoxLayout(orientation='vertical')
        self.book_title = TextInput(hint_text='Book Title')
        layout.add_widget(self.book_title)
        self.author_name = TextInput(hint_text="Author's Name")
        layout.add_widget(self.author_name)
        self.release_year = TextInput(hint_text='Release Year')
        layout.add_widget(self.release_year)
        self.num_pages = TextInput(hint_text='Number of Pages')
        layout.add_widget(self.num_pages)
        self.quantity_input = TextInput(hint_text='Quantity')  # Yeni eklendi
        layout.add_widget(self.quantity_input)  # Yeni eklendi
        add_btn = Button(text='Add')
        add_btn.bind(on_press=self.add_book_to_library)
        layout.add_widget(add_btn)
        popup = Popup(title='Add Book', content=layout, size_hint=(0.6, 0.6))
        popup.open()

    def add_book_to_library(self, instance):
        book_title = self.book_title.text.strip()
        author_name = self.author_name.text.strip()
        release_year = self.release_year.text.strip()
        num_pages = self.num_pages.text.strip()
        quantity = self.quantity_input.text.strip()

        if not book_title or not author_name or book_title.isdigit() or author_name.isdigit():
            error_popup = Popup(title='Error', content=Label(text='Please enter book title and author!'), size_hint=(None, None), size=(400, 200))
            error_popup.open()
        elif not release_year.isdigit() or not num_pages.isdigit() or not quantity.isdigit():
            error_popup = Popup(title='Error', content=Label(text='Release year, number of pages, and quantity must be numeric!'), size_hint=(None, None), size=(400, 200))
            error_popup.open()
        else:
            book_added = self.lib.add_book(book_title, author_name, release_year, num_pages, quantity)
            if book_added:
                success_popup = Popup(title='Success', content=Label(text='Book added successfully!'), size_hint=(None, None), size=(400, 200))
                success_popup.open()
            else:
                self.lib.update_quantity(book_title, int(quantity))
                success_popup = Popup(title='Success', content=Label(text='Quantity updated successfully!'), size_hint=(None, None), size=(400, 200))
                success_popup.open()

    def remove_book(self, instance):
        layout = BoxLayout(orientation='vertical')
        self.title_to_remove = TextInput(hint_text='Title of the book to remove')
        layout.add_widget(self.title_to_remove)
        remove_btn = Button(text='Remove')
        remove_btn.bind(on_press=self.remove_book_from_library)
        layout.add_widget(remove_btn)
        popup = Popup(title='Remove Book', content=layout, size_hint=(0.6, 0.6))
        popup.open()

    def remove_book_from_library(self, instance):
        title_to_remove = self.title_to_remove.text.strip()
        
        if title_to_remove !="":
            removed = self.lib.remove_book(title_to_remove)
            if removed:
                popup = Popup(title='Success', content=Label(text=f"Book '{title_to_remove}' removed successfully!"), size_hint=(None, None), size=(400, 200))
            else:
                popup = Popup(title='Error', content=Label(text=f"Book '{title_to_remove}' not found!"), size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
            popup = Popup(title='Error', content=Label(text=f"Title cannot be empty!"), size_hint=(None, None), size=(400, 200))
            popup.open()

class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        try:
            self.file = open(self.file_name, "a+")
        except Exception as e:
            print(f"Error: {e}")

    def __del__(self):
        self.file.close()

    def list_books_text(self):
        self.file.seek(0)
        lines = self.file.readlines()
        if not lines:
            return "No books available."
        else:
            books_text = ""
            for line in reversed(lines):  # Satırları tersine çevirerek en son eklenenin en üstte görünmesini sağlayın
                book_info = line.strip().split(',')
                book_name, author, release_date, num_pages, quantity = book_info
                books_text += f"Book: {book_name}, Author: {author}, Release Date: {release_date}, Number of Pages: {num_pages}, Quantity: {quantity}\n"
            return books_text
    
    def add_book(self, book_name, author, release_date, num_pages,quantity):
        book_info = f"{book_name},{author},{release_date},{num_pages},{quantity}\n"
        self.file.write(book_info)
        
    def remove_book(self, title_to_remove):
        self.file.seek(0)
        lines = self.file.readlines()
        self.file.seek(0)
        books_to_keep = []
        removed = False
        for line in lines:
            if title_to_remove in line:
                book_info = line.strip().split(',')
                if int(book_info[4]) > 1:
                    # Miktar 1'den fazlaysa bir azaltma yap
                    book_info[4] = str(int(book_info[4]) - 1)
                    new_line = ','.join(book_info) + '\n'
                    books_to_keep.append(new_line)
                else:
                    removed = True
            else:
                books_to_keep.append(line)
        self.file.truncate(0)
        self.file.seek(0)
        self.file.writelines(books_to_keep)
        return removed

    def update_quantity(self, book_name, increment):
        self.file.seek(0)
        lines = self.file.readlines()
        updated_lines = []
        found = False
        for line in lines:
            book_info = line.strip().split(',')
            if book_name == book_info[0]:
                new_quantity = int(book_info[4]) + increment
                if new_quantity < 0:
                    new_quantity = 0
                book_info[4] = str(new_quantity)
                line = ','.join(book_info) + '\n'
                found = True
            updated_lines.append(line)

        # Mevcut satırları güncellenmiş satırlarla birleştir ve dosyaya yaz
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_lines)
        
if __name__ == '__main__':
    LibraryApp().run()
