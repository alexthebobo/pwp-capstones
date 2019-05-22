class User(object):
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books={}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email=address
        print("email has been changed to :" + self.email)

    def __repr__(self):
        return "user : " + self.user + " - email : " + self.email + " - books : " + len(self.books)

    def __eq__(self, other_user):
        if self.name==other_user.name and self.email==other_user.email:return True
        return False
        
    def Read_Book(self,book,rating=None):
        self.books[book]=rating
        
    def get_average_rating(self):
        if len(self.books)==0:return 0
        values = [rating for rating in self.books.values() if rating is not None]
        return sum(values)/len(values)

    
class Book(object):
    
    def __init__(self,title,isbn):
        self.title=title
        self.isbn=isbn
        self.ratings=[]
        
    def __hash__(self):
        return hash((self.title,self.isbn))
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
            return self.isbn
        
    def set_isbn(self,newIsbn):
        self.isbn=newIsbn
        print("isbn was just updated")
    
    def add_rating(self,rating):
        if rating and rating>=0 and rating<=4:
            self.ratings.append(rating)
        else:
            print("Invalid rating")
    
    def __eq__(self,otherbook):
        if self.title==otherbook.title and self.isbn==otherbook.isbn:return True
        return False
    
    def get_average_rating(self):
        if len(self.ratings)==0:return 0
        else:return sum(self.ratings)/len(self.ratings)
        
    def __repr__(self):
        return "{} with ISBN : {}".format(self.title,self.isbn)
    
class Fiction(Book):
    def __init__(self,title,author,isbn):
        Book.__init__(self,title,isbn)
        self.author=author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{} by {}".format(self.title,self.author)
    
class Non_Fiction(Book):
    def __init__(self,title,subject,level,isbn):
        Book.__init__(self,title,isbn)
        self.subject=subject
        self.level=level
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title,self.level,self.subject)
    
class TomeRater():
    def __init__(self):
        self.users={}
        self.books={}
    
    def create_book(self,title,isbn):
        return Book(title,isbn)
    
    def create_novel(self,title,isbn,author):
        return Fiction(title,isbn,author)
    
    def create_non_fiction(self,title,isbn,subject,level):
        return Non_Fiction(title,isbn,subject,level)
    
    def add_book_to_user(self,book,email,rating=None):
        if email not in self.users:print("No user with this email "+email)
        else:
            self.users[email].Read_Book(book,rating)
            book.add_rating(rating)
            if book in self.books:self.books[book]+=1
            else:self.books[book]=1
            
    def add_user(self,name,email,user_books=None):
        self.users[email]=User(name,email)
        if user_books!=None:
            for uBook in user_books:
                self.add_book_to_user(uBook,email)
    
    def print_catalog(self):
        for b in self.books:print(b)
    
    def print_users(self):
        for u in self.users:print(u)

    def most_read_book(self):
        x=[0,0]
        for b,v in self.books.items():
            if v>=x[1]:
                x[0]=b
                x[1]=v
        return x[0]
    
    def highest_rated_book(self):
        x=[0,0]
        for b in self.books:
            if b.get_average_rating()>=x[1]:
                x[0]=b
                x[1]=b.get_average_rating()
        return x[0]
    
    def most_positive_user(self):
        x=[0,0]       
        for u,v in self.users.items():
            if v.get_average_rating()>=x[1]:
                x[0]=u
                x[1]=v.get_average_rating()
        return x[0]
    
    
            
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            