casestyle
==========
String case style converter (snake_case, camelCase, PascalCase, dash-case, CONST_CASE can be converted to each other).

* Include Functions:
    * casestyle.camelcase(string)
    * casestyle.pascalcase(string)
    * casestyle.snakecase(string)
    * casestyle.dashcase(string)
    * casestyle.constcase(string)
    * casestyle.casepreprocess(string)

* Other Useful Python String Methods:
    * str.title()
    * str.capitalize()
    * str.lowercase()
    * str.uppercase()
    * str.swapcase()

Installation
--------------

You can install "casestyle" via pip from `PyPI <https://pypi.python.org/pypi/casestyle>`_:

::

    $ pip install casestyle
	
Usage
-------

.. code-block:: python

    import casestyle
    casestyle.camelcase('foo bar baz') # => "fooBarBaz"
    casestyle.camelcase('fooBarBaz') # => "fooBarBaz"
    casestyle.camelcase('FooBarBaz') # => "fooBarBaz"
    casestyle.camelcase('foo_bar_baz') # => "fooBarBaz"
    casestyle.camelcase('foo-bar-baz') # => "fooBarBaz"
    casestyle.camelcase('FOO_BAR_BAZ') # => "fooBarBaz"
    casestyle.camelcase('foo _Bar___BAZ---Qux   quux') # => "fooBarBazQuxQuux"
    casestyle.camelcase('_foo_bar') # => "_fooBar"
    casestyle.camelcase('__foo_bar__') # => "__fooBar__"
    casestyle.camelcase('$foo_bar') # => "$fooBar"

    casestyle.pascalcase('foo bar baz') # => "FooBarBaz"
    casestyle.pascalcase('fooBarBaz') # => "FooBarBaz"
    casestyle.pascalcase('FooBarBaz') # => "FooBarBaz"
    casestyle.pascalcase('foo_bar_baz') # => "FooBarBaz"
    casestyle.pascalcase('foo-bar-baz') # => "FooBarBaz"
    casestyle.pascalcase('FOO_BAR_BAZ') # => "FooBarBaz"
    casestyle.pascalcase('foo _Bar___BAZ---Qux   quux') # => "FooBarBazQuxQuux"
    casestyle.pascalcase('_foo_bar') # => "_FooBar"
    casestyle.pascalcase('__foo_bar__') # => "__FooBar__"
    casestyle.pascalcase('$foo_bar') # => "$FooBar"

    casestyle.snakecase('foo bar baz') # => "foo_bar_baz"
    casestyle.snakecase('fooBarBaz') # => "foo_bar_baz"
    casestyle.snakecase('FooBarBaz') # => "foo_bar_baz"
    casestyle.snakecase('foo_bar_baz') # => "foo_bar_baz"
    casestyle.snakecase('foo-bar-baz') # => "foo_bar_baz"
    casestyle.snakecase('FOO_BAR_BAZ') # => "foo_bar_baz"
    casestyle.snakecase('foo _Bar___BAZ---Qux   quux') # => "foo_bar_baz_qux_quux"
    casestyle.snakecase('_foo_bar') # => "_foo_bar"
    casestyle.snakecase('__foo_bar__') # => "__foo_bar__"
    casestyle.snakecase('$foo_bar') # => "$foo_bar"

    casestyle.dashcase('foo bar baz') # => "foo-bar-baz"
    casestyle.dashcase('fooBarBaz') # => "foo-bar-baz"
    casestyle.dashcase('FooBarBaz') # => "foo-bar-baz"
    casestyle.dashcase('foo_bar_baz') # => "foo-bar-baz"
    casestyle.dashcase('foo-bar-baz') # => "foo-bar-baz"
    casestyle.dashcase('FOO_BAR_BAZ') # => "foo-bar-baz"
    casestyle.dashcase('foo _Bar___BAZ---Qux   quux') # => "foo-bar-baz-qux-quux"
    casestyle.dashcase('_foo_bar') # => "_foo-bar"
    casestyle.dashcase('__foo_bar__') # => "__foo-bar__"
    casestyle.dashcase('$foo_bar') # => "$foo-bar"

    casestyle.constcase('foo bar baz') # => "FOO_BAR_BAZ"
    casestyle.constcase('fooBarBaz') # => "FOO_BAR_BAZ"
    casestyle.constcase('FooBarBaz') # => "FOO_BAR_BAZ"
    casestyle.constcase('foo_bar_baz') # => "FOO_BAR_BAZ"
    casestyle.constcase('foo-bar-baz') # => "FOO_BAR_BAZ"
    casestyle.constcase('FOO_BAR_BAZ') # => "FOO_BAR_BAZ"
    casestyle.constcase('foo _Bar___BAZ---Qux   quux') # => "FOO_BAR_BAZ_QUX_QUUX"
    casestyle.constcase('_foo_bar') # => "_FOO_BAR"
    casestyle.constcase('__foo_bar__') # => "__FOO_BAR__"
    casestyle.constcase('$foo_bar') # => "$FOO_BAR"
