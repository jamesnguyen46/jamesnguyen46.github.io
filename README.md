# jamesnguyen46.github.io

A Github Page for James Nguyen.

## Tech stack

- [Django](https://docs.djangoproject.com/)
- [Pyrebase](https://github.com/thisbejim/Pyrebase)
- [django-distill](https://github.com/meeb/django-distill)

## Dev environment

Create `dev.env` file on root project as below :

```
DJANGO_DEBUG="True"
DJANGO_SECRET_KEY=""
FIREBASE_API_KEY=""
FIREBASE_AUTH_DOMAIN=""
FIREBASE_DATABASE_URL=""
FIREBASE_STORAGE_BUCKET=""
```

## Makefile

- `make` or `make run` : run Django server.
- `make active_env` : create the virtual environment and install the dependencies.
- `make gen` : generate static site to `static` and `docs` folder.
- `make clean` : remove the `static` and `docs` folder.

## Vscode task

- [Debugging](https://code.visualstudio.com/docs/editor/debugging): run `Django: run debug server` event in `Run and debug` view to run Django server and debug code.
- Other [tasks](https://code.visualstudio.com/docs/editor/tasks)
  - `Install development dependencies` task : create the virtual environment and install the dependencies.
  - `Generate static site` task : generate static site to `static` and `docs` folder.
  - `Remove the generated folders` task : remove the `static` and `docs` folder.

## Firebase

This project use realtime database to store the personal information. Firebase database structure as following:

### Page icon

```json
"page_icon": {
    "apple_touch": "",
    "favicon": ""
}
```

### Flags

```json
"flags": {
    "show_about_section": true,
    "show_experience_section": true,
    "show_skills_section": true,
    "show_testimonials_section": true
}
```

### Profile

```json
"profile": {
    "avatar_url": "",
    "hero_background": "",
    "whois": "",
    "favorite_quote": {
        "author": "",
        "quote": ""
    },
    "info": {
        "birthday": "",
        "email": "",
        "first_name": "",
        "last_name": "",
        "vietnamese_name": "",
        "job_title": "",
        "location": "",
    },
    "social_links": {
        "facebook": "",
        "github": "",
        "instagram": "",
        "linkedin": "",
        "skype": "",
        "twitter": "",
    }
}
```

### Experience

```json
"experience": {
    "summary": "",
    "company": {                    // Can create many with the name : "company1", "company2", ...
        "description": "",
        "homepage": "",
        "name": "",
        "location": "",
        "logo": "",
        "job": {                    // Can create many with the name : "job1", "job2", ...
            "title": "",
            "start": 1234567890,    // Timestamp
            "end": 1234567890,      // Timestamp
        }
    }
}
```

### Skills

```json
"skills": {
    "description": "",
    "1_text": {                     // Can create many with the name : "1_text1", "1_text2", ...
        "name": "",
        "str": ""                   // Can create many with the name : "str1", "str2", ...
    },
    "2_progress": {                 // Can create many with the name : "2_progress1", "2_progress2", ...
        "name": "",
        "items": {
            "key": "value"          // Key is skill name, value is progress percent. Example: java:70, kotlin:80
        }
    },
    "3_tag": {                      // Can create many with the name : "3_tag1", "3_tag2", ...
        "name": "",
        "value": ""                  // Comma-separated values. Example : java, kotlin, dart, swift
    }
}

// NOTE
//    - The number in front of "text", "progress", "tag" letter is the display order.
//    - "text", "progress", "tag" are the name of UI style.
```

### Testimonial

```json
"testimonials": {
    "description": "",
    "who": {                        // Can create many with the name : "who1", "who2", ...
        "name": "",
        "avatar": "",
        "job_title": "",
        "quote": ""
    }
}
```




