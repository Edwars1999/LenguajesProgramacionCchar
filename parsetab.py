
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AND ASIGNACION ASYNC BOOL BREAK BYTE CADENA CASE CHAR CLEAR COMA CONST CONTAINSKEY CONTINUE DECIMAL DEFAULT DESIGUALDAD DICTIONARY DIVISION DO DOUBLE ELSE ENTERO EXTERN FALSE FINSENTENCIA FLOAT FOR FOREACH IF IGUALDAD IN INT LIST LLAVEEND LLAVESTART LONG MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MODULO MULTIPLICA NEGACION NEW NULL OR PARENEND PARENSTART PRIVATE PROTECTED PUBLIC PUNTO RESTA RETURN SBYTE SHORT SPACE STACK STATIC STRING SUMA SWITCH THIS TRUE UINT ULONG UNSAFE USHORT VARIABLE VOID WHILEsentencias : condicionales\n                  | repeticiones\n                  | inicializacion repeticiones : opWHILEopWHILE : WHILE  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND\n               | WHILE  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND condicionales : opIFopIF : IF  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND\n            | IF  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND ELSE opIF\n            | IF  PARENSTART condicion PARENEND LLAVESTART  LLAVEEND ELSE LLAVESTART  LLAVEEND\n            | IF  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND\n            | IF  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND ELSE opIF\n            | IF  PARENSTART condicion PARENEND LLAVESTART  sentencias LLAVEEND ELSE LLAVESTART  LLAVEEND condicion : dato exComparadora dato\n                 | dato exComparadora condicion\n                 | PARENSTART condicion PARENEND exComparadora  condicion \n                 | PARENSTART condicion PARENEND\n                 | boleano\n                 | NEGACION boleano\n                 | NEGACION VARIABLE\n                 | VARIABLEexComparadora : AND\n                     | OR\n                     | MAYORQUE\n                     | MENORQUE\n                     | MAYORIGUAL\n                     | MENORIGUAL\n                     | IGUALDAD\n                     | DESIGUALDADinicializacion : declaracion\n                      | asignaciondeclaracion : tipoDato VARIABLE ASIGNACION dato FINSENTENCIA\n                   | tipoDato VARIABLE FINSENTENCIA\n                   | tipoDato VARIABLE ASIGNACION operaciones FINSENTENCIA\n                   | decEstructuradecEstructura : diccionariodiccionario : DICTIONARY MENORQUE clave COMA valor MAYORQUE VARIABLE ASIGNACION NEW DICTIONARY MENORQUE clave COMA valor MAYORQUE PARENSTART PARENEND FINSENTENCIA\n                   | DICTIONARY MENORQUE clave COMA valor MAYORQUE VARIABLE FINSENTENCIA\n                   | VARIABLE IGUALDAD NEW DICTIONARY MENORQUE clave COMA valor MAYORQUE PARENSTART PARENEND FINSENTENCIA\n                   | metodosDicmetodosDic : VARIABLE PUNTO ADD PARENSTART dato COMA valorMetDic PARENEND FINSENTENCIA\n                  | VARIABLE PUNTO CLEAR PARENSTART PARENEND FINSENTENCIA\n                  | VARIABLE PUNTO CONTAINSKEY PARENSTART dato PARENEND FINSENTENCIAvalorMetDic : dato\n                   | NEW estructuraclave : INT\n                | FLOAT\n                | DOUBLE\n                | STRING\n                | LONG\n                | CHAR\n                | SHORT\n                | BYTE\n                | SBYTE\n                | UINT\n                | USHORT\n                | ULONGvalor : tipoDato\n             | estructuraestructura :  DICTIONARY MENORQUE clave COMA valor MAYORQUE \n                  |  LIST MENORQUE valor MAYORQUE\n                  |  STACK MENORQUE valor MENORQUE  asignacion : VARIABLE ASIGNACION dato FINSENTENCIA\n                  | VARIABLE ASIGNACION boleano FINSENTENCIA\n                  | VARIABLE ASIGNACION operaciones FINSENTENCIAdato : VARIABLE \n            | numero\n            | CADENA tipoDato : INT\n                | FLOAT\n                | DOUBLE\n                | STRING\n                | LONG\n                | CHAR\n                | SHORT\n                | BYTE\n                | SBYTE\n                | UINT\n                | USHORT\n                | ULONG\n                | BOOLboleano : TRUE\n                | FALSE numero : ENTERO\n             | DECIMALoperaciones :  expresion repOp \n                   | expresion repOp : operador expresion \n            | operador expresion repOpexpresion : numero\n                 | VARIABLE\n                 | PARENSTART  operaciones PARENEND\n                 | PARENSTART  VARIABLE PARENEND\n                 | PARENSTART  numero PARENENDoperador : SUMA\n                | RESTA\n                | MULTIPLICA\n                | DIVISION\n                | MODULO '
    
_lr_action_items = {'IF':([0,111,115,150,164,],[9,9,9,9,9,]),'WHILE':([0,111,115,],[10,10,10,]),'VARIABLE':([0,11,14,15,16,17,18,19,20,21,22,23,24,25,26,30,31,33,37,41,50,58,78,79,80,81,82,83,84,85,86,96,97,98,99,100,101,106,108,111,115,135,142,146,],[12,32,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,42,42,52,42,88,52,103,114,-22,-23,-24,-25,-26,-27,-28,-29,120,-95,-96,-97,-98,-99,125,125,12,12,42,125,159,]),'INT':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[14,64,14,14,14,64,64,14,14,14,14,64,14,]),'FLOAT':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[15,65,15,15,15,65,65,15,15,15,15,65,15,]),'DOUBLE':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[16,66,16,16,16,66,66,16,16,16,16,66,16,]),'STRING':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[17,67,17,17,17,67,67,17,17,17,17,67,17,]),'LONG':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[18,68,18,18,18,68,68,18,18,18,18,68,18,]),'CHAR':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[19,69,19,19,19,69,69,19,19,19,19,69,19,]),'SHORT':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[20,70,20,20,20,70,70,20,20,20,20,70,20,]),'BYTE':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[21,71,21,21,21,71,71,21,21,21,21,71,21,]),'SBYTE':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[22,72,22,22,22,72,72,22,22,22,22,72,22,]),'UINT':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[23,73,23,23,23,73,73,23,23,23,23,73,23,]),'USHORT':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[24,74,24,24,24,74,74,24,24,24,24,74,24,]),'ULONG':([0,36,109,111,115,124,145,147,148,153,168,185,188,],[25,75,25,25,25,75,75,25,25,25,25,75,25,]),'BOOL':([0,109,111,115,147,148,153,168,188,],[26,26,26,26,26,26,26,26,26,]),'DICTIONARY':([0,59,109,111,115,147,148,153,156,168,179,188,],[28,105,129,28,28,129,129,129,129,129,183,129,]),'$end':([1,2,3,4,5,6,7,8,13,27,29,51,92,93,94,116,117,136,138,143,151,152,157,163,170,173,175,177,180,186,193,],[0,-1,-2,-3,-7,-4,-30,-31,-35,-36,-40,-33,-63,-64,-65,-32,-34,-8,-5,-42,-11,-6,-43,-9,-38,-10,-12,-41,-13,-39,-37,]),'LLAVEEND':([2,3,4,5,6,7,8,13,27,29,51,92,93,94,111,115,116,117,136,137,138,139,143,151,152,157,162,163,170,173,174,175,177,180,186,193,],[-1,-2,-3,-7,-4,-30,-31,-35,-36,-40,-33,-63,-64,-65,136,138,-32,-34,-8,151,-5,152,-42,-11,-6,-43,173,-9,-38,-10,180,-12,-41,-13,-39,-37,]),'PARENSTART':([9,10,30,31,33,37,50,58,60,61,62,78,79,80,81,82,83,84,85,86,96,97,98,99,100,101,135,176,190,],[30,31,37,37,58,37,58,58,106,107,108,37,-22,-23,-24,-25,-26,-27,-28,-29,58,-95,-96,-97,-98,-99,37,181,191,]),'ASIGNACION':([12,32,159,],[33,50,169,]),'IGUALDAD':([12,39,42,43,44,47,48,110,112,114,],[34,85,-66,-67,-68,-84,-85,85,85,-66,]),'PUNTO':([12,],[35,]),'MAYORQUE':([14,15,16,17,18,19,20,21,22,23,24,25,26,39,42,43,44,47,48,110,112,114,130,131,132,160,165,171,172,178,182,189,],[-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,81,-66,-67,-68,-84,-85,81,81,-66,146,-58,-59,171,176,-61,-62,182,-60,190,]),'MENORQUE':([14,15,16,17,18,19,20,21,22,23,24,25,26,28,39,42,43,44,47,48,105,110,112,114,129,131,132,133,134,161,171,172,182,183,],[-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-81,36,82,-66,-67,-68,-84,-85,124,82,82,-66,145,-58,-59,147,148,172,-61,-62,-60,185,]),'NEGACION':([30,31,37,78,79,80,81,82,83,84,85,86,135,],[41,41,41,41,-22,-23,-24,-25,-26,-27,-28,-29,41,]),'CADENA':([30,31,33,37,50,78,79,80,81,82,83,84,85,86,106,108,135,142,],[44,44,44,44,44,44,-22,-23,-24,-25,-26,-27,-28,-29,44,44,44,44,]),'TRUE':([30,31,33,37,41,78,79,80,81,82,83,84,85,86,135,],[45,45,45,45,45,45,-22,-23,-24,-25,-26,-27,-28,-29,45,]),'FALSE':([30,31,33,37,41,78,79,80,81,82,83,84,85,86,135,],[46,46,46,46,46,46,-22,-23,-24,-25,-26,-27,-28,-29,46,]),'ENTERO':([30,31,33,37,50,58,78,79,80,81,82,83,84,85,86,96,97,98,99,100,101,106,108,135,142,],[47,47,47,47,47,47,47,-22,-23,-24,-25,-26,-27,-28,-29,47,-95,-96,-97,-98,-99,47,47,47,47,]),'DECIMAL':([30,31,33,37,50,58,78,79,80,81,82,83,84,85,86,96,97,98,99,100,101,106,108,135,142,],[48,48,48,48,48,48,48,-22,-23,-24,-25,-26,-27,-28,-29,48,-95,-96,-97,-98,-99,48,48,48,48,]),'FINSENTENCIA':([32,44,45,46,47,48,52,53,54,55,56,57,90,91,95,118,119,120,121,122,123,127,140,144,159,166,184,192,],[51,-68,-82,-83,-84,-85,-66,92,93,94,-67,-87,116,117,-86,-88,-90,-91,-92,-93,-94,143,-89,157,170,177,186,193,]),'NEW':([34,142,169,],[59,156,179,]),'ADD':([35,],[60,]),'CLEAR':([35,],[61,]),'CONTAINSKEY':([35,],[62,]),'PARENEND':([38,40,42,43,44,45,46,47,48,49,57,76,87,88,95,102,103,104,107,110,112,113,114,118,119,120,121,122,123,125,128,140,149,154,155,167,171,172,181,182,191,],[77,-18,-21,-67,-68,-82,-83,-84,-85,89,-87,110,-19,-20,-86,121,122,123,127,-17,-14,-15,-21,-88,-90,-91,-92,-93,-94,-66,144,-89,-16,-44,166,-45,-61,-62,184,-60,192,]),'AND':([39,42,43,44,47,48,110,112,114,],[79,-66,-67,-68,-84,-85,79,79,-66,]),'OR':([39,42,43,44,47,48,110,112,114,],[80,-66,-67,-68,-84,-85,80,80,-66,]),'MAYORIGUAL':([39,42,43,44,47,48,110,112,114,],[83,-66,-67,-68,-84,-85,83,83,-66,]),'MENORIGUAL':([39,42,43,44,47,48,110,112,114,],[84,-66,-67,-68,-84,-85,84,84,-66,]),'DESIGUALDAD':([39,42,43,44,47,48,110,112,114,],[86,-66,-67,-68,-84,-85,86,86,-66,]),'COMA':([43,44,47,48,63,64,65,66,67,68,69,70,71,72,73,74,75,125,126,141,158,187,],[-67,-68,-84,-85,109,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-66,142,153,168,188,]),'SUMA':([47,48,52,56,57,103,104,118,119,120,121,122,123,],[-84,-85,-91,-90,97,-91,-90,97,-90,-91,-92,-93,-94,]),'RESTA':([47,48,52,56,57,103,104,118,119,120,121,122,123,],[-84,-85,-91,-90,98,-91,-90,98,-90,-91,-92,-93,-94,]),'MULTIPLICA':([47,48,52,56,57,103,104,118,119,120,121,122,123,],[-84,-85,-91,-90,99,-91,-90,99,-90,-91,-92,-93,-94,]),'DIVISION':([47,48,52,56,57,103,104,118,119,120,121,122,123,],[-84,-85,-91,-90,100,-91,-90,100,-90,-91,-92,-93,-94,]),'MODULO':([47,48,52,56,57,103,104,118,119,120,121,122,123,],[-84,-85,-91,-90,101,-91,-90,101,-90,-91,-92,-93,-94,]),'LLAVESTART':([77,89,150,164,],[111,115,162,174,]),'LIST':([109,147,148,153,156,168,188,],[133,133,133,133,133,133,133,]),'STACK':([109,147,148,153,156,168,188,],[134,134,134,134,134,134,134,]),'ELSE':([136,151,],[150,164,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencias':([0,111,115,],[1,137,139,]),'condicionales':([0,111,115,],[2,2,2,]),'repeticiones':([0,111,115,],[3,3,3,]),'inicializacion':([0,111,115,],[4,4,4,]),'opIF':([0,111,115,150,164,],[5,5,5,163,175,]),'opWHILE':([0,111,115,],[6,6,6,]),'declaracion':([0,111,115,],[7,7,7,]),'asignacion':([0,111,115,],[8,8,8,]),'tipoDato':([0,109,111,115,147,148,153,168,188,],[11,131,11,11,131,131,131,131,131,]),'decEstructura':([0,111,115,],[13,13,13,]),'diccionario':([0,111,115,],[27,27,27,]),'metodosDic':([0,111,115,],[29,29,29,]),'condicion':([30,31,37,78,135,],[38,49,76,113,149,]),'dato':([30,31,33,37,50,78,106,108,135,142,],[39,39,53,39,90,112,126,128,39,154,]),'boleano':([30,31,33,37,41,78,135,],[40,40,54,40,87,40,40,]),'numero':([30,31,33,37,50,58,78,96,106,108,135,142,],[43,43,56,43,56,104,43,119,43,43,43,43,]),'operaciones':([33,50,58,],[55,91,102,]),'expresion':([33,50,58,96,],[57,57,57,118,]),'clave':([36,124,145,185,],[63,141,158,187,]),'exComparadora':([39,110,112,],[78,135,78,]),'repOp':([57,118,],[95,140,]),'operador':([57,118,],[96,96,]),'valor':([109,147,148,153,168,188,],[130,160,161,165,178,189,]),'estructura':([109,147,148,153,156,168,188,],[132,132,132,132,167,132,132,]),'valorMetDic':([142,],[155,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencias","S'",1,None,None,None),
  ('sentencias -> condicionales','sentencias',1,'p_sentencias','sintax.py',10),
  ('sentencias -> repeticiones','sentencias',1,'p_sentencias','sintax.py',11),
  ('sentencias -> inicializacion','sentencias',1,'p_sentencias','sintax.py',12),
  ('repeticiones -> opWHILE','repeticiones',1,'p_repeticiones','sintax.py',17),
  ('opWHILE -> WHILE PARENSTART condicion PARENEND LLAVESTART LLAVEEND','opWHILE',6,'p_opWhile','sintax.py',20),
  ('opWHILE -> WHILE PARENSTART condicion PARENEND LLAVESTART sentencias LLAVEEND','opWHILE',7,'p_opWhile','sintax.py',21),
  ('condicionales -> opIF','condicionales',1,'p_condicionales','sintax.py',25),
  ('opIF -> IF PARENSTART condicion PARENEND LLAVESTART LLAVEEND','opIF',6,'p_opIf','sintax.py',28),
  ('opIF -> IF PARENSTART condicion PARENEND LLAVESTART LLAVEEND ELSE opIF','opIF',8,'p_opIf','sintax.py',29),
  ('opIF -> IF PARENSTART condicion PARENEND LLAVESTART LLAVEEND ELSE LLAVESTART LLAVEEND','opIF',9,'p_opIf','sintax.py',30),
  ('opIF -> IF PARENSTART condicion PARENEND LLAVESTART sentencias LLAVEEND','opIF',7,'p_opIf','sintax.py',31),
  ('opIF -> IF PARENSTART condicion PARENEND LLAVESTART sentencias LLAVEEND ELSE opIF','opIF',9,'p_opIf','sintax.py',32),
  ('opIF -> IF PARENSTART condicion PARENEND LLAVESTART sentencias LLAVEEND ELSE LLAVESTART LLAVEEND','opIF',10,'p_opIf','sintax.py',33),
  ('condicion -> dato exComparadora dato','condicion',3,'p_condicion','sintax.py',36),
  ('condicion -> dato exComparadora condicion','condicion',3,'p_condicion','sintax.py',37),
  ('condicion -> PARENSTART condicion PARENEND exComparadora condicion','condicion',5,'p_condicion','sintax.py',38),
  ('condicion -> PARENSTART condicion PARENEND','condicion',3,'p_condicion','sintax.py',39),
  ('condicion -> boleano','condicion',1,'p_condicion','sintax.py',40),
  ('condicion -> NEGACION boleano','condicion',2,'p_condicion','sintax.py',41),
  ('condicion -> NEGACION VARIABLE','condicion',2,'p_condicion','sintax.py',42),
  ('condicion -> VARIABLE','condicion',1,'p_condicion','sintax.py',43),
  ('exComparadora -> AND','exComparadora',1,'p_exComparadora','sintax.py',46),
  ('exComparadora -> OR','exComparadora',1,'p_exComparadora','sintax.py',47),
  ('exComparadora -> MAYORQUE','exComparadora',1,'p_exComparadora','sintax.py',48),
  ('exComparadora -> MENORQUE','exComparadora',1,'p_exComparadora','sintax.py',49),
  ('exComparadora -> MAYORIGUAL','exComparadora',1,'p_exComparadora','sintax.py',50),
  ('exComparadora -> MENORIGUAL','exComparadora',1,'p_exComparadora','sintax.py',51),
  ('exComparadora -> IGUALDAD','exComparadora',1,'p_exComparadora','sintax.py',52),
  ('exComparadora -> DESIGUALDAD','exComparadora',1,'p_exComparadora','sintax.py',53),
  ('inicializacion -> declaracion','inicializacion',1,'p_inicializacion','sintax.py',56),
  ('inicializacion -> asignacion','inicializacion',1,'p_inicializacion','sintax.py',57),
  ('declaracion -> tipoDato VARIABLE ASIGNACION dato FINSENTENCIA','declaracion',5,'p_declaracion','sintax.py',60),
  ('declaracion -> tipoDato VARIABLE FINSENTENCIA','declaracion',3,'p_declaracion','sintax.py',61),
  ('declaracion -> tipoDato VARIABLE ASIGNACION operaciones FINSENTENCIA','declaracion',5,'p_declaracion','sintax.py',62),
  ('declaracion -> decEstructura','declaracion',1,'p_declaracion','sintax.py',63),
  ('decEstructura -> diccionario','decEstructura',1,'p_decEstructura','sintax.py',66),
  ('diccionario -> DICTIONARY MENORQUE clave COMA valor MAYORQUE VARIABLE ASIGNACION NEW DICTIONARY MENORQUE clave COMA valor MAYORQUE PARENSTART PARENEND FINSENTENCIA','diccionario',18,'p_diccionario','sintax.py',69),
  ('diccionario -> DICTIONARY MENORQUE clave COMA valor MAYORQUE VARIABLE FINSENTENCIA','diccionario',8,'p_diccionario','sintax.py',70),
  ('diccionario -> VARIABLE IGUALDAD NEW DICTIONARY MENORQUE clave COMA valor MAYORQUE PARENSTART PARENEND FINSENTENCIA','diccionario',12,'p_diccionario','sintax.py',71),
  ('diccionario -> metodosDic','diccionario',1,'p_diccionario','sintax.py',72),
  ('metodosDic -> VARIABLE PUNTO ADD PARENSTART dato COMA valorMetDic PARENEND FINSENTENCIA','metodosDic',9,'p_metodosDic','sintax.py',75),
  ('metodosDic -> VARIABLE PUNTO CLEAR PARENSTART PARENEND FINSENTENCIA','metodosDic',6,'p_metodosDic','sintax.py',76),
  ('metodosDic -> VARIABLE PUNTO CONTAINSKEY PARENSTART dato PARENEND FINSENTENCIA','metodosDic',7,'p_metodosDic','sintax.py',77),
  ('valorMetDic -> dato','valorMetDic',1,'p_valorMetDic','sintax.py',81),
  ('valorMetDic -> NEW estructura','valorMetDic',2,'p_valorMetDic','sintax.py',82),
  ('clave -> INT','clave',1,'p_clave','sintax.py',85),
  ('clave -> FLOAT','clave',1,'p_clave','sintax.py',86),
  ('clave -> DOUBLE','clave',1,'p_clave','sintax.py',87),
  ('clave -> STRING','clave',1,'p_clave','sintax.py',88),
  ('clave -> LONG','clave',1,'p_clave','sintax.py',89),
  ('clave -> CHAR','clave',1,'p_clave','sintax.py',90),
  ('clave -> SHORT','clave',1,'p_clave','sintax.py',91),
  ('clave -> BYTE','clave',1,'p_clave','sintax.py',92),
  ('clave -> SBYTE','clave',1,'p_clave','sintax.py',93),
  ('clave -> UINT','clave',1,'p_clave','sintax.py',94),
  ('clave -> USHORT','clave',1,'p_clave','sintax.py',95),
  ('clave -> ULONG','clave',1,'p_clave','sintax.py',96),
  ('valor -> tipoDato','valor',1,'p_valor','sintax.py',99),
  ('valor -> estructura','valor',1,'p_valor','sintax.py',100),
  ('estructura -> DICTIONARY MENORQUE clave COMA valor MAYORQUE','estructura',6,'p_estructura','sintax.py',103),
  ('estructura -> LIST MENORQUE valor MAYORQUE','estructura',4,'p_estructura','sintax.py',104),
  ('estructura -> STACK MENORQUE valor MENORQUE','estructura',4,'p_estructura','sintax.py',105),
  ('asignacion -> VARIABLE ASIGNACION dato FINSENTENCIA','asignacion',4,'p_asignacion','sintax.py',108),
  ('asignacion -> VARIABLE ASIGNACION boleano FINSENTENCIA','asignacion',4,'p_asignacion','sintax.py',109),
  ('asignacion -> VARIABLE ASIGNACION operaciones FINSENTENCIA','asignacion',4,'p_asignacion','sintax.py',110),
  ('dato -> VARIABLE','dato',1,'p_dato','sintax.py',113),
  ('dato -> numero','dato',1,'p_dato','sintax.py',114),
  ('dato -> CADENA','dato',1,'p_dato','sintax.py',115),
  ('tipoDato -> INT','tipoDato',1,'p_tipoDato','sintax.py',118),
  ('tipoDato -> FLOAT','tipoDato',1,'p_tipoDato','sintax.py',119),
  ('tipoDato -> DOUBLE','tipoDato',1,'p_tipoDato','sintax.py',120),
  ('tipoDato -> STRING','tipoDato',1,'p_tipoDato','sintax.py',121),
  ('tipoDato -> LONG','tipoDato',1,'p_tipoDato','sintax.py',122),
  ('tipoDato -> CHAR','tipoDato',1,'p_tipoDato','sintax.py',123),
  ('tipoDato -> SHORT','tipoDato',1,'p_tipoDato','sintax.py',124),
  ('tipoDato -> BYTE','tipoDato',1,'p_tipoDato','sintax.py',125),
  ('tipoDato -> SBYTE','tipoDato',1,'p_tipoDato','sintax.py',126),
  ('tipoDato -> UINT','tipoDato',1,'p_tipoDato','sintax.py',127),
  ('tipoDato -> USHORT','tipoDato',1,'p_tipoDato','sintax.py',128),
  ('tipoDato -> ULONG','tipoDato',1,'p_tipoDato','sintax.py',129),
  ('tipoDato -> BOOL','tipoDato',1,'p_tipoDato','sintax.py',130),
  ('boleano -> TRUE','boleano',1,'p_boleano','sintax.py',134),
  ('boleano -> FALSE','boleano',1,'p_boleano','sintax.py',135),
  ('numero -> ENTERO','numero',1,'p_numero','sintax.py',138),
  ('numero -> DECIMAL','numero',1,'p_numero','sintax.py',139),
  ('operaciones -> expresion repOp','operaciones',2,'p_operaciones','sintax.py',142),
  ('operaciones -> expresion','operaciones',1,'p_operaciones','sintax.py',143),
  ('repOp -> operador expresion','repOp',2,'p_repOpe','sintax.py',146),
  ('repOp -> operador expresion repOp','repOp',3,'p_repOpe','sintax.py',147),
  ('expresion -> numero','expresion',1,'p_expresion','sintax.py',150),
  ('expresion -> VARIABLE','expresion',1,'p_expresion','sintax.py',151),
  ('expresion -> PARENSTART operaciones PARENEND','expresion',3,'p_expresion','sintax.py',152),
  ('expresion -> PARENSTART VARIABLE PARENEND','expresion',3,'p_expresion','sintax.py',153),
  ('expresion -> PARENSTART numero PARENEND','expresion',3,'p_expresion','sintax.py',154),
  ('operador -> SUMA','operador',1,'p_operador','sintax.py',157),
  ('operador -> RESTA','operador',1,'p_operador','sintax.py',158),
  ('operador -> MULTIPLICA','operador',1,'p_operador','sintax.py',159),
  ('operador -> DIVISION','operador',1,'p_operador','sintax.py',160),
  ('operador -> MODULO','operador',1,'p_operador','sintax.py',161),
]
