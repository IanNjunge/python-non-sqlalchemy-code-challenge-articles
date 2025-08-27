class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 50): raise TypeError("name must be a string between 1 and 50 characters")
        self._name = name
        
    @property   
    def name(self):
        return self._name
    
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property  
    def name(self):
        return self._name 
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise TypeError("name must be a string between 2 and 16 characters")
        self._name = value
               
    @property
    def category(self):
        return self._category    
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or not value.strip():
            raise TypeError("category must be a non-empty string")
        self._category = value
        

class Article:
    all = [] #store every article created
    
    def __init__(self, author, magazine, title):
        self._author = author  #private attributes
        self._magazine = magazine
        

        if not isinstance(title, str)or not(5 <=len(title) <= 50): raise TypeError("title must be a string between 5 to 50 characters")
        self._title = title
        
        Article.all.append(self)    
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author): raise TypeError("author must be an instance of Author")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine): raise TypeError("magazine must be an instance of Magazine")
        self._magazine = value
         
    @property
    def title(self):
        return self._title
    

    

            
            
        
              