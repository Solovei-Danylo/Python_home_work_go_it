from setuptools import setup, find_namespace_packages

setup(name='Python_sort_files_finish',
      version='0.1',
      description='Сортує задану папку- перевіряє внутрішні вкладення/ Форматує утворюючи нові папки і розархивовує архіви, також переіменовує.',
      url='https://github.com/Solovei-Danylo/Python_home_work_go_it',
      author='Solovei-Danylo',
      author_email='',
      license='License',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['python_sort = Python_sort_files_finish.Sort_files:main']})
