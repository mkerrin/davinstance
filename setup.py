from setuptools import setup, find_packages

setup(
    name = "davinstance",
    version = "0.1",

    package_dir = {"": "src"},
    packages = find_packages("src"),

    include_package_data = True,
    zip_safe = False,
    install_requires = [
        "setuptools",

        "z3c.dav",
        "z3c.davapp.zopefile",
        "z3c.davapp.zopeappfile",
        "z3c.davapp.zopelocking",
        ],

    entry_points = """
    [paste.app_factory]
    main = davinstance.startup:application_factory

    [paste.global_paster_command]
    shell = davinstance.debug:Shell
    """,
    )
