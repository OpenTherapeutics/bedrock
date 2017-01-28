import os

from invoke import task

PROJECT = "bedrock"

@task
def clean(ctx):
    """Removes all the cache files"""
    ctx.run("find . -type d -name __pycache__ | xargs rm -rf")


@task
def install(ctx):
    """Installs the libraries required to run the application"""
    ctx.run("pip install -U pip")
    ctx.run("pip install -qr requirements/base.txt")


@task(install)
def develop(ctx):
    """Installs all the libraries used for development"""
    ctx.run("pip install -qr requirements/develop.txt")


@task(develop)
def checks(ctx):
    """Runs pep8/flake8 checks on the code"""
    ctx.run("pep8 .")
    ctx.run("flake8 .")


@task(develop)
def test(ctx):
    """Runs the tests"""
    ctx.run(
        "py.test --cov-config .coveragerc --cov-report html --cov-report term --cov={}".format(PROJECT),
        pty=True
    )
