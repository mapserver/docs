# -*- coding: utf-8 -*-
#
# MapServer documentation build configuration file, created by
# sphinx-quickstart on Fri Nov 21 09:49:43 2008.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.append(os.path.abspath('.'))

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
#extensions = ['labels' ,'rst2pdf.pdfbuilder']
extensions = ['labels']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.txt'

# The encoding of source files.
source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'MapServer'
copyright = u'2013, Regents of the University of Minnesota'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '6.2'
# The full version, including alpha/beta/rc tags.
release = '6.2.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['howto', 'redirection', 'users-manual']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Exclude subversion directories
exclude_patterns = ['**/.svn']

# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'sphinx.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "MapServer " + release + " documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Home"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "mapserver.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['sourcelink.html', 'sidebar2.html', 'localtoc2.html', 'searchbox.html'],
"index":["indexsidebar.html", 'searchbox.html']}
# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {"index":'index.html'}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'MapServerdoc'

# Hide source from sidebar (see http://sphinx.pocoo.org/config.html#confval-html_show_sourcelink)
html_show_sourcelink = False

# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('documentation', 'MapServer.tex', ur'MapServer Documentation',
   ur'The MapServer Team', 'manual', False),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = './_static/banner-large.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# Additional stuff for the LaTeX preamble.
latex_preamble = '\setcounter{tocdepth}{3}'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
#

# -- Options for PDF output ---------------------------------------

    # Grouping the document tree into PDF files. List of tuples
    # (source start file, target name, title, author).
pdf_documents = [
    ('documentation', u'MapServer', u'MapServer Documentation', u'The MapServer Team'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
#pdf_compressed=False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path=['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
#pdf_language="en_EN"

# If false, no index is generated.
#pdf_use_index = True

# If false, no modindex is generated.
#pdf_use_modindex = True

# If false, no coverpage is generated.
#pdf_use_coverpage = True 


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = 'MapServer Documentation'
epub_author = 'Steve Lime'
epub_publisher = 'http://mapserver.org'
epub_copyright = copyright

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'URL'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'http://mapserver.org'

# A unique identification for the text.
#epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

from pygments.lexer import RegexLexer, bygroups,combined, include
from pygments.token import *
from pygments import highlight
from pygments.formatters import HtmlFormatter


class WKTLexer(RegexLexer):
    name = 'wkt'
    aliases = ['wkt']
    filenames = ['*.wkt']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'[{}\[\]();,-.]+', Punctuation),
            (r'(PROJCS)\b', Generic.Heading),
            (r'(PARAMETER|PROJECTION|SPHEROID|DATUM|GEOGCS|AXIS)\b', Keyword),
            (r'(PRIMEM|UNIT|TOWGS84)\b', Keyword.Constant),
            (r'(AUTHORITY)\b', Name.Builtin),
            (r'[$a-zA-Z_][a-zA-Z0-9_]*', Name.Other),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'[0-9]+', Number.Integer),
            (r'"(\\\\|\\"|[^"])*"', String.Double),
            (r"'(\\\\|\\'|[^'])*'", String.Single),
        ]
    }

import re
builtins = (r'(ANNOTATION|'
            r'AUTO|BEVEL|BITMAP|BUTT|CARTOLINE|CC|CENTER|'
            r'CHART|CIRCLE|CL|CR|CSV|MYSQL|'
            r'POSTGRESQL|DEFAULT|DD|ELLIPSE|EMBED|FALSE|FEET|FOLLOW|'
            r'GIANT|HATCH|HILITE|INCHES|KILOMETERS|LARGE|LC|'
            r'LEFT|LINE|LL|LOCAL|LR|MEDIUM|METERS|MILES|MITER|MULTIPLE|NONE|'
            r'NORMAL|OFF|OGR|ON|ONE-TO-ONE|ONE-TO-MANY|ORACLESPATIAL|'
            r'PERCENTAGES|PIXMAP|PIXELS|POINT|POLYGON|POSTGIS|MYGIS|'
            r'PLUGIN|QUERY|RASTER|RIGHT|ROUND|SDE|SELECTED|SIMPLE|SINGLE|'
            r'SMALL|SQUARE|TINY|TRIANGLE|TRUE|TRUETYPE|UC|UL|UNION|UR|UV_ANGLE|UV_MINUS_ANGLE|UV_LENGTH|UV_LENGTH_2|UVRASTER|VECTOR|'
            r'WFS|WMS|ALPHA|'
            r'GIF|JPEG|JPG|PNG|WBMP|SWF|PDF|GTIFF|PC256|RGB|RGBA|INT16|FLOAT32|GD|'
            r'AGG|CAIRO|PNG8|SVG|KML|KMZ|GDAL|UTFGRID'
            r')\b')

keywords = (r'(ALIGN|'
            r'ALPHACOLOR|ANCHORPOINT|ANGLE|ANTIALIAS|AUTHOR|BACKGROUNDCOLOR|BACKGROUNDSHADOWCOLOR|'
            r'BACKGROUNDSHADOWSIZE|BANDSITEM|BROWSEFORMAT|BUFFER|CHARACTER|CLASS|CLASSITEM|'
            r'CLASSGROUP|CLUSTER|COLOR|CONFIG|CONNECTION|CONNECTIONTYPE|DATA|DATAPATTERN|DEBUG|'
            r'DRIVER|DUMP|EMPTY|ENCODING|END|ERROR|EXPRESSION|EXTENT|EXTENSION|FEATURE|'
            r'FILLED|FILTER|FILTERITEM|FOOTER|FONT|FONTSET|FORCE|FORMATOPTION|FROM|GAP|GEOMTRANSFORM|'
            r'GRID|GRIDSTEP|GRATICULE|GROUP|HEADER|IMAGE|IMAGECOLOR|IMAGETYPE|IMAGEQUALITY|IMAGEPATH|'
            r'IMAGEURL|INCLUDE|INDEX|INITIALGAP|INTERLACE|INTERVALS|JOIN|KEYIMAGE|KEYSIZE|KEYSPACING|LABEL|'
            r'LABELCACHE|LABELFORMAT|LABELITEM|LABELMAXSCALE|LABELMAXSCALEDENOM|'
            r'LABELMINSCALE|LABELMINSCALEDENOM|LABELREQUIRES|LATLON|LAYER|LEADER|LEGEND|'
            r'LEGENDFORMAT|LINECAP|LINEJOIN|LINEJOINMAXSIZE|LOG|MAP|MARKER|MARKERSIZE|'
            r'MASK|MAXARCS|MAXBOXSIZE|MAXDISTANCE|MAXFEATURES|MAXINTERVAL|MAXSCALE|MAXSCALEDENOM|MINSCALE|'
            r'MINSCALEDENOM|MAXGEOWIDTH|MAXLENGTH|MAXSIZE|MAXSUBDIVIDE|MAXTEMPLATE|'
            r'MAXWIDTH|METADATA|MIMETYPE|MINARCS|MINBOXSIZE|MINDISTANCE|'
            r'MINFEATURESIZE|MININTERVAL|MINSCALE|MINSCALEDENOM|MINGEOWIDTH'
            r'MINLENGTH|MINSIZE|MINSUBDIVIDE|MINTEMPLATE|MINWIDTH|NAME|OFFSET|OFFSITE|'
            r'OPACITY|OUTLINECOLOR|OUTLINEWIDTH|OUTPUTFORMAT|OVERLAYBACKGROUNDCOLOR|'
            r'OVERLAYCOLOR|OVERLAYMAXSIZE|OVERLAYMINSIZE|OVERLAYOUTLINECOLOR|'
            r'OVERLAYSIZE|OVERLAYSYMBOL|PARTIALS|PATTERN|POINTS|POLAROFFSET|POSITION|POSTLABELCACHE|'
            r'PRIORITY|PROCESSING|PROJECTION|QUERYFORMAT|QUERYMAP|REFERENCE|REGION|'
            r'RELATIVETO|REQUIRES|RESOLUTION|SCALE|SCALEDENOM|SHADOWCOLOR|SHADOWSIZE|'
            r'SHAPEPATH|SIZE|SIZEUNITS|STATUS|STYLE|STYLEITEM|SYMBOL|SYMBOLSCALE|'
            r'SYMBOLSCALEDENOM|SYMBOLSET|TABLE|TEMPLATE|TEMPLATEPATTERN|TEXT|'
            r'TILEINDEX|TILEITEM|TILESRS|TITLE|TO|TOLERANCE|TOLERANCEUNITS|TRANSPARENCY|'
            r'TRANSPARENT|TRANSFORM|TYPE|UNITS|UTFDATA|UTFITEM|WEB|WIDTH|WKT|WRAP|IMAGEMODE|VALIDATION'
            r')\b')

class MapFileLexer(RegexLexer):
    name = 'mapfile'
    aliases = ['mapfile']
    filenames = ['*.map']

    flags = re.IGNORECASE
    tokens = {
        'root': [
            (r'\s+', Text),
            (r'\[.*?\]', Name.Other),
            (r'[{}\[\]();,-.]+', Punctuation),
            (r'#.*', Comment),
            (r'(AND|OR|NOT|EQ|GT|LT|GE|LE|NE|IN|IEQ)\b', Operator.Word),
            (r'!=|==|<=|>=|=~|&&|\|\||[-~+/*%=<>&^|./\$]', Operator),
            ('(?:[rR]|[uU][rR]|[rR][uU])"', String, 'dqs'),
            ("(?:[rR]|[uU][rR]|[rR][uU])'", String, 'sqs'),
            ('[uU]?"', String, combined('stringescape', 'dqs')),
            ("[uU]?'", String, combined('stringescape', 'sqs')),
#            (constants, Keyword.Constant),
#            (r"""[]{}:(),;[]""", Punctuation),
            # (r'(MAP)\b', Generic.Heading),
            (keywords, Keyword),
            (builtins, Name.Builtin),
            (r'[0-9][0-9]*\.[0-9]+([eE][0-9]+)?[fd]?', Number.Float),
            (r'[0-9]+', Number.Integer),

        ],
        'dqs': [
            (r'"', String, '#pop'),
            (r'\\\\|\\"|\\\n', String.Escape), # included here again for raw strings
            include('strings')
        ],
        'sqs': [
            (r"'", String, '#pop'),
            (r"\\\\|\\'|\\\n", String.Escape), # included here again for raw strings
            include('strings')
        ],
        'tdqs': [
            (r'"""', String, '#pop'),
            include('strings'),
            include('nl')
        ],
        'tsqs': [
            (r"'''", String, '#pop'),
            include('strings'),
            include('nl')
        ],
        'strings': [
            (r'%(\([a-zA-Z0-9_]+\))?[-#0 +]*([0-9]+|[*])?(\.([0-9]+|[*]))?'
             '[hlL]?[diouxXeEfFgGcrs%]', String.Interpol),
            (r'[^\\\'"%\n]+', String),
            # quotes, percents and backslashes must be parsed one at a time
            (r'[\'"\\]', String),
            # unhandled string formatting sign
            (r'%', String)
            # newlines are an error (use "nl" state)
        ],
        'nl': [
            (r'\n', String)
        ],
        'stringescape': [
            (r'\\([\\abfnrtv"\']|\n|N{.*?}|u[a-fA-F0-9]{4}|'
             r'U[a-fA-F0-9]{8}|x[a-fA-F0-9]{2}|[0-7]{1,3})', String.Escape)
        ],
    }


def setup(app):
    from sphinx.highlighting import lexers
    lexers['wkt'] = WKTLexer()
    lexers['mapfile'] = MapFileLexer()
