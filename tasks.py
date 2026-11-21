from invoke import task

@task
def start(ctx):
    ctx.run("python src/app.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src; coverage html", pty=True)
