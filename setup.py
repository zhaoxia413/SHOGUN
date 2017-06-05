from setuptools import setup

__author__ = "Knights Lab"
__copyright__ = "Copyright (c) 2016--, %s" % __author__
__credits__ = ["Benjamin Hillmann", "Dan Knights", "Gabe Al-Ghalith", "Tonya Ward", "Pajau Vangay"]
__email__ = "hillm096@cs.umn.edu"
__license__ = "AGPL"
__maintainer__ = "Benjamin Hillmann"
__version__ = "0.0.1-dev0"

long_description = ''

setup(
    name='shogun',
    version=__version__,
    packages=["shogun"],
    url='',
    license=__license__,
    author=__author__,
    author_email=__email__,
    description='',
    long_description=long_description,
    keywords='',
    install_requires=['Click'],
    entry_points={
        'console_scripts': [
            'shogun = shogun.__main__:cli'
        ]
    },
    extras_require={
        'test': ['pytest', 'pytest-cov'],
        'demo': ['jupyter', 'jupyter_client', 'ipython'],
        'doc': ['sphinx'],
    },
)

# scripts=glob(os.path.join('shogun', 'scripts', '*py')),

# 'shogun_bt2_align = shogun.scripts.shogun_bt2_align:shogun_bt2_align',
# 'shogun_bt2_db = shogun.scripts.shogun_bt2_db:shogun_bt2_db',
# 'shogun_bt2_lca = shogun.scripts.shogun_bt2_lca:shogun_bt2_lca',
# 'shogun_bt2_capitalist = shogun.scripts.shogun_bt2_capitalist:shogun_bt2_capitalist',
# 'shogun_utree_db = shogun.scripts.shogun_utree_db:shogun_utree_db',
# 'shogun_utree_lca = shogun.scripts.shogun_utree_lca:shogun_utree_lca',
# 'shogun_utree_capitalist = shogun.scripts.shogun_utree_capitalist:shogun_utree_capitalist',
# 'shogun_utree_functional = shogun.scripts.shogun_utree_functional:shogun_utree_functional',
# 'shogun_bugbase = shogun.scripts.shogun_bugbase:shogun_bugbase',
# 'extract_genome_lengths = shogun.scripts.extract_genome_lengths:extract_genome_lengths',
# 'kegg_predictions = shogun.scripts.kegg_predictions:main',
# 'kegg_mapping_extract_img_id = shogun.scripts.kegg_mapping_extract_img_id:main',
# 'kegg_parse_img_ids = shogun.scripts.kegg_parse_img_ids:main',
