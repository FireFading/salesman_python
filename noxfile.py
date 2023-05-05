import nox


@nox.session
def format(session: nox.Session) -> None:
    session.install("ufmt", "black", "isort")
    session.run("ufmt", "format", "core", "interface")
    session.run("black", "--config=configs/.black.toml", "core", "interface")
    session.run("isort", "--sp=configs/.isort.cfg", "core", "interface")


@nox.session
def lint(session: nox.Session) -> None:
    session.install("ruff", "flake8")
    session.run(
        "ruff", "check", "--config=configs/.ruff.toml", "--fix", "core", "interface"
    )
    session.run("flake8", "--config=configs/.flake8", "core", "interface")
