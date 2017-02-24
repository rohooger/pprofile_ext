from setuptools import setup


setup(
    name='pprofile_ext',
    version='1.0.0',
    license='MIT',

    author='Ronnie Hoogerwerf',
    author_email='rohooger@gmail.com',
    url='http://github.com/rohooger/pprofile_ext',

    description='',
    long_description='',

    classifiers=[
        'Development Status :: 3 = Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
    ],

    packages=[
        'pprofile_ext',
        'pprofile_ext.html',
    ],

    # dependencies
    install_requires=[
        'pprofile>=1.7.3',
        'pygments>=2.0.0',
    ]
)
