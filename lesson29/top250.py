#!/Users/valeria/src/morning-ninjas/venv/bin/python3

import argparse
import psycopg2


class MoviesModel:

    def __init__(self):
        self._conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='top250movies',
        user='postgres',
        password='postgres')

    # def check_movie_exists(self, movie_name: str) -> bool:
    #     query = f"""
    #     SELECT * FROM imdb_top
    #     WHERE movie_name ilike '{movie_name}'
    #     """
    #     with self._conn:
    #         with self._conn.cursor() as cur:
    #             cur.execute(query)
    #             result = cur.fetchone()
    #     return result is not None


    def check_movie_exists(self, movie_name: str, rating: float) -> bool:
        query = f"""
        SELECT * FROM imdb_top
        WHERE movie_name ilike %s OR rating >= %s
        """
        with self._conn:
            with self._conn.cursor() as cur:
                cur.execute(query, (movie_name, rating))
                result = cur.fetchone()
        return result is not None

    def get_movies_by_rating(self, rating: float) -> list:
        query = f"""
        SELECT * FROM imdb_top
        WHERE rating > {rating}
        """
        with self._conn:
            with self._conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
        return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n')
    parser.add_argument('--rating', '-r', type=float)

    args = parser.parse_args()
    print(args)
    if not args.name and not args.rating:
        print('Error: You have to provide one of --name of --rating')
    elif args.name and args.rating:
        print('Error: You have to provide only one of --name or --rating')
    else:
        model = MoviesModel()
        if args.name:
            result = model.check_movie_exists(args.name)
            if result:
                print(f"The movie {args.name} is among top 250 IMDB movies")
            else:
                print(f"The movie {args.name} is not among top 250 IMDB movies")
        else:
            print(model.get_movies_by_rating(args.rating))


