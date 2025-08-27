class Article:
    all = [] #store every article created
    
    def __init__(self, author, magazine, title):
        from author import Author
        from magazine import Magazine
        
        if not isinstance(author, Author): raise TypeError("author must be an instance of Author class")
        if not isinstance(magazine, Magazine): raise TypeError("magazine must be an instance of Magazine class")
        if not isinstance(title, str)or not(5 <=len(title) <= 50): raise TypeError("title must be a string of 5 to 50 characters")
            
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
              