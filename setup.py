from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='pretaweb.pretamap',
      version=version,
      description="Popup imagemap for plone content",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Plone',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='popup imagemap plone content imaging editor tinymce',
      author='Dylan Jay',
      author_email='software@pretaweb.com',
      maintainer='Leonardo J. Caballero G.',
      maintainer_email='leonardocaballero@gmail.com',
      url='https://github.com/djay/pretaweb.pretamap',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['pretaweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.js.jquery',
          'Products.TinyMCE',
          'zopyx.tinymceplugins.imgmap',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
