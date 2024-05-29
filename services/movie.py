from models.movies import Movie as MovieModel

class MovieService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movies_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    

    def create_movie(self, movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()

        return
    
    def update_movie(self, id, movie):
        movie_update = self.db.query(MovieModel).filter(MovieModel.id == id).update(movie.dict())
        self.db.commit()
        return movie_update
    
    def delete_movie(self, id):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        self.db.delete(movie)
        self.db.commit()
        return
    

