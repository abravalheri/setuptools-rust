from os.path import dirname

import nox

SETUPTOOLS_RUST = dirname(dirname(dirname(__file__)))


@nox.session()
def test(session: nox.Session):
    session.install(SETUPTOOLS_RUST, "wheel", "pytest")
    session.install("--no-build-isolation", ".")
    session.run("pytest", *session.posargs)


@nox.session()
def setuptools_install(session: nox.Session):
    session.install(SETUPTOOLS_RUST, "pytest")
    session.run("python", "setup.py", "install")
    session.run("pytest", *session.posargs)
