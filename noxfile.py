import nox


@nox.session(python=["3.10", "3.11"])
def tests(session):
    session.install("pytest")
    session.run("pytest", "test_library.py")
