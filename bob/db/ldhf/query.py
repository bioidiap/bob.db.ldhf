#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
# Tue Aug 14 14:28:00 CEST 2015
#
# Copyright (C) 2012-2014 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import six
from bob.db.base import utils
from .models import *
from .models import PROTOCOLS, GROUPS, PURPOSES
from .driver import Interface
import bob.db.base

SQLITE_FILE = Interface().files()[0]

class Database(bob.db.base.SQLiteDatabase):

  """Wrapper class for the Long Distance Heterogeneous Face Database (LDHF-DB) (http://biolab.korea.ac.kr/database/)

  """

  def __init__(self, original_directory = None, original_extension = None):
    # call base class constructors to open a session to the database
    super(Database, self).__init__(SQLITE_FILE, File,
                                   original_directory, original_extension)
  
  
  def protocols(self):
    return PROTOCOLS

  def purposes(self):
    return PURPOSES

  @property
  def modality_separator(self):
      return "photo"

  @property
  def modalities(self):
      return ['photo', 'sketch']


  def annotations(self, file, annotation_type="eyes_center"):
    """This function returns the annotations for the given file id as a dictionary.

    **Parameters**
    
    file: :py:class:`bob.db.base.File`
      The File object you want to retrieve the annotations for,
      
    **Return**
      A dictionary of annotations, for face images usually something like {'leye':(le_y,le_x), 'reye':(re_y,re_x), ...},
      or None if there are no annotations for the given file ID (which is the case in this base class implementation).
    """    
    return file.annotations(annotation_type=annotation_type)


  def objects(self, groups = None, protocol = None, purposes = None, model_ids = None, **kwargs):
    """
      This function returns lists of File objects, which fulfill the given restrictions.
    """

    #Checking inputs
    groups    = self.check_parameters_for_validity(groups, "group", GROUPS)
    protocols = self.check_parameters_for_validity(protocol, "protocol", PROTOCOLS) 
    purposes  = self.check_parameters_for_validity(purposes, "purpose", PURPOSES)

    #You need to select only one protocol
    if (len(protocols) > 1):
      raise ValueError("Please, select only one of the following protocols {0}".format(protocols))
 
    #Querying
    query = self.query(bob.db.ldhf.File, bob.db.ldhf.Protocol_File_Association).join(bob.db.ldhf.Protocol_File_Association).join(bob.db.ldhf.Client)

    #filtering
    query = query.filter(bob.db.ldhf.Protocol_File_Association.group.in_(groups))
    query = query.filter(bob.db.ldhf.Protocol_File_Association.protocol.in_(protocols))
    query = query.filter(bob.db.ldhf.Protocol_File_Association.purpose.in_(purposes))

    if model_ids is not None:     
      if type(model_ids) is not list and type(model_ids) is not tuple:
        model_ids = [model_ids]
     
      #if you provide a client object as input and not the ids    
      if type(model_ids[0]) is bob.db.ldhf.Client:
        model_aux = []
        for m in model_ids:
          model_aux.append(m.id)
        model_ids = model_aux       

      query = query.filter(bob.db.ldhf.Client.id.in_(model_ids))

    raw_files = query.all()
    files     = []
    for f in raw_files:
      f[0].group    = f[1].group
      f[0].purpose  = f[1].purpose
      f[0].protocol = f[1].protocol
      files.append(f[0])

    return files



  def get_client_by_id(self, client_id):
    """
    Get the client object from its ID
    """    

    query = self.query(bob.db.ldhf.Client).filter(bob.db.ldhf.Client.id == client_id)
    assert len(query.all())==1
    return query.all()[0]

    

  def model_ids(self, protocol=None, groups=None):

    #Checking inputs
    groups    = self.check_parameters_for_validity(groups, "group", GROUPS)
    protocols = self.check_parameters_for_validity(protocol, "protocol", PROTOCOLS) 

    #You need to select only one protocol
    if (len(protocols) > 1):
      raise ValueError("Please, select only one of the following protocols {0}".format(protocols))
 
    #Querying
    query = self.query(bob.db.ldhf.Client).join(bob.db.ldhf.File).join(bob.db.ldhf.Protocol_File_Association)

    #filtering
    query = query.filter(bob.db.ldhf.Protocol_File_Association.group.in_(groups))
    query = query.filter(bob.db.ldhf.Protocol_File_Association.protocol.in_(protocols))

    return [c.id for c in query.all()]


  def groups(self, protocol = None, **kwargs):
    """This function returns the list of groups for this database."""
    return GROUPS



  def tmodel_ids(self, groups = None, protocol = None, **kwargs):
    """This function returns the ids of the T-Norm models of the given groups for the given protocol."""

    return []


  def tobjects(self, protocol=None, model_ids=None, groups=None):
    #No TObjects    
    return []


  def zobjects(self, protocol=None, groups=None):
    #No TObjects    
    return []

