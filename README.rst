.. vim: set fileencoding=utf-8 :
.. Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
.. Thu Apr 16 16:39:01 CEST 2015

   
.. image:: http://img.shields.io/badge/docs-stable-yellow.png
   :target: https://www.idiap.ch/software/bob/docs/bob/bob.db.ldhf/stable/index.html
.. image:: http://img.shields.io/badge/docs-latest-orange.png
   :target: http://beatubulatest.lab.idiap.ch/private/docs/bob/bob.db.ldhf/master/index.html
.. image:: https://gitlab.idiap.ch/bob/bob.db.ldhf/badges/master/build.svg
   :target: https://gitlab.idiap.ch/bob/bob.db.ldhf/commits/master
.. image:: https://img.shields.io/badge/gitlab-project-0000c0.svg
   :target: https://github.com/bioidiap/bob.db.ldhf
.. image:: http://img.shields.io/pypi/v/bob.db.ldhf.png
   :target: https://pypi.python.org/pypi/bob.db.ldhf
.. image:: https://img.shields.io/badge/original-data--files-a000a0.png
   :target: http://biolab.korea.ac.kr/database/
   
   

=======================================================
Long Distance Heterogeneous Face Database (LDHF-DB)
=======================================================

This package contains the access API and descriptions for the `Long Distance Heterogeneous Face Database (LDHF-DB) <http://biolab.korea.ac.kr/database/>`. 
The actual raw data for the database should be downloaded from the original URL. 
This package only contains the Bob accessor methods to use the DB directly from python, with the original protocol of the database.

Long Distance Heterogeneous Face Database (LDHF-DB) is for research on VIS-NIR face recognition.
It includes 100 identities faces captured in both VIS and NIR (at nighttime) in different standoffs: 1m, 60m, 100m and 150m.

This package implements the cross-disntance and cross-spectral evaluation protocol described in the paper::

  D. Kang, H. Han, A. K. Jain, and S.-W. Lee, "Nighttime Face Recognition at Large Standoff: Cross-Distance and Cross-Spectral Matching", Pattern Recognition, Vol. 47, No. 12, 2014, pp. 3750-3766.

Installation
------------

Follow our `installation`_ instructions. Then, to install this package, run::
   
   $ conda install bob.db.ldhf


Contact
-------

   For questions or reporting issues to this software package, contact our
   development `mailing list`_.


.. Place your references here:
.. _bob: https://www.idiap.ch/software/bob
.. _installation: https://gitlab.idiap.ch/bob/bob/wikis/Installation
.. _mailing list: https://groups.google.com/forum/?fromgroups#!forum/bob-devel
