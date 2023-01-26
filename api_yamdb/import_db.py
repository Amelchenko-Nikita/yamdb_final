import csv
import os

from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title, User)

path = "api_yamdb/static/data/"
os.chdir(path)


with open('category.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Category(
            id=row['id'],
            name=row['name'],
            slug=row['slug']
        )
        p.save()


with open('comments.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Comment(
            id=row['id'],
            review=Review.objects.get(id=row['review_id']),
            text=row['text'],
            author=User.objects.get(id=row['author']),
            pub_date=row['pub_date']
        )
        p.save()


with open('genre_title.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = GenreTitle(
            id=row['id'],
            title=Title.objects.get(id=row['title_id']),
            genre=Genre.objects.get(id=row['genre_id'])
        )
        p.save()


with open('genre.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Genre(
            id=row['id'],
            name=row['name'],
            slug=row['slug']
        )
        p.save()


with open('review.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Review(
            id=row['id'],
            title=Title.objects.get(id=row['title_id']),
            text=row['text'], author=User.objects.get(id=row['author']),
            score=row['score'], pub_date=row['pub_date']
        )
        p.save()


with open('titles.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Title(
            id=row['id'],
            name=row['name'],
            year=row['year'],
            category=Category.objects.get(id=row['category'])
        )
        p.save()


with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = User(
            id=row['id'],
            username=row['username'],
            email=row['email'],
            role=row['role'],
            bio=row['bio'],
            first_name=row['first_name'],
            last_name=row['last_name']
        )
        p.save()
