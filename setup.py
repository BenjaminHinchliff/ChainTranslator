from distutils.core import setup

setup(
    name="ChainTranslator",
    packages=["ChainTranslator"],
    version="1.0.0",
    license="MIT",
    description="a package to mess up text via google translate",
    author="Benjamin Hinchliff",
    url="https://github.com/SuniTheFish/ChainTranslator",
    download_url="https://github.com/SuniTheFish/ChainTranslator/archive/1.0.0.tar.gz",
    keywords=["google", "translator", "useless", "stupid", "random", "chain", "translator", "ChainTranslator"],
    install_requires=[
        'googletrans'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Text Processing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ]
)