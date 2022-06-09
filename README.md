# jamesnguyen46.github.io

A Github Page for James Nguyen.

## Library

- [Django](https://docs.djangoproject.com/)
- [Pyrebase](https://github.com/thisbejim/Pyrebase)
- [django-distill](https://github.com/meeb/django-distill)

## Dev environment

Create `dev.env` file on root project as below :

```
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=
FIREBASE_API_KEY=
FIREBASE_AUTH_DOMAIN=
FIREBASE_DATABASE_URL=
FIREBASE_STORAGE_BUCKET=
FIREBASE_PROJECT_ID=
FIREBASE_PRIVATE_KEY_ID=
FIREBASE_PRIVATE_KEY=
FIREBASE_CLIENT_EMAIL=
FIREBASE_CLIENT_ID=
FIREBASE_CLIENT_CERT_URL=
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

### Resources

```json
"resources": {
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
// --------------- NOTE ------------------
//  + Use "extra_info" to show the additional information such as email, location, birthday...
//  + "1" key : can create many with the name : "1", "2", ...]
// ---------------------------------------
"profile": {
    "hero_background": "",
    "favorite_quote": {
        "author": "",
        "quote": ""
    },
    "info": {
        "avatar_url": "",
        "whois": "",
        "first_name": "",
        "last_name": "",
        "job_title": "",
    },
    "extra_info": {
        "1": {
            "css_class": "",
            "name": "",
            "value": ""
        }
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
// --------------- NOTE ------------------
//  + "company" key : can create many with the name : "company1", "company2", ...
//  + "job" key : can create many with the name : "job1", "job2", ...
//  + "start", "end" key : timestamp
// ---------------------------------------
"experience": {
    "summary": "",
    "company": {
        "description": "",
        "homepage": "",
        "name": "",
        "location": "",
        "logo": "",
        "job": {
            "title": "",
            "start": 1234567890,
            "end": 1234567890
        }
    }
}
```

### Skills

```json
// --------------- NOTE ------------------
//  + "1_text" key : can create many with the name : "1_text1", "1_text2", ...
//  + "1_text.str" key : can create many with the name : "str1", "str2", ...
//
//  + "2_progress" key : can create many with the name : "2_progress1", "2_progress2", ...
//  + "<key>: <value>" : key is skill name, value is progress percent. Example: java:70, kotlin:80
//
//  + "3_tag" key : can create many with the name : "3_tag1", "3_tag2", ...
//  + "3_tag.value" key : comma-separated values. Example : java, kotlin, dart, swift
//
//  + The number in front of "text", "progress", "tag" letter is the display order.
//  + "text", "progress", "tag" are the name of UI style.
// ---------------------------------------
"skills": {
    "description": "",
    "1_text": {
        "name": "",
        "str": ""
    },
    "2_progress": {
        "name": "",
        "items": {
            "<key>": "<value>"
        }
    },
    "3_tag": {
        "name": "",
        "value": ""
    }
}
```

### Testimonial

```json
// --------------- NOTE ------------------
//  + "who" key : can create many with the name : "who1", "who2", ...
// ---------------------------------------
"testimonials": {
    "description": "",
    "who": {
        "name": "",
        "avatar": "",
        "job_title": "",
        "quote": ""
    }
}
```
