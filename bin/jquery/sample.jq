def normalize: [            
      inputs                
    | .Action as $a
    | .Group[]
    |   {Action:$a, Group:.Id}
      + reduce .Units[] as $u ({};.["Unit\($u)"]="1")
  ];

def columns:
  [ .[] | keys[] ] | unique ;

def rows($names):
    .[] | [ .[$names[]] ] | map( .//"0" );

normalize | columns as $names | $names, rows($names) | join(",")
