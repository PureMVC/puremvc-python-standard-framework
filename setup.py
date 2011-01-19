from distutils.core import setup

setup(name='PureMVC',
      version='1.2',
      description='PureMVC Python Framework',
      author='Toby de Havilland',
      author_email='toby.de.havilland@puremvc.org',
      url='http://www.puremvc.org',
	  package_dir={'': 'src'},
      packages=['puremvc', 'puremvc.patterns'],
)
