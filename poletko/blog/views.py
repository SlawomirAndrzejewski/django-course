from django.shortcuts import render
from datetime import date

all_posts = [
    {
        'slug': 'my-traveling',
        'image': 'traveler.jpg',
        'author': 'Sławomir',
        'date': date(2021, 7, 14),
        'title': 'My travels',
        'excerpt': 'There is nothing like travelinguuss!',
        'content': '''
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste quod recusandae nobis vitae vero ducimus pariatur at facilis officiis, 
            deleniti culpa mollitia tenetur maxime officia magni animi sed? Delectus, tenetur!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste quod recusandae nobis vitae vero ducimus pariatur at facilis officiis, 
            deleniti culpa mollitia tenetur maxime officia magni animi sed? Delectus, tenetur!
        '''
    },
    {
        'slug': 'my-vegies',
        'image': 'traveler.jpg',
        'author': 'Sławomir',
        'date': date(2021, 7, 14),
        'title': 'My vegies',
        'excerpt': 'There is nothing like traveling!',
        'content': '''
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste quod recusandae nobis vitae vero ducimus pariatur at facilis officiis, 
            deleniti culpa mollitia tenetur maxime officia magni animi sed? Delectus, tenetur!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste quod recusandae nobis vitae vero ducimus pariatur at facilis officiis, 
            deleniti culpa mollitia tenetur maxime officia magni animi sed? Delectus, tenetur!
        '''
    },
    {
        'slug': 'my-money',
        'image': 'traveler.jpg',
        'author': 'Sławomir',
        'date': date(2021, 7, 14),
        'title': 'My money',
        'excerpt': 'There is nothing like traveling!',
        'content': '''
            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste quod recusandae nobis vitae vero ducimus pariatur at facilis officiis, 
            deleniti culpa mollitia tenetur maxime officia magni animi sed? Delectus, tenetur!

            Lorem ipsum dolor sit, amet consectetur adipisicing elit. Iste quod recusandae nobis vitae vero ducimus pariatur at facilis officiis, 
            deleniti culpa mollitia tenetur maxime officia magni animi sed? Delectus, tenetur!
        '''
    },
]


def get_date(post):
    return post['date']


def starting_page(request):
    # wybiera trzy ostatnie elementy listy, sprawdź o co chodzi !
    sorted_posts = sorted(all_posts, key=get_date)
    latests_posts = sorted_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latests_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'posts': all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })
