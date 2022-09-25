from setuptools import setup

setup(name='sort',
      version='1',
      description='Сортує задану папку- перевіряє внутрішні вкладення/ Форматує утворюючи нові папки і розархивовує архіви, також переіменовує.',
      url='https://github.com/Solovei-Danylo/Python_home_work_go_it',
      author='Solovei-Danylo',
      author_email='',
      license='License',
      packages=['sort'],
      entry_points={'console_scripts': ['clean_folder = sort.sort:main']})
