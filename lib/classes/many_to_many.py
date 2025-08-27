class Author:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 50): 
            raise TypeError("name must be a string between 1 and 50 characters")
        self._name = name
        
    @property   
    def name(self):
        return self._name
    
    #Articles by author
    def articles(self):
        return [article for article in Article.all if article.author is self]
    
    #Magazines author is a part of
    @property
    def magazines(self):
        return list({article.magazine for article in self.articles()})
    
    #new article for author
    def add_articles(self, magazine, title):
        return Article(self, magazine, title)
    
    #topics author wrote about
    def topic_areas(self):
        return list({article.magazine.category for article in self.articles()})
    
    
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
        
    #all the articles in magazine   
    def articles(self):
        return [article for article in Article.all if article.magazine is self]
    
    #titles of all articles of magazine
    def article_titles(self):
        return [article.title for article in self.articles()]
    
    #authors of magazine
    def contributors(self):
        return list ({article.author for article in self.articles()})
    
    #authors of more than 2 articles
    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
    
    
class Article:
    #stores every article
    all = [] 
    
    def __init__(self, author, magazine, title):
        if not isinstance(title, str)or not(5 <=len(title) <= 50): 
            raise TypeError("title must be a string between 5 to 50 characters")
        if not isinstance(magazine, Magazine): 
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str) or not (5 <= len(title) <=50): 
            raise TypeError("title must be string between 5 and 50 characters")
        
        #private attributes
        self._title = title
        self._author = author  
        self._magazine = magazine
        
        Article.all.append(self)    
        
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an instance of Author")
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine): 
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine = value
        
    @property
    def title(self):
        return self._title
    

    

            
            
        
              