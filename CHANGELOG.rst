**0.8.13 - 11/15/18**

 - Fix broken doc dependency

**0.8.12 - 11/15/18**

 - Remove mean age and year columns

**0.8.11 - 11/15/18**

 - Bugfix where transitions were casting pandas indices to series.
 - Add better error message when a none is found in the configuration.

**0.8.10 - 11/5/18**

 - Added ``add_components`` method to simulation context.
 - Added typing info to interactive interface.

**0.8.9 - 10/23/18**

 - Accept ``.yml`` model specifications
 - Redesign interpolation. Order zero only at this point.

**0.8.8 - 10/09/18**

 - Raise error if multiple components set same default configuration.
 - Loosen error checking in value manager

**0.8.7 - 09/25/18**

 - Distinguish between missing and cyclic population table dependencies.
 - Initial draft of tutorial documentation

**0.8.6 - 09/07/18**

 - Workaround for hdf metadata limitation when writing dataframes with a large
   number of columns

**0.8.5 - 08/22/18**

 - Add integration with Zenodo to produce DOIs
 - Added default get_components implementation for component manager

**0.8.4 - 08/02/18**

 - Standardized a bunch of packaging stuff.

**0.8.2 - 07/24/18**

 - Added ``test`` command to verify and installation
 - Updated ``README`` with installation instructions.


**0.8.1 - 07/24/18**

 - Move to source layout.
 - Set tests to install first and then test installed package.
 - Renamed ``test_util`` to resolve naming collision during test.

**0.8.0 - 07/24/18**

 - Initial release
