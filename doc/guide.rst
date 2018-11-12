.. vim: set fileencoding=utf-8 :
.. @author: Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
.. @date:   Mon Oct 19 11:10:18 CEST 2015

==============
 User's Guide
==============

This package contains the access API and descriptions for the Long Distance Heterogeneous Face Database `LDHF-DB`_ database.
It only contains the Bob_ accessor methods to use the DB directly from python, with our certified protocols.
The actual raw data for the database should be downloaded from the original URL.

The Database Interface
----------------------

The :py:class:`bob.db.ldhf.Database` complies with the standard biometric verification database as described in `bob.db.base <bob.db.base>`_, implementing the interface :py:class:`bob.db.base.SQLiteDatabase`.

LDHF-DB Protocols
-----------------

There are 10 protocols implemented in this database ('split1','split2','split3','split4','split5','split6','split7','split8','split9','split10').

The protocols correspond to 10-fold cross-validation letting 90 identities for training and 10 for evaluation for each fold (randomly selected), as described in:

.. code-block:: latex

  @article{kang2014nighttime,
    title={Nighttime face recognition at large standoff: Cross-distance and cross-spectral matching},
    author={Kang, Dongoh and Han, Hu and Jain, Anil K and Lee, Seong-Whan},
    journal={Pattern Recognition},
    volume={47},
    number={12},
    pages={3750--3766},
    year={2014},
    publisher={Elsevier}
  }


According to the mentioned publication were implemented the cross-spectral and the cross-distance evaluations where the 1m VIS images are used for enrollment and the NIR images with different standoffs (1m, 60m, 100m and 150m) are used for probing.




.. _LDHF-DB: http://biolab.korea.ac.kr/database/
.. _bob: https://www.idiap.ch/software/bob
