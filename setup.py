from setuptools import setup

setup(
    use_scm_version={"write_to": "text2epub/_version.py"},
    setup_requires=["setuptools_scm"],
)
