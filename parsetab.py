
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftorleftandleftnotleftigualdaddiferenteleftmayormenorleftmasmenosleftpordivElse False If Nada True and diferente div id igualdad llavA llavC mas mayor menor menos not numero or parA parC porINI    : INSTRUCCIONES INSTRUCCIONES    : INSTRUCCIONES INSTRUCCION\n                      | INSTRUCCION  INSTRUCCION : If parA S parC llavA INSTRUCCIONES llavC\n                    | If parA S parC llavA INSTRUCCIONES llavC Else llavA INSTRUCCIONES llavC\n                    | Nada  S : L L : L or ML : MM : M and NEGM : NEGNEG : not S\n           | RR : E mayor ER : E menor ER : E igualdad ER : E diferente ER : parA S parCR : TrueR : FalseE : E mas T\n         | E menos T\n         | TT : T por F\n         | T div F\n         | F F : parA E parC\n        | numero \n        | id'
    
_lr_action_items = {'If':([0,2,3,5,6,39,51,53,55,56,57,],[4,4,-3,-6,-2,4,4,-4,4,4,-5,]),'Nada':([0,2,3,5,6,39,51,53,55,56,57,],[5,5,-3,-6,-2,5,5,-4,5,5,-5,]),'$end':([1,2,3,5,6,53,57,],[0,-1,-3,-6,-2,-4,-5,]),'llavC':([3,5,6,51,53,56,57,],[-3,-6,-2,53,-4,57,-5,]),'parA':([4,7,8,13,22,26,27,29,30,31,32,33,34,35,36,43,],[7,8,22,8,22,8,8,43,43,43,43,43,43,43,43,43,]),'not':([7,8,13,22,26,27,],[13,13,13,13,13,13,]),'True':([7,8,13,22,26,27,],[16,16,16,16,16,16,]),'False':([7,8,13,22,26,27,],[17,17,17,17,17,17,]),'numero':([7,8,13,22,26,27,29,30,31,32,33,34,35,36,43,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'id':([7,8,13,22,26,27,29,30,31,32,33,34,35,36,43,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'parC':([9,10,11,12,14,16,17,18,19,20,21,23,24,28,37,38,40,41,42,44,45,46,47,48,49,50,52,],[25,-7,-9,-11,-13,-19,-20,-23,-26,-28,-29,37,38,-12,-18,-27,-8,-10,-14,-15,-16,-17,-21,-22,-24,-25,38,]),'and':([10,11,12,14,16,17,18,19,20,21,28,37,38,40,41,42,44,45,46,47,48,49,50,],[-7,27,-11,-13,-19,-20,-23,-26,-28,-29,-12,-18,-27,27,-10,-14,-15,-16,-17,-21,-22,-24,-25,]),'or':([10,11,12,14,16,17,18,19,20,21,28,37,38,40,41,42,44,45,46,47,48,49,50,],[26,-9,-11,-13,-19,-20,-23,-26,-28,-29,-12,-18,-27,-8,-10,-14,-15,-16,-17,-21,-22,-24,-25,]),'mayor':([15,18,19,20,21,24,38,47,48,49,50,],[29,-23,-26,-28,-29,29,-27,-21,-22,-24,-25,]),'menor':([15,18,19,20,21,24,38,47,48,49,50,],[30,-23,-26,-28,-29,30,-27,-21,-22,-24,-25,]),'igualdad':([15,18,19,20,21,24,38,47,48,49,50,],[31,-23,-26,-28,-29,31,-27,-21,-22,-24,-25,]),'diferente':([15,18,19,20,21,24,38,47,48,49,50,],[32,-23,-26,-28,-29,32,-27,-21,-22,-24,-25,]),'mas':([15,18,19,20,21,24,38,42,44,45,46,47,48,49,50,52,],[33,-23,-26,-28,-29,33,-27,33,33,33,33,-21,-22,-24,-25,33,]),'menos':([15,18,19,20,21,24,38,42,44,45,46,47,48,49,50,52,],[34,-23,-26,-28,-29,34,-27,34,34,34,34,-21,-22,-24,-25,34,]),'por':([18,19,20,21,38,47,48,49,50,],[35,-26,-28,-29,-27,35,35,-24,-25,]),'div':([18,19,20,21,38,47,48,49,50,],[36,-26,-28,-29,-27,36,36,-24,-25,]),'llavA':([25,54,],[39,55,]),'Else':([53,],[54,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'INI':([0,],[1,]),'INSTRUCCIONES':([0,39,55,],[2,51,56,]),'INSTRUCCION':([0,2,39,51,55,56,],[3,6,3,6,3,6,]),'S':([7,8,13,22,],[9,23,28,23,]),'L':([7,8,13,22,],[10,10,10,10,]),'M':([7,8,13,22,26,],[11,11,11,11,40,]),'NEG':([7,8,13,22,26,27,],[12,12,12,12,12,41,]),'R':([7,8,13,22,26,27,],[14,14,14,14,14,14,]),'E':([7,8,13,22,26,27,29,30,31,32,43,],[15,24,15,24,15,15,42,44,45,46,52,]),'T':([7,8,13,22,26,27,29,30,31,32,33,34,43,],[18,18,18,18,18,18,18,18,18,18,47,48,18,]),'F':([7,8,13,22,26,27,29,30,31,32,33,34,35,36,43,],[19,19,19,19,19,19,19,19,19,19,19,19,49,50,19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> INI","S'",1,None,None,None),
  ('INI -> INSTRUCCIONES','INI',1,'p_incio','gramatica.py',93),
  ('INSTRUCCIONES -> INSTRUCCIONES INSTRUCCION','INSTRUCCIONES',2,'p_lsInstrucciones','gramatica.py',99),
  ('INSTRUCCIONES -> INSTRUCCION','INSTRUCCIONES',1,'p_lsInstrucciones','gramatica.py',100),
  ('INSTRUCCION -> If parA S parC llavA INSTRUCCIONES llavC','INSTRUCCION',7,'p_instrucciones','gramatica.py',110),
  ('INSTRUCCION -> If parA S parC llavA INSTRUCCIONES llavC Else llavA INSTRUCCIONES llavC','INSTRUCCION',11,'p_instrucciones','gramatica.py',111),
  ('INSTRUCCION -> Nada','INSTRUCCION',1,'p_instrucciones','gramatica.py',112),
  ('S -> L','S',1,'p_s','gramatica.py',145),
  ('L -> L or M','L',3,'p_l','gramatica.py',149),
  ('L -> M','L',1,'p_l2','gramatica.py',161),
  ('M -> M and NEG','M',3,'p_M','gramatica.py',165),
  ('M -> NEG','M',1,'p_M2','gramatica.py',177),
  ('NEG -> not S','NEG',2,'p_Not','gramatica.py',181),
  ('NEG -> R','NEG',1,'p_Not','gramatica.py',182),
  ('R -> E mayor E','R',3,'p_R1','gramatica.py',194),
  ('R -> E menor E','R',3,'p_R2','gramatica.py',209),
  ('R -> E igualdad E','R',3,'p_R3','gramatica.py',224),
  ('R -> E diferente E','R',3,'p_R4','gramatica.py',239),
  ('R -> parA S parC','R',3,'p_R5','gramatica.py',254),
  ('R -> True','R',1,'p_R6','gramatica.py',258),
  ('R -> False','R',1,'p_R7','gramatica.py',269),
  ('E -> E mas T','E',3,'p_E','gramatica.py',281),
  ('E -> E menos T','E',3,'p_E','gramatica.py',282),
  ('E -> T','E',1,'p_E','gramatica.py',283),
  ('T -> T por F','T',3,'p_T','gramatica.py',298),
  ('T -> T div F','T',3,'p_T','gramatica.py',299),
  ('T -> F','T',1,'p_T','gramatica.py',300),
  ('F -> parA E parC','F',3,'p_F','gramatica.py',315),
  ('F -> numero','F',1,'p_F','gramatica.py',316),
  ('F -> id','F',1,'p_F','gramatica.py',317),
]
