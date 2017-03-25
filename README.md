# Deploy The Docs

## Motivation

This project was created as a convenient solution to hosting statically 
generated documentation for internal Python projects. Services such as 
[readthedocs](https://readthedocs.org/) may not be suitable for hosting the 
documentation of proprietary software.

At [Eniram](http://www.eniram.fi/) we already have CI to generate the static 
html pages for the docs but wanted an API to deploy and host them.

### Technologies

We use [Django](https://www.djangoproject.com/) and 
[django-rest-framework](http://www.django-rest-framework.org/) for the API. The
wsgi webserver is [gunicorn](http://gunicorn.org/) and requests are proxied to 
it by [nginx](https://www.nginx.com/).

The frontend is built using [react](https://facebook.github.io/react/) and
[react-bootstrap](https://react-bootstrap.github.io/) and static assets are 
collected and bundled using [webpack](https://webpack.js.org/).

## Installation

You will need [docker-compose](https://docs.docker.com/compose/) and 
[nodejs](https://nodejs.org/) to get started.

1. Fork and clone this repository to get a local copy of the code.
2. Run `npm install && npm build` in the `frontend/` subfolder to prepare the
   static assets.
3. Run `docker-compose build` to create Docker images for the api and frontend
   services.
4. Run `docker-compose up` to start the services.

The homepage is available at `http://localhost:8080/` and the API at 
`http://localhost:8080/api/v1/projects/`.

## Development

For easier iteration while developing, you can run the 
[webpack-dev-server](https://webpack.js.org/guides/development/#webpack-dev-server)
and Django development server.

From the `api` subfolder:

```bash
# You may need to collect the static assets if DEBUG=False
python manage.py collectstatic --clear --no-input

# After that you can run the development server
python manage.py runserver
```

From the `frontend` subfolder:

```bash
# Kick off the webpack-dev-server for live reloading on code changes
npm run start
```

Then visit the url `http://localhost:8080` to access the application. During 
development the uploaded projects will be extracted to the `uploaded` subfolder 
in the project root.

## Usage

### Terminology

<dl>
  <dt>Project</dt>
  <dd>
    An internal software project which may have many Versions of its own
    documentation
  </dd>
  <dt>Version</dt>
  <dd>
    A specific version of the given project. This allows you to host docs for
    different versions of the same project.
  </dd>
</dl>

### API

* `/api/v1/projects/<project>/<version>/`

  **Methods:** `GET` | `POST` | `DELETE`
  **Description:** Send a `POST` request to this endpoint with a zip file 
  containing the prebuilt documentation (from Sphinx or mkdocs or similar). This
  will extract and store the content at the location defined by `DOCS_ROOT`.

* `/api/v1/projects/<project>/`

  **Methods:** `GET`
  **Description:** View all the versions associated with a given `<project>`.

* `/api/v1/projects/`

  **Methods:** `GET`
  **Description:** View all the uploaded projects and their versions.

## Beware

This service requires no authentication to upload/delete the static files and 
offers no protection against malicious content uploaded by any user.
