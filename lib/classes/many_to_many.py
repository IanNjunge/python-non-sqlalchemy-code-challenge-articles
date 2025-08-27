class Article:
    all = [] #store every article created
    
    def __init__(self, author, magazine, title):
        from author import Author
        from magazine import Magazine
        
        
        if not isinstance(author, Author): raise TypeError("author must be an instance of Author class")
        if not isinstance(magazine, Magazine): raise TypeError("magazine must be an instance of Magazine class")
        if not isinstance(title, str)or not(5 <=len(title) <= 50): raise TypeError("title must be a string between 5 to 50 characters")
          
         #private attributes   
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)    
        
    @property
    def author(self):
        return self._author
    
    @property
    def magazine(self):
        return self._magazine
         
    @property
    def title(self):
        return self._title
    
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 50): raise TypeError("name must be a string between 1 and 50 characters")
        self._name = name
    
    @property   
    def name(self):
        return self._name
    
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise TypeError("name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or not category.strip():
            raise TypeError("category must be a non-empty string")
        self._name = name
        self._category = category
        
    @property
    def name(self):
        return self._name        
            
    @property
    def category(self):
        return self._category
            
            
        
              