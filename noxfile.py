import nox


@nox.session(python=["3.8", "3.9"])
def tests(session):
    session.install("-r", "requirements.txt")
    session.run("pytest", "-v", "--cov=library", "--cov-report=term-missing")
    session.run("coverage", "report", "-m", external=True)
