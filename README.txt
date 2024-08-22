
# mylifts

**mylifts** is a Django-based web application designed for fitness enthusiasts to create accounts, share their lifting records, follow other users, and stay updated with posts from their network. The project features full CRUD functionalities, user authentication, a following system, and a dynamically updated user feed.

## Features

- **User Authentication**: Register, log in, and manage your profile.
- **CRUD Operations**: Create, read, update, and delete posts, comments, and lifting records.
- **Follow System**: Follow other users and get notified about their latest posts.
- **User Feed**: A dynamic feed that updates at a fixed interval to show the latest posts from followed users.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/mylifts.git
   cd mylifts
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Register an Account**: Click on "Register" and fill in the required details to create a new account.
- **Log In**: Use your credentials to log in and access your dashboard.
- **Create Posts and Records**: Share your lifting records and thoughts with the community.
- **Follow Users**: Discover and follow other users to stay updated on their activities.
- **View User Feed**: Check your feed to see the latest posts from the users you follow.

## Project Structure

```
C:.
├───API
├───authentication
│   ├───migrations
│   ├───templates
├───feed
│   ├───migrations
│   ├───templates
├───jobs
├───lifters
│   ├───migrations
│   ├───templates
├───main
│   ├───migrations
├───media
│   ├───comment_default_profile_images
│   └───images
├───my_lifts
├───pages
│   ├───migrations
├───records
│   ├───migrations
│   ├───templates
├───static
├───templates
└───__pycache__
```

- **authentication**: Manages user authentication and registration.
- **feed**: Handles the user feed and the display of posts from followed users.
- **jobs**: Contains background jobs (if any).
- **lifters**: Manages the core functionalities related to user profiles and their lifting records.
- **media**: Stores media files such as images and videos.
- **my_lifts**: Contains project settings and configurations.
- **pages**: Manages static pages.
- **records**: Handles the CRUD operations for lifting records.
- **static**: Contains static files like CSS, JavaScript, and images.
- **templates**: Stores HTML templates used across the app.

## Technologies Used

- **Django**: Python web framework.
- **Python**: Backend programming language.
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For dynamic content.
- **Bootstrap**: Frontend framework for responsive design.

## License

This project is currently unlicensed. You may choose to apply a license if you wish to make it open-source or restrict usage.
