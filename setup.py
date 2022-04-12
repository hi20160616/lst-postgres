from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name="List Postgres",
    install_requires=[
        "Flask >= 2.0"
        "Werkzeug >= 2.0",
        "Jinja2 >= 3.0",
        "itsdangerous >= 2.0",
        "importlib-metadata >= 3.6.0; python_version >= '3.10'",
        "psycopg2-binary >= 2.9.0",
    ],
    extras_require={
        "async": ["asgiref >= 3.2"],
        "dotenv": ["python-dotenv"],
    },
)
