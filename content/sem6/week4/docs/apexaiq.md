---
layout: default
title: "This is Dockerized"
---

# ApexaiQ internship

Code and Docs from my time at apexaiq. it uses jekyll for the site and python for the scripts.

## Setup

you need ruby and python. 

ruby stuff:
```bash
bundle install

```

python stuff:

```bash
source jadu/bin/activate
pip install -r requirements.txt

```

## Run it

to spin up the docs site locally:

```bash
bundle exec jekyll serve

```

check `localhost:4000`.

for the weekly code, just `cd` into the specific week's `code` folder and run the scripts. make sure the python venv is active.

## For Docker Users
### Build image :
  ```bash
  docker build -t apexaiq-docs:<version> .
  ```
### Run built image (for Noobs (ubuntu)):
  ```bash
  docker run -p 4000:4000 apexaiq-docs:<versio>
  ```
  ### For Arch users (anonymize volumes due to gem dependency mismatch) :
  ```bash
  docker run -u $(id -u):$(id -g) -v $(pwd):/srv/jekyll -v /srv/jekyll/vendor -p 4000:4000 apexaiq-docs:<version>
  ```

## License

do whatever you want with it.


