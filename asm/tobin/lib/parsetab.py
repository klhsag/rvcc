
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '161367662966802CA482930E5A760A6B'
    
_lr_action_items = {'LABEL':([0,10,14,],[3,13,19,]),'OPCODE':([0,],[5,]),'NEWLINE':([0,6,8,12,13,17,18,19,],[4,9,-8,15,16,20,21,22,]),'$end':([1,2,4,9,15,16,20,21,22,],[0,-1,-9,-2,-5,-6,-3,-4,-7,]),'COLUMN':([3,],[6,]),'REGISTER':([5,10,14,],[8,8,8,]),'COMMA':([7,8,11,],[10,-8,14,]),'IMMEDIATE':([10,14,],[12,18,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,],[2,]),'register':([5,10,14,],[7,11,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program_statement','parser.py',33),
  ('program -> LABEL COLUMN NEWLINE','program',3,'p_program_label','parser.py',41),
  ('statement -> OPCODE register COMMA register COMMA register NEWLINE','statement',7,'p_statement_R','parser.py',53),
  ('statement -> OPCODE register COMMA register COMMA IMMEDIATE NEWLINE','statement',7,'p_statement_I_S_SB','parser.py',68),
  ('statement -> OPCODE register COMMA IMMEDIATE NEWLINE','statement',5,'p_statement_U_UJ','parser.py',113),
  ('statement -> OPCODE register COMMA LABEL NEWLINE','statement',5,'p_statement_UJ_LABEL','parser.py',144),
  ('statement -> OPCODE register COMMA register COMMA LABEL NEWLINE','statement',7,'p_statement_SB__JALR_LABEL','parser.py',160),
  ('register -> REGISTER','register',1,'p_register','parser.py',185),
  ('statement -> NEWLINE','statement',1,'p_statement_none','parser.py',197),
]
