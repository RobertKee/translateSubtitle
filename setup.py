from setuptools import __version__, setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
exec(open("src/translate/version.py").read())

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='translate_subtitles',
    version=__version__,
    description='translate subtitle files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Robert Kee',
    author_email='roberthayeskee@gmail.com',
    keywords='subtitles, srt, translate',
    package_dir={'': 'src'}, 
    packages=find_packages(where='src'), 
    python_requires='>=3.6, <4',
    install_requires=['googletrans', 'Path'],
    entry_points={  
        'console_scripts': [
            'subtitleTranslate=translate.subtitle_translate:translate_subtitles',
        ],
    },
)
