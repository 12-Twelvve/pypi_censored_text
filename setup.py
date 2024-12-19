from setuptools import setup

setup(
    name='censoredzz',
    version='1.0.0',
    description='Python package for censoring profane words in Nepali-(Roman) text',
    author='Kuber Budhathoki, Amardeep Khatri',
    author_email='koobear99@gmail.com, amrkhatri97@gmail.com',
    url='https://github.com/12-Twelvve/pypi_censored_text',
    packages=['censoredzz'],
    install_requires=[
        'regex',
        # 'numpy',
    ],
)
